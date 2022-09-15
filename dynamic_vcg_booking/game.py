from __future__ import annotations

import os
import random
from typing import TYPE_CHECKING, Dict, List

import pandas as pd
from util.logger import logger

from vaccine_booking.algorithms.RSD.random_serial_dictatorship import (
    RandomSerialDictatorship,
)
from vaccine_booking.elements.applicant import Applicant
from vaccine_booking.elements.basics.result_writer import Result, ResultWriter, Writable
from vaccine_booking.elements.message import Message
from vaccine_booking.elements.organisation import Organisation
from vaccine_booking.elements.preference import Preference
from vaccine_booking.elements.slot import Slot, outside
from vaccine_booking.settings.config import ConfigManager
from vaccine_booking.strategies.maximax import Maximax
from vaccine_booking.strategies.minimax import Minimax
from vaccine_booking.strategies.mean import Mean
from vaccine_booking.strategies.strategy import Strategy

import wandb
#wandb.init(entity="vaccine_booking", project="Normal_Distribution_Preference", group="level3_Maximax")
#wandb.init(entity="vaccine_booking", project="Normal_Distribution_Preference", group="level3_Minimax")
wandb.init(entity="vaccine_booking", project="Normal_Distribution_Preference", group="level3_Mean") 

logger.info("(reading json file ...)")
# Json から読み込んだデータを DataClass として config に保存
config_manager = ConfigManager(os.environ["SETTING_NAME"])
global_config = config_manager.get_global_config()
configs = config_manager.get_configs()
## csv関連
# preference_csv=[]
# preference_csv.append(["round","applicant_id","市民会館_weekday_Mon_am_9-10","市民会館_weekday_Mon_am_10-11","市民会館_weekday_Mon_pm_13-14","市民会館_weekday_Mon_pm_14-15","市民会館_weekend_Sat_am_9-10","市民会館_weekend_Sat_am_10-11","市民会館_weekend_Sat_pm_13-14","市民会館_weekend_Sat_pm_14-15","outside","RSDの順番"])
# message_csv=[]
# message_csv.append(["round","applicant_id","メッセージ1","メッセージ2","メッセージ3","メッセージ4"])
# allocation_csv=[]
# allocation_csv.append(["round","市民会館_weekday_Mon_am_9-10","市民会館_weekday_Mon_am_10-11","市民会館_weekday_Mon_pm_13-14","市民会館_weekday_Mon_pm_14-15","市民会館_weekend_Sat_am_9-10","市民会館_weekend_Sat_am_10-11","市民会館_weekend_Sat_pm_13-14","市民会館_weekend_Sat_pm_14-15"])
# cancel_csv=[]
# cancel_csv.append(["round","applicant_0","applicant_1","applicant_2","applicant_3","applicant_4","applicant_5","applicant_6","applicant_7","applicant_8","applicant_9"])



class Game(Writable):
    def __init__(self, name: str, strategy: Strategy, seed: int):
        # super().__init__(name)  # Wrirable親クラスの init を呼び出す
        self.seed = seed
        self.name = name
        self.strategy = strategy
        self.all_applicant_list: List[Applicant] = []
        self.organisation_list: List[Organisation] = []
        self.all_slot_list: List[Slot] = []
        self.all_message_list: List[Message] = []
        self.result = Result(
            [
                "unvaccination_nums",
                "cancel_nums",
                "vaccination_nums",
                "total_capacity",
            ]
        )
        self._setup()

    def _setup(self):
        logger.info("set up organisations")
        for organisation_name, config in configs.items():
            organisation = Organisation(organisation_name)
            cls = globals()[config.algorithm]  # jsonで書かれたクラス名をインスタンス化
            algorithm = cls(organisation)
            organisation.set_algorithm(algorithm)
            self.organisation_list.append(organisation)
            logger.info(
                f"   -> {organisation_name} uses **{algorithm.__class__.__name__}**"
            )

        logger.info("set up all slots")
        slot_list_temp = []
        for organisation in self.organisation_list:
            slot_list_temp.append(organisation.get_slot_list())
        self.all_slot_list = sum(slot_list_temp, [])  # Listの入れ子を解除
        # Outside として特別なスロットを追加
        self.all_slot_list.append(outside)

        logger.info("set up all messages")
        message_list_temp = []
        for organisation in self.organisation_list:
            message_list_temp.append(organisation.get_message_list())
        self.all_message_list = sum(message_list_temp, [])  # Listの入れ子を解除
        # # Outside として特別なスロットを追加
        # self.all_message_list.append(outside) # messageの平均値はoutsideより低くなると、outsideを報告する

        logger.info("set up applicants")
        # for applicant_name, priority in config_manager.get_applicant_data():
        for applicant_name in config_manager.get_applicant_data():
            self.all_applicant_list.append(
                Applicant(
                    applicant_name,
                    self.all_slot_list,  # 組織を超えた全Slot
                    self.all_message_list,
                    self.strategy,
                )
            )

        logger.info("set up preference for slot")
        # 選好の設定 (ランダム、無差別含む)
        random.seed(self.seed)
        for applicant in self.all_applicant_list:
            slot_pref = Preference()
            for slot in self.all_slot_list:
                if slot != outside:
                    slot_pref.set(slot, random.gauss(100,10))
                else:
                    slot_pref.set(slot, random.gauss(60,10))
            applicant.set_preference(slot_pref)
            slot_pref.set_owner(applicant)

        # 確認のためのprint
        # for applicant in self.all_applicant_list:
        #     applicant.get_preference().print_preference()   

    def current_print(self) -> None:
        logger.info("[Summary]")
        logger.info(f"# of Unvaccinated People：{self.unvaccination_nums}")
        logger.info(f"# of People who canceled more than one: {self.cancel_nums}")

        vaccination_nums = 0
        total_capacity = 0
        for organisation in self.organisation_list:
            total_capacity = sum(config_manager.set_capacity(organisation_name=organisation.name))
        for i in self.all_slot_list:
            #print(i.get_allocation())
            vaccination_nums += len(i.get_allocation())
        logger.info(f"Vaccination Rate: {vaccination_nums}/{total_capacity}")

        # Resultクラスにデータを保存
        self.result.add_row(
            column_names=[
                "unvaccination_nums",
                "cancel_nums",
                "vaccination_nums",
                "total_capacity",
            ],
            row_data=[
                self.unvaccination_nums,
                self.cancel_nums,
                vaccination_nums,
                total_capacity,
            ],
        )
        wandb.log(
            {
                "application_nums" : self.unvaccination_nums,
                "cancel_nums": self.cancel_nums,
                "vaccination_nums": vaccination_nums,
            }
        )
        # # ****** 以下、Debug時の出力 *****
        logger.debug("結果を出力します")
        for organisation, allocation in self.allocation_dict.items():
            logger.debug(f"{organisation.get_name()}:")
            #allocation.print_allocation()
        logger.debug("接種状況の詳細を出力します(キャンセル処理後)")
        for slot in self.all_slot_list:
            logger.debug(
                f"{slot.get_name()}: {[str(v) for v in slot.get_allocation()]}"
            )

    def get_all_applicant_list(self) -> List[Applicant]:
        return self.all_applicant_list

    def get_all_slot_list(self) -> List[Slot]:
        return self.all_slot_list

    def get_result(self) -> Dict[str, List[float]]:
        return self.result.get_data_dict()

    def start(self):
        round_nums = global_config.round_nums  # 繰り返しゲームのラウンド数

        logger.info("run algorithm")
        for round in range(1, round_nums + 1):
            logger.info(f"########## Round {round} ############")

            random.seed(round+10*self.seed)
            # 初期化
            self.current_applicant_list = []
            for applicant in self.all_applicant_list:
                applicant.initialize()
                if applicant.get_vaccination_nums() == 0:
                    self.current_applicant_list.append(applicant)
            for slot in self.all_slot_list:
                slot.initialize()
            for organisation in self.organisation_list:
                organisation.initialize()
                organisation.set_applicant_list(self.current_applicant_list)

            # 各組織でアルゴリズム実行
            self.allocation_dict = {}
            for organisation in self.organisation_list:
                # key=Organisationクラス、value=Allocationクラス として設定
                organisation.round=round
                self.allocation_dict[organisation] = organisation.execute()
                

            # ワクチン接種とキャンセルカウント
            logger.debug("キャンセル確認：")
            self.unvaccination_nums = 0
            self.cancel_nums = 0
            row_csv=[]
            row_csv.append(round)
            for i in self.current_applicant_list:
                if len(i.get_decision()) > 0:
                    self.unvaccination_nums += 1
                    i.vaccinate()  # ワクチン接種（キャンセルしたらcancel=Trueに）
                    if i.is_cancelled():
                        self.cancel_nums += 1
                        logger.debug(f"cancel:{i.get_name()}")

            # for player in self.all_applicant_list:    
            #     row_csv.append(player.cancel)
            # cancel_csv.append(row_csv)

            # 結果の出力
            if round == 1:
                self.result_writer = ResultWriter(*self.organisation_list)
                self.result_writer.add(self)  # このゲーム自身も Writableの子クラスのため追加可
            self.result_writer.current_print()

        logger.info("########## End of Simulation ############")
        logger.info("save summary output as csv")

        # import csv
        # f = open('./output/preference.csv', 'w')
        # writer = csv.writer(f)
        # writer.writerows(preference_csv)
        # f.close()
        # f = open('./output/message.csv', 'w')
        # writer = csv.writer(f)
        # writer.writerows(message_csv)
        # f.close()
        # f = open('./output/allocation.csv', 'w')
        # writer = csv.writer(f)
        # writer.writerows(allocation_csv)
        # f.close()
        # f = open('./output/cancel_csv.csv', 'w')
        # writer = csv.writer(f)
        # writer.writerows(cancel_csv)
        # f.close()

        # self.result_writer.write_to_csv("./output")

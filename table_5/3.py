import re
from traceback import print_tb
from numpy.lib.function_base import average
import pandas as pd
import random
import itertools
import copy
import wandb

# wandb.init(
#     entity="dbx",
#     project="VCG_Booking",
#     group="Dynamic_VCG_5seats",
#     name="FCFS_res_fee5_VCG_cancel_fee5_test",
# )
# table = 5, course = 2
num_steps = 100
total_FCFS_revenue_list = []
total_FCFS_utility_list = []
total_FCFS_social_list = []
total_VCG_revenue_list = []
total_VCG_utility_list = []
total_VCG_social_list = []
for run in range(num_steps):
    wandb.init(
        entity="dbx",
        project="VCG_Booking",
        group="FCFS_res_fee0_VCG_cancel_fee0",
        name=f"run{run}",
    )
    random.seed(run)
    bug = 0
    table_total = 5
    FCFS_revenue_list = []
    VCG_revenue_list = []
    party_num = 5
    days = 3
    party_list = []
    report_table = []
    random_table = []
    res_revenue2 = 0
    utility1 = 0
    utility2 = 0

    def add_party(party_list):
        while len(party_list) < 200:
            party_name = len(party_list)
            party_size = random.randint(1, 4)
            party_info = {}
            party_info[f"p{party_name}"] = {}
            for course in itertools.product("AB", repeat=party_size):
                for day in range(1, days + 1):
                    if party_size == 1:
                        for table in range(party_size, 6):
                            if table == 1:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(1, 5)
                            if table == 2:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(2, 9)

                            if table == 3:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(3, 12)

                            if table == 4:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 14)

                            if table == 5:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 15)
                    if party_size == 2:
                        for table in range(party_size, 6):
                            if table == 2:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(2, 10)

                            if table == 3:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(3, 14)

                            if table == 4:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 18)

                            if table == 5:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 21)

                    if party_size == 3:
                        for table in range(party_size, 6):
                            if table == 3:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(3, 15)
                            if table == 4:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 19)
                            if table == 5:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 23)
                    if party_size == 4:
                        for table in range(party_size, 6):
                            if table == 4:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 20)
                            if table == 5:
                                party_info[f"p{party_name}"][
                                    f"s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 24)
            party_list.append(party_info)
        return party_list

    party_list = add_party(party_list)
    # print(party_list)
    # FCFS Mechanism
    party_list_fcfs = copy.deepcopy(party_list)
    seat_allocate = {}
    capacity_allocate = {}
    total_FCFS_utility = 0
    total_FCFS_revenue = 0
    total_FCFS_social = 0
    fcfs_len = 0
    FCFS_party_preference_list = []
    FCFS_revenue_list = []
    FCFS_utility_list = []
    FCFS_social_list = []

    # VCG mechanism

    # party_list_vcg = copy.deepcopy(party_list)

    reject_parties_list = []
    VCG_party_list = []
    seat_allocate_vcg = {}
    capacity_allocate_vcg = {}
    optimal_party_allocation = []
    total_VCG_revenue = 0
    total_VCG_utility = 0
    total_VCG_social = 0
    VCG_revenue_list = []
    VCG_utility_list = []
    VCG_social_list = []
    vcg_party_info_dict = {}
    vcg_party_info_dict_dict = {}
    for party_info in party_list:
        # print(party_info)
        for choice, value in list(party_info.values())[0].items():
            # print(list(party_info.keys())[0])
            vcg_party_info_dict[(list(party_info.keys())[0], choice, value)] = (
                choice.count("A") * 10 + choice.count("B") * 15 + value
            )
        vcg_party_info_dict = sorted(
            vcg_party_info_dict.items(), key=lambda x: x[1], reverse=True
        )[
            :10
        ]  # changing bid number
        vcg_party_info_dict_dict[list(party_info.keys())[0]] = vcg_party_info_dict
        vcg_party_info_dict = {}
        # break
        # key=player,value=((name, choice, table value),total value)
        # print("vcg_party_info_dict_dict:", vcg_party_info_dict_dict)
    party_list_vcg = list(vcg_party_info_dict_dict.values())

    party_changed = 0
    final_allocated_party_list = []
    total_cancellations = 0
    for i in range(0, 33):
        seat_allocate[str(i)] = 0
        capacity_allocate[str(i)] = 0
        seat_allocate_vcg[str(i)] = []
        capacity_allocate_vcg[str(i)] = 0
    for i in range(30):  # simulation period
        FCFS_party_list = []
        FCFS_revenue = 0
        table_revenue = 0
        course_revenue = 0
        utility_FCFS = 0
        print("-------------------------------------")
        print("-----------------FCFS----------------")
        print("-------------------------------------")
        while len(FCFS_party_preference_list) < 5:
            FCFS_party_preference_list.append(party_list_fcfs.pop(0))
            FCFS_party_preference_dict = {}
            for key, value in FCFS_party_preference_list[-1].items():
                # key = key.replace("_"," ").replace("(", "").replace(")", "").replace(",", "").replace("'", "").split()
                # key = player, values = {[info:value,...]}
                value = sorted(
                    value.items(),
                    key=lambda x: x[1],
                    reverse=True,
                )
                value_priced = []
                for v in value:
                    v = list(v)
                    if v[0][-1] == "1":
                        # print(v[-1])
                        v[-1] = v[-1] - 0
                    if v[0][-1] == "2":
                        v[-1] = v[-1] - 0
                    if v[0][-1] == "3":
                        v[-1] = v[-1] - 0
                    if v[0][-1] == "4":
                        v[-1] = v[-1] - 0
                    if v[0][-1] == "5":
                        v[-1] = v[-1] - 0
                    if v[-1] >= 0:
                        value_priced.append(v)
                FCFS_party_preference_dict[key] = value_priced
            # print("FCFS_party_preference_dict:", FCFS_party_preference_dict)
            FCFS_party_list.append(FCFS_party_preference_dict)
        print("FCFS_party_list:", FCFS_party_list)
        if fcfs_len != 0:
            FCFS_party_list = FCFS_party_preference_list[:fcfs_len] + FCFS_party_list
            FCFS_party_preference_list = FCFS_party_list
        else:
            FCFS_party_preference_list = FCFS_party_list
        # print("FCFS_party_preference_list:", FCFS_party_preference_list)
        # print("FCFS_party_list:", FCFS_party_list)
        report_list = []
        for fcfs_party in FCFS_party_list:
            # print("fcfs_party:", fcfs_party)
            for player, info in fcfs_party.items():
                if len(info) > 0:
                    report = [player, info[0]]
                    report_list.append(report)
        print("report_list : ", report_list)
        final_allocation = []
        final_report_list = copy.deepcopy(report_list)
        party_allocated_list = []
        for slot in report_list:
            if slot[0] not in party_allocated_list:
                if (
                    seat_allocate[str(int(slot[1][0][4]) + i)] + int(slot[1][0][-1])
                    <= 5
                ):
                    if (
                        capacity_allocate[str(int(slot[1][0][4]) + i)]
                        + int(slot[1][0][1])
                        <= 4
                    ):
                        final_allocation.append(slot)
                        party_allocated_list.append(slot[0])
                        seat_allocate[str(int(slot[1][0][4]) + i)] += int(
                            slot[1][0][-1]
                        )
                        capacity_allocate[str(int(slot[1][0][4]) + i)] += int(
                            slot[1][0][1]
                        )
        print("seat_allocate:", seat_allocate)
        print("final_allocation:", final_allocation)
        FCFS_party_preference_list_copy = copy.deepcopy(FCFS_party_preference_list)
        # print(FCFS_party_preference_list_copy)
        for fcfs_copy in FCFS_party_preference_list_copy:
            for key, values in fcfs_copy.items():
                if key in party_allocated_list or values == []:
                    FCFS_party_preference_list.remove(fcfs_copy)
        fcfs_len = len(FCFS_party_preference_list)
        # print("FCFS_party_preference_list:", FCFS_party_preference_list)
        for allo in final_allocation:
            table_revenue += int(allo[1][0][-1]) * 5
            course_revenue += allo[1][0].count("A") * 10 + allo[1][0].count("B") * 15
            utility_FCFS += allo[1][1]

        FCFS_revenue = table_revenue + course_revenue
        FCFS_social = FCFS_revenue + utility_FCFS
        total_FCFS_revenue += FCFS_revenue
        total_FCFS_utility += utility_FCFS
        total_FCFS_social += FCFS_social
        FCFS_revenue_list.append(FCFS_revenue)
        FCFS_utility_list.append(utility_FCFS)
        FCFS_social_list.append(FCFS_social)
        # print("seat_allocate:",seat_allocate)
        # print("capacity_allocate:",capacity_allocate)
        print("FCFS_revenue:", FCFS_revenue)
        # print("total_FCFS_revenue:", total_FCFS_revenue)
        print("FCFS_utility:", utility_FCFS)
        # print("total_FCFS_utility:", total_FCFS_utility)
        # print("total_FCFS_social:", total_FCFS_social)

        print("-------------------------------------")
        print("-----------------VCG-----------------")
        print("-------------------------------------")
        vcg_party_allocated_list = []

        VCG_party_sorted_2 = {}
        VCG_party_sorted_3 = {}
        VCG_revenue = 0
        VCG_utility = 0
        VCG_table_revenue = 0
        VCG_course_revenue = 0

        # print("party_list_vcg:", party_list_vcg)
        while len(VCG_party_list) < 5:
            VCG_party_list.append(party_list_vcg.pop(0))
        # print("party_list_vcg:", party_list_vcg)
        # print("VCG_party_list:", VCG_party_list)

        # 把昨天的预约成功的人的信息重新整合进今天的预约信息中
        vcg_allocation = []
        pre_day_allocated_party = []
        pre_day_allocated_party_2 = []
        pre_day_allocated_party_temp = []
        for seat_day_party in seat_allocate_vcg[str(1 + i)]:
            for pre_day_party in vcg_party_info_dict_dict[seat_day_party[0]]:
                pre_choice = list(pre_day_party[0][1])
                pre_choice[4] = str(int(pre_choice[4]) - 1)
                pre_choice = "".join(pre_choice)
                pre_day_party_tolist = list(pre_day_party)
                pre_day_party_tolist[0] = list(pre_day_party[0])
                pre_day_party_tolist[0][1] = pre_choice
                if pre_day_party_tolist[0][1][4] != "0":
                    pre_day_allocated_party_temp.append(pre_day_party_tolist)
            pre_day_allocated_party.append(pre_day_allocated_party_temp)
            pre_day_allocated_party_temp = []
        if len(pre_day_allocated_party) > 0:
            for lenp in range(len(pre_day_allocated_party)):
                VCG_party_list.append(pre_day_allocated_party[lenp])
        for seat_day_party in seat_allocate_vcg[str(2 + i)]:
            for pre_day_party in vcg_party_info_dict_dict[seat_day_party[0]]:
                pre_choice = list(pre_day_party[0][1])
                pre_choice[4] = str(int(pre_choice[4]) - 1)
                pre_choice = "".join(pre_choice)
                pre_day_party_tolist = list(pre_day_party)
                pre_day_party_tolist[0] = list(pre_day_party[0])
                pre_day_party_tolist[0][1] = pre_choice
                if pre_day_party_tolist[0][1][4] != "0":
                    pre_day_allocated_party_temp.append(pre_day_party_tolist)
            pre_day_allocated_party_2.append(pre_day_allocated_party_temp)
            pre_day_allocated_party_temp = []
            # print("pre_day_allocated_party_2:", pre_day_allocated_party_2)
        if len(pre_day_allocated_party_2) > 0:
            for lenp in range(len(pre_day_allocated_party_2)):
                VCG_party_list.append(pre_day_allocated_party_2[lenp])
        # 一个party一个party地执行vcg
        original_party_list = []
        possible_outcome_list = []
        possible_outcome_list_sorted = []
        for party_info_list in VCG_party_list:
            possible_outcome_list_temp = []
            original_party_list.append(party_info_list[0][0][0])
            # print("original_party_list:", original_party_list)
            # print("party_info_list:", party_info_list, len(party_info_list))
            for party_info_tuple in party_info_list[:]:
                party_info_tuple = list(party_info_tuple)
                # print("party_info_tuple:", party_info_tuple)
                for current_outcome in possible_outcome_list_sorted:
                    possible_outcome_list_temp.append(
                        current_outcome + party_info_tuple
                    )
            # print("possible_outcome_list:", possible_outcome_list)

            # print("original:", len(possible_outcome_list_temp))

            # print("new:", len(possible_outcome_list_temp))
            possible_outcome_list += possible_outcome_list_temp
            for party_info_tuple in party_info_list[:]:
                party_info_tuple = list(party_info_tuple)
                possible_outcome_list.insert(0, party_info_tuple)
            # 排序，取前100
            for outcome in possible_outcome_list:
                outcome_sv = 0
                for out in outcome:
                    if type(out) == int:
                        outcome_sv += out
                outcome.append(str(outcome_sv))

            # possible_outcome_list_sorted = sorted(
            #     possible_outcome_list, key=lambda x: int(x[-1]), reverse=True
            # )[:100]
            # print(
            #     "possible_outcome_list_sorted:",
            #     possible_outcome_list_sorted,
            #     len(possible_outcome_list_sorted),
            # )
            # 将不符合条件的outcome删除
            possible_outcome_list_copy = possible_outcome_list[:]
            for outcome_temp in possible_outcome_list_copy:
                table_day1 = 0
                table_day2 = 0
                table_day3 = 0
                for outcome_te in outcome_temp:
                    # print("outcome_te:", outcome_te)
                    if type(outcome_te) == tuple or type(outcome_te) == list:
                        if outcome_te[1][4] == "1":
                            table_day1 += int(outcome_te[1][-1])
                        elif outcome_te[1][4] == "2":
                            table_day2 += int(outcome_te[1][-1])
                        elif outcome_te[1][4] == "3":
                            table_day3 += int(outcome_te[1][-1])
                if table_day1 > 5 or table_day2 > 5 or table_day3 > 5:
                    possible_outcome_list.remove(outcome_temp)
            possible_outcome_list_sorted = sorted(
                possible_outcome_list, key=lambda x: int(x[-1]), reverse=True
            )
            # print(
            #     "new possible_outcome_list_sorted:",
            #     possible_outcome_list_sorted,
            # )
            # print(
            #     len(possible_outcome_list_sorted),
            # )
            # print("possible_outcome_list:", possible_outcome_list)
            # Define the VCG allocation for each round
            vcg_allocation = possible_outcome_list_sorted[:1]
            # 计算revenue
            vcg_social_value = 0

            for new_allo in vcg_allocation[0]:
                # print(new_allo)
                if type(new_allo) == tuple or type(new_allo) == list:
                    vcg_social_value += new_allo[2]
                    seat_allocate_copy = seat_allocate_vcg[
                        str(int(new_allo[1][4]) + i)
                    ][:]
                    for pre_day_party_info in seat_allocate_copy:
                        if pre_day_party_info not in vcg_allocation[0]:
                            seat_allocate_vcg[str(int(new_allo[1][4]) + i)].remove(
                                pre_day_party_info
                            )
                    if new_allo not in seat_allocate_vcg[str(int(new_allo[1][4]) + i)]:
                        vcg_party_allocated_list.append(new_allo[0])
                        optimal_party_allocation.append(new_allo[0])
                        seat_allocate_vcg[str(int(new_allo[1][4]) + i)].append(new_allo)
        print("vcg_social_value:", vcg_social_value)
        print("vcg_allocation:", vcg_allocation)
        # calculate cancellations for the current day
        remain_party_list = []
        party_cancelled = 0
        for party in vcg_allocation[0]:
            if type(party) == tuple or type(party) == list:
                remain_party_list.append(party[0])
        # print("remain_party_list:", remain_party_list)
        for op in set(vcg_party_allocated_list):
            if op not in remain_party_list:
                party_cancelled += 1
        print(set(vcg_party_allocated_list))
        print("party_cancelled:", party_cancelled)
        total_cancellations += party_cancelled
        # calculate monetary transfer
        vcg_utility = 0
        for seat_allo in seat_allocate_vcg[str(1 + i)]:
            vcg_social_part1 = vcg_social_value - (seat_allo[-1])
            print("seat_all for day ", i, ":", seat_allo)
            VCG_party_list_copy = VCG_party_list
            sepossible_outcome_list_sorted = []
            sepossible_outcome_list = []
            for separty_info_list in VCG_party_list:
                # print(separty_info_list[0][0][0], seat_allo[0])
                if separty_info_list[0][0][0] == seat_allo[0]:
                    VCG_party_list_copy.remove(separty_info_list)
                    # print(len(VCG_party_list_copy))
            for separty_info_list in VCG_party_list_copy:
                sevcg_social_value = 0
                sepossible_outcome_list_temp = []
                # print("separty_info_list:", separty_info_list, len(separty_info_list))
                for separty_info_tuple in separty_info_list[:]:
                    separty_info_tuple = list(separty_info_tuple)
                    # print("party_info_tuple:", party_info_tuple)
                    for securrent_outcome in sepossible_outcome_list_sorted:
                        sepossible_outcome_list_temp.append(
                            securrent_outcome + separty_info_tuple
                        )
                sepossible_outcome_list += sepossible_outcome_list_temp
                for separty_info_tuple in separty_info_list[:]:
                    separty_info_tuple = list(separty_info_tuple)
                    sepossible_outcome_list.insert(0, separty_info_tuple)
                # 排序，取前100
                for seoutcome in sepossible_outcome_list:
                    seoutcome_sv = 0
                    for seout in seoutcome:
                        if type(seout) == int:
                            seoutcome_sv += seout
                    seoutcome.append(str(seoutcome_sv))

                # print("sepossible_outcome_list_sorted:", sepossible_outcome_list_sorted)
                # print(len(sepossible_outcome_list_sorted))
                # 将不符合条件的outcome删除
                sepossible_outcome_list_copy = sepossible_outcome_list[:]
                for seoutcome_temp in sepossible_outcome_list_copy:
                    setable_day1 = 0
                    setable_day2 = 0
                    setable_day3 = 0
                    for seoutcome_te in seoutcome_temp:
                        # print("outcome_te:", outcome_te)
                        if type(seoutcome_te) == tuple or type(seoutcome_te) == list:
                            if seoutcome_te[1][4] == "1":
                                setable_day1 += int(seoutcome_te[1][-1])
                            elif seoutcome_te[1][4] == "2":
                                setable_day2 += int(seoutcome_te[1][-1])
                            elif seoutcome_te[1][4] == "3":
                                setable_day3 += int(seoutcome_te[1][-1])
                    if setable_day1 > 5 or setable_day2 > 5 or setable_day3 > 5:
                        sepossible_outcome_list.remove(seoutcome_temp)

                sepossible_outcome_list_sorted = sorted(
                    sepossible_outcome_list,
                    key=lambda x: int(x[-1]),
                    reverse=True,
                )
                # print(
                #     "new sepossible_outcome_list_sorted:",
                #     sepossible_outcome_list_sorted,
                # )
                # print(
                #     len(sepossible_outcome_list_sorted),
                # )
                # print("possible_outcome_list:", possible_outcome_list)
            # Define the VCG allocation for each round
            # print("sepossible_outcome_list_sorted:", sepossible_outcome_list_sorted)
            sevcg_allocation = sepossible_outcome_list_sorted[:1]
            for sevcg in sevcg_allocation[0]:
                # 计算revenue
                # print("sevcg_allocation:", sevcg_allocation)
                if type(sevcg) == tuple or type(sevcg) == list:
                    sevcg_social_value += sevcg[-1]
            monetary_transfer = sevcg_social_value - vcg_social_part1
            vcg_utility += seat_allo[-1] - monetary_transfer
            VCG_revenue += (
                monetary_transfer
                + seat_allo[1].count("A") * 10
                + seat_allo[1].count("B") * 15
                - party_cancelled * 0
            )
            print("sevcg_social_value:", sevcg_social_value)
            print("sevcg_allocation:", sevcg_allocation)
            final_allocated_party_list.append(seat_allo[0])
        print("VCG revenue:", VCG_revenue)
        print("seat_allocate_vcg:", seat_allocate_vcg)
        # print("optimal_party_allocation:", optimal_party_allocation)
        # print("final_allocated_party_list:", final_allocated_party_list)
        VCG_revenue_list.append(VCG_revenue)
        VCG_social_list.append(vcg_social_value)
        VCG_utility_list.append(vcg_utility)
        VCG_party_list = []
        wandb.log(
            {
                "FCFS_revenue": FCFS_revenue,
                "VCG_revenue": VCG_revenue,
            }
        )
    wandb.finish(exit_code=1)
    for allo_party in set(optimal_party_allocation):
        # print("allo_party:", allo_party)
        # if allo_party not in final_allocated_party_list:
        #     party_cancelled += 1
        # else:
        if optimal_party_allocation.count(allo_party) > 1:
            party_changed += 1
    # print(party_cancelled, party_changed)
    total_VCG_revenue_list.append(sum(VCG_revenue_list))
    total_FCFS_revenue_list.append(total_FCFS_revenue)
    print("VCG_revenue_list:", VCG_revenue_list)
    print("VCG_social_list:", VCG_social_list)
    print("VCG_utility_list:", VCG_utility_list)
    print("total vcg revenue:", sum(VCG_revenue_list))
    print("FCFS revenue list:", FCFS_revenue_list)
    print("FCFS_social_list:", FCFS_social_list)
    print("FCFS_utility_list:", FCFS_utility_list)
    print("total fcfs revenue:", sum(FCFS_revenue_list))

    # columns = ["FCFS_revenue", "VCG_revenue"]
    # revenue_dict = {
    #     "FCFS_revenue": FCFS_revenue_list,
    #     "VCG_revenue": VCG_revenue_list,
    # }
    # revenue_data = pd.DataFrame(revenue_dict)
    # xs = [i for i in range(30)]
    # ys = [revenue_data[c][:30] for c in columns]

    # wandb.log(
    #     {
    #         "restaurant_revenue": wandb.plot.line_series(
    #             xs=xs, ys=ys, keys=columns, title="Restaurant Revenue"
    #         )
    #     }
    # )

#         # columns = ["FCFS_utility", "VCG_utility"]
#         # utility_dict = {
#         #     "FCFS_utility": FCFS_utility_list,
#         #     "VCG_utility": VCG_utility_list,
#         # }
#         # utility_data = pd.DataFrame(utility_dict)
#         # xs = [i for i in range(30)]
#         # ys = [utility_data[c][:30] for c in columns]

#         # wandb.log(
#         #     {
#         #         f"utility_run{run}": wandb.plot.line_series(
#         #             xs=xs, ys=ys, keys=columns, title="Utility Metrix"
#         #         )
#         #     }
#         # )

#         # columns = ["FCFS_social", "VCG_social"]
#         # social_dict = {"FCFS_social": FCFS_social_list, "VCG_social": VCG_social_list}
#         # social_data = pd.DataFrame(social_dict)
#         # xs = [i for i in range(30)]
#         # ys = [social_data[c][:30] for c in columns]

#         # wandb.log(
#         #     {
#         #         f"social_run{run}": wandb.plot.line_series(
#         #             xs=xs, ys=ys, keys=columns, title="Social Value Metrix"
#         #         )
#         #     }
#         # )

columns = ["Total_FCFS_revenue", "Total_VCG_revenue"]
revenue_dict = {
    "Total_FCFS_revenue": total_FCFS_revenue_list,
    "Total_VCG_revenue": total_VCG_revenue_list,
}
revenue_data = pd.DataFrame(revenue_dict)
xs = [i for i in range(num_steps)]
ys = [revenue_data[c][:num_steps] for c in columns]

# columns_u = ["Total_FCFS_utility", "Total_VCG_utility"]
# utility_dict = {
#     "Total_FCFS_utility": total_FCFS_utility_list,
#     "Total_VCG_utility": total_VCG_utility_list,
# }
# utility_data = pd.DataFrame(utility_dict)
# xs_u = [i for i in range(num_steps)]
# ys_u = [utility_data[c][:num_steps] for c in columns_u]

# columns_s = ["Total_FCFS_social", "Total_VCG_social"]
# social_dict = {
#     "Total_FCFS_social": total_FCFS_social_list,
#     "Total_VCG_social": total_VCG_social_list,
# }
# social_data = pd.DataFrame(social_dict)
# xs_s = [i for i in range(num_steps)]
# ys_s = [social_data[c][:num_steps] for c in columns_s]
wandb.init(
    entity="dbx",
    project="VCG_Booking",
    group="FCFS_res_fee0_VCG_cancel_fee0",
    name="total_revenue_comparison",
)
wandb.log(
    {
        "total_rev": wandb.plot.line_series(
            xs=xs, ys=ys, keys=columns, title="Total Restaurant Revenue"
        )
    }
)

# # wandb.log(
# #     {
# #         "total_uti": wandb.plot.line_series(
# #             xs=xs_u, ys=ys_u, keys=columns_u, title="Total Utility Metrix"
# #         )
# #     }
# # )

# # wandb.log(
# #     {
# #         "total_soc": wandb.plot.line_series(
# #             xs=xs_s, ys=ys_s, keys=columns_s, title="Total Social Value Metrix"
# #         )
# #     }
# # )

import re
from traceback import print_tb
from numpy.lib.function_base import average
import pandas as pd
import random
import itertools
import copy
import wandb

# wandb.init(
#     entity="vaccine_booking",
#     project="VCG_Booking",
#     group="Dynamic_Seats_5",
#     name="five_reservation_fee",
# )
# table = 5, course = 2
num_steps = 1
total_FCFS_revenue_list = []
total_FCFS_utility_list = []
total_FCFS_social_list = []
total_VCG_revenue_list = []
total_VCG_utility_list = []
total_VCG_social_list = []
for run in range(num_steps):
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
        while len(party_list) < 60:
            party_name = len(party_list)
            party_size = random.randint(1, 4)
            party_info = {}
            for course in itertools.product("AB", repeat=party_size):
                for day in range(1, days + 1):
                    if party_size == 1:
                        for table in range(party_size, 6):
                            if table == 1:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(1, 5)
                            if table == 2:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(2, 9)
                            if table == 3:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(3, 12)
                            if table == 4:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 14)
                            if table == 5:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 15)
                    if party_size == 2:
                        for table in range(party_size, 6):
                            if table == 2:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(2, 10)
                            if table == 3:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(3, 14)
                            if table == 4:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 18)
                            if table == 5:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 21)
                    if party_size == 3:
                        for table in range(party_size, 6):
                            if table == 3:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(3, 15)
                            if table == 4:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 19)
                            if table == 5:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(5, 23)
                    if party_size == 4:
                        for table in range(party_size, 6):
                            if table == 4:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
                                ] = random.randint(4, 20)
                            if table == 5:
                                party_info[
                                    f"p{party_name}_s{party_size}_d{day}_{course}_t{table}"
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
    party_list_vcg = copy.deepcopy(party_list)
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

    for i in range(0, 33):
        seat_allocate[str(i)] = 0
        capacity_allocate[str(i)] = 0
        seat_allocate_vcg[str(i)] = []
        capacity_allocate_vcg[str(i)] = 0
    for i in range(3):  # simulation period
        FCFS_party_list = []
        FCFS_revenue = 0
        table_revenue = 0
        course_revenue = 0
        utility_FCFS = 0
        while len(FCFS_party_preference_list) < 5:
            FCFS_party_preference_list.append(party_list_fcfs.pop(0))
            FCFS_party_preference_dict = {}
            for key, value in FCFS_party_preference_list[-1].items():
                # key = key.replace("_"," ").replace("(", "").replace(")", "").replace(",", "").replace("'", "").split()
                if key[-1] == "1":
                    value = value - 5
                if key[-1] == "2":
                    value = value - 10
                if key[-1] == "3":
                    value = value - 15
                if key[-1] == "4":
                    value = value - 20
                if key[-1] == "5":
                    value = value - 25
                if value >= 0:
                    FCFS_party_preference_dict[key] = value
            FCFS_party_list.append(FCFS_party_preference_dict)
        # print("FCFS_party_list:", FCFS_party_list)
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
            report = sorted(fcfs_party.items(), key=lambda x: x[1], reverse=True)
            # print(report)
            if len(report) > 0:
                report_list.append(report[0])
        print("report_list : ", report_list)
        final_allocation = []
        final_report_list = copy.deepcopy(report_list)
        party_allocated_list = []
        for slot in report_list:
            if slot[0][2] == "_":
                if slot[0][1] not in party_allocated_list:
                    if seat_allocate[str(int(slot[0][7]) + i)] + int(slot[0][-1]) <= 5:
                        if (
                            capacity_allocate[str(int(slot[0][7]) + i)]
                            + int(slot[0][4])
                            <= 4
                        ):
                            final_allocation.append(slot)
                            party_allocated_list.append(slot[0][1])
                            seat_allocate[str(int(slot[0][7]) + i)] += int(slot[0][-1])
                            capacity_allocate[str(int(slot[0][7]) + i)] += int(
                                slot[0][4]
                            )
            else:
                if (slot[0][1] + slot[0][2]) not in party_allocated_list:
                    if seat_allocate[str(int(slot[0][8]) + i)] + int(slot[0][-1]) <= 5:
                        if (
                            capacity_allocate[str(int(slot[0][8]) + i)]
                            + int(slot[0][5])
                            <= 4
                        ):
                            final_allocation.append(slot)
                            party_allocated_list.append((slot[0][1] + slot[0][2]))
                            seat_allocate[str(int(slot[0][8]) + i)] += int(slot[0][-1])
                            capacity_allocate[str(int(slot[0][8]) + i)] += int(
                                slot[0][5]
                            )
        print("seat_allocate:", seat_allocate)
        print("final_allocation:", final_allocation)
        FCFS_party_preference_list_copy = copy.deepcopy(FCFS_party_preference_list)
        for fcfs_copy in FCFS_party_preference_list_copy:
            for key in fcfs_copy.keys():
                if key[2] == "_" and key[1] in party_allocated_list:
                    FCFS_party_preference_list.remove(fcfs_copy)
                    break
                elif key[2] != "_" and (key[1] + key[2]) in party_allocated_list:
                    FCFS_party_preference_list.remove(fcfs_copy)
                    break
        fcfs_len = len(FCFS_party_preference_list)
        # print("FCFS_party_preference_list:", FCFS_party_preference_list)
        for allo in final_allocation:
            table_revenue += int(allo[0][-1]) * 5
            course_revenue += allo[0].count("A") * 10 + allo[0].count("B") * 15
            utility_FCFS += allo[-1]

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
        print("total_FCFS_revenue:", total_FCFS_revenue)
        print("FCFS_utility:", utility_FCFS)
        print("total_FCFS_utility:", total_FCFS_utility)
        print("total_FCFS_social:", total_FCFS_social)

        VCG_party_list_sorted = []
        VCG_party_sorted = {}
        VCG_party_sorted_2 = {}
        VCG_party_sorted_3 = {}
        VCG_revenue = 0
        VCG_utility = 0
        VCG_table_revenue = 0
        VCG_course_revenue = 0
        while len(VCG_party_list) < 5:
            VCG_party_list.append(party_list_vcg.pop(0))
        # print("VCG_party_list:", VCG_party_list)
        for vcg_party in VCG_party_list:
            for key, value in vcg_party.items():
                if key[2] == "_" and key[7] == "1":
                    VCG_party_sorted[key] = value
                elif key[2] != "_" and key[8] == "1":
                    VCG_party_sorted[key] = value
                elif key[2] == "_" and key[7] == "2":
                    VCG_party_sorted_2[key] = value
                elif key[2] != "_" and key[8] == "2":
                    VCG_party_sorted_2[key] = value
                elif key[2] == "_" and key[7] == "3":
                    VCG_party_sorted_3[key] = value
                elif key[2] != "_" and key[8] == "3":
                    VCG_party_sorted_3[key] = value
        VCG_party_list_sorted.append(VCG_party_sorted)
        VCG_party_list_sorted.append(VCG_party_sorted_2)
        VCG_party_list_sorted.append(VCG_party_sorted_3)
        print(f"---------------DAY{i}----------------")
        party_name_last_day_list = []
        for vcg_day in range(len(VCG_party_list_sorted)):
            VCG_setup_preference_dict = {}
            VCG_setup_preference_dict[1] = []
            VCG_setup_preference_dict[2] = []
            VCG_setup_preference_dict[3] = []
            VCG_setup_preference_dict[4] = []
            VCG_setup_preference_dict[5] = []
            len_last_day = len(seat_allocate_vcg[str(vcg_day + i + 1)])
            if len_last_day > 0:
                for party_info in seat_allocate_vcg[str(vcg_day + i + 1)]:
                    # print(party_info)
                    VCG_party_list_sorted[vcg_day][party_info[0]] = party_info[1]
            if len(seat_allocate_vcg[str(vcg_day + i)]) > 0:
                for party_info in seat_allocate_vcg[str(vcg_day + i)]:
                    if party_info[0][2] == "_":
                        party_name_last_day_list.append(party_info[0][1])
                    else:
                        party_name_last_day_list.append(party_info[0][1:3])
                print("party_name_last_day_list:", party_name_last_day_list)
            # print("VCG_party_list_sorted:", VCG_party_list_sorted[vcg_day])
            for key, value in VCG_party_list_sorted[vcg_day].items():
                if (key[2] == "_" and key[1] not in party_name_last_day_list) or (
                    key[2] != "_" and key[1:3] not in party_name_last_day_list
                ):
                    if key[-1] == "1":
                        VCG_setup_preference_dict[1].append((key, value))
                    elif key[-1] == "2":
                        VCG_setup_preference_dict[2].append((key, value))
                    elif key[-1] == "3":
                        VCG_setup_preference_dict[3].append((key, value))
                    elif key[-1] == "4":
                        VCG_setup_preference_dict[4].append((key, value))
                    elif key[-1] == "5":
                        VCG_setup_preference_dict[5].append((key, value))
            # print("VCG_setup_preference_dict:", VCG_setup_preference_dict)
            for table, info in VCG_setup_preference_dict.items():
                if table == 1:
                    report_table1 = sorted(info, key=lambda x: x[-1], reverse=True)
                if table == 2:
                    report_table2 = sorted(info, key=lambda x: x[-1], reverse=True)
                if table == 3:
                    report_table3 = sorted(info, key=lambda x: x[-1], reverse=True)
                if table == 4:
                    report_table4 = sorted(info, key=lambda x: x[-1], reverse=True)
                if table == 5:
                    report_table5 = sorted(info, key=lambda x: x[-1], reverse=True)
            vcg_report_list = [
                report_table1,
                report_table2,
                report_table3,
                report_table4,
                report_table5,
            ]
            # print(report_table1)
            # print(report_table2)
            # print(report_table3)
            # print(report_table4)
            # print(report_table5)
            vcg_report_no_repeat_list = []
            for vcg_report in vcg_report_list:
                vcg_report_no_repeat = []
                party_name_list = []
                for report in vcg_report:
                    if report[0][2] == "_" and report[0][1] not in party_name_list:
                        vcg_report_no_repeat.append(report)
                        party_name_list.append(report[0][1])
                    if report[0][2] != "_" and report[0][1:3] not in party_name_list:
                        vcg_report_no_repeat.append(report)
                        party_name_list.append(report[0][1:3])
                    set(party_name_list)
                    # print(vcg_report_no_repeat)
                vcg_report_no_repeat_list.append(vcg_report_no_repeat)
            report_table1 = vcg_report_no_repeat_list[0]
            report_table2 = vcg_report_no_repeat_list[1]
            report_table3 = vcg_report_no_repeat_list[2]
            report_table4 = vcg_report_no_repeat_list[3]
            report_table5 = vcg_report_no_repeat_list[4]
            print(report_table1)
            print(report_table2)
            print(report_table3)
            print(report_table4)
            print(report_table5)
            # outcome 1*4
            outcome1_list = []
            value_1 = 0
            for can in report_table1:
                outcome1_list.append(can)
                if len(outcome1_list) >= 4:
                    break
            for outcome in outcome1_list:
                value_1 = value_1 + outcome[-1]
            print("outcome1 : ", outcome1_list)
            # outcome 2*2+1
            outcome2_list = []
            value_2 = 0
            player_2 = []
            for can in report_table2:
                outcome2_list.append(can)
                if can[0][2] == "_":
                    player_2.append(can[0][1])
                else:
                    player_2.append(can[0][1:3])
                if len(outcome2_list) >= 2:
                    break
            seat_sum = 0
            cap_sum = 0
            for outcome in outcome2_list:
                if outcome[0][2] == "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][4])
                elif outcome[0][2] != "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][5])
            if report_table1[0][0][2] == "_":
                if report_table1[0][0][1] not in player_2:
                    if seat_sum >= 5 or cap_sum >= 4:
                        break
                    outcome2_list.append(report_table1[0])
            if report_table1[0][0][2] != "_":
                if report_table1[0][0][1:3] not in player_2:
                    if seat_sum >= 5 or cap_sum >= 4:
                        break
                    outcome2_list.append(report_table1[0])
            for outcome in outcome2_list:
                value_2 = value_2 + outcome[-1]
            print("outcome2 : ", outcome2_list)
            # outcome for 2+1*3
            outcome3_list = []
            value_3 = 0
            player_3 = []
            for can in report_table2:
                outcome3_list.append(can)
                if can[0][2] == "_":
                    player_3.append(can[0][1])
                else:
                    player_3.append(can[0][1:3])
                if len(outcome3_list) >= 1:
                    break
            seat_sum = 0
            cap_sum = 0
            for outcome in outcome3_list:
                if outcome[0][2] == "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][4])
                elif outcome[0][2] != "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][5])
            for can in report_table1:
                if can[0][2] == "_":
                    if can[0][1] not in player_3:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome3_list.append(can)
                if can[0][2] != "_":
                    if can[0][1:3] not in player_3:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome3_list.append(can)
            for outcome in outcome3_list:
                value_3 = value_3 + outcome[-1]
            print("outcome3 : ", outcome3_list)
            # outcome for 3+2
            outcome4_list = []
            value_4 = 0
            player_4 = []
            for can in report_table3:
                outcome4_list.append(can)
                if can[0][2] == "_":
                    player_4.append(can[0][1])
                elif can[0][2] != "_":
                    player_4.append(can[0][1:3])
                if len(outcome4_list) >= 1:
                    break
            for outcome in outcome4_list:
                if outcome[0][2] == "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][4])
                elif outcome[0][2] != "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][5])
            for can in report_table2:
                if can[0][2] == "_":
                    if can[0][1] not in player_4:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome4_list.append(can)
                if can[0][2] != "_":
                    if can[0][1:3] not in player_4:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome4_list.append(can)
            for outcome in outcome4_list:
                value_4 = value_4 + outcome[-1]
            print("outcome4 : ", outcome4_list)
            # outcome for 3+1+1
            outcome5_list = []
            value_5 = 0
            player_5 = []
            for can in report_table3:
                outcome5_list.append(can)
                if can[0][2] == "_":
                    player_5.append(can[0][1])
                elif can[0][2] != "_":
                    player_5.append(can[0][1:3])
                if len(outcome5_list) >= 1:
                    break
            for outcome in outcome5_list:
                if outcome[0][2] == "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][4])
                elif outcome[0][2] != "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][5])
            for can in report_table1:
                if can[0][2] == "_":
                    if can[0][1] not in player_5:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome5_list.append(can)
                if can[0][2] != "_":
                    if can[0][1:3] not in player_5:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome5_list.append(can)
            for outcome in outcome5_list:
                value_5 = value_5 + outcome[-1]
            print("outcome5 : ", outcome5_list)
            # outcome for 4+1
            outcome6_list = []
            value_6 = 0
            player_6 = []
            for can in report_table4:
                outcome6_list.append(can)
                if can[0][2] == "_":
                    player_6.append(can[0][1])
                elif can[0][2] != "_":
                    player_6.append(can[0][1:3])
                if len(outcome6_list) >= 1:
                    break
            for outcome in outcome4_list:
                if outcome[0][2] == "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][4])
                elif outcome[0][2] != "_":
                    seat_sum += int(outcome[0][-1])
                    cap_sum += int(outcome[0][5])
            for can in report_table1:
                if can[0][2] == "_":
                    if can[0][1] not in player_6:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome6_list.append(can)
                if can[0][2] != "_":
                    if can[0][1:3] not in player_6:
                        if seat_sum >= 5:
                            break
                        if cap_sum >= 4:
                            break
                        outcome6_list.append(can)
            for outcome in outcome6_list:
                value_6 = value_6 + outcome[-1]
            print("outcome6 : ", outcome6_list)
            # outcome for 5
            outcome7_list = []
            value_7 = 0
            for can in report_table5:
                outcome7_list.append(can)
                if len(outcome7_list) >= 1:
                    break
            for outcome in outcome7_list:
                value_7 = value_7 + outcome[-1]
            print("outcome7 : ", outcome7_list)
            outcomes_list = [
                outcome1_list,
                outcome2_list,
                outcome3_list,
                outcome4_list,
                outcome5_list,
                outcome6_list,
                outcome7_list,
            ]
            values = [
                value_1,
                value_2,
                value_3,
                value_4,
                value_5,
                value_6,
                value_7,
            ]
            report_table1_copy = copy.deepcopy(report_table1)
            report_table2_copy = copy.deepcopy(report_table2)
            report_table3_copy = copy.deepcopy(report_table3)
            report_table4_copy = copy.deepcopy(report_table4)
            report_table5_copy = copy.deepcopy(report_table5)
            # find the optimal outcome
            for a in range(len(values)):
                value_a = values[a]
                if value_a == max(values):
                    social_value = value_a
                    for m in range(len(outcomes_list)):
                        outcome_m = outcomes_list[m]
                        if m == a:
                            print("optimal allocation : ", outcome_m)
                            seats_value = 0
                            for outcome in outcome_m:
                                seats_value += outcome[1]
                                # if outcome[0][2] == "_":
                                #     optimal_party_allocation.append(outcome[0][1])
                                # else:
                                #     optimal_party_allocation.append(outcome[0][1:3])
                            if len_last_day > 0:
                                for party_info in seat_allocate_vcg[
                                    str(vcg_day + i + 1)
                                ]:
                                    print("party_info:", party_info)
                                    print("outcome_m:", outcome_m)
                                    if party_info not in outcome_m:
                                        reject_parties_list.append(party_info)
                            seat_allocate_vcg[str(vcg_day + i + 1)] = outcome_m
                            print("seat_allocate_vcg : ", seat_allocate_vcg)
                            print("best_seats_value : ", seats_value)
                            for p in outcome_m:
                                # calcluate second price
                                if p[0][2] == "_":
                                    report_table1 = [
                                        k
                                        for k in report_table1_copy
                                        if k[0][1] != p[0][1]
                                    ]
                                    report_table2 = [
                                        k
                                        for k in report_table2_copy
                                        if k[0][1] != p[0][1]
                                    ]
                                    report_table3 = [
                                        k
                                        for k in report_table3_copy
                                        if k[0][1] != p[0][1]
                                    ]
                                    report_table4 = [
                                        k
                                        for k in report_table4_copy
                                        if k[0][1] != p[0][1]
                                    ]
                                    report_table5 = [
                                        k
                                        for k in report_table5_copy
                                        if k[0][1] != p[0][1]
                                    ]
                                elif p[0][2] != "_":
                                    report_table1 = [
                                        k
                                        for k in report_table1_copy
                                        if k[0][1:3] != p[0][1:3]
                                    ]
                                    report_table2 = [
                                        k
                                        for k in report_table2_copy
                                        if k[0][1:3] != p[0][1:3]
                                    ]
                                    report_table3 = [
                                        k
                                        for k in report_table3_copy
                                        if k[0][1:3] != p[0][1:3]
                                    ]
                                    report_table4 = [
                                        k
                                        for k in report_table4_copy
                                        if k[0][1:3] != p[0][1:3]
                                    ]
                                    report_table5 = [
                                        k
                                        for k in report_table5_copy
                                        if k[0][1:3] != p[0][1:3]
                                    ]
                                # outcome 1*4
                                outcome1_list = []
                                value_1 = 0
                                for can in report_table1:
                                    outcome1_list.append(can)
                                    if len(outcome1_list) >= 4:
                                        break
                                for outcome in outcome1_list:
                                    value_1 = value_1 + outcome[-1]
                                print("outcome1 : ", outcome1_list)
                                # outcome 2*2+1
                                outcome2_list = []
                                value_2 = 0
                                player_2 = []
                                for can in report_table2:
                                    outcome2_list.append(can)
                                    if can[0][2] == "_":
                                        player_2.append(can[0][1])
                                    else:
                                        player_2.append(can[0][1:3])
                                    if len(outcome2_list) >= 2:
                                        break
                                seat_sum = 0
                                cap_sum = 0
                                for outcome in outcome2_list:
                                    if outcome[0][2] == "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][4])
                                    elif outcome[0][2] != "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][5])
                                for can in report_table1:
                                    if can[0][2] == "_":
                                        if can[0][1] not in player_2:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome2_list.append(can)
                                    if can[0][2] != "_":
                                        if can[0][1:3] not in player_2:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome2_list.append(can)
                                for outcome in outcome2_list:
                                    value_2 = value_2 + outcome[-1]
                                print("outcome2 : ", outcome2_list)
                                # outcome for 2+1*3
                                outcome3_list = []
                                value_3 = 0
                                player_3 = []
                                for can in report_table2:
                                    outcome3_list.append(can)
                                    if can[0][2] == "_":
                                        player_3.append(can[0][1])
                                    else:
                                        player_3.append(can[0][1:3])
                                    if len(outcome3_list) >= 1:
                                        break
                                seat_sum = 0
                                cap_sum = 0
                                for outcome in outcome3_list:
                                    if outcome[0][2] == "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][4])
                                    elif outcome[0][2] != "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][5])
                                for can in report_table1:
                                    if can[0][2] == "_":
                                        if can[0][1] not in player_3:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome3_list.append(can)
                                    if can[0][2] != "_":
                                        if can[0][1:3] not in player_3:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome3_list.append(can)
                                for outcome in outcome3_list:
                                    value_3 = value_3 + outcome[-1]
                                print("outcome3 : ", outcome3_list)
                                # outcome for 3+2
                                outcome4_list = []
                                value_4 = 0
                                player_4 = []
                                for can in report_table3:
                                    outcome4_list.append(can)
                                    if can[0][2] == "_":
                                        player_4.append(can[0][1])
                                    elif can[0][2] != "_":
                                        player_4.append(can[0][1:3])
                                    if len(outcome4_list) >= 1:
                                        break
                                for outcome in outcome4_list:
                                    if outcome[0][2] == "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][4])
                                    elif outcome[0][2] != "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][5])
                                for can in report_table2:
                                    if can[0][2] == "_":
                                        if can[0][1] not in player_4:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome4_list.append(can)
                                    if can[0][2] != "_":
                                        if can[0][1:3] not in player_4:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome4_list.append(can)
                                for outcome in outcome4_list:
                                    value_4 = value_4 + outcome[-1]
                                print("outcome4 : ", outcome4_list)
                                # outcome for 3+1+1
                                outcome5_list = []
                                value_5 = 0
                                player_5 = []
                                for can in report_table3:
                                    outcome5_list.append(can)
                                    if can[0][2] == "_":
                                        player_5.append(can[0][1])
                                    elif can[0][2] != "_":
                                        player_5.append(can[0][1:3])
                                    if len(outcome5_list) >= 1:
                                        break
                                for outcome in outcome5_list:
                                    if outcome[0][2] == "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][4])
                                    elif outcome[0][2] != "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][5])
                                for can in report_table1:
                                    if can[0][2] == "_":
                                        if can[0][1] not in player_5:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome5_list.append(can)
                                    if can[0][2] != "_":
                                        if can[0][1:3] not in player_5:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome5_list.append(can)
                                for outcome in outcome5_list:
                                    value_5 = value_5 + outcome[-1]
                                print("outcome5 : ", outcome5_list)
                                # outcome for 4+1
                                outcome6_list = []
                                value_6 = 0
                                player_6 = []
                                for can in report_table4:
                                    outcome6_list.append(can)
                                    if can[0][2] == "_":
                                        player_6.append(can[0][1])
                                    elif can[0][2] != "_":
                                        player_6.append(can[0][1:3])
                                    if len(outcome6_list) >= 1:
                                        break
                                for outcome in outcome4_list:
                                    if outcome[0][2] == "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][4])
                                    elif outcome[0][2] != "_":
                                        seat_sum += int(outcome[0][-1])
                                        cap_sum += int(outcome[0][5])
                                for can in report_table1:
                                    if can[0][2] == "_":
                                        if can[0][1] not in player_6:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome6_list.append(can)
                                    if can[0][2] != "_":
                                        if can[0][1:3] not in player_6:
                                            if seat_sum >= 5:
                                                break
                                            if cap_sum >= 4:
                                                break
                                            outcome6_list.append(can)
                                for outcome in outcome6_list:
                                    value_6 = value_6 + outcome[-1]
                                print("outcome6 : ", outcome6_list)
                                # outcome for 5
                                outcome7_list = []
                                value_7 = 0
                                for can in report_table5:
                                    outcome7_list.append(can)
                                    if len(outcome7_list) >= 1:
                                        break
                                for outcome in outcome7_list:
                                    value_7 = value_7 + outcome[-1]
                                print("outcome7 : ", outcome7_list)
                                outcomes_list = [
                                    outcome1_list,
                                    outcome2_list,
                                    outcome3_list,
                                    outcome4_list,
                                    outcome5_list,
                                    outcome6_list,
                                    outcome7_list,
                                ]
                                values = [
                                    value_1,
                                    value_2,
                                    value_3,
                                    value_4,
                                    value_5,
                                    value_6,
                                    value_7,
                                ]
                                for n in range(len(values)):
                                    if values[n] == max(values):
                                        second_value = values[n]
                                        for o in range(len(outcomes_list)):
                                            if o == n:
                                                print(
                                                    "second best allocation : ",
                                                    outcomes_list[o],
                                                )
                                                second_seats_value = 0
                                                for second_outcome in outcomes_list[o]:
                                                    second_seats_value += (
                                                        second_outcome[1]
                                                    )
                                                print(
                                                    "second_best_value : ",
                                                    second_seats_value,
                                                )
                                                monetary_transfer = -(
                                                    seats_value
                                                    - p[1]
                                                    - second_seats_value
                                                )
                                                VCG_revenue = (
                                                    VCG_revenue
                                                    + p[0].count("A") * 10
                                                    + p[0].count("B") * 15
                                                    + monetary_transfer
                                                )
                                                VCG_utility += p[1] - monetary_transfer
                                                break
                                        break
                            break
                    break
        print("seat_allocate_vcg:", seat_allocate_vcg)
        VCG_social = VCG_revenue + VCG_utility
        VCG_revenue_list.append(VCG_revenue)
        VCG_utility_list.append(VCG_utility)
        VCG_social_list.append(VCG_social)
        total_VCG_revenue += VCG_revenue
        total_VCG_utility += VCG_utility
        total_VCG_social += VCG_social
        VCG_party_list = []
        # VCG_party_list_copy = copy.deepcopy(VCG_party_list)
        # for VCG_party in VCG_party_list_copy:
        #     print(VCG_party)
        #     for party_info in seat_allocate_vcg.values():
        #         print(party_info)
        #         if VCG_party in party_info:
        #             VCG_party_list.remove(VCG_party)
        # for key, value in VCG_party.items():
        #     if key[2] == "_":
        #         if key[1] in optimal_party_allocation:
        #             VCG_party_list.remove(VCG_party)
        #             break
        #     elif key[2] != "_":
        #         if key[1:3] in optimal_party_allocation:
        #             VCG_party_list.remove(VCG_party)
        #             break
        # print("optimal_party_allocation:", optimal_party_allocation)
        print("VCG_revenue : ", VCG_revenue)
        print("total_VCG_revenue : ", total_VCG_revenue)
        print("total_VCG_utility : ", total_VCG_utility)
        print("total_VCG_social : ", total_VCG_social)
        print("reject_parties:", reject_parties_list)
    total_FCFS_revenue_list.append(total_FCFS_revenue)
    total_VCG_revenue_list.append(total_VCG_revenue)
    total_FCFS_utility_list.append(total_FCFS_utility)
    total_VCG_utility_list.append(total_VCG_utility)
    total_FCFS_social_list.append(total_FCFS_social)
    total_VCG_social_list.append(total_VCG_social)

    # print(total_FCFS_revenue_list,total_VCG_revenue_list)
    # print(total_FCFS_utility_list,total_VCG_utility_list)
    # print(total_FCFS_social_list,total_VCG_social_list)
    if run == 0:
        columns = ["FCFS_revenue", "VCG_revenue"]
        revenue_dict = {
            "FCFS_revenue": FCFS_revenue_list,
            "VCG_revenue": VCG_revenue_list,
        }
        revenue_data = pd.DataFrame(revenue_dict)
        xs = [i for i in range(30)]
        ys = [revenue_data[c][:30] for c in columns]

        # wandb.log(
        #     {
        #         f"revenue_run{run}": wandb.plot.line_series(
        #             xs=xs, ys=ys, keys=columns, title="Revenue Metrix"
        #         )
        #     }
        # )

        # columns = ["FCFS_utility", "VCG_utility"]
        # utility_dict = {
        #     "FCFS_utility": FCFS_utility_list,
        #     "VCG_utility": VCG_utility_list,
        # }
        # utility_data = pd.DataFrame(utility_dict)
        # xs = [i for i in range(30)]
        # ys = [utility_data[c][:30] for c in columns]

        # wandb.log(
        #     {
        #         f"utility_run{run}": wandb.plot.line_series(
        #             xs=xs, ys=ys, keys=columns, title="Utility Metrix"
        #         )
        #     }
        # )

        # columns = ["FCFS_social", "VCG_social"]
        # social_dict = {"FCFS_social": FCFS_social_list, "VCG_social": VCG_social_list}
        # social_data = pd.DataFrame(social_dict)
        # xs = [i for i in range(30)]
        # ys = [social_data[c][:30] for c in columns]

        # wandb.log(
        #     {
        #         f"social_run{run}": wandb.plot.line_series(
        #             xs=xs, ys=ys, keys=columns, title="Social Value Metrix"
        #         )
        #     }
        # )

columns = ["Total_FCFS_revenue", "Total_VCG_revenue"]
revenue_dict = {
    "Total_FCFS_revenue": total_FCFS_revenue_list,
    "Total_VCG_revenue": total_VCG_revenue_list,
}
revenue_data = pd.DataFrame(revenue_dict)
xs = [i for i in range(num_steps)]
ys = [revenue_data[c][:num_steps] for c in columns]

columns_u = ["Total_FCFS_utility", "Total_VCG_utility"]
utility_dict = {
    "Total_FCFS_utility": total_FCFS_utility_list,
    "Total_VCG_utility": total_VCG_utility_list,
}
utility_data = pd.DataFrame(utility_dict)
xs_u = [i for i in range(num_steps)]
ys_u = [utility_data[c][:num_steps] for c in columns_u]

columns_s = ["Total_FCFS_social", "Total_VCG_social"]
social_dict = {
    "Total_FCFS_social": total_FCFS_social_list,
    "Total_VCG_social": total_VCG_social_list,
}
social_data = pd.DataFrame(social_dict)
xs_s = [i for i in range(num_steps)]
ys_s = [social_data[c][:num_steps] for c in columns_s]

# wandb.log(
#     {
#         "total_rev": wandb.plot.line_series(
#             xs=xs, ys=ys, keys=columns, title="Total Revenue Metrix"
#         )
#     }
# )

# wandb.log(
#     {
#         "total_uti": wandb.plot.line_series(
#             xs=xs_u, ys=ys_u, keys=columns_u, title="Total Utility Metrix"
#         )
#     }
# )

# wandb.log(
#     {
#         "total_soc": wandb.plot.line_series(
#             xs=xs_s, ys=ys_s, keys=columns_s, title="Total Social Value Metrix"
#         )
#     }
# )

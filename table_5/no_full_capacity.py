import pandas as pd
import random

# table = 5, course = 3, consumer = 30


def getIndexes(p, p_report):
    """ Get index positions of value in dataframe."""
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = p.isin([p_report])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append([row, col, p_report])
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos


total_res_rev = 0
total_res_rev_full_capacity = 0
full_capacity_larger = 0
for z in range(100):
    print("----------------round", z, "-------------------")
    consumer = 10
    res_revenue = 0
    res_revenue_full_capacity = 0
    report_table = []
    for i in range(consumer):
        pi = pd.DataFrame(
            [
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
            ],
            columns=["A", "B", "C"],
            index=[1, 2, 3, 4, 5],
        )
        pi_A = pi.sort_values("A", ascending=False)
        pi_A = pi_A["A"]
        pi_A_list = pi_A.tolist()
        pi_B = pi.sort_values("B", ascending=False)
        pi_B = pi_B["B"]
        pi_B_list = pi_B.tolist()
        pi_C = pi.sort_values("C", ascending=False)
        pi_C = pi_C["C"]
        pi_C_list = pi_C.tolist()
        pi_value_list = pi_A_list + pi_B_list + pi_C_list
        pi_value_list.sort(reverse=True)
        pi_report = []
        for j in set(pi_value_list):
            for k in range(pi_value_list.count(j)):
                pi_report = pi_report + [[i + 1,] + getIndexes(pi, j)[k]]
        report_table = report_table + pi_report

    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    for bid in report_table:
        if bid[1] == 1:
            report_table_1.append(bid)
        elif bid[1] == 2:
            report_table_2.append(bid)
        elif bid[1] == 3:
            report_table_3.append(bid)
        elif bid[1] == 4:
            report_table_4.append(bid)
        elif bid[1] == 5:
            report_table_5.append(bid)

    # fill the blank list
    while len(report_table_1) < 20:
        report_table_1.append([0, 1, 0, 0])
    while len(report_table_2) < 10:
        report_table_2.append([0, 2, 0, 0])
    while len(report_table_3) < 10:
        report_table_3.append([0, 3, 0, 0])
    while len(report_table_4) < 10:
        report_table_4.append([0, 4, 0, 0])
    while len(report_table_5) < 10:
        report_table_5.append([0, 5, 0, 0])

    def takeValue(elem):
        return elem[3]

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)

    report_table_list = [
        report_table_1,
        report_table_2,
        report_table_3,
        report_table_4,
        report_table_5,
    ]

    # outcome for full capacity
    value_full_capacity = 0
    outcome_full_capacity_list = [
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
    ]
    player_full_capacity_list = []
    for i in outcome_full_capacity_list:
        if i[0] != 0:
            player_full_capacity_list.append(i[0])
    report_table_full_capacity = report_table_1[5:]
    for i in report_table_full_capacity:
        if i[0] in player_full_capacity_list:
            report_table_full_capacity.remove(i)
    for i in range(len(outcome_full_capacity_list)):
        for j in range(1, (len(outcome_full_capacity_list) - i)):
            if (
                outcome_full_capacity_list[i][0]
                == outcome_full_capacity_list[i + j][0]
                != 0
            ):
                outcome_full_capacity_list[i + j] = report_table_full_capacity[0]
                report_table_full_capacity.remove(report_table_full_capacity[0])
    for i in outcome_full_capacity_list:
        value_full_capacity = value_full_capacity + i[3]
    # outcome for 1*4
    value_1 = 0
    outcome1_list = [
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
    ]
    player_list_1 = []
    for i in outcome1_list:
        if i[0] != 0:
            player_list_1.append(i[0])
    report_table_1_changed = report_table_1[4:]
    for i in report_table_1_changed:
        if i[0] in player_list_1:
            report_table_1_changed.remove(i)
    for i in range(len(outcome1_list)):
        for j in range(1, (len(outcome1_list) - i)):
            if outcome1_list[i][0] == outcome1_list[i + j][0] != 0:
                outcome1_list[i + j] = report_table_1_changed[0]
                report_table_1_changed.remove(report_table_1_changed[0])
    for i in outcome1_list:
        value_1 = value_1 + i[3]

    # outcome for 2*2+1
    value_2 = 0
    outcome2_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_1[0],
    ]
    player_list_2 = []
    for i in outcome2_list:
        if i[0] != 0:
            player_list_2.append(i[0])
    report_table_2_changed_1 = report_table_1[1:]
    report_table_2_changed_2 = report_table_2[2:]
    for i in report_table_2_changed_1:
        if i[0] in player_list_2:
            report_table_2_changed_1.remove(i)
    for i in report_table_2_changed_2:
        if i[0] in player_list_2:
            report_table_2_changed_2.remove(i)
    for i in range(len(outcome2_list)):
        for j in range(1, (len(outcome2_list) - i)):
            if outcome2_list[i][0] == outcome2_list[i + j][0] != 0:
                if outcome2_list[i + j][1] == 1:
                    outcome2_list[i + j] = report_table_2_changed_1[0]
                    report_table_2_changed_1.remove(report_table_2_changed_1[0])
                elif outcome2_list[i + j][1] == 2:
                    outcome2_list[i + j] = report_table_2_changed_2[0]
                    report_table_2_changed_2.remove(report_table_2_changed_2[0])
    for i in outcome2_list:
        value_2 = value_2 + i[3]

    # outcome for 2+1*3
    value_3 = 0
    outcome3_list = [
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
    ]
    player_list_3 = []
    for i in outcome3_list:
        if i[0] != 0:
            player_list_3.append(i[0])
    report_table_3_changed_1 = report_table_1[3:]
    report_table_3_changed_2 = report_table_2[1:]
    for i in report_table_3_changed_1:
        if i[0] in player_list_3:
            report_table_3_changed_1.remove(i)
    for i in report_table_3_changed_2:
        if i[0] in player_list_3:
            report_table_3_changed_2.remove(i)
    for i in range(len(outcome3_list)):
        for j in range(1, (len(outcome3_list) - i)):
            if outcome3_list[i][0] == outcome3_list[i + j][0] != 0:
                if outcome3_list[i + j][1] == 1:
                    outcome3_list[i + j] = report_table_3_changed_1[0]
                    report_table_3_changed_1.remove(report_table_3_changed_1[0])
                elif outcome3_list[i + j][1] == 2:
                    outcome3_list[i + j] = report_table_3_changed_2[0]
                    report_table_3_changed_2.remove(report_table_3_changed_2[0])
    for i in outcome3_list:
        value_3 = value_3 + i[3]

    # outcome for 3+2
    value_4 = 0
    outcome4_list = [
        report_table_3[0],
        report_table_2[0],
    ]
    player_list_4 = []
    for i in outcome4_list:
        if i[0] != 0:
            player_list_4.append(i[0])
    report_table_4_changed_2 = report_table_2[1:]
    report_table_4_changed_3 = report_table_3[1:]
    for i in report_table_4_changed_2:
        if i[0] in player_list_4:
            report_table_4_changed_2.remove(i)
    for i in report_table_4_changed_3:
        if i[0] in player_list_4:
            report_table_4_changed_3.remove(i)
    for i in range(len(outcome4_list)):
        for j in range(1, (len(outcome4_list) - i)):
            if outcome4_list[i][0] == outcome4_list[i + j][0] != 0:
                if outcome4_list[i + j][1] == 2:
                    outcome4_list[i + j] = report_table_4_changed_2[0]
                    report_table_4_changed_2.remove(report_table_4_changed_2[0])
                elif outcome4_list[i + j][1] == 3:
                    outcome4_list[i + j] = report_table_4_changed_3[0]
                    report_table_4_changed_3.remove(report_table_4_changed_3[0])
    for i in outcome4_list:
        value_4 = value_4 + i[3]

    # outcome for 3+1+1
    value_5 = 0
    outcome5_list = [
        report_table_3[0],
        report_table_1[0],
        report_table_1[1],
    ]
    player_list_5 = []
    for i in outcome5_list:
        if i[0] != 0:
            player_list_5.append(i[0])
    report_table_5_changed_1 = report_table_1[2:]
    report_table_5_changed_3 = report_table_3[1:]
    for i in report_table_5_changed_1:
        if i[0] in player_list_5:
            report_table_5_changed_1.remove(i)
    for i in report_table_5_changed_3:
        if i[0] in player_list_5:
            report_table_5_changed_3.remove(i)
    for i in range(len(outcome5_list)):
        for j in range(1, (len(outcome5_list) - i)):
            if outcome5_list[i][0] == outcome5_list[i + j][0] != 0:
                if outcome5_list[i + j][1] == 1:
                    outcome5_list[i + j] = report_table_5_changed_1[0]
                    report_table_5_changed_1.remove(report_table_5_changed_1[0])
                elif outcome5_list[i + j][1] == 3:
                    outcome5_list[i + j] = report_table_5_changed_3[0]
                    report_table_5_changed_3.remove(report_table_5_changed_3[0])
    for i in outcome5_list:
        value_5 = value_5 + i[3]

    # outcome for 4+1
    value_6 = 0
    outcome6_list = [
        report_table_4[0],
        report_table_1[0],
    ]
    player_list_6 = []
    for i in outcome6_list:
        if i[0] != 0:
            player_list_6.append(i[0])
    report_table_6_changed_1 = report_table_1[1:]
    report_table_6_changed_4 = report_table_4[1:]
    for i in report_table_6_changed_1:
        if i[0] in player_list_6:
            report_table_6_changed_1.remove(i)
    for i in report_table_6_changed_4:
        if i[0] in player_list_6:
            report_table_6_changed_4.remove(i)
    for i in range(len(outcome6_list)):
        for j in range(1, (len(outcome6_list) - i)):
            if outcome6_list[i][0] == outcome6_list[i + j][0] != 0:
                if outcome6_list[i + j][1] == 1:
                    outcome6_list[i + j] = report_table_6_changed_1[0]
                    report_table_6_changed_1.remove(report_table_6_changed_1[0])
                elif outcome6_list[i + j][1] == 4:
                    outcome6_list[i + j] = report_table_6_changed_4[0]
                    report_table_6_changed_4.remove(report_table_6_changed_4[0])
    for i in outcome6_list:
        value_6 = value_6 + i[3]

    # outcome for 5
    value_7 = 0
    outcome7_list = [report_table_5[0]]
    for i in outcome7_list:
        value_7 = value_7 + i[3]

    outcomes_list = [
        outcome1_list,
        outcome2_list,
        outcome3_list,
        outcome4_list,
        outcome5_list,
        outcome6_list,
        outcome7_list,
    ]
    outcomes_full_capacity_list = [
        outcome_full_capacity_list,
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
    values_full_capacity = [
        value_full_capacity,
        value_1,
        value_2,
        value_3,
        value_4,
        value_5,
        value_6,
        value_7,
    ]
    # find the optimal outcome
    for a in range(len(values)):
        value_a = values[a]
        if value_a == max(values):
            social_value = value_a
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == a:
                    print("optimal allocation : ", outcome_m)
                    for p in outcome_m:
                        # calcluate second price
                        sereport_table_1 = [k for k in report_table_1 if k[0] != p[0]]
                        sereport_table_2 = [k for k in report_table_2 if k[0] != p[0]]
                        sereport_table_3 = [k for k in report_table_3 if k[0] != p[0]]
                        sereport_table_4 = [k for k in report_table_4 if k[0] != p[0]]
                        sereport_table_5 = [k for k in report_table_5 if k[0] != p[0]]

                        # outcome for 1*4
                        sevalue_1 = 0
                        seoutcome1_list = [
                            sereport_table_1[0],
                            sereport_table_1[1],
                            sereport_table_1[2],
                            sereport_table_1[3],
                        ]
                        seplayer_list_1 = []
                        for i in seoutcome1_list:
                            if i[0] != 0:
                                seplayer_list_1.append(i[0])
                        sereport_table_1_changed = sereport_table_1[4:]
                        for i in sereport_table_1_changed:
                            if i[0] in seplayer_list_1:
                                sereport_table_1_changed.remove(i)
                        for i in range(len(seoutcome1_list)):
                            for j in range(1, (len(seoutcome1_list) - i)):
                                if (
                                    seoutcome1_list[i][0]
                                    == seoutcome1_list[i + j][0]
                                    != 0
                                ):
                                    seoutcome1_list[i + j] = sereport_table_1_changed[0]
                                    sereport_table_1_changed.remove(
                                        sereport_table_1_changed[0]
                                    )
                        for i in seoutcome1_list:
                            sevalue_1 = sevalue_1 + i[3]

                        # outcome for 2*2+1
                        sevalue_2 = 0
                        seoutcome2_list = [
                            sereport_table_2[0],
                            sereport_table_2[1],
                            sereport_table_1[0],
                        ]
                        seplayer_list_2 = []
                        for i in seoutcome2_list:
                            if i[0] != 0:
                                seplayer_list_2.append(i[0])
                        sereport_table_2_changed_1 = sereport_table_1[1:]
                        sereport_table_2_changed_2 = sereport_table_2[2:]
                        for i in sereport_table_2_changed_1:
                            if i[0] in seplayer_list_2:
                                sereport_table_2_changed_1.remove(i)
                        for i in sereport_table_2_changed_2:
                            if i[0] in seplayer_list_2:
                                sereport_table_2_changed_2.remove(i)
                        for i in range(len(seoutcome2_list)):
                            for j in range(1, (len(seoutcome2_list) - i)):
                                if (
                                    seoutcome2_list[i][0]
                                    == seoutcome2_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome2_list[i + j][1] == 1:
                                        seoutcome2_list[
                                            i + j
                                        ] = sereport_table_2_changed_1[0]
                                        sereport_table_2_changed_1.remove(
                                            sereport_table_2_changed_1[0]
                                        )
                                    elif seoutcome2_list[i + j][1] == 2:
                                        seoutcome2_list[
                                            i + j
                                        ] = sereport_table_2_changed_2[0]
                                        sereport_table_2_changed_2.remove(
                                            sereport_table_2_changed_2[0]
                                        )
                        for i in seoutcome2_list:
                            sevalue_2 = sevalue_2 + i[3]

                        # outcome for 2+1*3
                        sevalue_3 = 0
                        seoutcome3_list = [
                            sereport_table_2[0],
                            sereport_table_1[0],
                            sereport_table_1[1],
                            sereport_table_1[2],
                        ]
                        seplayer_list_3 = []
                        for i in seoutcome3_list:
                            if i[0] != 0:
                                seplayer_list_3.append(i[0])
                        sereport_table_3_changed_1 = sereport_table_1[3:]
                        sereport_table_3_changed_2 = sereport_table_2[1:]
                        for i in sereport_table_3_changed_1:
                            if i[0] in seplayer_list_3:
                                sereport_table_3_changed_1.remove(i)
                        for i in sereport_table_3_changed_2:
                            if i[0] in seplayer_list_3:
                                sereport_table_3_changed_2.remove(i)
                        for i in range(len(seoutcome3_list)):
                            for j in range(1, (len(seoutcome3_list) - i)):
                                if (
                                    seoutcome3_list[i][0]
                                    == seoutcome3_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome3_list[i + j][1] == 1:
                                        seoutcome3_list[
                                            i + j
                                        ] = sereport_table_3_changed_1[0]
                                        sereport_table_3_changed_1.remove(
                                            sereport_table_3_changed_1[0]
                                        )
                                    elif seoutcome3_list[i + j][1] == 2:
                                        seoutcome3_list[
                                            i + j
                                        ] = sereport_table_3_changed_2[0]
                                        sereport_table_3_changed_2.remove(
                                            sereport_table_3_changed_2[0]
                                        )
                        for i in seoutcome3_list:
                            sevalue_3 = sevalue_3 + i[3]

                        # outcome for 3+2
                        sevalue_4 = 0
                        seoutcome4_list = [
                            sereport_table_3[0],
                            sereport_table_2[0],
                        ]
                        seplayer_list_4 = []
                        for i in seoutcome4_list:
                            if i[0] != 0:
                                seplayer_list_4.append(i[0])
                        sereport_table_4_changed_2 = sereport_table_2[1:]
                        sereport_table_4_changed_3 = sereport_table_3[1:]
                        for i in sereport_table_4_changed_2:
                            if i[0] in seplayer_list_4:
                                sereport_table_4_changed_2.remove(i)
                        for i in sereport_table_4_changed_3:
                            if i[0] in seplayer_list_4:
                                sereport_table_4_changed_3.remove(i)
                        for i in range(len(seoutcome4_list)):
                            for j in range(1, (len(seoutcome4_list) - i)):
                                if (
                                    seoutcome4_list[i][0]
                                    == seoutcome4_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome4_list[i + j][1] == 2:
                                        seoutcome4_list[
                                            i + j
                                        ] = sereport_table_4_changed_2[0]
                                        sereport_table_4_changed_2.remove(
                                            sereport_table_4_changed_2[0]
                                        )
                                    elif seoutcome4_list[i + j][1] == 3:
                                        seoutcome4_list[
                                            i + j
                                        ] = sereport_table_4_changed_3[0]
                                        sereport_table_4_changed_3.remove(
                                            sereport_table_4_changed_3[0]
                                        )
                        for i in seoutcome4_list:
                            sevalue_4 = sevalue_4 + i[3]

                        # outcome for 3+1+1
                        sevalue_5 = 0
                        seoutcome5_list = [
                            sereport_table_3[0],
                            sereport_table_1[0],
                            sereport_table_1[1],
                        ]
                        seplayer_list_5 = []
                        for i in seoutcome5_list:
                            if i[0] != 0:
                                seplayer_list_5.append(i[0])
                        sereport_table_5_changed_1 = sereport_table_1[2:]
                        sereport_table_5_changed_3 = sereport_table_3[1:]
                        for i in sereport_table_5_changed_1:
                            if i[0] in seplayer_list_5:
                                sereport_table_5_changed_1.remove(i)
                        for i in sereport_table_5_changed_3:
                            if i[0] in seplayer_list_5:
                                sereport_table_5_changed_3.remove(i)
                        for i in range(len(seoutcome5_list)):
                            for j in range(1, (len(seoutcome5_list) - i)):
                                if (
                                    seoutcome5_list[i][0]
                                    == seoutcome5_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome5_list[i + j][1] == 1:
                                        seoutcome5_list[
                                            i + j
                                        ] = sereport_table_5_changed_1[0]
                                        sereport_table_5_changed_1.remove(
                                            sereport_table_5_changed_1[0]
                                        )
                                    elif seoutcome5_list[i + j][1] == 3:
                                        seoutcome5_list[
                                            i + j
                                        ] = sereport_table_5_changed_3[0]
                                        sereport_table_5_changed_3.remove(
                                            sereport_table_5_changed_3[0]
                                        )
                        for i in seoutcome5_list:
                            sevalue_5 = sevalue_5 + i[3]

                        # outcome for 4+1
                        sevalue_6 = 0
                        seoutcome6_list = [
                            sereport_table_4[0],
                            sereport_table_1[0],
                        ]
                        seplayer_list_6 = []
                        for i in seoutcome6_list:
                            if i[0] != 0:
                                seplayer_list_6.append(i[0])
                        sereport_table_6_changed_1 = sereport_table_1[1:]
                        sereport_table_6_changed_4 = sereport_table_4[1:]
                        for i in sereport_table_6_changed_1:
                            if i[0] in seplayer_list_6:
                                sereport_table_6_changed_1.remove(i)
                        for i in sereport_table_6_changed_4:
                            if i[0] in seplayer_list_6:
                                sereport_table_6_changed_4.remove(i)
                        for i in range(len(seoutcome6_list)):
                            for j in range(1, (len(seoutcome6_list) - i)):
                                if (
                                    seoutcome6_list[i][0]
                                    == seoutcome6_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome6_list[i + j][1] == 1:
                                        seoutcome6_list[
                                            i + j
                                        ] = sereport_table_6_changed_1[0]
                                        sereport_table_6_changed_1.remove(
                                            sereport_table_6_changed_1[0]
                                        )
                                    elif seoutcome6_list[i + j][1] == 4:
                                        seoutcome6_list[
                                            i + j
                                        ] = sereport_table_6_changed_4[0]
                                        sereport_table_6_changed_4.remove(
                                            sereport_table_6_changed_4[0]
                                        )
                        for i in seoutcome6_list:
                            sevalue_6 = sevalue_6 + i[3]

                        # outcome for 5
                        sevalue_7 = 0
                        seoutcome7_list = [sereport_table_5[0]]
                        for i in seoutcome7_list:
                            sevalue_7 = sevalue_7 + i[3]
                        sevalues = [
                            sevalue_1,
                            sevalue_2,
                            sevalue_3,
                            sevalue_4,
                            sevalue_5,
                            sevalue_6,
                            sevalue_7,
                        ]
                        seoutcomes_list = [
                            seoutcome1_list,
                            seoutcome2_list,
                            seoutcome3_list,
                            seoutcome4_list,
                            seoutcome5_list,
                            seoutcome6_list,
                            seoutcome7_list,
                        ]
                        for n in range(len(sevalues)):
                            if sevalues[n] == max(sevalues):
                                second_value = sevalues[n]
                                for o in range(len(seoutcomes_list)):
                                    if o == n:
                                        print(
                                            "second best allocation : ",
                                            seoutcomes_list[o],
                                        )
                                        monetary_transfer = -(
                                            social_value - p[3] - second_value
                                        )
                                        res_revenue = res_revenue + monetary_transfer
                                    else:
                                        pass
                                break
            break
        else:
            pass

    # find the optimal outcome
    for b in range(len(values_full_capacity)):
        if values_full_capacity[b] == max(values_full_capacity):
            social_value_full_capacity = values_full_capacity[b]
            for m in range(len(outcomes_full_capacity_list)):
                outcome_full_capacity_m = outcomes_full_capacity_list[m]
                if m == b:
                    print(
                        "optimal allocation for full capacity: ",
                        outcome_full_capacity_m,
                    )
                    for p in outcome_full_capacity_m:
                        # calcluate second price
                        sereport_table_1 = [k for k in report_table_1 if k[0] != p[0]]
                        sereport_table_2 = [k for k in report_table_2 if k[0] != p[0]]
                        sereport_table_3 = [k for k in report_table_3 if k[0] != p[0]]
                        sereport_table_4 = [k for k in report_table_4 if k[0] != p[0]]
                        sereport_table_5 = [k for k in report_table_5 if k[0] != p[0]]
                        # outcome for full capacity
                        sevalue_full_capacity = 0
                        seoutcome_full_capacity_list = [
                            sereport_table_1[0],
                            sereport_table_1[1],
                            sereport_table_1[2],
                            sereport_table_1[3],
                            sereport_table_1[4],
                        ]
                        seplayer_full_capacity_list = []
                        for i in seoutcome_full_capacity_list:
                            if i[0] != 0:
                                seplayer_full_capacity_list.append(i[0])
                        sereport_table_full_capacity = sereport_table_1[5:]
                        for i in sereport_table_full_capacity:
                            if i[0] in seplayer_full_capacity_list:
                                sereport_table_full_capacity.remove(i)
                        for i in range(len(seoutcome_full_capacity_list)):
                            for j in range(1, (len(seoutcome_full_capacity_list) - i)):
                                if (
                                    seoutcome_full_capacity_list[i][0]
                                    == seoutcome_full_capacity_list[i + j][0]
                                    != 0
                                ):
                                    seoutcome_full_capacity_list[
                                        i + j
                                    ] = sereport_table_full_capacity[0]
                                    sereport_table_full_capacity.remove(
                                        sereport_table_full_capacity[0]
                                    )
                        for i in seoutcome_full_capacity_list:
                            sevalue_full_capacity = sevalue_full_capacity + i[3]

                        # outcome for 1*4
                        sevalue_1 = 0
                        seoutcome1_list = [
                            sereport_table_1[0],
                            sereport_table_1[1],
                            sereport_table_1[2],
                            sereport_table_1[3],
                        ]
                        seplayer_list_1 = []
                        for i in seoutcome1_list:
                            if i[0] != 0:
                                seplayer_list_1.append(i[0])
                        sereport_table_1_changed = sereport_table_1[4:]
                        for i in sereport_table_1_changed:
                            if i[0] in seplayer_list_1:
                                sereport_table_1_changed.remove(i)
                        for i in range(len(seoutcome1_list)):
                            for j in range(1, (len(seoutcome1_list) - i)):
                                if (
                                    seoutcome1_list[i][0]
                                    == seoutcome1_list[i + j][0]
                                    != 0
                                ):
                                    seoutcome1_list[i + j] = sereport_table_1_changed[0]
                                    sereport_table_1_changed.remove(
                                        sereport_table_1_changed[0]
                                    )
                        for i in seoutcome1_list:
                            sevalue_1 = sevalue_1 + i[3]

                        # outcome for 2*2+1
                        sevalue_2 = 0
                        seoutcome2_list = [
                            sereport_table_2[0],
                            sereport_table_2[1],
                            sereport_table_1[0],
                        ]
                        seplayer_list_2 = []
                        for i in seoutcome2_list:
                            if i[0] != 0:
                                seplayer_list_2.append(i[0])
                        sereport_table_2_changed_1 = sereport_table_1[1:]
                        sereport_table_2_changed_2 = sereport_table_2[2:]
                        for i in sereport_table_2_changed_1:
                            if i[0] in seplayer_list_2:
                                sereport_table_2_changed_1.remove(i)
                        for i in sereport_table_2_changed_2:
                            if i[0] in seplayer_list_2:
                                sereport_table_2_changed_2.remove(i)
                        for i in range(len(seoutcome2_list)):
                            for j in range(1, (len(seoutcome2_list) - i)):
                                if (
                                    seoutcome2_list[i][0]
                                    == seoutcome2_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome2_list[i + j][1] == 1:
                                        seoutcome2_list[
                                            i + j
                                        ] = sereport_table_2_changed_1[0]
                                        sereport_table_2_changed_1.remove(
                                            sereport_table_2_changed_1[0]
                                        )
                                    elif seoutcome2_list[i + j][1] == 2:
                                        seoutcome2_list[
                                            i + j
                                        ] = sereport_table_2_changed_2[0]
                                        sereport_table_2_changed_2.remove(
                                            sereport_table_2_changed_2[0]
                                        )
                        for i in seoutcome2_list:
                            sevalue_2 = sevalue_2 + i[3]

                        # outcome for 2+1*3
                        sevalue_3 = 0
                        seoutcome3_list = [
                            sereport_table_2[0],
                            sereport_table_1[0],
                            sereport_table_1[1],
                            sereport_table_1[2],
                        ]
                        seplayer_list_3 = []
                        for i in seoutcome3_list:
                            if i[0] != 0:
                                seplayer_list_3.append(i[0])
                        sereport_table_3_changed_1 = sereport_table_1[3:]
                        sereport_table_3_changed_2 = sereport_table_2[1:]
                        for i in sereport_table_3_changed_1:
                            if i[0] in seplayer_list_3:
                                sereport_table_3_changed_1.remove(i)
                        for i in sereport_table_3_changed_2:
                            if i[0] in seplayer_list_3:
                                sereport_table_3_changed_2.remove(i)
                        for i in range(len(seoutcome3_list)):
                            for j in range(1, (len(seoutcome3_list) - i)):
                                if (
                                    seoutcome3_list[i][0]
                                    == seoutcome3_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome3_list[i + j][1] == 1:
                                        seoutcome3_list[
                                            i + j
                                        ] = sereport_table_3_changed_1[0]
                                        sereport_table_3_changed_1.remove(
                                            sereport_table_3_changed_1[0]
                                        )
                                    elif seoutcome3_list[i + j][1] == 2:
                                        seoutcome3_list[
                                            i + j
                                        ] = sereport_table_3_changed_2[0]
                                        sereport_table_3_changed_2.remove(
                                            sereport_table_3_changed_2[0]
                                        )
                        for i in seoutcome3_list:
                            sevalue_3 = sevalue_3 + i[3]

                        # outcome for 3+2
                        sevalue_4 = 0
                        seoutcome4_list = [
                            sereport_table_3[0],
                            sereport_table_2[0],
                        ]
                        seplayer_list_4 = []
                        for i in seoutcome4_list:
                            if i[0] != 0:
                                seplayer_list_4.append(i[0])
                        sereport_table_4_changed_2 = sereport_table_2[1:]
                        sereport_table_4_changed_3 = sereport_table_3[1:]
                        for i in sereport_table_4_changed_2:
                            if i[0] in seplayer_list_4:
                                sereport_table_4_changed_2.remove(i)
                        for i in sereport_table_4_changed_3:
                            if i[0] in seplayer_list_4:
                                sereport_table_4_changed_3.remove(i)
                        for i in range(len(seoutcome4_list)):
                            for j in range(1, (len(seoutcome4_list) - i)):
                                if (
                                    seoutcome4_list[i][0]
                                    == seoutcome4_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome4_list[i + j][1] == 2:
                                        seoutcome4_list[
                                            i + j
                                        ] = sereport_table_4_changed_2[0]
                                        sereport_table_4_changed_2.remove(
                                            sereport_table_4_changed_2[0]
                                        )
                                    elif seoutcome4_list[i + j][1] == 3:
                                        seoutcome4_list[
                                            i + j
                                        ] = sereport_table_4_changed_3[0]
                                        sereport_table_4_changed_3.remove(
                                            sereport_table_4_changed_3[0]
                                        )
                        for i in seoutcome4_list:
                            sevalue_4 = sevalue_4 + i[3]

                        # outcome for 3+1+1
                        sevalue_5 = 0
                        seoutcome5_list = [
                            sereport_table_3[0],
                            sereport_table_1[0],
                            sereport_table_1[1],
                        ]
                        seplayer_list_5 = []
                        for i in seoutcome5_list:
                            if i[0] != 0:
                                seplayer_list_5.append(i[0])
                        sereport_table_5_changed_1 = sereport_table_1[2:]
                        sereport_table_5_changed_3 = sereport_table_3[1:]
                        for i in sereport_table_5_changed_1:
                            if i[0] in seplayer_list_5:
                                sereport_table_5_changed_1.remove(i)
                        for i in sereport_table_5_changed_3:
                            if i[0] in seplayer_list_5:
                                sereport_table_5_changed_3.remove(i)
                        for i in range(len(seoutcome5_list)):
                            for j in range(1, (len(seoutcome5_list) - i)):
                                if (
                                    seoutcome5_list[i][0]
                                    == seoutcome5_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome5_list[i + j][1] == 1:
                                        seoutcome5_list[
                                            i + j
                                        ] = sereport_table_5_changed_1[0]
                                        sereport_table_5_changed_1.remove(
                                            sereport_table_5_changed_1[0]
                                        )
                                    elif seoutcome5_list[i + j][1] == 3:
                                        seoutcome5_list[
                                            i + j
                                        ] = sereport_table_5_changed_3[0]
                                        sereport_table_5_changed_3.remove(
                                            sereport_table_5_changed_3[0]
                                        )
                        for i in seoutcome5_list:
                            sevalue_5 = sevalue_5 + i[3]

                        # outcome for 4+1
                        sevalue_6 = 0
                        seoutcome6_list = [
                            sereport_table_4[0],
                            sereport_table_1[0],
                        ]
                        seplayer_list_6 = []
                        for i in seoutcome6_list:
                            if i[0] != 0:
                                seplayer_list_6.append(i[0])
                        sereport_table_6_changed_1 = sereport_table_1[1:]
                        sereport_table_6_changed_4 = sereport_table_4[1:]
                        for i in sereport_table_6_changed_1:
                            if i[0] in seplayer_list_6:
                                sereport_table_6_changed_1.remove(i)
                        for i in sereport_table_6_changed_4:
                            if i[0] in seplayer_list_6:
                                sereport_table_6_changed_4.remove(i)
                        for i in range(len(seoutcome6_list)):
                            for j in range(1, (len(seoutcome6_list) - i)):
                                if (
                                    seoutcome6_list[i][0]
                                    == seoutcome6_list[i + j][0]
                                    != 0
                                ):
                                    if seoutcome6_list[i + j][1] == 1:
                                        seoutcome6_list[
                                            i + j
                                        ] = sereport_table_6_changed_1[0]
                                        sereport_table_6_changed_1.remove(
                                            sereport_table_6_changed_1[0]
                                        )
                                    elif seoutcome6_list[i + j][1] == 4:
                                        seoutcome6_list[
                                            i + j
                                        ] = sereport_table_6_changed_4[0]
                                        sereport_table_6_changed_4.remove(
                                            sereport_table_6_changed_4[0]
                                        )
                        for i in seoutcome6_list:
                            sevalue_6 = sevalue_6 + i[3]

                        # outcome for 5
                        sevalue_7 = 0
                        seoutcome7_list = [sereport_table_5[0]]
                        for i in seoutcome7_list:
                            sevalue_7 = sevalue_7 + i[3]
                        sevalues_full_capacity = [
                            sevalue_full_capacity,
                            sevalue_1,
                            sevalue_2,
                            sevalue_3,
                            sevalue_4,
                            sevalue_5,
                            sevalue_6,
                            sevalue_7,
                        ]
                        seoutcomes_full_capacity_list = [
                            seoutcome_full_capacity_list,
                            seoutcome1_list,
                            seoutcome2_list,
                            seoutcome3_list,
                            seoutcome4_list,
                            seoutcome5_list,
                            seoutcome6_list,
                            seoutcome7_list,
                        ]
                        for n in range(len(sevalues_full_capacity)):
                            if sevalues_full_capacity[n] == max(sevalues_full_capacity):
                                second_value_full_capacity = sevalues_full_capacity[n]
                                for o in range(len(seoutcomes_full_capacity_list)):
                                    if o == n:
                                        print(
                                            "second best allocation for full capacity: ",
                                            seoutcomes_full_capacity_list[o],
                                        )
                                        monetary_transfer_full_capacity = -(
                                            social_value_full_capacity
                                            - p[3]
                                            - second_value_full_capacity
                                        )
                                        res_revenue_full_capacity = (
                                            res_revenue_full_capacity
                                            + monetary_transfer_full_capacity
                                        )
                                    else:
                                        pass
                                break
            break
        else:
            pass
    print("restaurant revenue : ", res_revenue)
    print("restaurant revenue for full capacity: ", res_revenue_full_capacity)
    total_res_rev = total_res_rev + res_revenue
    total_res_rev_full_capacity = (
        total_res_rev_full_capacity + res_revenue_full_capacity
    )
    if res_revenue_full_capacity > res_revenue:
        full_capacity_larger = full_capacity_larger + 1
ave_res_rev = total_res_rev / 100
ave_res_rev_full_capacity = total_res_rev_full_capacity / 100
print("restaurant revenue for full capacity is larger : ", full_capacity_larger)
print("average restaurant revenue without full capacity : ", ave_res_rev)
print("average restaurant revenue with full capacity : ", ave_res_rev_full_capacity)

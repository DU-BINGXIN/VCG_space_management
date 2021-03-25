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


utility_change_1 = 0
bug = 0  # initialize the number of situations when truth-telling strategy is not dominant strategy
for z in range(10000):
    consumer = 20
    report_table = []
    random_table = []
    for i in range(consumer):
        pi = pd.DataFrame(
            [
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
            ],
            columns=["A", "B", "C"],
            index=[1, 2, 3, 4, 5, 6],
        )
        pi_random = pd.DataFrame(
            [
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
            ],
            columns=["A", "B", "C"],
            index=[1, 2, 3, 4, 5, 6],
        )

        if i == 0:
            p1_report = []
            p1 = pi
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
            # two reported situation
            pi_value_1 = pi_value_list[0]
            pi_value_2 = pi_value_list[1]
            if pi_value_1 != pi_value_2:
                p1_report_1 = [i + 1,] + getIndexes(pi, pi_value_1)[0]
                p1_report_2 = [i + 1,] + getIndexes(pi, pi_value_2)[0]
            else:
                p1_report_1 = [i + 1,] + getIndexes(pi, pi_value_1)[0]
                p1_report_2 = [i + 1,] + getIndexes(pi, pi_value_2)[1]
            p1_report.append(p1_report_1)
            p1_report.append(p1_report_2)

        pi_random_A = pi_random.sort_values("A", ascending=False)
        pi_random_A = pi_random_A["A"]
        pi_random_A_list = pi_random_A.tolist()
        pi_random_B = pi_random.sort_values("B", ascending=False)
        pi_random_B = pi_random_B["B"]
        pi_random_B_list = pi_random_B.tolist()
        pi_random_C = pi_random.sort_values("C", ascending=False)
        pi_random_C = pi_random_C["C"]
        pi_random_C_list = pi_random_C.tolist()
        pi_random_value_list = pi_random_A_list + pi_random_B_list + pi_random_C_list
        pi_random_value_list.sort(reverse=True)
        # two randomly reported situation
        pi_random_value_1 = pi_random_value_list[0]
        pi_random_value_2 = pi_random_value_list[1]
        if pi_random_value_1 != pi_random_value_2:
            pi_random_report_1 = [i + 1,] + getIndexes(pi_random, pi_random_value_1)[0]
            pi_random_report_2 = [i + 1,] + getIndexes(pi_random, pi_random_value_2)[0]
        else:
            pi_random_report_1 = [i + 1,] + getIndexes(pi_random, pi_random_value_1)[0]
            pi_random_report_2 = [i + 1,] + getIndexes(pi_random, pi_random_value_2)[1]
        random_table = random_table + [pi_random_report_1] + [pi_random_report_2]

    # classify tables with table numbers
    report_table = [i for i in random_table if i[0] != 1]
    report_table.append(p1_report_1)
    report_table.append(p1_report_2)
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_table)):
        if report_table[i][1] == 1:
            report_table_1.append(report_table[i])
        elif report_table[i][1] == 2:
            report_table_2.append(report_table[i])
        elif report_table[i][1] == 3:
            report_table_3.append(report_table[i])
        elif report_table[i][1] == 4:
            report_table_4.append(report_table[i])
        elif report_table[i][1] == 5:
            report_table_5.append(report_table[i])
        elif report_table[i][1] == 6:
            report_table_6.append(report_table[i])
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
    while len(report_table_6) < 10:
        report_table_6.append([0, 6, 0, 0])

    def takeValue(elem):
        return elem[3]

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)
    report_table_list = [
        report_table_1,
        report_table_2,
        report_table_3,
        report_table_4,
        report_table_5,
        report_table_6,
    ]

    # outcome for 1*5
    value_1 = 0
    outcome1_list = [
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
    ]
    player_list_1 = []
    for i in outcome1_list:
        if i[0] != 0:
            player_list_1.append(i[0])
    report_table_1_changed = report_table_1[5:]
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

    # outcome for 2*2+1+1
    value_2 = 0
    outcome2_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_1[0],
        report_table_1[1],
    ]
    player_list_2 = []
    for i in outcome2_list:
        if i[0] != 0:
            player_list_2.append(i[0])
    report_table_2_changed_1 = report_table_1[2:]
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

    # outcome for 2+1*4
    value_3 = 0
    outcome3_list = [
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
    ]
    player_list_3 = []
    for i in outcome3_list:
        if i[0] != 0:
            player_list_3.append(i[0])
    report_table_3_changed_1 = report_table_1[4:]
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

    # outcome for 3+2+1
    value_4 = 0
    outcome4_list = [
        report_table_3[0],
        report_table_2[0],
        report_table_1[0],
    ]
    player_list_4 = []
    for i in outcome4_list:
        if i[0] != 0:
            player_list_4.append(i[0])
    report_table_4_changed_1 = report_table_1[1:]
    report_table_4_changed_2 = report_table_2[1:]
    report_table_4_changed_3 = report_table_3[1:]
    for i in report_table_4_changed_1:
        if i[0] in player_list_4:
            report_table_4_changed_1.remove(i)
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
                elif outcome4_list[i + j][1] == 1:
                    outcome4_list[i + j] = report_table_4_changed_1[0]
                    report_table_4_changed_1.remove(report_table_4_changed_1[0])
    for i in outcome4_list:
        value_4 = value_4 + i[3]

    # outcome for 3+1+1+1
    value_5 = 0
    outcome5_list = [
        report_table_3[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
    ]
    player_list_5 = []
    for i in outcome5_list:
        if i[0] != 0:
            player_list_5.append(i[0])
    report_table_5_changed_1 = report_table_1[3:]
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

    # outcome for 4+1+1
    value_6 = 0
    outcome6_list = [
        report_table_4[0],
        report_table_1[0],
        report_table_1[1],
    ]
    player_list_6 = []
    for i in outcome6_list:
        if i[0] != 0:
            player_list_6.append(i[0])
    report_table_6_changed_1 = report_table_1[2:]
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

    # outcome for 5+1
    value_7 = 0
    outcome7_list = [
        report_table_5[0],
        report_table_1[0],
    ]
    player_list_7 = []
    for i in outcome7_list:
        if i[0] != 0:
            player_list_7.append(i[0])
    report_table_7_changed_1 = report_table_1[1:]
    report_table_7_changed_5 = report_table_5[1:]
    for i in report_table_7_changed_1:
        if i[0] in player_list_7:
            report_table_7_changed_1.remove(i)
    for i in report_table_7_changed_5:
        if i[0] in player_list_7:
            report_table_7_changed_5.remove(i)
    for i in range(len(outcome7_list)):
        for j in range(1, (len(outcome7_list) - i)):
            if outcome7_list[i][0] == outcome7_list[i + j][0] != 0:
                if outcome7_list[i + j][1] == 1:
                    outcome7_list[i + j] = report_table_7_changed_1[0]
                    report_table_7_changed_1.remove(report_table_7_changed_1[0])
                elif outcome7_list[i + j][1] == 5:
                    outcome7_list[i + j] = report_table_7_changed_5[0]
                    report_table_7_changed_5.remove(report_table_7_changed_5[0])
    for i in outcome7_list:
        value_7 = value_7 + i[3]
    # outcome for 2*3
    value_8 = 0
    outcome8_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_2[2],
    ]
    player_list_8 = []
    for i in outcome8_list:
        if i[0] != 0:
            player_list_8.append(i[0])
    report_table_8_changed = report_table_2[3:]
    for i in report_table_8_changed:
        if i[0] in player_list_8:
            report_table_8_changed.remove(i)
    for i in range(len(outcome8_list)):
        for j in range(1, (len(outcome8_list) - i)):
            if outcome8_list[i][0] == outcome8_list[i + j][0] != 0:
                outcome8_list[i + j] = report_table_8_changed[0]
                report_table_8_changed.remove(report_table_8_changed[0])
    for i in outcome8_list:
        value_8 = value_8 + i[3]
    # outcome for 3*2
    value_9 = 0
    outcome9_list = [
        report_table_3[0],
        report_table_3[1],
    ]
    player_list_9 = []
    for i in outcome9_list:
        if i[0] != 0:
            player_list_9.append(i[0])
    report_table_9_changed_3 = report_table_3[2:]
    for i in report_table_9_changed_3:
        if i[0] in player_list_9:
            report_table_9_changed_3.remove(i)
    for i in range(len(outcome9_list)):
        for j in range(1, (len(outcome9_list) - i)):
            if outcome9_list[i][0] == outcome9_list[i + j][0] != 0:
                if outcome9_list[i + j][1] == 3:
                    outcome9_list[i + j] = report_table_9_changed_3[0]
                    report_table_9_changed_3.remove(report_table_9_changed_3[0])
    for i in outcome9_list:
        value_9 = value_9 + i[3]
    # outcome for 4+2
    value_10 = 0
    outcome10_list = [report_table_4[0], report_table_2[0]]
    player_list_10 = []
    for i in outcome10_list:
        if i[0] != 0:
            player_list_10.append(i[0])
    report_table_10_changed_2 = report_table_2[1:]
    report_table_10_changed_4 = report_table_4[1:]
    for i in report_table_10_changed_2:
        if i[0] in player_list_10:
            report_table_10_changed_2.remove(i)
    for i in report_table_10_changed_4:
        if i[0] in player_list_10:
            report_table_10_changed_4.remove(i)
    for i in range(len(outcome10_list)):
        for j in range(1, (len(outcome10_list) - i)):
            if outcome10_list[i][0] == outcome10_list[i + j][0] != 0:
                if outcome10_list[i + j][1] == 2:
                    outcome10_list[i + j] = report_table_10_changed_2[0]
                    report_table_10_changed_2.remove(report_table_10_changed_2[0])
                elif outcome10_list[i + j][1] == 4:
                    outcome10_list[i + j] = report_table_10_changed_4[0]
                    report_table_10_changed_4.remove(report_table_10_changed_4[0])
    for i in outcome10_list:
        value_10 = value_10 + i[3]
    # outcome for 6
    value_11 = 0
    outcome11_list = [report_table_6[0]]
    player_list_11 = []
    for i in outcome11_list:
        if i[0] != 0:
            player_list_11.append(i[0])
    report_table_11_changed_6 = report_table_6[1:]
    for i in report_table_11_changed_6:
        if i[0] in player_list_11:
            report_table_11_changed_6.remove(i)
    for i in range(len(outcome11_list)):
        for j in range(1, (len(outcome11_list) - i)):
            if outcome11_list[i][0] == outcome11_list[i + j][0] != 0:
                if outcome11_list[i + j][1] == 6:
                    outcome11_list[i + j] = report_table_11_changed_6[0]
                    report_table_11_changed_6.remove(report_table_11_changed_6[0])
    for i in outcome11_list:
        value_11 = value_11 + i[3]
    outcomes_list = [
        outcome1_list,
        outcome2_list,
        outcome3_list,
        outcome4_list,
        outcome5_list,
        outcome6_list,
        outcome7_list,
        outcome8_list,
        outcome9_list,
        outcome10_list,
        outcome11_list,
    ]
    values = [
        value_1,
        value_2,
        value_3,
        value_4,
        value_5,
        value_6,
        value_7,
        value_8,
        value_9,
        value_10,
        value_11,
    ]
    utility_truth_1 = (
        0  # initialize the utility of player one under truth-telling strategy
    )

    # find the optimal outcome
    for a in range(len(values)):
        value_a = values[a]
        if value_a == max(values):
            social_value = value_a
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == a:
                    for p in outcome_m:
                        if p[0] == 1:
                            print(z, "---truth---")
                            print(
                                "allocate",
                                "table",
                                p[1],
                                " and course",
                                p[2],
                                "to player",
                                p[0],
                            )

                            # calcluate second price
                            sereport_table_1 = [k for k in report_table_1 if k[0] != 1]
                            sereport_table_2 = [k for k in report_table_2 if k[0] != 1]
                            sereport_table_3 = [k for k in report_table_3 if k[0] != 1]
                            sereport_table_4 = [k for k in report_table_4 if k[0] != 1]
                            sereport_table_5 = [k for k in report_table_5 if k[0] != 1]
                            sereport_table_6 = [k for k in report_table_6 if k[0] != 1]
                            # outcome for 1*5
                            sevalue_1 = 0
                            seoutcome1_list = [
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                            ]
                            seplayer_list_1 = []
                            for i in seoutcome1_list:
                                if i[0] != 0:
                                    seplayer_list_1.append(i[0])
                            sereport_table_1_changed = sereport_table_1[5:]
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
                                        seoutcome1_list[
                                            i + j
                                        ] = sereport_table_1_changed[0]
                                        sereport_table_1_changed.remove(
                                            sereport_table_1_changed[0]
                                        )
                            for i in seoutcome1_list:
                                sevalue_1 = sevalue_1 + i[3]

                            # outcome for 2*2+1+1
                            sevalue_2 = 0
                            seoutcome2_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            seplayer_list_2 = []
                            for i in seoutcome2_list:
                                if i[0] != 0:
                                    seplayer_list_2.append(i[0])
                            sereport_table_2_changed_1 = sereport_table_1[2:]
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

                            # outcome for 2+1*4
                            sevalue_3 = 0
                            seoutcome3_list = [
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            seplayer_list_3 = []
                            for i in seoutcome3_list:
                                if i[0] != 0:
                                    seplayer_list_3.append(i[0])
                            sereport_table_3_changed_1 = sereport_table_1[4:]
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

                            # outcome for 3+2+1
                            sevalue_4 = 0
                            seoutcome4_list = [
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_4 = []
                            for i in seoutcome4_list:
                                if i[0] != 0:
                                    seplayer_list_4.append(i[0])
                            sereport_table_4_changed_1 = sereport_table_1[1:]
                            sereport_table_4_changed_2 = sereport_table_2[1:]
                            sereport_table_4_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_4_changed_1:
                                if i[0] in seplayer_list_4:
                                    sereport_table_4_changed_1.remove(i)
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
                                        elif seoutcome4_list[i + j][1] == 1:
                                            seoutcome4_list[
                                                i + j
                                            ] = sereport_table_4_changed_1[0]
                                            sereport_table_4_changed_1.remove(
                                                sereport_table_4_changed_1[0]
                                            )
                            for i in seoutcome4_list:
                                sevalue_4 = sevalue_4 + i[3]

                            # outcome for 3+1+1+1
                            sevalue_5 = 0
                            seoutcome5_list = [
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            seplayer_list_5 = []
                            for i in seoutcome5_list:
                                if i[0] != 0:
                                    seplayer_list_5.append(i[0])
                            sereport_table_5_changed_1 = sereport_table_1[3:]
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

                            # outcome for 4+1+1
                            sevalue_6 = 0
                            seoutcome6_list = [
                                sereport_table_4[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            seplayer_list_6 = []
                            for i in seoutcome6_list:
                                if i[0] != 0:
                                    seplayer_list_6.append(i[0])
                            sereport_table_6_changed_1 = sereport_table_1[2:]
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

                            # outcome for 5+1
                            sevalue_7 = 0
                            seoutcome7_list = [
                                sereport_table_5[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_7 = []
                            for i in seoutcome7_list:
                                if i[0] != 0:
                                    seplayer_list_7.append(i[0])
                            sereport_table_7_changed_1 = sereport_table_1[1:]
                            sereport_table_7_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_7_changed_1:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_1.remove(i)
                            for i in sereport_table_7_changed_5:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_5.remove(i)
                            for i in range(len(seoutcome7_list)):
                                for j in range(1, (len(seoutcome7_list) - i)):
                                    if (
                                        seoutcome7_list[i][0]
                                        == seoutcome7_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome7_list[i + j][1] == 1:
                                            seoutcome7_list[
                                                i + j
                                            ] = sereport_table_7_changed_1[0]
                                            sereport_table_7_changed_1.remove(
                                                sereport_table_7_changed_1[0]
                                            )
                                        elif seoutcome7_list[i + j][1] == 5:
                                            seoutcome7_list[
                                                i + j
                                            ] = sereport_table_7_changed_5[0]
                                            sereport_table_7_changed_5.remove(
                                                sereport_table_7_changed_5[0]
                                            )
                            for i in seoutcome7_list:
                                sevalue_7 = sevalue_7 + i[3]
                            # outcome for 2*3
                            sevalue_8 = 0
                            seoutcome8_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                            ]
                            seplayer_list_8 = []
                            for i in outcome8_list:
                                if i[0] != 0:
                                    seplayer_list_8.append(i[0])
                            sereport_table_8_changed = sereport_table_2[3:]
                            for i in sereport_table_8_changed:
                                if i[0] in seplayer_list_8:
                                    sereport_table_8_changed.remove(i)
                            for i in range(len(seoutcome8_list)):
                                for j in range(1, (len(seoutcome8_list) - i)):
                                    if (
                                        seoutcome8_list[i][0]
                                        == seoutcome8_list[i + j][0]
                                        != 0
                                    ):
                                        seoutcome8_list[
                                            i + j
                                        ] = sereport_table_8_changed[0]
                                        sereport_table_8_changed.remove(
                                            sereport_table_8_changed[0]
                                        )
                            for i in seoutcome8_list:
                                sevalue_8 = sevalue_8 + i[3]
                            # outcome for 3*2
                            sevalue_9 = 0
                            seoutcome9_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                            ]
                            seplayer_list_9 = []
                            for i in seoutcome9_list:
                                if i[0] != 0:
                                    seplayer_list_9.append(i[0])
                            sereport_table_9_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_9_changed_3:
                                if i[0] in seplayer_list_9:
                                    sereport_table_9_changed_3.remove(i)
                            for i in range(len(seoutcome9_list)):
                                for j in range(1, (len(seoutcome9_list) - i)):
                                    if (
                                        seoutcome9_list[i][0]
                                        == seoutcome9_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome9_list[i + j][1] == 3:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_3[0]
                                            sereport_table_9_changed_3.remove(
                                                sereport_table_9_changed_3[0]
                                            )
                            for i in seoutcome9_list:
                                sevalue_9 = sevalue_9 + i[3]
                            # outcome for 4+2
                            sevalue_10 = 0
                            seoutcome10_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                            ]
                            seplayer_list_10 = []
                            for i in seoutcome10_list:
                                if i[0] != 0:
                                    seplayer_list_10.append(i[0])
                            sereport_table_10_changed_2 = sereport_table_2[1:]
                            sereport_table_10_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_10_changed_2:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_2.remove(i)
                            for i in sereport_table_10_changed_4:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_4.remove(i)
                            for i in range(len(seoutcome10_list)):
                                for j in range(1, (len(seoutcome10_list) - i)):
                                    if (
                                        seoutcome10_list[i][0]
                                        == seoutcome10_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome10_list[i + j][1] == 2:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_2[0]
                                            sereport_table_10_changed_2.remove(
                                                sereport_table_10_changed_2[0]
                                            )
                                        elif seoutcome10_list[i + j][1] == 4:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_4[0]
                                            sereport_table_10_changed_4.remove(
                                                sereport_table_10_changed_4[0]
                                            )
                            for i in seoutcome10_list:
                                sevalue_10 = sevalue_10 + i[3]
                            # outcome for 6
                            sevalue_11 = 0
                            seoutcome11_list = [sereport_table_6[0]]
                            seplayer_list_11 = []
                            for i in seoutcome11_list:
                                if i[0] != 0:
                                    seplayer_list_11.append(i[0])
                            sereport_table_11_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_11_changed_6:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_6.remove(i)
                            for i in range(len(seoutcome11_list)):
                                for j in range(1, (len(seoutcome11_list) - i)):
                                    if (
                                        seoutcome11_list[i][0]
                                        == seoutcome11_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome11_list[i + j][1] == 6:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_6[0]
                                            sereport_table_11_changed_6.remove(
                                                sereport_table_11_changed_6[0]
                                            )
                            for i in seoutcome11_list:
                                sevalue_11 = sevalue_11 + i[3]
                            sevalues = [
                                sevalue_1,
                                sevalue_2,
                                sevalue_3,
                                sevalue_4,
                                sevalue_5,
                                sevalue_6,
                                sevalue_7,
                                sevalue_8,
                                sevalue_9,
                                sevalue_10,
                                sevalue_11,
                            ]
                            for n in sevalues:
                                if n == max(sevalues):
                                    second_value = n
                                    monetary_transfer = -(
                                        social_value - p[3] - second_value
                                    )
                                    res_revenue = res_revenue + monetary_transfer
                                    utility_truth_1 = p[3] - monetary_transfer
                                    print("utility for", p[0], ":", utility_truth_1)
                                    break
                                else:
                                    pass
            break
        else:
            pass

    # if player one random-telling, others random-telling
    random_table_1 = []
    random_table_2 = []
    random_table_3 = []
    random_table_4 = []
    random_table_5 = []
    random_table_6 = []
    random_table_list = [
        random_table_1,
        random_table_2,
        random_table_3,
        random_table_4,
        random_table_5,
        random_table_6,
    ]
    for i in range(len(random_table)):
        if random_table[i][1] == 1:
            random_table_1.append(random_table[i])
        elif random_table[i][1] == 2:
            random_table_2.append(random_table[i])
        elif random_table[i][1] == 3:
            random_table_3.append(random_table[i])
        elif random_table[i][1] == 4:
            random_table_4.append(random_table[i])
        elif random_table[i][1] == 5:
            random_table_5.append(random_table[i])
        elif random_table[i][1] == 6:
            random_table_6.append(random_table[i])
    # fill the blank list
    while len(random_table_1) < 20:
        random_table_1.append([0, 1, 0, 0])
    while len(random_table_2) < 10:
        random_table_2.append([0, 2, 0, 0])
    while len(random_table_3) < 10:
        random_table_3.append([0, 3, 0, 0])
    while len(random_table_4) < 10:
        random_table_4.append([0, 4, 0, 0])
    while len(random_table_5) < 10:
        random_table_5.append([0, 5, 0, 0])
    while len(random_table_6) < 10:
        random_table_6.append([0, 6, 0, 0])
    random_table_1.sort(key=takeValue, reverse=True)
    random_table_2.sort(key=takeValue, reverse=True)
    random_table_3.sort(key=takeValue, reverse=True)
    random_table_4.sort(key=takeValue, reverse=True)
    random_table_5.sort(key=takeValue, reverse=True)
    random_table_6.sort(key=takeValue, reverse=True)
    # outcome for 1*5
    random_value_1 = 0
    random_outcome1_list = [
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
    ]
    random_player_list_1 = []
    for i in random_outcome1_list:
        if i[0] != 0:
            random_player_list_1.append(i[0])
    random_table_1_changed = random_table_1[5:]
    for i in random_table_1_changed:
        if i[0] in random_player_list_1:
            random_table_1_changed.remove(i)
    for i in range(len(random_outcome1_list)):
        for j in range(1, (len(random_outcome1_list) - i)):
            if random_outcome1_list[i][0] == random_outcome1_list[i + j][0] != 0:
                random_outcome1_list[i + j] = random_table_1_changed[0]
                random_table_1_changed.remove(random_table_1_changed[0])
    for i in random_outcome1_list:
        random_value_1 = random_value_1 + i[3]

    # outcome for 2*2+1+1
    random_value_2 = 0
    random_outcome2_list = [
        random_table_2[0],
        random_table_2[1],
        random_table_1[0],
        random_table_1[1],
    ]
    random_player_list_2 = []
    for i in random_outcome2_list:
        if i[0] != 0:
            random_player_list_2.append(i[0])
    random_table_2_changed_1 = random_table_1[2:]
    random_table_2_changed_2 = random_table_2[2:]
    for i in random_table_2_changed_1:
        if i[0] in random_player_list_2:
            random_table_2_changed_1.remove(i)
    for i in random_table_2_changed_2:
        if i[0] in random_player_list_2:
            random_table_2_changed_2.remove(i)
    for i in range(len(random_outcome2_list)):
        for j in range(1, (len(random_outcome2_list) - i)):
            if random_outcome2_list[i][0] == random_outcome2_list[i + j][0] != 0:
                if random_outcome2_list[i + j][1] == 1:
                    random_outcome2_list[i + j] = random_table_2_changed_1[0]
                    random_table_2_changed_1.remove(random_table_2_changed_1[0])
                elif random_outcome2_list[i + j][1] == 2:
                    random_outcome2_list[i + j] = random_table_2_changed_2[0]
                    random_table_2_changed_2.remove(random_table_2_changed_2[0])
    for i in random_outcome2_list:
        random_value_2 = random_value_2 + i[3]

    # outcome for 2+1*4
    random_value_3 = 0
    random_outcome3_list = [
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
    ]
    random_player_list_3 = []
    for i in random_outcome3_list:
        if i[0] != 0:
            random_player_list_3.append(i[0])
    random_table_3_changed_1 = random_table_1[4:]
    random_table_3_changed_2 = random_table_2[1:]
    for i in random_table_3_changed_1:
        if i[0] in random_player_list_3:
            random_table_3_changed_1.remove(i)
    for i in random_table_3_changed_2:
        if i[0] in random_player_list_3:
            random_table_3_changed_2.remove(i)
    for i in range(len(random_outcome3_list)):
        for j in range(1, (len(random_outcome3_list) - i)):
            if random_outcome3_list[i][0] == random_outcome3_list[i + j][0] != 0:
                if random_outcome3_list[i + j][1] == 1:
                    random_outcome3_list[i + j] = random_table_3_changed_1[0]
                    random_table_3_changed_1.remove(random_table_3_changed_1[0])
                elif random_outcome3_list[i + j][1] == 2:
                    random_outcome3_list[i + j] = random_table_3_changed_2[0]
                    random_table_3_changed_2.remove(random_table_3_changed_2[0])
    for i in random_outcome3_list:
        random_value_3 = random_value_3 + i[3]

    # outcome for 3+2+1
    random_value_4 = 0
    random_outcome4_list = [
        random_table_3[0],
        random_table_2[0],
        random_table_1[0],
    ]
    random_player_list_4 = []
    for i in random_outcome4_list:
        if i[0] != 0:
            random_player_list_4.append(i[0])
    random_table_4_changed_1 = random_table_1[1:]
    random_table_4_changed_2 = random_table_2[1:]
    random_table_4_changed_3 = random_table_3[1:]
    for i in random_table_4_changed_1:
        if i[0] in random_player_list_4:
            random_table_4_changed_1.remove(i)
    for i in random_table_4_changed_2:
        if i[0] in random_player_list_4:
            random_table_4_changed_2.remove(i)
    for i in random_table_4_changed_3:
        if i[0] in random_player_list_4:
            random_table_4_changed_3.remove(i)
    for i in range(len(random_outcome4_list)):
        for j in range(1, (len(random_outcome4_list) - i)):
            if random_outcome4_list[i][0] == random_outcome4_list[i + j][0] != 0:
                if random_outcome4_list[i + j][1] == 2:
                    random_outcome4_list[i + j] = random_table_4_changed_2[0]
                    random_table_4_changed_2.remove(random_table_4_changed_2[0])
                elif random_outcome4_list[i + j][1] == 3:
                    random_outcome4_list[i + j] = random_table_4_changed_3[0]
                    random_table_4_changed_3.remove(random_table_4_changed_3[0])
                elif random_outcome4_list[i + j][1] == 1:
                    random_outcome4_list[i + j] = random_table_4_changed_1[0]
                    random_table_4_changed_1.remove(random_table_4_changed_1[0])
    for i in random_outcome4_list:
        random_value_4 = random_value_4 + i[3]

    # outcome for 3+1+1+1
    random_value_5 = 0
    random_outcome5_list = [
        random_table_3[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
    ]
    random_player_list_5 = []
    for i in random_outcome5_list:
        if i[0] != 0:
            random_player_list_5.append(i[0])
    random_table_5_changed_1 = random_table_1[3:]
    random_table_5_changed_3 = random_table_3[1:]
    for i in random_table_5_changed_1:
        if i[0] in random_player_list_5:
            random_table_5_changed_1.remove(i)
    for i in random_table_5_changed_3:
        if i[0] in random_player_list_5:
            random_table_5_changed_3.remove(i)
    for i in range(len(random_outcome5_list)):
        for j in range(1, (len(random_outcome5_list) - i)):
            if random_outcome5_list[i][0] == random_outcome5_list[i + j][0] != 0:
                if random_outcome5_list[i + j][1] == 1:
                    random_outcome5_list[i + j] = random_table_5_changed_1[0]
                    random_table_5_changed_1.remove(random_table_5_changed_1[0])
                elif random_outcome5_list[i + j][1] == 3:
                    random_outcome5_list[i + j] = random_table_5_changed_3[0]
                    random_table_5_changed_3.remove(random_table_5_changed_3[0])
    for i in random_outcome5_list:
        random_value_5 = random_value_5 + i[3]

    # outcome for 4+1+1
    random_value_6 = 0
    random_outcome6_list = [
        random_table_4[0],
        random_table_1[0],
        random_table_1[1],
    ]
    random_player_list_6 = []
    for i in random_outcome6_list:
        if i[0] != 0:
            random_player_list_6.append(i[0])
    random_table_6_changed_1 = random_table_1[2:]
    random_table_6_changed_4 = random_table_4[1:]
    for i in random_table_6_changed_1:
        if i[0] in random_player_list_6:
            random_table_6_changed_1.remove(i)
    for i in random_table_6_changed_4:
        if i[0] in random_player_list_6:
            random_table_6_changed_4.remove(i)
    for i in range(len(random_outcome6_list)):
        for j in range(1, (len(random_outcome6_list) - i)):
            if random_outcome6_list[i][0] == random_outcome6_list[i + j][0] != 0:
                if random_outcome6_list[i + j][1] == 1:
                    random_outcome6_list[i + j] = random_table_6_changed_1[0]
                    random_table_6_changed_1.remove(random_table_6_changed_1[0])
                elif random_outcome6_list[i + j][1] == 4:
                    random_outcome6_list[i + j] = random_table_6_changed_4[0]
                    random_table_6_changed_4.remove(random_table_6_changed_4[0])
    for i in random_outcome6_list:
        random_value_6 = random_value_6 + i[3]

    # outcome for 5+1
    random_value_7 = 0
    random_outcome7_list = [
        random_table_5[0],
        random_table_1[0],
    ]
    random_player_list_7 = []
    for i in random_outcome7_list:
        if i[0] != 0:
            random_player_list_7.append(i[0])
    random_table_7_changed_1 = random_table_1[1:]
    random_table_7_changed_5 = random_table_5[1:]
    for i in random_table_7_changed_1:
        if i[0] in random_player_list_7:
            random_table_7_changed_1.remove(i)
    for i in random_table_7_changed_5:
        if i[0] in random_player_list_7:
            random_table_7_changed_5.remove(i)
    for i in range(len(random_outcome7_list)):
        for j in range(1, (len(random_outcome7_list) - i)):
            if random_outcome7_list[i][0] == random_outcome7_list[i + j][0] != 0:
                if random_outcome7_list[i + j][1] == 1:
                    random_outcome7_list[i + j] = random_table_7_changed_1[0]
                    random_table_7_changed_1.remove(random_table_7_changed_1[0])
                elif random_outcome7_list[i + j][1] == 5:
                    random_outcome7_list[i + j] = random_table_7_changed_5[0]
                    random_table_7_changed_5.remove(random_table_7_changed_5[0])
    for i in random_outcome7_list:
        random_value_7 = random_value_7 + i[3]
    # outcome for 2*3
    random_value_8 = 0
    random_outcome8_list = [
        random_table_2[0],
        random_table_2[1],
        random_table_2[2],
    ]
    random_player_list_8 = []
    for i in random_outcome8_list:
        if i[0] != 0:
            random_player_list_8.append(i[0])
    random_table_8_changed = random_table_2[3:]
    for i in random_table_8_changed:
        if i[0] in random_player_list_8:
            random_table_8_changed.remove(i)
    for i in range(len(random_outcome8_list)):
        for j in range(1, (len(random_outcome8_list) - i)):
            if random_outcome8_list[i][0] == random_outcome8_list[i + j][0] != 0:
                random_outcome8_list[i + j] = random_table_8_changed[0]
                random_table_8_changed.remove(random_table_8_changed[0])
    for i in random_outcome8_list:
        random_value_8 = random_value_8 + i[3]
    # outcome for 3*2
    random_value_9 = 0
    random_outcome9_list = [
        random_table_3[0],
        random_table_3[1],
    ]
    random_player_list_9 = []
    for i in random_outcome9_list:
        if i[0] != 0:
            random_player_list_9.append(i[0])
    random_table_9_changed_3 = random_table_3[2:]
    for i in random_table_9_changed_3:
        if i[0] in random_player_list_9:
            random_table_9_changed_3.remove(i)
    for i in range(len(random_outcome9_list)):
        for j in range(1, (len(random_outcome9_list) - i)):
            if random_outcome9_list[i][0] == random_outcome9_list[i + j][0] != 0:
                if random_outcome9_list[i + j][1] == 3:
                    random_outcome9_list[i + j] = random_table_9_changed_3[0]
                    random_table_9_changed_3.remove(random_table_9_changed_3[0])
    for i in random_outcome9_list:
        random_value_9 = random_value_9 + i[3]
    # outcome for 4+2
    random_value_10 = 0
    random_outcome10_list = [random_table_4[0], random_table_2[0]]
    random_player_list_10 = []
    for i in random_outcome10_list:
        if i[0] != 0:
            random_player_list_10.append(i[0])
    random_table_10_changed_2 = random_table_2[1:]
    random_table_10_changed_4 = random_table_4[1:]
    for i in random_table_10_changed_2:
        if i[0] in random_player_list_10:
            random_table_10_changed_2.remove(i)
    for i in random_table_10_changed_4:
        if i[0] in random_player_list_10:
            random_table_10_changed_4.remove(i)
    for i in range(len(random_outcome10_list)):
        for j in range(1, (len(random_outcome10_list) - i)):
            if random_outcome10_list[i][0] == random_outcome10_list[i + j][0] != 0:
                if random_outcome10_list[i + j][1] == 2:
                    random_outcome10_list[i + j] = random_table_10_changed_2[0]
                    random_table_10_changed_2.remove(random_table_10_changed_2[0])
                elif random_outcome10_list[i + j][1] == 4:
                    random_outcome10_list[i + j] = random_table_10_changed_4[0]
                    random_table_10_changed_4.remove(random_table_10_changed_4[0])
    for i in random_outcome10_list:
        random_value_10 = random_value_10 + i[3]
    # outcome for 6
    random_value_11 = 0
    random_outcome11_list = [random_table_6[0]]
    random_player_list_11 = []
    for i in random_outcome11_list:
        if i[0] != 0:
            random_player_list_11.append(i[0])
    random_table_11_changed_6 = random_table_6[1:]
    for i in random_table_11_changed_6:
        if i[0] in random_player_list_11:
            random_table_11_changed_6.remove(i)
    for i in range(len(random_outcome11_list)):
        for j in range(1, (len(random_outcome11_list) - i)):
            if random_outcome11_list[i][0] == random_outcome11_list[i + j][0] != 0:
                if random_outcome11_list[i + j][1] == 6:
                    random_outcome11_list[i + j] = random_table_11_changed_6[0]
                    random_table_11_changed_6.remove(random_table_11_changed_6[0])
    for i in random_outcome11_list:
        random_value_11 = random_value_11 + i[3]
    random_outcomes_list = [
        random_outcome1_list,
        random_outcome2_list,
        random_outcome3_list,
        random_outcome4_list,
        random_outcome5_list,
        random_outcome6_list,
        random_outcome7_list,
        random_outcome8_list,
        random_outcome9_list,
        random_outcome10_list,
        random_outcome11_list,
    ]
    random_values = [
        random_value_1,
        random_value_2,
        random_value_3,
        random_value_4,
        random_value_5,
        random_value_6,
        random_value_7,
        random_value_8,
        random_value_9,
        random_value_10,
        random_value_11,
    ]
    utility_random_1 = (
        0  # initialize the utility of player one under random-telling strategy
    )
    # find the optimal outcome
    for a in range(len(random_values)):
        random_value_a = random_values[a]
        if random_value_a == max(random_values):
            social_value = random_value_a
            res_revenue = 0
            for m in range(len(random_outcomes_list)):
                random_outcome_m = random_outcomes_list[m]
                if m == a:
                    for p in random_outcome_m:
                        if p[0] == 1:
                            print(z, "---random---")
                            print(
                                "allocate",
                                "table",
                                p[1],
                                " and course",
                                p[2],
                                "to player",
                                p[0],
                            )

                            # calcluate second price
                            sereport_table_1 = [k for k in random_table_1 if k[0] != 1]
                            sereport_table_2 = [k for k in random_table_2 if k[0] != 1]
                            sereport_table_3 = [k for k in random_table_3 if k[0] != 1]
                            sereport_table_4 = [k for k in random_table_4 if k[0] != 1]
                            sereport_table_5 = [k for k in random_table_5 if k[0] != 1]
                            sereport_table_6 = [k for k in random_table_6 if k[0] != 1]

                            # outcome for 1*5
                            sevalue_1 = 0
                            seoutcome1_list = [
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                            ]
                            seplayer_list_1 = []
                            for i in seoutcome1_list:
                                if i[0] != 0:
                                    seplayer_list_1.append(i[0])
                            sereport_table_1_changed = sereport_table_1[5:]
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
                                        seoutcome1_list[
                                            i + j
                                        ] = sereport_table_1_changed[0]
                                        sereport_table_1_changed.remove(
                                            sereport_table_1_changed[0]
                                        )
                            for i in seoutcome1_list:
                                sevalue_1 = sevalue_1 + i[3]

                            # outcome for 2*2+1+1
                            sevalue_2 = 0
                            seoutcome2_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            seplayer_list_2 = []
                            for i in seoutcome2_list:
                                if i[0] != 0:
                                    seplayer_list_2.append(i[0])
                            sereport_table_2_changed_1 = sereport_table_1[2:]
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

                            # outcome for 2+1*4
                            sevalue_3 = 0
                            seoutcome3_list = [
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            seplayer_list_3 = []
                            for i in seoutcome3_list:
                                if i[0] != 0:
                                    seplayer_list_3.append(i[0])
                            sereport_table_3_changed_1 = sereport_table_1[4:]
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

                            # outcome for 3+2+1
                            sevalue_4 = 0
                            seoutcome4_list = [
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_4 = []
                            for i in seoutcome4_list:
                                if i[0] != 0:
                                    seplayer_list_4.append(i[0])
                            sereport_table_4_changed_1 = sereport_table_1[1:]
                            sereport_table_4_changed_2 = sereport_table_2[1:]
                            sereport_table_4_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_4_changed_1:
                                if i[0] in seplayer_list_4:
                                    sereport_table_4_changed_1.remove(i)
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
                                        elif seoutcome4_list[i + j][1] == 1:
                                            seoutcome4_list[
                                                i + j
                                            ] = sereport_table_4_changed_1[0]
                                            sereport_table_4_changed_1.remove(
                                                sereport_table_4_changed_1[0]
                                            )
                            for i in seoutcome4_list:
                                sevalue_4 = sevalue_4 + i[3]

                            # outcome for 3+1+1+1
                            sevalue_5 = 0
                            seoutcome5_list = [
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            seplayer_list_5 = []
                            for i in seoutcome5_list:
                                if i[0] != 0:
                                    seplayer_list_5.append(i[0])
                            sereport_table_5_changed_1 = sereport_table_1[3:]
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

                            # outcome for 4+1+1
                            sevalue_6 = 0
                            seoutcome6_list = [
                                sereport_table_4[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            seplayer_list_6 = []
                            for i in seoutcome6_list:
                                if i[0] != 0:
                                    seplayer_list_6.append(i[0])
                            sereport_table_6_changed_1 = sereport_table_1[2:]
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

                            # outcome for 5+1
                            sevalue_7 = 0
                            seoutcome7_list = [
                                sereport_table_5[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_7 = []
                            for i in seoutcome7_list:
                                if i[0] != 0:
                                    seplayer_list_7.append(i[0])
                            sereport_table_7_changed_1 = sereport_table_1[1:]
                            sereport_table_7_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_7_changed_1:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_1.remove(i)
                            for i in sereport_table_7_changed_5:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_5.remove(i)
                            for i in range(len(seoutcome7_list)):
                                for j in range(1, (len(seoutcome7_list) - i)):
                                    if (
                                        seoutcome7_list[i][0]
                                        == seoutcome7_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome7_list[i + j][1] == 1:
                                            seoutcome7_list[
                                                i + j
                                            ] = sereport_table_7_changed_1[0]
                                            sereport_table_7_changed_1.remove(
                                                sereport_table_7_changed_1[0]
                                            )
                                        elif seoutcome7_list[i + j][1] == 5:
                                            seoutcome7_list[
                                                i + j
                                            ] = sereport_table_7_changed_5[0]
                                            sereport_table_7_changed_5.remove(
                                                sereport_table_7_changed_5[0]
                                            )
                            for i in seoutcome7_list:
                                sevalue_7 = sevalue_7 + i[3]
                            # outcome for 2*3
                            sevalue_8 = 0
                            seoutcome8_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                            ]
                            seplayer_list_8 = []
                            for i in outcome8_list:
                                if i[0] != 0:
                                    seplayer_list_8.append(i[0])
                            sereport_table_8_changed = sereport_table_2[3:]
                            for i in sereport_table_8_changed:
                                if i[0] in seplayer_list_8:
                                    sereport_table_8_changed.remove(i)
                            for i in range(len(seoutcome8_list)):
                                for j in range(1, (len(seoutcome8_list) - i)):
                                    if (
                                        seoutcome8_list[i][0]
                                        == seoutcome8_list[i + j][0]
                                        != 0
                                    ):
                                        seoutcome8_list[
                                            i + j
                                        ] = sereport_table_8_changed[0]
                                        sereport_table_8_changed.remove(
                                            sereport_table_8_changed[0]
                                        )
                            for i in seoutcome8_list:
                                sevalue_8 = sevalue_8 + i[3]
                            # outcome for 3*2
                            sevalue_9 = 0
                            seoutcome9_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                            ]
                            seplayer_list_9 = []
                            for i in seoutcome9_list:
                                if i[0] != 0:
                                    seplayer_list_9.append(i[0])
                            sereport_table_9_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_9_changed_3:
                                if i[0] in seplayer_list_9:
                                    sereport_table_9_changed_3.remove(i)
                            for i in range(len(seoutcome9_list)):
                                for j in range(1, (len(seoutcome9_list) - i)):
                                    if (
                                        seoutcome9_list[i][0]
                                        == seoutcome9_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome9_list[i + j][1] == 3:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_3[0]
                                            sereport_table_9_changed_3.remove(
                                                sereport_table_9_changed_3[0]
                                            )
                            for i in seoutcome9_list:
                                sevalue_9 = sevalue_9 + i[3]
                            # outcome for 4+2
                            sevalue_10 = 0
                            seoutcome10_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                            ]
                            seplayer_list_10 = []
                            for i in seoutcome10_list:
                                if i[0] != 0:
                                    seplayer_list_10.append(i[0])
                            sereport_table_10_changed_2 = sereport_table_2[1:]
                            sereport_table_10_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_10_changed_2:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_2.remove(i)
                            for i in sereport_table_10_changed_4:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_4.remove(i)
                            for i in range(len(seoutcome10_list)):
                                for j in range(1, (len(seoutcome10_list) - i)):
                                    if (
                                        seoutcome10_list[i][0]
                                        == seoutcome10_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome10_list[i + j][1] == 2:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_2[0]
                                            sereport_table_10_changed_2.remove(
                                                sereport_table_10_changed_2[0]
                                            )
                                        elif seoutcome10_list[i + j][1] == 4:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_4[0]
                                            sereport_table_10_changed_4.remove(
                                                sereport_table_10_changed_4[0]
                                            )
                            for i in seoutcome10_list:
                                sevalue_10 = sevalue_10 + i[3]
                            # outcome for 6
                            sevalue_11 = 0
                            seoutcome11_list = [sereport_table_6[0]]
                            seplayer_list_11 = []
                            for i in seoutcome11_list:
                                if i[0] != 0:
                                    seplayer_list_11.append(i[0])
                            sereport_table_11_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_11_changed_6:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_6.remove(i)
                            for i in range(len(seoutcome11_list)):
                                for j in range(1, (len(seoutcome11_list) - i)):
                                    if (
                                        seoutcome11_list[i][0]
                                        == seoutcome11_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome11_list[i + j][1] == 6:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_6[0]
                                            sereport_table_11_changed_6.remove(
                                                sereport_table_11_changed_6[0]
                                            )
                            for i in seoutcome11_list:
                                sevalue_11 = sevalue_11 + i[3]
                            sevalues = [
                                sevalue_1,
                                sevalue_2,
                                sevalue_3,
                                sevalue_4,
                                sevalue_5,
                                sevalue_6,
                                sevalue_7,
                                sevalue_8,
                                sevalue_9,
                                sevalue_10,
                                sevalue_11,
                            ]
                            for n in sevalues:
                                if n == max(sevalues):
                                    second_value = n
                                    monetary_transfer = -(
                                        social_value - p[3] - second_value
                                    )
                                    res_revenue = res_revenue + monetary_transfer
                                    p1_value = p1.loc[p[1], p[2]]
                                    utility_random_1 = p1_value - monetary_transfer
                                    print("utility for", p[0], ":", utility_random_1)
                                    break
                                else:
                                    pass
            break
        else:
            pass
    utility_change_1 = utility_change_1 + (utility_truth_1 - utility_random_1)
    if utility_random_1 > utility_truth_1:
        bug = bug + 1

print("bug =", bug)

utility_change_1 = utility_change_1 / 10000
print("average utility changed under truth-telling strategy:", utility_change_1)
"""
bug = 14
average utility changed under truth-telling strategy: 2.5267
"""

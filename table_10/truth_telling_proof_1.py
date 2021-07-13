import pandas as pd
import random

# table = 10, course = 3, consumer = 30


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
    consumer = 100
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
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
            ],
            columns=["A", "B", "C"],
            index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )
        pi_random = pd.DataFrame(
            [
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
                [random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
            ],
            columns=["A", "B", "C"],
            index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

        if i == 0:
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
            # one reported situation
            pi_value = pi_value_list[0]
            pi_report = [i + 1,] + getIndexes(pi, pi_value)[0]
            p1_report = pi_report

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
        # one randomly reported situation
        pi_random_value = pi_random_value_list[0]
        pi_random_report = [i + 1,] + getIndexes(pi_random, pi_random_value)[0]
        random_table = random_table + [pi_random_report]

    # classify tables with table numbers
    report_table = [i for i in random_table if i[0] != 1]
    report_table.append(p1_report)
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    report_table_7 = []
    report_table_8 = []
    report_table_9 = []
    report_table_10 = []
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
        elif report_table[i][1] == 7:
            report_table_7.append(report_table[i])
        elif report_table[i][1] == 8:
            report_table_8.append(report_table[i])
        elif report_table[i][1] == 9:
            report_table_9.append(report_table[i])
        elif report_table[i][1] == 10:
            report_table_10.append(report_table[i])

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
    while len(report_table_7) < 10:
        report_table_7.append([0, 7, 0, 0])
    while len(report_table_8) < 10:
        report_table_8.append([0, 8, 0, 0])
    while len(report_table_9) < 10:
        report_table_9.append([0, 9, 0, 0])
    while len(report_table_10) < 10:
        report_table_10.append([0, 10, 0, 0])

    def takeValue(elem):
        return elem[3]

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)
    report_table_7.sort(key=takeValue, reverse=True)
    report_table_8.sort(key=takeValue, reverse=True)
    report_table_9.sort(key=takeValue, reverse=True)
    report_table_10.sort(key=takeValue, reverse=True)
    report_table_list = [
        report_table_1,
        report_table_2,
        report_table_3,
        report_table_4,
        report_table_5,
        report_table_6,
        report_table_7,
        report_table_8,
        report_table_9,
        report_table_10,
    ]

    # outcome for 1*9
    value_1 = 0
    outcome1_list = [
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
        report_table_1[5],
        report_table_1[6],
        report_table_1[7],
        report_table_1[8],
    ]
    for i in outcome1_list:
        value_1 = value_1 + i[3]
    # outcome for 2*5
    value_2 = 0
    outcome2_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_2[2],
        report_table_2[3],
        report_table_2[4],
    ]
    for i in outcome2_list:
        value_2 = value_2 + i[3]
    # outcome for 2*4+1*2
    value_3 = 0
    outcome3_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_2[2],
        report_table_2[3],
        report_table_1[0],
        report_table_1[1],
    ]
    for i in outcome3_list:
        value_3 = value_3 + i[3]
    # outcome for 2*3+1*4
    value_4 = 0
    outcome4_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_2[2],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
    ]
    for i in outcome4_list:
        value_4 = value_4 + i[3]
    # outcome for 2*2+1*6
    value_5 = 0
    outcome5_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
        report_table_1[5],
    ]
    for i in outcome5_list:
        value_5 = value_5 + i[3]
    # outcome for 2+1*8
    value_6 = 0
    outcome6_list = [
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
        report_table_1[5],
        report_table_1[6],
        report_table_1[7],
    ]
    for i in outcome6_list:
        value_6 = value_6 + i[3]
    # outcome for 3*3+1
    value_7 = 0
    outcome7_list = [
        report_table_3[0],
        report_table_3[1],
        report_table_3[2],
        report_table_1[0],
    ]
    for i in outcome7_list:
        value_7 = value_7 + i[3]
    # outcome for 3*2+2*2
    value_8 = 0
    outcome8_list = [
        report_table_3[0],
        report_table_3[1],
        report_table_2[0],
        report_table_2[1],
    ]
    for i in outcome8_list:
        value_8 = value_8 + i[3]
    # outcome for 3*2+2+1+1
    value_9 = 0
    outcome9_list = [
        report_table_3[0],
        report_table_3[1],
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
    ]
    for i in outcome9_list:
        value_9 = value_9 + i[3]
    # outcome for 3*2+1*4
    value_10 = 0
    outcome10_list = [
        report_table_3[0],
        report_table_3[1],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
    ]
    for i in outcome10_list:
        value_10 = value_10 + i[3]
    # outcome for 3+2*2+1*3
    value_11 = 0
    outcome11_list = [
        report_table_3[0],
        report_table_2[0],
        report_table_2[1],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
    ]
    for i in outcome11_list:
        value_11 = value_11 + i[3]
    # outcome for 3+2+1*5
    value_12 = 0
    outcome12_list = [
        report_table_3[0],
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
    ]
    for i in outcome12_list:
        value_12 = value_12 + i[3]
    # outcome for 3+1*7
    value_13 = 0
    outcome13_list = [
        report_table_3[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
        report_table_1[5],
        report_table_1[6],
    ]
    for i in outcome13_list:
        value_13 = value_13 + i[3]
    # outcome for 4*2+2
    value_14 = 0
    outcome14_list = [report_table_4[0], report_table_4[1], report_table_2[0]]
    for i in outcome14_list:
        value_14 = value_14 + i[3]
    # outcome for 4*2+1*2
    value_15 = 0
    outcome15_list = [
        report_table_4[0],
        report_table_4[1],
        report_table_1[0],
        report_table_1[1],
    ]
    for i in outcome15_list:
        value_15 = value_15 + i[3]
    # outcome for 4+3*2
    value_16 = 0
    outcome16_list = [report_table_4[0], report_table_3[0], report_table_3[1]]
    for i in outcome16_list:
        value_16 = value_16 + i[3]
    # outcome for 4+3+2+1
    value_17 = 0
    outcome17_list = [
        report_table_4[0],
        report_table_3[0],
        report_table_2[0],
        report_table_1[0],
    ]
    for i in outcome17_list:
        value_17 = value_17 + i[3]
    # outcome for 4+3+1*3
    value_18 = 0
    outcome18_list = [
        report_table_4[0],
        report_table_3[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
    ]
    for i in outcome18_list:
        value_18 = value_18 + i[3]
    # outcome for 4+2*3
    value_19 = 0
    outcome19_list = [
        report_table_4[0],
        report_table_2[0],
        report_table_2[1],
        report_table_2[2],
    ]
    for i in outcome19_list:
        value_19 = value_19 + i[3]
    # outcome for 4+2*2+1*2
    value_20 = 0
    outcome20_list = [
        report_table_4[0],
        report_table_2[0],
        report_table_2[1],
        report_table_1[0],
        report_table_1[1],
    ]
    for i in outcome20_list:
        value_20 = value_20 + i[3]
    # outcome for 4+2+1*4
    value_21 = 0
    outcome21_list = [
        report_table_4[0],
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
    ]
    for i in outcome21_list:
        value_21 = value_21 + i[3]
    # outcome for 4+1*6
    value_22 = 0
    outcome22_list = [
        report_table_4[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
        report_table_1[5],
    ]
    for i in outcome22_list:
        value_22 = value_22 + i[3]
    # outcome for 5*2
    value_23 = 0
    outcome23_list = [report_table_5[0], report_table_5[1]]
    for i in outcome23_list:
        value_23 = value_23 + i[3]
    # outcome for 5+4+1
    value_24 = 0
    outcome24_list = [report_table_5[0], report_table_4[0], report_table_1[0]]
    for i in outcome24_list:
        value_24 = value_24 + i[3]
    # outcome for 5+3+2
    value_25 = 0
    outcome25_list = [report_table_5[0], report_table_3[0], report_table_2[0]]
    for i in outcome25_list:
        value_25 = value_25 + i[3]
    # outcome for 5+3+1*2
    value_26 = 0
    outcome26_list = [
        report_table_5[0],
        report_table_3[0],
        report_table_1[0],
        report_table_1[1],
    ]
    for i in outcome26_list:
        value_26 = value_26 + i[3]
    # outcome for 5+2*2+1
    value_27 = 0
    outcome27_list = [
        report_table_5[0],
        report_table_2[0],
        report_table_2[1],
        report_table_1[0],
    ]
    for i in outcome27_list:
        value_27 = value_27 + i[3]
    # outcome for 5+2+1*3
    value_28 = 0
    outcome28_list = [
        report_table_5[0],
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
    ]
    for i in outcome28_list:
        value_28 = value_28 + i[3]
    # outcome for 5+1*5
    value_29 = 0
    outcome29_list = [
        report_table_5[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
        report_table_1[4],
    ]
    for i in outcome29_list:
        value_29 = value_29 + i[3]
    # outcome for 6+4
    value_30 = 0
    outcome30_list = [report_table_6[0], report_table_4[0]]
    for i in outcome30_list:
        value_30 = value_30 + i[3]
    # outcome for 6+3+1
    value_31 = 0
    outcome31_list = [report_table_6[0], report_table_3[0], report_table_1[0]]
    for i in outcome31_list:
        value_31 = value_31 + i[3]
    # outcome for 6+2*2
    value_32 = 0
    outcome32_list = [report_table_6[0], report_table_2[0], report_table_2[1]]
    for i in outcome32_list:
        value_32 = value_32 + i[3]
    # outcome for 6+2+1*2
    value_33 = 0
    outcome33_list = [
        report_table_6[0],
        report_table_2[0],
        report_table_1[0],
        report_table_1[1],
    ]
    for i in outcome33_list:
        value_33 = value_33 + i[3]
    # outcome for 6+1*4
    value_34 = 0
    outcome34_list = [
        report_table_6[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
        report_table_1[3],
    ]
    for i in outcome34_list:
        value_34 = value_34 + i[3]
    # outcome for 7+3
    value_35 = 0
    outcome35_list = [report_table_7[0], report_table_3[0]]
    for i in outcome35_list:
        value_35 = value_35 + i[3]
    # outcome for 7+2+1
    value_36 = 0
    outcome36_list = [report_table_7[0], report_table_2[0], report_table_1[0]]
    for i in outcome36_list:
        value_36 = value_36 + i[3]
    # outcome for 7+1*3
    value_37 = 0
    outcome37_list = [
        report_table_7[0],
        report_table_1[0],
        report_table_1[1],
        report_table_1[2],
    ]
    for i in outcome37_list:
        value_37 = value_37 + i[3]
    # outcome for 8+2
    value_38 = 0
    outcome38_list = [report_table_8[0], report_table_2[0]]
    for i in outcome38_list:
        value_38 = value_38 + i[3]
    # outcome for 8+1*2
    value_39 = 0
    outcome39_list = [report_table_8[0], report_table_1[0], report_table_1[1]]
    for i in outcome39_list:
        value_39 = value_39 + i[3]
    # outcome for 9+1
    value_40 = 0
    outcome40_list = [report_table_9[0], report_table_1[0]]
    for i in outcome40_list:
        value_40 = value_40 + i[3]
    # outcome for 10
    value_41 = 0
    outcome41_list = [report_table_10[0]]
    for i in outcome41_list:
        value_41 = value_41 + i[3]
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
        outcome12_list,
        outcome13_list,
        outcome14_list,
        outcome15_list,
        outcome16_list,
        outcome17_list,
        outcome18_list,
        outcome19_list,
        outcome20_list,
        outcome21_list,
        outcome22_list,
        outcome23_list,
        outcome24_list,
        outcome25_list,
        outcome26_list,
        outcome27_list,
        outcome28_list,
        outcome29_list,
        outcome30_list,
        outcome31_list,
        outcome32_list,
        outcome33_list,
        outcome34_list,
        outcome35_list,
        outcome36_list,
        outcome37_list,
        outcome38_list,
        outcome39_list,
        outcome40_list,
        outcome41_list,
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
        value_12,
        value_13,
        value_14,
        value_15,
        value_16,
        value_17,
        value_18,
        value_19,
        value_20,
        value_21,
        value_22,
        value_23,
        value_24,
        value_25,
        value_26,
        value_27,
        value_28,
        value_29,
        value_30,
        value_31,
        value_32,
        value_33,
        value_34,
        value_35,
        value_36,
        value_37,
        value_38,
        value_39,
        value_40,
        value_41,
    ]
    utility_truth_1 = (
        0  # initialize the utility of player one under truth-telling strategy
    )

    # find the optimal outcome
    for i in range(len(values)):
        value_i = values[i]
        if value_i == max(values):
            social_value = value_i
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == i:
                    for j in outcome_m:
                        if j[0] == 1:
                            print(
                                z,
                                "-----TRUTH--------" "allocate",
                                "table",
                                j[1],
                                " and course",
                                j[2],
                                "to player",
                                j[0],
                            )

                            # calcluate second price
                            sereport_table_1 = [k for k in report_table_1 if k[0] != 1]
                            sereport_table_2 = [k for k in report_table_2 if k[0] != 1]
                            sereport_table_3 = [k for k in report_table_3 if k[0] != 1]
                            sereport_table_4 = [k for k in report_table_4 if k[0] != 1]
                            sereport_table_5 = [k for k in report_table_5 if k[0] != 1]
                            sereport_table_6 = [k for k in report_table_6 if k[0] != 1]
                            sereport_table_7 = [k for k in report_table_7 if k[0] != 1]
                            sereport_table_8 = [k for k in report_table_8 if k[0] != 1]
                            sereport_table_9 = [k for k in report_table_9 if k[0] != 1]
                            sereport_table_10 = [
                                k for k in report_table_10 if k[0] != 1
                            ]

                            # outcome for 1*9
                            sevalue_1 = 0
                            seoutcome1_list = [
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                                sereport_table_1[6],
                                sereport_table_1[7],
                                sereport_table_1[8],
                            ]
                            for i in seoutcome1_list:
                                sevalue_1 = sevalue_1 + i[3]
                            # outcome for 2*5
                            sevalue_2 = 0
                            seoutcome2_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_2[3],
                                sereport_table_2[4],
                            ]
                            for i in seoutcome2_list:
                                sevalue_2 = sevalue_2 + i[3]
                            # outcome for 2*4+1*2
                            sevalue_3 = 0
                            seoutcome3_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_2[3],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome3_list:
                                sevalue_3 = sevalue_3 + i[3]
                            # outcome for 2*3+1*4
                            sevalue_4 = 0
                            seoutcome4_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome4_list:
                                sevalue_4 = sevalue_4 + i[3]
                            # outcome for 2*2+1*6
                            sevalue_5 = 0
                            seoutcome5_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                            ]
                            for i in seoutcome5_list:
                                sevalue_5 = sevalue_5 + i[3]
                            # outcome for 2+1*8
                            sevalue_6 = 0
                            seoutcome6_list = [
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                                sereport_table_1[6],
                                sereport_table_1[7],
                            ]
                            for i in seoutcome6_list:
                                sevalue_6 = sevalue_6 + i[3]
                            # outcome for 3*3+1
                            sevalue_7 = 0
                            seoutcome7_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_3[2],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome7_list:
                                sevalue_7 = sevalue_7 + i[3]
                            # outcome for 3*2+2*2
                            sevalue_8 = 0
                            seoutcome8_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_2[0],
                                sereport_table_2[1],
                            ]
                            for i in seoutcome8_list:
                                sevalue_8 = sevalue_8 + i[3]
                            # outcome for 3*2+2+1+1
                            sevalue_9 = 0
                            seoutcome9_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome9_list:
                                sevalue_9 = sevalue_9 + i[3]
                            # outcome for 3*2+1*4
                            sevalue_10 = 0
                            seoutcome10_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome10_list:
                                sevalue_10 = sevalue_10 + i[3]
                            # outcome for 3+2*2+1*3
                            sevalue_11 = 0
                            seoutcome11_list = [
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome11_list:
                                sevalue_11 = sevalue_11 + i[3]
                            # outcome for 3+2+1*5
                            sevalue_12 = 0
                            seoutcome12_list = [
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                            ]
                            for i in seoutcome12_list:
                                sevalue_12 = sevalue_12 + i[3]
                            # outcome for 3+1*7
                            sevalue_13 = 0
                            seoutcome13_list = [
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                                sereport_table_1[6],
                            ]
                            for i in seoutcome13_list:
                                sevalue_13 = sevalue_13 + i[3]
                            # outcome for 4*2+2
                            sevalue_14 = 0
                            seoutcome14_list = [
                                sereport_table_4[0],
                                sereport_table_4[1],
                                sereport_table_2[0],
                            ]
                            for i in seoutcome14_list:
                                sevalue_14 = sevalue_14 + i[3]
                            # outcome for 4*2+1*2
                            sevalue_15 = 0
                            seoutcome15_list = [
                                sereport_table_4[0],
                                sereport_table_4[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome15_list:
                                sevalue_15 = sevalue_15 + i[3]
                            # outcome for 4+3*2
                            sevalue_16 = 0
                            seoutcome16_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_3[1],
                            ]
                            for i in seoutcome16_list:
                                sevalue_16 = sevalue_16 + i[3]
                            # outcome for 4+3+2+1
                            sevalue_17 = 0
                            seoutcome17_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome17_list:
                                sevalue_17 = sevalue_17 + i[3]
                            # outcome for 4+3+1*3
                            sevalue_18 = 0
                            seoutcome18_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome18_list:
                                sevalue_18 = sevalue_18 + i[3]
                            # outcome for 4+2*3
                            sevalue_19 = 0
                            seoutcome19_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                            ]
                            for i in seoutcome19_list:
                                sevalue_19 = sevalue_19 + i[3]
                            # outcome for 4+2*2+1*2
                            sevalue_20 = 0
                            seoutcome20_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome20_list:
                                sevalue_20 = sevalue_20 + i[3]
                            # outcome for 4+2+1*4
                            sevalue_21 = 0
                            seoutcome21_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome21_list:
                                sevalue_21 = sevalue_21 + i[3]
                            # outcome for 4+1*6
                            sevalue_22 = 0
                            seoutcome22_list = [
                                sereport_table_4[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                            ]
                            for i in seoutcome22_list:
                                sevalue_22 = sevalue_22 + i[3]
                            # outcome for 5*2
                            sevalue_23 = 0
                            seoutcome23_list = [
                                sereport_table_5[0],
                                sereport_table_5[1],
                            ]
                            for i in seoutcome23_list:
                                sevalue_23 = sevalue_23 + i[3]
                            # outcome for 5+4+1
                            sevalue_24 = 0
                            seoutcome24_list = [
                                sereport_table_5[0],
                                sereport_table_4[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome24_list:
                                sevalue_24 = sevalue_24 + i[3]
                            # outcome for 5+3+2
                            sevalue_25 = 0
                            seoutcome25_list = [
                                sereport_table_5[0],
                                sereport_table_3[0],
                                sereport_table_2[0],
                            ]
                            for i in seoutcome25_list:
                                sevalue_25 = sevalue_25 + i[3]
                            # outcome for 5+3+1*2
                            sevalue_26 = 0
                            seoutcome26_list = [
                                sereport_table_5[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome26_list:
                                sevalue_26 = sevalue_26 + i[3]
                            # outcome for 5+2*2+1
                            sevalue_27 = 0
                            seoutcome27_list = [
                                sereport_table_5[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome27_list:
                                sevalue_27 = sevalue_27 + i[3]
                            # outcome for 5+2+1*3
                            sevalue_28 = 0
                            seoutcome28_list = [
                                sereport_table_5[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome28_list:
                                sevalue_28 = sevalue_28 + i[3]
                            # outcome for 5+1*5
                            sevalue_29 = 0
                            seoutcome29_list = [
                                sereport_table_5[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                            ]
                            for i in seoutcome29_list:
                                sevalue_29 = sevalue_29 + i[3]
                            # outcome for 6+4
                            sevalue_30 = 0
                            seoutcome30_list = [
                                sereport_table_6[0],
                                sereport_table_4[0],
                            ]
                            for i in seoutcome30_list:
                                sevalue_30 = sevalue_30 + i[3]
                            # outcome for 6+3+1
                            sevalue_31 = 0
                            seoutcome31_list = [
                                sereport_table_6[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome31_list:
                                sevalue_31 = sevalue_31 + i[3]
                            # outcome for 6+2*2
                            sevalue_32 = 0
                            seoutcome32_list = [
                                sereport_table_6[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                            ]
                            for i in seoutcome32_list:
                                sevalue_32 = sevalue_32 + i[3]
                            # outcome for 6+2+1*2
                            sevalue_33 = 0
                            seoutcome33_list = [
                                sereport_table_6[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome33_list:
                                sevalue_33 = sevalue_33 + i[3]
                            # outcome for 6+1*4
                            sevalue_34 = 0
                            seoutcome34_list = [
                                sereport_table_6[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome34_list:
                                sevalue_34 = sevalue_34 + i[3]
                            # outcome for 7+3
                            sevalue_35 = 0
                            seoutcome35_list = [
                                sereport_table_7[0],
                                sereport_table_3[0],
                            ]
                            for i in seoutcome35_list:
                                sevalue_35 = sevalue_35 + i[3]
                            # outcome for 7+2+1
                            sevalue_36 = 0
                            seoutcome36_list = [
                                sereport_table_7[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome36_list:
                                sevalue_36 = sevalue_36 + i[3]
                            # outcome for 7+1*3
                            sevalue_37 = 0
                            seoutcome37_list = [
                                sereport_table_7[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome37_list:
                                sevalue_37 = sevalue_37 + i[3]
                            # outcome for 8+2
                            sevalue_38 = 0
                            seoutcome38_list = [
                                sereport_table_8[0],
                                sereport_table_2[0],
                            ]
                            for i in seoutcome38_list:
                                sevalue_38 = sevalue_38 + i[3]
                            # outcome for 8+1*2
                            sevalue_39 = 0
                            seoutcome39_list = [
                                sereport_table_8[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome39_list:
                                sevalue_39 = sevalue_39 + i[3]
                            # outcome for 9+1
                            sevalue_40 = 0
                            seoutcome40_list = [
                                sereport_table_9[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome40_list:
                                sevalue_40 = sevalue_40 + i[3]
                            # outcome for 10
                            sevalue_41 = 0
                            seoutcome41_list = [sereport_table_10[0]]
                            for i in seoutcome41_list:
                                sevalue_41 = sevalue_41 + i[3]

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
                                sevalue_12,
                                sevalue_13,
                                sevalue_14,
                                sevalue_15,
                                sevalue_16,
                                sevalue_17,
                                sevalue_18,
                                sevalue_19,
                                sevalue_20,
                                sevalue_21,
                                sevalue_22,
                                sevalue_23,
                                sevalue_24,
                                sevalue_25,
                                sevalue_26,
                                sevalue_27,
                                sevalue_28,
                                sevalue_29,
                                sevalue_30,
                                sevalue_31,
                                sevalue_32,
                                sevalue_33,
                                sevalue_34,
                                sevalue_35,
                                sevalue_36,
                                sevalue_37,
                                sevalue_38,
                                sevalue_39,
                                sevalue_40,
                                sevalue_41,
                            ]
                            for n in sevalues:
                                if n == max(sevalues):
                                    second_value = n
                                    monetary_transfer = -(
                                        social_value - j[3] - second_value
                                    )
                                    res_revenue = res_revenue + monetary_transfer
                                    utility_truth_1 = j[3] - monetary_transfer
                                    print("utility for", j[0], ":", utility_truth_1)
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
    random_table_7 = []
    random_table_8 = []
    random_table_9 = []
    random_table_10 = []
    random_table_list = [
        random_table_1,
        random_table_2,
        random_table_3,
        random_table_4,
        random_table_5,
        random_table_6,
        random_table_7,
        random_table_8,
        random_table_9,
        random_table_10,
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
        elif random_table[i][1] == 7:
            random_table_7.append(random_table[i])
        elif random_table[i][1] == 8:
            random_table_8.append(random_table[i])
        elif random_table[i][1] == 9:
            random_table_9.append(random_table[i])
        elif random_table[i][1] == 10:
            random_table_10.append(random_table[i])
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
    while len(random_table_7) < 10:
        random_table_7.append([0, 7, 0, 0])
    while len(random_table_8) < 10:
        random_table_8.append([0, 8, 0, 0])
    while len(random_table_9) < 10:
        random_table_9.append([0, 9, 0, 0])
    while len(random_table_10) < 10:
        random_table_10.append([0, 10, 0, 0])

    random_table_1.sort(key=takeValue, reverse=True)
    random_table_2.sort(key=takeValue, reverse=True)
    random_table_3.sort(key=takeValue, reverse=True)
    random_table_4.sort(key=takeValue, reverse=True)
    random_table_5.sort(key=takeValue, reverse=True)
    random_table_6.sort(key=takeValue, reverse=True)
    random_table_7.sort(key=takeValue, reverse=True)
    random_table_8.sort(key=takeValue, reverse=True)
    random_table_9.sort(key=takeValue, reverse=True)
    random_table_10.sort(key=takeValue, reverse=True)
    # outcome for 1*9
    random_value_1 = 0
    random_outcome1_list = [
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
        random_table_1[5],
        random_table_1[6],
        random_table_1[7],
        random_table_1[8],
    ]
    for i in random_outcome1_list:
        random_value_1 = random_value_1 + i[3]
    # outcome for 2*5
    random_value_2 = 0
    random_outcome2_list = [
        random_table_2[0],
        random_table_2[1],
        random_table_2[2],
        random_table_2[3],
        random_table_2[4],
    ]
    for i in random_outcome2_list:
        random_value_2 = random_value_2 + i[3]
    # outcome for 2*4+1*2
    random_value_3 = 0
    random_outcome3_list = [
        random_table_2[0],
        random_table_2[1],
        random_table_2[2],
        random_table_2[3],
        random_table_1[0],
        random_table_1[1],
    ]
    for i in random_outcome3_list:
        random_value_3 = random_value_3 + i[3]
    # outcome for 2*3+1*4
    random_value_4 = 0
    random_outcome4_list = [
        random_table_2[0],
        random_table_2[1],
        random_table_2[2],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
    ]
    for i in random_outcome4_list:
        random_value_4 = random_value_4 + i[3]
    # outcome for 2*2+1*6
    random_value_5 = 0
    random_outcome5_list = [
        random_table_2[0],
        random_table_2[1],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
        random_table_1[5],
    ]
    for i in random_outcome5_list:
        random_value_5 = random_value_5 + i[3]
    # outcome for 2+1*8
    random_value_6 = 0
    random_outcome6_list = [
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
        random_table_1[5],
        random_table_1[6],
        random_table_1[7],
    ]
    for i in random_outcome6_list:
        random_value_6 = random_value_6 + i[3]
    # outcome for 3*3+1
    random_value_7 = 0
    random_outcome7_list = [
        random_table_3[0],
        random_table_3[1],
        random_table_3[2],
        random_table_1[0],
    ]
    for i in random_outcome7_list:
        random_value_7 = random_value_7 + i[3]
    # outcome for 3*2+2*2
    random_value_8 = 0
    random_outcome8_list = [
        random_table_3[0],
        random_table_3[1],
        random_table_2[0],
        random_table_2[1],
    ]
    for i in random_outcome8_list:
        random_value_8 = random_value_8 + i[3]
    # outcome for 3*2+2+1+1
    random_value_9 = 0
    random_outcome9_list = [
        random_table_3[0],
        random_table_3[1],
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
    ]
    for i in random_outcome9_list:
        random_value_9 = random_value_9 + i[3]
    # outcome for 3*2+1*4
    random_value_10 = 0
    random_outcome10_list = [
        random_table_3[0],
        random_table_3[1],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
    ]
    for i in random_outcome10_list:
        random_value_10 = random_value_10 + i[3]
    # outcome for 3+2*2+1*3
    random_value_11 = 0
    random_outcome11_list = [
        random_table_3[0],
        random_table_2[0],
        random_table_2[1],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
    ]
    for i in random_outcome11_list:
        random_value_11 = random_value_11 + i[3]
    # outcome for 3+2+1*5
    random_value_12 = 0
    random_outcome12_list = [
        random_table_3[0],
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
    ]
    for i in random_outcome12_list:
        random_value_12 = random_value_12 + i[3]
    # outcome for 3+1*7
    random_value_13 = 0
    random_outcome13_list = [
        random_table_3[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
        random_table_1[5],
        random_table_1[6],
    ]
    for i in random_outcome13_list:
        random_value_13 = random_value_13 + i[3]
    # outcome for 4*2+2
    random_value_14 = 0
    random_outcome14_list = [
        random_table_4[0],
        random_table_4[1],
        random_table_2[0],
    ]
    for i in random_outcome14_list:
        random_value_14 = random_value_14 + i[3]
    # outcome for 4*2+1*2
    random_value_15 = 0
    random_outcome15_list = [
        random_table_4[0],
        random_table_4[1],
        random_table_1[0],
        random_table_1[1],
    ]
    for i in random_outcome15_list:
        random_value_15 = random_value_15 + i[3]
    # outcome for 4+3*2
    random_value_16 = 0
    random_outcome16_list = [random_table_4[0], random_table_3[0], random_table_3[1]]
    for i in random_outcome16_list:
        random_value_16 = random_value_16 + i[3]
    # outcome for 4+3+2+1
    random_value_17 = 0
    random_outcome17_list = [
        random_table_4[0],
        random_table_3[0],
        random_table_2[0],
        random_table_1[0],
    ]
    for i in random_outcome17_list:
        random_value_17 = random_value_17 + i[3]
    # outcome for 4+3+1*3
    random_value_18 = 0
    random_outcome18_list = [
        random_table_4[0],
        random_table_3[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
    ]
    for i in random_outcome18_list:
        random_value_18 = random_value_18 + i[3]
    # outcome for 4+2*3
    random_value_19 = 0
    random_outcome19_list = [
        random_table_4[0],
        random_table_2[0],
        random_table_2[1],
        random_table_2[2],
    ]
    for i in random_outcome19_list:
        random_value_19 = random_value_19 + i[3]
    # outcome for 4+2*2+1*2
    random_value_20 = 0
    random_outcome20_list = [
        random_table_4[0],
        random_table_2[0],
        random_table_2[1],
        random_table_1[0],
        random_table_1[1],
    ]
    for i in random_outcome20_list:
        random_value_20 = random_value_20 + i[3]
    # outcome for 4+2+1*4
    random_value_21 = 0
    random_outcome21_list = [
        random_table_4[0],
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
    ]
    for i in random_outcome21_list:
        random_value_21 = random_value_21 + i[3]
    # outcome for 4+1*6
    random_value_22 = 0
    random_outcome22_list = [
        random_table_4[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
        random_table_1[5],
    ]
    for i in random_outcome22_list:
        random_value_22 = random_value_22 + i[3]
    # outcome for 5*2
    random_value_23 = 0
    random_outcome23_list = [random_table_5[0], random_table_5[1]]
    for i in random_outcome23_list:
        random_value_23 = random_value_23 + i[3]
    # outcome for 5+4+1
    random_value_24 = 0
    random_outcome24_list = [random_table_5[0], random_table_4[0], random_table_1[0]]
    for i in random_outcome24_list:
        random_value_24 = random_value_24 + i[3]
    # outcome for 5+3+2
    random_value_25 = 0
    random_outcome25_list = [random_table_5[0], random_table_3[0], random_table_2[0]]
    for i in random_outcome25_list:
        random_value_25 = random_value_25 + i[3]
    # outcome for 5+3+1*2
    random_value_26 = 0
    random_outcome26_list = [
        random_table_5[0],
        random_table_3[0],
        random_table_1[0],
        random_table_1[1],
    ]
    for i in random_outcome26_list:
        random_value_26 = random_value_26 + i[3]
    # outcome for 5+2*2+1
    random_value_27 = 0
    random_outcome27_list = [
        random_table_5[0],
        random_table_2[0],
        random_table_2[1],
        random_table_1[0],
    ]
    for i in random_outcome27_list:
        random_value_27 = random_value_27 + i[3]
    # outcome for 5+2+1*3
    random_value_28 = 0
    random_outcome28_list = [
        random_table_5[0],
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
    ]
    for i in random_outcome28_list:
        random_value_28 = random_value_28 + i[3]
    # outcome for 5+1*5
    random_value_29 = 0
    random_outcome29_list = [
        random_table_5[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
        random_table_1[4],
    ]
    for i in random_outcome29_list:
        random_value_29 = random_value_29 + i[3]
    # outcome for 6+4
    random_value_30 = 0
    random_outcome30_list = [random_table_6[0], random_table_4[0]]
    for i in random_outcome30_list:
        random_value_30 = random_value_30 + i[3]
    # outcome for 6+3+1
    random_value_31 = 0
    random_outcome31_list = [random_table_6[0], random_table_3[0], random_table_1[0]]
    for i in random_outcome31_list:
        random_value_31 = random_value_31 + i[3]
    # outcome for 6+2*2
    random_value_32 = 0
    random_outcome32_list = [random_table_6[0], random_table_2[0], random_table_2[1]]
    for i in random_outcome32_list:
        random_value_32 = random_value_32 + i[3]
    # outcome for 6+2+1*2
    random_value_33 = 0
    random_outcome33_list = [
        random_table_6[0],
        random_table_2[0],
        random_table_1[0],
        random_table_1[1],
    ]
    for i in random_outcome33_list:
        random_value_33 = random_value_33 + i[3]
    # outcome for 6+1*4
    random_value_34 = 0
    random_outcome34_list = [
        random_table_6[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
        random_table_1[3],
    ]
    for i in random_outcome34_list:
        random_value_34 = random_value_34 + i[3]
    # outcome for 7+3
    random_value_35 = 0
    random_outcome35_list = [random_table_7[0], random_table_3[0]]
    for i in random_outcome35_list:
        random_value_35 = random_value_35 + i[3]
    # outcome for 7+2+1
    random_value_36 = 0
    random_outcome36_list = [random_table_7[0], random_table_2[0], random_table_1[0]]
    for i in random_outcome36_list:
        random_value_36 = random_value_36 + i[3]
    # outcome for 7+1*3
    random_value_37 = 0
    random_outcome37_list = [
        random_table_7[0],
        random_table_1[0],
        random_table_1[1],
        random_table_1[2],
    ]
    for i in random_outcome37_list:
        random_value_37 = random_value_37 + i[3]
    # outcome for 8+2
    random_value_38 = 0
    random_outcome38_list = [random_table_8[0], random_table_2[0]]
    for i in random_outcome38_list:
        random_value_38 = random_value_38 + i[3]
    # outcome for 8+1*2
    random_value_39 = 0
    random_outcome39_list = [random_table_8[0], random_table_1[0], random_table_1[1]]
    for i in random_outcome39_list:
        random_value_39 = random_value_39 + i[3]
    # outcome for 9+1
    random_value_40 = 0
    random_outcome40_list = [random_table_9[0], random_table_1[0]]
    for i in random_outcome40_list:
        random_value_40 = random_value_40 + i[3]
    # outcome for 10
    random_value_41 = 0
    random_outcome41_list = [random_table_10[0]]
    for i in random_outcome41_list:
        random_value_41 = random_value_41 + i[3]
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
        random_outcome12_list,
        random_outcome13_list,
        random_outcome14_list,
        random_outcome15_list,
        random_outcome16_list,
        random_outcome17_list,
        random_outcome18_list,
        random_outcome19_list,
        random_outcome20_list,
        random_outcome21_list,
        random_outcome22_list,
        random_outcome23_list,
        random_outcome24_list,
        random_outcome25_list,
        random_outcome26_list,
        random_outcome27_list,
        random_outcome28_list,
        random_outcome29_list,
        random_outcome30_list,
        random_outcome31_list,
        random_outcome32_list,
        random_outcome33_list,
        random_outcome34_list,
        random_outcome35_list,
        random_outcome36_list,
        random_outcome37_list,
        random_outcome38_list,
        random_outcome39_list,
        random_outcome40_list,
        random_outcome41_list,
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
        random_value_12,
        random_value_13,
        random_value_14,
        random_value_15,
        random_value_16,
        random_value_17,
        random_value_18,
        random_value_19,
        random_value_20,
        random_value_21,
        random_value_22,
        random_value_23,
        random_value_24,
        random_value_25,
        random_value_26,
        random_value_27,
        random_value_28,
        random_value_29,
        random_value_30,
        random_value_31,
        random_value_32,
        random_value_33,
        random_value_34,
        random_value_35,
        random_value_36,
        random_value_37,
        random_value_38,
        random_value_39,
        random_value_40,
        random_value_41,
    ]
    utility_random_1 = (
        0  # initialize the utility of player one under random-telling strategy
    )
    # find the optimal outcome
    for i in range(len(random_values)):
        random_value_i = random_values[i]
        if random_value_i == max(random_values):
            social_value = random_value_i
            res_revenue = 0
            for m in range(len(random_outcomes_list)):
                random_outcome_m = random_outcomes_list[m]
                if m == i:
                    for j in random_outcome_m:
                        if j[0] == 1:
                            print(
                                z,
                                "------random---------" "allocate",
                                "table",
                                j[1],
                                " and course",
                                j[2],
                                "to player",
                                j[0],
                            )
                            # calcluate second price
                            sereport_table_1 = [k for k in random_table_1 if k[0] != 1]
                            sereport_table_2 = [k for k in random_table_2 if k[0] != 1]
                            sereport_table_3 = [k for k in random_table_3 if k[0] != 1]
                            sereport_table_4 = [k for k in random_table_4 if k[0] != 1]
                            sereport_table_5 = [k for k in random_table_5 if k[0] != 1]
                            sereport_table_6 = [k for k in random_table_6 if k[0] != 1]
                            sereport_table_7 = [k for k in random_table_7 if k[0] != 1]
                            sereport_table_8 = [k for k in random_table_8 if k[0] != 1]
                            sereport_table_9 = [k for k in random_table_9 if k[0] != 1]
                            sereport_table_10 = [
                                k for k in random_table_10 if k[0] != 1
                            ]

                            # outcome for 1*9
                            sevalue_1 = 0
                            seoutcome1_list = [
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                                sereport_table_1[6],
                                sereport_table_1[7],
                                sereport_table_1[8],
                            ]
                            for i in seoutcome1_list:
                                sevalue_1 = sevalue_1 + i[3]
                            # outcome for 2*5
                            sevalue_2 = 0
                            seoutcome2_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_2[3],
                                sereport_table_2[4],
                            ]
                            for i in seoutcome2_list:
                                sevalue_2 = sevalue_2 + i[3]
                            # outcome for 2*4+1*2
                            sevalue_3 = 0
                            seoutcome3_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_2[3],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome3_list:
                                sevalue_3 = sevalue_3 + i[3]
                            # outcome for 2*3+1*4
                            sevalue_4 = 0
                            seoutcome4_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome4_list:
                                sevalue_4 = sevalue_4 + i[3]
                            # outcome for 2*2+1*6
                            sevalue_5 = 0
                            seoutcome5_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                            ]
                            for i in seoutcome5_list:
                                sevalue_5 = sevalue_5 + i[3]
                            # outcome for 2+1*8
                            sevalue_6 = 0
                            seoutcome6_list = [
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                                sereport_table_1[6],
                                sereport_table_1[7],
                            ]
                            for i in seoutcome6_list:
                                sevalue_6 = sevalue_6 + i[3]
                            # outcome for 3*3+1
                            sevalue_7 = 0
                            seoutcome7_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_3[2],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome7_list:
                                sevalue_7 = sevalue_7 + i[3]
                            # outcome for 3*2+2*2
                            sevalue_8 = 0
                            seoutcome8_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_2[0],
                                sereport_table_2[1],
                            ]
                            for i in seoutcome8_list:
                                sevalue_8 = sevalue_8 + i[3]
                            # outcome for 3*2+2+1+1
                            sevalue_9 = 0
                            seoutcome9_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome9_list:
                                sevalue_9 = sevalue_9 + i[3]
                            # outcome for 3*2+1*4
                            sevalue_10 = 0
                            seoutcome10_list = [
                                sereport_table_3[0],
                                sereport_table_3[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome10_list:
                                sevalue_10 = sevalue_10 + i[3]
                            # outcome for 3+2*2+1*3
                            sevalue_11 = 0
                            seoutcome11_list = [
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome11_list:
                                sevalue_11 = sevalue_11 + i[3]
                            # outcome for 3+2+1*5
                            sevalue_12 = 0
                            seoutcome12_list = [
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                            ]
                            for i in seoutcome12_list:
                                sevalue_12 = sevalue_12 + i[3]
                            # outcome for 3+1*7
                            sevalue_13 = 0
                            seoutcome13_list = [
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                                sereport_table_1[6],
                            ]
                            for i in seoutcome13_list:
                                sevalue_13 = sevalue_13 + i[3]
                            # outcome for 4*2+2
                            sevalue_14 = 0
                            seoutcome14_list = [
                                sereport_table_4[0],
                                sereport_table_4[1],
                                sereport_table_2[0],
                            ]
                            for i in seoutcome14_list:
                                sevalue_14 = sevalue_14 + i[3]
                            # outcome for 4*2+1*2
                            sevalue_15 = 0
                            seoutcome15_list = [
                                sereport_table_4[0],
                                sereport_table_4[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome15_list:
                                sevalue_15 = sevalue_15 + i[3]
                            # outcome for 4+3*2
                            sevalue_16 = 0
                            seoutcome16_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_3[1],
                            ]
                            for i in seoutcome16_list:
                                sevalue_16 = sevalue_16 + i[3]
                            # outcome for 4+3+2+1
                            sevalue_17 = 0
                            seoutcome17_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome17_list:
                                sevalue_17 = sevalue_17 + i[3]
                            # outcome for 4+3+1*3
                            sevalue_18 = 0
                            seoutcome18_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome18_list:
                                sevalue_18 = sevalue_18 + i[3]
                            # outcome for 4+2*3
                            sevalue_19 = 0
                            seoutcome19_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                            ]
                            for i in seoutcome19_list:
                                sevalue_19 = sevalue_19 + i[3]
                            # outcome for 4+2*2+1*2
                            sevalue_20 = 0
                            seoutcome20_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome20_list:
                                sevalue_20 = sevalue_20 + i[3]
                            # outcome for 4+2+1*4
                            sevalue_21 = 0
                            seoutcome21_list = [
                                sereport_table_4[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome21_list:
                                sevalue_21 = sevalue_21 + i[3]
                            # outcome for 4+1*6
                            sevalue_22 = 0
                            seoutcome22_list = [
                                sereport_table_4[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                                sereport_table_1[5],
                            ]
                            for i in seoutcome22_list:
                                sevalue_22 = sevalue_22 + i[3]
                            # outcome for 5*2
                            sevalue_23 = 0
                            seoutcome23_list = [
                                sereport_table_5[0],
                                sereport_table_5[1],
                            ]
                            for i in seoutcome23_list:
                                sevalue_23 = sevalue_23 + i[3]
                            # outcome for 5+4+1
                            sevalue_24 = 0
                            seoutcome24_list = [
                                sereport_table_5[0],
                                sereport_table_4[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome24_list:
                                sevalue_24 = sevalue_24 + i[3]
                            # outcome for 5+3+2
                            sevalue_25 = 0
                            seoutcome25_list = [
                                sereport_table_5[0],
                                sereport_table_3[0],
                                sereport_table_2[0],
                            ]
                            for i in seoutcome25_list:
                                sevalue_25 = sevalue_25 + i[3]
                            # outcome for 5+3+1*2
                            sevalue_26 = 0
                            seoutcome26_list = [
                                sereport_table_5[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome26_list:
                                sevalue_26 = sevalue_26 + i[3]
                            # outcome for 5+2*2+1
                            sevalue_27 = 0
                            seoutcome27_list = [
                                sereport_table_5[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome27_list:
                                sevalue_27 = sevalue_27 + i[3]
                            # outcome for 5+2+1*3
                            sevalue_28 = 0
                            seoutcome28_list = [
                                sereport_table_5[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome28_list:
                                sevalue_28 = sevalue_28 + i[3]
                            # outcome for 5+1*5
                            sevalue_29 = 0
                            seoutcome29_list = [
                                sereport_table_5[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                                sereport_table_1[4],
                            ]
                            for i in seoutcome29_list:
                                sevalue_29 = sevalue_29 + i[3]
                            # outcome for 6+4
                            sevalue_30 = 0
                            seoutcome30_list = [
                                sereport_table_6[0],
                                sereport_table_4[0],
                            ]
                            for i in seoutcome30_list:
                                sevalue_30 = sevalue_30 + i[3]
                            # outcome for 6+3+1
                            sevalue_31 = 0
                            seoutcome31_list = [
                                sereport_table_6[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome31_list:
                                sevalue_31 = sevalue_31 + i[3]
                            # outcome for 6+2*2
                            sevalue_32 = 0
                            seoutcome32_list = [
                                sereport_table_6[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                            ]
                            for i in seoutcome32_list:
                                sevalue_32 = sevalue_32 + i[3]
                            # outcome for 6+2+1*2
                            sevalue_33 = 0
                            seoutcome33_list = [
                                sereport_table_6[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome33_list:
                                sevalue_33 = sevalue_33 + i[3]
                            # outcome for 6+1*4
                            sevalue_34 = 0
                            seoutcome34_list = [
                                sereport_table_6[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                                sereport_table_1[3],
                            ]
                            for i in seoutcome34_list:
                                sevalue_34 = sevalue_34 + i[3]
                            # outcome for 7+3
                            sevalue_35 = 0
                            seoutcome35_list = [
                                sereport_table_7[0],
                                sereport_table_3[0],
                            ]
                            for i in seoutcome35_list:
                                sevalue_35 = sevalue_35 + i[3]
                            # outcome for 7+2+1
                            sevalue_36 = 0
                            seoutcome36_list = [
                                sereport_table_7[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome36_list:
                                sevalue_36 = sevalue_36 + i[3]
                            # outcome for 7+1*3
                            sevalue_37 = 0
                            seoutcome37_list = [
                                sereport_table_7[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                                sereport_table_1[2],
                            ]
                            for i in seoutcome37_list:
                                sevalue_37 = sevalue_37 + i[3]
                            # outcome for 8+2
                            sevalue_38 = 0
                            seoutcome38_list = [
                                sereport_table_8[0],
                                sereport_table_2[0],
                            ]
                            for i in seoutcome38_list:
                                sevalue_38 = sevalue_38 + i[3]
                            # outcome for 8+1*2
                            sevalue_39 = 0
                            seoutcome39_list = [
                                sereport_table_8[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            for i in seoutcome39_list:
                                sevalue_39 = sevalue_39 + i[3]
                            # outcome for 9+1
                            sevalue_40 = 0
                            seoutcome40_list = [
                                sereport_table_9[0],
                                sereport_table_1[0],
                            ]
                            for i in seoutcome40_list:
                                sevalue_40 = sevalue_40 + i[3]
                            # outcome for 10
                            sevalue_41 = 0
                            seoutcome41_list = [sereport_table_10[0]]
                            for i in seoutcome41_list:
                                sevalue_41 = sevalue_41 + i[3]

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
                                sevalue_12,
                                sevalue_13,
                                sevalue_14,
                                sevalue_15,
                                sevalue_16,
                                sevalue_17,
                                sevalue_18,
                                sevalue_19,
                                sevalue_20,
                                sevalue_21,
                                sevalue_22,
                                sevalue_23,
                                sevalue_24,
                                sevalue_25,
                                sevalue_26,
                                sevalue_27,
                                sevalue_28,
                                sevalue_29,
                                sevalue_30,
                                sevalue_31,
                                sevalue_32,
                                sevalue_33,
                                sevalue_34,
                                sevalue_35,
                                sevalue_36,
                                sevalue_37,
                                sevalue_38,
                                sevalue_39,
                                sevalue_40,
                                sevalue_41,
                            ]
                            for n in sevalues:
                                if n == max(sevalues):
                                    second_value = n
                                    monetary_transfer = -(
                                        social_value - j[3] - second_value
                                    )
                                    res_revenue = res_revenue + monetary_transfer
                                    p1_value = p1.loc[j[1], j[2]]
                                    utility_random_1 = p1_value - monetary_transfer
                                    print("utility for", j[0], ":", utility_random_1)
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
bug = 699
average utility changed under truth-telling strategy: 2.3849

bug = 858
average utility changed under truth-telling strategy: 0.6568
"""

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
    consumer = 50
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
            # one reported situation
            pi_value_1 = pi_value_list[0]
            p1_report_1 = [i + 1,] + getIndexes(pi, pi_value_1)[0]
            # two reported situation
            pi_value_2 = pi_value_list[1]
            if pi_value_1 == pi_value_2:
                p1_report_2 = [i + 1,] + getIndexes(pi, pi_value_2)[1]
            else:
                p1_report_2 = [i + 1,] + getIndexes(pi, pi_value_2)[0]
            # three reported situation
            pi_value_3 = pi_value_list[2]
            if pi_value_3 == pi_value_1:
                p1_report_3 = [i + 1,] + getIndexes(pi, pi_value_3)[2]
            elif pi_value_3 == pi_value_2 != pi_value_1:
                p1_report_3 = [i + 1,] + getIndexes(pi, pi_value_3)[1]
            else:
                p1_report_3 = [i + 1,] + getIndexes(pi, pi_value_3)[0]
            p1_report.append(p1_report_1)
            p1_report.append(p1_report_2)
            p1_report.append(p1_report_3)

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
        # one reported situation
        pi_random_value_1 = pi_random_value_list[0]
        pi_random_report_1 = [i + 1,] + getIndexes(pi_random, pi_random_value_1)[0]
        # two reported situation
        pi_random_value_2 = pi_random_value_list[1]
        if pi_random_value_1 == pi_random_value_2:
            pi_random_report_2 = [i + 1,] + getIndexes(pi_random, pi_random_value_2)[1]
        else:
            pi_random_report_2 = [i + 1,] + getIndexes(pi_random, pi_random_value_2)[0]
        # three reported situation
        pi_random_value_3 = pi_random_value_list[2]
        if pi_random_value_3 == pi_random_value_1:
            pi_random_report_3 = [i + 1,] + getIndexes(pi_random, pi_random_value_3)[2]
        elif pi_random_value_3 == pi_random_value_2 != pi_random_value_1:
            pi_random_report_3 = [i + 1,] + getIndexes(pi_random, pi_random_value_3)[1]
        else:
            pi_random_report_3 = [i + 1,] + getIndexes(pi_random, pi_random_value_3)[0]
        random_table = (
            random_table
            + [pi_random_report_1]
            + [pi_random_report_2]
            + [pi_random_report_3]
        )

    # classify tables with table numbers
    report_table = [i for i in random_table if i[0] != 1]
    report_table.append(p1_report_1)
    report_table.append(p1_report_2)
    report_table.append(p1_report_3)
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
    player_list_1 = []
    for i in outcome1_list:
        if i[0] != 0:
            player_list_1.append(i[0])
    report_table_1_changed = report_table_1[9:]
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
    # outcome for 2*5
    value_2 = 0
    outcome2_list = [
        report_table_2[0],
        report_table_2[1],
        report_table_2[2],
        report_table_2[3],
        report_table_2[4],
    ]
    player_list_2 = []
    for i in outcome2_list:
        if i[0] != 0:
            player_list_2.append(i[0])
    report_table_2_changed = report_table_2[5:]
    for i in report_table_2_changed:
        if i[0] in player_list_2:
            report_table_2_changed.remove(i)
    for i in range(len(outcome2_list)):
        for j in range(1, (len(outcome2_list) - i)):
            if outcome2_list[i][0] == outcome2_list[i + j][0] != 0:
                outcome2_list[i + j] = report_table_2_changed[0]
                report_table_2_changed.remove(report_table_2_changed[0])
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
    player_list_3 = []
    for i in outcome3_list:
        if i[0] != 0:
            player_list_3.append(i[0])
    report_table_3_changed_1 = report_table_1[2:]
    report_table_3_changed_2 = report_table_2[4:]
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
    player_list_4 = []
    for i in outcome4_list:
        if i[0] != 0:
            player_list_4.append(i[0])
    report_table_4_changed_1 = report_table_1[4:]
    report_table_4_changed_2 = report_table_2[3:]
    for i in report_table_4_changed_1:
        if i[0] in player_list_4:
            report_table_4_changed_1.remove(i)
    for i in report_table_4_changed_2:
        if i[0] in player_list_4:
            report_table_4_changed_2.remove(i)
    for i in range(len(outcome4_list)):
        for j in range(1, (len(outcome4_list) - i)):
            if outcome4_list[i][0] == outcome4_list[i + j][0] != 0:
                if outcome4_list[i + j][1] == 1:
                    outcome4_list[i + j] = report_table_4_changed_1[0]
                    report_table_4_changed_1.remove(report_table_4_changed_1[0])
                elif outcome4_list[i + j][1] == 2:
                    outcome4_list[i + j] = report_table_4_changed_2[0]
                    report_table_4_changed_2.remove(report_table_4_changed_2[0])
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
    player_list_5 = []
    for i in outcome5_list:
        if i[0] != 0:
            player_list_5.append(i[0])
    report_table_5_changed_1 = report_table_1[6:]
    report_table_5_changed_2 = report_table_2[2:]
    for i in report_table_5_changed_1:
        if i[0] in player_list_5:
            report_table_5_changed_1.remove(i)
    for i in report_table_5_changed_2:
        if i[0] in player_list_5:
            report_table_5_changed_2.remove(i)
    for i in range(len(outcome5_list)):
        for j in range(1, (len(outcome5_list) - i)):
            if outcome5_list[i][0] == outcome5_list[i + j][0] != 0:
                if outcome5_list[i + j][1] == 1:
                    outcome5_list[i + j] = report_table_5_changed_1[0]
                    report_table_5_changed_1.remove(report_table_5_changed_1[0])
                elif outcome5_list[i + j][1] == 2:
                    outcome5_list[i + j] = report_table_5_changed_2[0]
                    report_table_5_changed_2.remove(report_table_5_changed_2[0])
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
    player_list_6 = []
    for i in outcome6_list:
        if i[0] != 0:
            player_list_6.append(i[0])
    report_table_6_changed_1 = report_table_1[8:]
    report_table_6_changed_2 = report_table_2[1:]
    for i in report_table_6_changed_1:
        if i[0] in player_list_6:
            report_table_6_changed_1.remove(i)
    for i in report_table_6_changed_2:
        if i[0] in player_list_6:
            report_table_6_changed_2.remove(i)
    for i in range(len(outcome6_list)):
        for j in range(1, (len(outcome6_list) - i)):
            if outcome6_list[i][0] == outcome6_list[i + j][0] != 0:
                if outcome6_list[i + j][1] == 1:
                    outcome6_list[i + j] = report_table_6_changed_1[0]
                    report_table_6_changed_1.remove(report_table_6_changed_1[0])
                elif outcome6_list[i + j][1] == 2:
                    outcome6_list[i + j] = report_table_6_changed_2[0]
                    report_table_6_changed_2.remove(report_table_6_changed_2[0])
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
    player_list_7 = []
    for i in outcome7_list:
        if i[0] != 0:
            player_list_7.append(i[0])
    report_table_7_changed_1 = report_table_1[1:]
    report_table_7_changed_3 = report_table_3[3:]
    for i in report_table_7_changed_1:
        if i[0] in player_list_7:
            report_table_7_changed_1.remove(i)
    for i in report_table_7_changed_3:
        if i[0] in player_list_7:
            report_table_7_changed_3.remove(i)
    for i in range(len(outcome7_list)):
        for j in range(1, (len(outcome7_list) - i)):
            if outcome7_list[i][0] == outcome7_list[i + j][0] != 0:
                if outcome7_list[i + j][1] == 1:
                    outcome7_list[i + j] = report_table_7_changed_1[0]
                    report_table_7_changed_1.remove(report_table_7_changed_1[0])
                elif outcome7_list[i + j][1] == 3:
                    outcome7_list[i + j] = report_table_7_changed_3[0]
                    report_table_7_changed_3.remove(report_table_7_changed_3[0])
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
    player_list_8 = []
    for i in outcome8_list:
        if i[0] != 0:
            player_list_8.append(i[0])
    report_table_8_changed_2 = report_table_2[2:]
    report_table_8_changed_3 = report_table_3[2:]
    for i in report_table_8_changed_2:
        if i[0] in player_list_8:
            report_table_8_changed_2.remove(i)
    for i in report_table_8_changed_3:
        if i[0] in player_list_8:
            report_table_8_changed_3.remove(i)
    for i in range(len(outcome8_list)):
        for j in range(1, (len(outcome8_list) - i)):
            if outcome8_list[i][0] == outcome8_list[i + j][0] != 0:
                if outcome8_list[i + j][1] == 2:
                    outcome8_list[i + j] = report_table_8_changed_2[0]
                    report_table_8_changed_2.remove(report_table_8_changed_2[0])
                elif outcome8_list[i + j][1] == 3:
                    outcome8_list[i + j] = report_table_8_changed_3[0]
                    report_table_8_changed_3.remove(report_table_8_changed_3[0])
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
    player_list_9 = []
    for i in outcome9_list:
        if i[0] != 0:
            player_list_9.append(i[0])
    report_table_9_changed_1 = report_table_1[2:]
    report_table_9_changed_2 = report_table_2[1:]
    report_table_9_changed_3 = report_table_3[2:]
    for i in report_table_9_changed_1:
        if i[0] in player_list_9:
            report_table_9_changed_1.remove(i)
    for i in report_table_9_changed_2:
        if i[0] in player_list_9:
            report_table_9_changed_2.remove(i)
    for i in report_table_9_changed_3:
        if i[0] in player_list_9:
            report_table_9_changed_3.remove(i)
    for i in range(len(outcome9_list)):
        for j in range(1, (len(outcome9_list) - i)):
            if outcome9_list[i][0] == outcome9_list[i + j][0] != 0:
                if outcome9_list[i + j][1] == 1:
                    outcome9_list[i + j] = report_table_9_changed_1[0]
                    report_table_9_changed_1.remove(report_table_9_changed_1[0])
                elif outcome9_list[i + j][1] == 2:
                    outcome9_list[i + j] = report_table_9_changed_2[0]
                    report_table_9_changed_2.remove(report_table_9_changed_2[0])
                elif outcome9_list[i + j][1] == 3:
                    outcome9_list[i + j] = report_table_9_changed_3[0]
                    report_table_9_changed_3.remove(report_table_9_changed_3[0])
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
    player_list_10 = []
    for i in outcome10_list:
        if i[0] != 0:
            player_list_10.append(i[0])
    report_table_10_changed_1 = report_table_1[4:]
    report_table_10_changed_3 = report_table_3[2:]
    for i in report_table_10_changed_1:
        if i[0] in player_list_10:
            report_table_10_changed_1.remove(i)
    for i in report_table_10_changed_3:
        if i[0] in player_list_10:
            report_table_10_changed_3.remove(i)
    for i in range(len(outcome10_list)):
        for j in range(1, (len(outcome10_list) - i)):
            if outcome10_list[i][0] == outcome10_list[i + j][0] != 0:
                if outcome10_list[i + j][1] == 1:
                    outcome10_list[i + j] = report_table_10_changed_1[0]
                    report_table_10_changed_1.remove(report_table_10_changed_1[0])
                elif outcome10_list[i + j][1] == 3:
                    outcome10_list[i + j] = report_table_10_changed_3[0]
                    report_table_10_changed_3.remove(report_table_10_changed_3[0])
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
    player_list_11 = []
    for i in outcome11_list:
        if i[0] != 0:
            player_list_11.append(i[0])
    report_table_11_changed_1 = report_table_1[3:]
    report_table_11_changed_2 = report_table_2[2:]
    report_table_11_changed_3 = report_table_3[1:]
    for i in report_table_11_changed_1:
        if i[0] in player_list_11:
            report_table_11_changed_1.remove(i)
    for i in report_table_11_changed_2:
        if i[0] in player_list_11:
            report_table_11_changed_2.remove(i)
    for i in report_table_11_changed_3:
        if i[0] in player_list_11:
            report_table_11_changed_3.remove(i)
    for i in range(len(outcome11_list)):
        for j in range(1, (len(outcome11_list) - i)):
            if outcome11_list[i][0] == outcome11_list[i + j][0] != 0:
                if outcome11_list[i + j][1] == 1:
                    outcome11_list[i + j] = report_table_11_changed_1[0]
                    report_table_11_changed_1.remove(report_table_11_changed_1[0])
                elif outcome11_list[i + j][1] == 2:
                    outcome11_list[i + j] = report_table_11_changed_2[0]
                    report_table_11_changed_2.remove(report_table_11_changed_2[0])
                elif outcome11_list[i + j][1] == 3:
                    outcome11_list[i + j] = report_table_11_changed_3[0]
                    report_table_11_changed_3.remove(report_table_11_changed_3[0])
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
    player_list_12 = []
    for i in outcome12_list:
        if i[0] != 0:
            player_list_12.append(i[0])
    report_table_12_changed_1 = report_table_1[5:]
    report_table_12_changed_2 = report_table_2[1:]
    report_table_12_changed_3 = report_table_3[1:]
    for i in report_table_12_changed_1:
        if i[0] in player_list_12:
            report_table_12_changed_1.remove(i)
    for i in report_table_12_changed_2:
        if i[0] in player_list_12:
            report_table_12_changed_2.remove(i)
    for i in report_table_12_changed_3:
        if i[0] in player_list_12:
            report_table_12_changed_3.remove(i)
    for i in range(len(outcome12_list)):
        for j in range(1, (len(outcome12_list) - i)):
            if outcome12_list[i][0] == outcome12_list[i + j][0] != 0:
                if outcome12_list[i + j][1] == 1:
                    outcome12_list[i + j] = report_table_12_changed_1[0]
                    report_table_12_changed_1.remove(report_table_12_changed_1[0])
                elif outcome12_list[i + j][1] == 2:
                    outcome12_list[i + j] = report_table_12_changed_2[0]
                    report_table_12_changed_2.remove(report_table_12_changed_2[0])
                elif outcome12_list[i + j][1] == 3:
                    outcome12_list[i + j] = report_table_12_changed_3[0]
                    report_table_12_changed_3.remove(report_table_12_changed_3[0])
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
    player_list_13 = []
    for i in outcome13_list:
        if i[0] != 0:
            player_list_13.append(i[0])
    report_table_13_changed_1 = report_table_1[7:]
    report_table_13_changed_3 = report_table_3[1:]
    for i in report_table_13_changed_1:
        if i[0] in player_list_13:
            report_table_13_changed_1.remove(i)
    for i in report_table_13_changed_3:
        if i[0] in player_list_13:
            report_table_13_changed_3.remove(i)
    for i in range(len(outcome13_list)):
        for j in range(1, (len(outcome13_list) - i)):
            if outcome13_list[i][0] == outcome13_list[i + j][0] != 0:
                if outcome13_list[i + j][1] == 1:
                    outcome13_list[i + j] = report_table_13_changed_1[0]
                    report_table_13_changed_1.remove(report_table_13_changed_1[0])
                elif outcome13_list[i + j][1] == 3:
                    outcome13_list[i + j] = report_table_13_changed_3[0]
                    report_table_13_changed_3.remove(report_table_13_changed_3[0])
    for i in outcome13_list:
        value_13 = value_13 + i[3]
    # outcome for 4*2+2
    value_14 = 0
    outcome14_list = [report_table_4[0], report_table_4[1], report_table_2[0]]
    player_list_14 = []
    for i in outcome14_list:
        if i[0] != 0:
            player_list_14.append(i[0])
    report_table_14_changed_2 = report_table_2[1:]
    report_table_14_changed_4 = report_table_4[2:]
    for i in report_table_14_changed_2:
        if i[0] in player_list_14:
            report_table_14_changed_2.remove(i)
    for i in report_table_14_changed_4:
        if i[0] in player_list_14:
            report_table_14_changed_4.remove(i)
    for i in range(len(outcome14_list)):
        for j in range(1, (len(outcome14_list) - i)):
            if outcome14_list[i][0] == outcome14_list[i + j][0] != 0:
                if outcome14_list[i + j][1] == 2:
                    outcome14_list[i + j] = report_table_14_changed_2[0]
                    report_table_14_changed_2.remove(report_table_14_changed_2[0])
                elif outcome14_list[i + j][1] == 4:
                    outcome14_list[i + j] = report_table_14_changed_4[0]
                    report_table_14_changed_4.remove(report_table_14_changed_4[0])
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
    player_list_15 = []
    for i in outcome15_list:
        if i[0] != 0:
            player_list_15.append(i[0])
    report_table_15_changed_1 = report_table_1[2:]
    report_table_15_changed_4 = report_table_4[2:]
    for i in report_table_15_changed_1:
        if i[0] in player_list_15:
            report_table_15_changed_1.remove(i)
    for i in report_table_15_changed_4:
        if i[0] in player_list_15:
            report_table_15_changed_4.remove(i)
    for i in range(len(outcome15_list)):
        for j in range(1, (len(outcome15_list) - i)):
            if outcome15_list[i][0] == outcome15_list[i + j][0] != 0:
                if outcome15_list[i + j][1] == 1:
                    outcome15_list[i + j] = report_table_15_changed_1[0]
                    report_table_15_changed_1.remove(report_table_15_changed_1[0])
                elif outcome15_list[i + j][1] == 4:
                    outcome15_list[i + j] = report_table_15_changed_4[0]
                    report_table_15_changed_4.remove(report_table_15_changed_4[0])
    for i in outcome15_list:
        value_15 = value_15 + i[3]
    # outcome for 4+3*2
    value_16 = 0
    outcome16_list = [report_table_4[0], report_table_3[0], report_table_3[1]]
    player_list_16 = []
    for i in outcome16_list:
        if i[0] != 0:
            player_list_16.append(i[0])
    report_table_16_changed_3 = report_table_3[2:]
    report_table_16_changed_4 = report_table_4[1:]
    for i in report_table_16_changed_3:
        if i[0] in player_list_16:
            report_table_16_changed_3.remove(i)
    for i in report_table_16_changed_4:
        if i[0] in player_list_16:
            report_table_16_changed_4.remove(i)
    for i in range(len(outcome16_list)):
        for j in range(1, (len(outcome16_list) - i)):
            if outcome16_list[i][0] == outcome16_list[i + j][0] != 0:
                if outcome16_list[i + j][1] == 3:
                    outcome16_list[i + j] = report_table_16_changed_3[0]
                    report_table_16_changed_3.remove(report_table_16_changed_3[0])
                elif outcome16_list[i + j][1] == 4:
                    outcome16_list[i + j] = report_table_16_changed_4[0]
                    report_table_16_changed_4.remove(report_table_16_changed_4[0])
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
    player_list_17 = []
    for i in outcome17_list:
        if i[0] != 0:
            player_list_17.append(i[0])
    report_table_17_changed_1 = report_table_1[1:]
    report_table_17_changed_2 = report_table_2[1:]
    report_table_17_changed_3 = report_table_3[1:]
    report_table_17_changed_4 = report_table_4[1:]
    for i in report_table_17_changed_1:
        if i[0] in player_list_17:
            report_table_17_changed_1.remove(i)
    for i in report_table_17_changed_2:
        if i[0] in player_list_17:
            report_table_17_changed_2.remove(i)
    for i in report_table_17_changed_3:
        if i[0] in player_list_17:
            report_table_17_changed_3.remove(i)
    for i in report_table_17_changed_4:
        if i[0] in player_list_17:
            report_table_17_changed_4.remove(i)
    for i in range(len(outcome17_list)):
        for j in range(1, (len(outcome17_list) - i)):
            if outcome17_list[i][0] == outcome17_list[i + j][0] != 0:
                if outcome17_list[i + j][1] == 1:
                    outcome17_list[i + j] = report_table_17_changed_1[0]
                    report_table_17_changed_1.remove(report_table_17_changed_1[0])
                elif outcome17_list[i + j][1] == 2:
                    outcome17_list[i + j] = report_table_17_changed_2[0]
                    report_table_17_changed_2.remove(report_table_17_changed_2[0])
                elif outcome17_list[i + j][1] == 3:
                    outcome17_list[i + j] = report_table_17_changed_3[0]
                    report_table_17_changed_3.remove(report_table_17_changed_3[0])
                elif outcome17_list[i + j][1] == 4:
                    outcome17_list[i + j] = report_table_17_changed_4[0]
                    report_table_17_changed_4.remove(report_table_17_changed_4[0])
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
    player_list_18 = []
    for i in outcome18_list:
        if i[0] != 0:
            player_list_18.append(i[0])
    report_table_18_changed_1 = report_table_1[3:]
    report_table_18_changed_3 = report_table_3[1:]
    report_table_18_changed_4 = report_table_4[1:]
    for i in report_table_18_changed_1:
        if i[0] in player_list_18:
            report_table_18_changed_1.remove(i)
    for i in report_table_18_changed_3:
        if i[0] in player_list_18:
            report_table_18_changed_3.remove(i)
    for i in report_table_18_changed_4:
        if i[0] in player_list_18:
            report_table_18_changed_4.remove(i)
    for i in range(len(outcome18_list)):
        for j in range(1, (len(outcome18_list) - i)):
            if outcome18_list[i][0] == outcome18_list[i + j][0] != 0:
                if outcome18_list[i + j][1] == 1:
                    outcome18_list[i + j] = report_table_18_changed_1[0]
                    report_table_18_changed_1.remove(report_table_18_changed_1[0])
                elif outcome18_list[i + j][1] == 3:
                    outcome18_list[i + j] = report_table_18_changed_3[0]
                    report_table_18_changed_3.remove(report_table_18_changed_3[0])
                elif outcome18_list[i + j][1] == 4:
                    outcome18_list[i + j] = report_table_18_changed_4[0]
                    report_table_18_changed_4.remove(report_table_18_changed_4[0])
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
    player_list_19 = []
    for i in outcome19_list:
        if i[0] != 0:
            player_list_19.append(i[0])
    report_table_19_changed_2 = report_table_2[3:]
    report_table_19_changed_4 = report_table_4[1:]
    for i in report_table_19_changed_2:
        if i[0] in player_list_19:
            report_table_19_changed_2.remove(i)
    for i in report_table_19_changed_4:
        if i[0] in player_list_19:
            report_table_19_changed_4.remove(i)
    for i in range(len(outcome19_list)):
        for j in range(1, (len(outcome19_list) - i)):
            if outcome19_list[i][0] == outcome19_list[i + j][0] != 0:
                if outcome19_list[i + j][1] == 2:
                    outcome19_list[i + j] = report_table_19_changed_2[0]
                    report_table_19_changed_2.remove(report_table_19_changed_2[0])
                elif outcome19_list[i + j][1] == 4:
                    outcome19_list[i + j] = report_table_19_changed_4[0]
                    report_table_19_changed_4.remove(report_table_19_changed_4[0])
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
    player_list_20 = []
    for i in outcome20_list:
        if i[0] != 0:
            player_list_20.append(i[0])
    report_table_20_changed_1 = report_table_1[2:]
    report_table_20_changed_2 = report_table_2[2:]
    report_table_20_changed_4 = report_table_4[1:]
    for i in report_table_20_changed_1:
        if i[0] in player_list_20:
            report_table_20_changed_1.remove(i)
    for i in report_table_20_changed_2:
        if i[0] in player_list_20:
            report_table_20_changed_2.remove(i)
    for i in report_table_20_changed_4:
        if i[0] in player_list_20:
            report_table_20_changed_4.remove(i)
    for i in range(len(outcome20_list)):
        for j in range(1, (len(outcome20_list) - i)):
            if outcome20_list[i][0] == outcome20_list[i + j][0] != 0:
                if outcome20_list[i + j][1] == 1:
                    outcome20_list[i + j] = report_table_20_changed_1[0]
                    report_table_20_changed_1.remove(report_table_20_changed_1[0])
                elif outcome20_list[i + j][1] == 2:
                    outcome20_list[i + j] = report_table_20_changed_2[0]
                    report_table_20_changed_2.remove(report_table_20_changed_2[0])
                elif outcome20_list[i + j][1] == 4:
                    outcome20_list[i + j] = report_table_20_changed_4[0]
                    report_table_20_changed_4.remove(report_table_20_changed_4[0])
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
    player_list_21 = []
    for i in outcome21_list:
        if i[0] != 0:
            player_list_21.append(i[0])
    report_table_21_changed_1 = report_table_1[4:]
    report_table_21_changed_2 = report_table_2[1:]
    report_table_21_changed_4 = report_table_4[1:]
    for i in report_table_21_changed_1:
        if i[0] in player_list_21:
            report_table_21_changed_1.remove(i)
    for i in report_table_21_changed_2:
        if i[0] in player_list_21:
            report_table_21_changed_2.remove(i)
    for i in report_table_21_changed_4:
        if i[0] in player_list_21:
            report_table_21_changed_4.remove(i)
    for i in range(len(outcome21_list)):
        for j in range(1, (len(outcome21_list) - i)):
            if outcome21_list[i][0] == outcome21_list[i + j][0] != 0:
                if outcome21_list[i + j][1] == 1:
                    outcome21_list[i + j] = report_table_21_changed_1[0]
                    report_table_21_changed_1.remove(report_table_21_changed_1[0])
                elif outcome21_list[i + j][1] == 2:
                    outcome21_list[i + j] = report_table_21_changed_2[0]
                    report_table_21_changed_2.remove(report_table_21_changed_2[0])
                elif outcome21_list[i + j][1] == 4:
                    outcome21_list[i + j] = report_table_21_changed_4[0]
                    report_table_21_changed_4.remove(report_table_21_changed_4[0])
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
    player_list_22 = []
    for i in outcome22_list:
        if i[0] != 0:
            player_list_22.append(i[0])
    report_table_22_changed_1 = report_table_1[6:]
    report_table_22_changed_4 = report_table_4[1:]
    for i in report_table_22_changed_1:
        if i[0] in player_list_22:
            report_table_22_changed_1.remove(i)
    for i in report_table_22_changed_4:
        if i[0] in player_list_22:
            report_table_22_changed_4.remove(i)
    for i in range(len(outcome22_list)):
        for j in range(1, (len(outcome22_list) - i)):
            if outcome22_list[i][0] == outcome22_list[i + j][0] != 0:
                if outcome22_list[i + j][1] == 1:
                    outcome22_list[i + j] = report_table_22_changed_1[0]
                    report_table_22_changed_1.remove(report_table_22_changed_1[0])
                elif outcome22_list[i + j][1] == 4:
                    outcome22_list[i + j] = report_table_22_changed_4[0]
                    report_table_22_changed_4.remove(report_table_22_changed_4[0])
    for i in outcome22_list:
        value_22 = value_22 + i[3]
    # outcome for 5*2
    value_23 = 0
    outcome23_list = [report_table_5[0], report_table_5[1]]
    player_list_23 = []
    for i in outcome23_list:
        if i[0] != 0:
            player_list_23.append(i[0])
    report_table_23_changed_5 = report_table_5[2:]
    for i in report_table_23_changed_5:
        if i[0] in player_list_23:
            report_table_23_changed_5.remove(i)
    for i in range(len(outcome23_list)):
        for j in range(1, (len(outcome23_list) - i)):
            if outcome23_list[i][0] == outcome23_list[i + j][0] != 0:
                if outcome23_list[i + j][1] == 5:
                    outcome23_list[i + j] = report_table_23_changed_5[0]
                    report_table_23_changed_5.remove(report_table_23_changed_5[0])
    for i in outcome23_list:
        value_23 = value_23 + i[3]
    # outcome for 5+4+1
    value_24 = 0
    outcome24_list = [report_table_5[0], report_table_4[0], report_table_1[0]]
    player_list_24 = []
    for i in outcome24_list:
        if i[0] != 0:
            player_list_24.append(i[0])
    report_table_24_changed_1 = report_table_1[1:]
    report_table_24_changed_4 = report_table_4[1:]
    report_table_24_changed_5 = report_table_5[1:]
    for i in report_table_24_changed_1:
        if i[0] in player_list_24:
            report_table_24_changed_1.remove(i)
    for i in report_table_24_changed_4:
        if i[0] in player_list_24:
            report_table_24_changed_4.remove(i)
    for i in report_table_24_changed_5:
        if i[0] in player_list_24:
            report_table_24_changed_5.remove(i)
    for i in range(len(outcome24_list)):
        for j in range(1, (len(outcome24_list) - i)):
            if outcome24_list[i][0] == outcome24_list[i + j][0] != 0:
                if outcome24_list[i + j][1] == 1:
                    outcome24_list[i + j] = report_table_24_changed_1[0]
                    report_table_24_changed_1.remove(report_table_24_changed_1[0])
                elif outcome24_list[i + j][1] == 4:
                    outcome24_list[i + j] = report_table_24_changed_4[0]
                    report_table_24_changed_4.remove(report_table_24_changed_4[0])
                elif outcome24_list[i + j][1] == 5:
                    outcome24_list[i + j] = report_table_24_changed_5[0]
                    report_table_24_changed_5.remove(report_table_24_changed_5[0])
    for i in outcome24_list:
        value_24 = value_24 + i[3]
    # outcome for 5+3+2
    value_25 = 0
    outcome25_list = [report_table_5[0], report_table_3[0], report_table_2[0]]
    player_list_25 = []
    for i in outcome25_list:
        if i[0] != 0:
            player_list_25.append(i[0])
    report_table_25_changed_2 = report_table_2[1:]
    report_table_25_changed_3 = report_table_3[1:]
    report_table_25_changed_5 = report_table_5[1:]
    for i in report_table_25_changed_2:
        if i[0] in player_list_25:
            report_table_25_changed_2.remove(i)
    for i in report_table_25_changed_3:
        if i[0] in player_list_25:
            report_table_25_changed_3.remove(i)
    for i in report_table_25_changed_5:
        if i[0] in player_list_25:
            report_table_25_changed_5.remove(i)
    for i in range(len(outcome25_list)):
        for j in range(1, (len(outcome25_list) - i)):
            if outcome25_list[i][0] == outcome25_list[i + j][0] != 0:
                if outcome25_list[i + j][1] == 2:
                    outcome25_list[i + j] = report_table_25_changed_2[0]
                    report_table_25_changed_2.remove(report_table_25_changed_2[0])
                elif outcome25_list[i + j][1] == 3:
                    outcome25_list[i + j] = report_table_25_changed_3[0]
                    report_table_25_changed_3.remove(report_table_25_changed_3[0])
                elif outcome25_list[i + j][1] == 5:
                    outcome25_list[i + j] = report_table_25_changed_5[0]
                    report_table_25_changed_5.remove(report_table_25_changed_5[0])
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
    player_list_26 = []
    for i in outcome26_list:
        if i[0] != 0:
            player_list_26.append(i[0])
    report_table_26_changed_1 = report_table_1[2:]
    report_table_26_changed_3 = report_table_3[1:]
    report_table_26_changed_5 = report_table_5[1:]
    for i in report_table_26_changed_1:
        if i[0] in player_list_26:
            report_table_26_changed_1.remove(i)
    for i in report_table_26_changed_3:
        if i[0] in player_list_26:
            report_table_26_changed_3.remove(i)
    for i in report_table_26_changed_5:
        if i[0] in player_list_26:
            report_table_26_changed_5.remove(i)
    for i in range(len(outcome26_list)):
        for j in range(1, (len(outcome26_list) - i)):
            if outcome26_list[i][0] == outcome26_list[i + j][0] != 0:
                if outcome26_list[i + j][1] == 1:
                    outcome26_list[i + j] = report_table_26_changed_1[0]
                    report_table_26_changed_1.remove(report_table_26_changed_1[0])
                elif outcome26_list[i + j][1] == 3:
                    outcome26_list[i + j] = report_table_26_changed_3[0]
                    report_table_26_changed_3.remove(report_table_26_changed_3[0])
                elif outcome26_list[i + j][1] == 5:
                    outcome26_list[i + j] = report_table_26_changed_5[0]
                    report_table_26_changed_5.remove(report_table_26_changed_5[0])
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
    player_list_27 = []
    for i in outcome27_list:
        if i[0] != 0:
            player_list_27.append(i[0])
    report_table_27_changed_1 = report_table_1[1:]
    report_table_27_changed_2 = report_table_2[2:]
    report_table_27_changed_5 = report_table_5[1:]
    for i in report_table_27_changed_1:
        if i[0] in player_list_27:
            report_table_27_changed_1.remove(i)
    for i in report_table_27_changed_2:
        if i[0] in player_list_27:
            report_table_27_changed_2.remove(i)
    for i in report_table_27_changed_5:
        if i[0] in player_list_27:
            report_table_27_changed_5.remove(i)
    for i in range(len(outcome27_list)):
        for j in range(1, (len(outcome27_list) - i)):
            if outcome27_list[i][0] == outcome27_list[i + j][0] != 0:
                if outcome27_list[i + j][1] == 1:
                    outcome27_list[i + j] = report_table_27_changed_1[0]
                    report_table_27_changed_1.remove(report_table_27_changed_1[0])
                elif outcome27_list[i + j][1] == 2:
                    outcome27_list[i + j] = report_table_27_changed_2[0]
                    report_table_27_changed_2.remove(report_table_27_changed_2[0])
                elif outcome27_list[i + j][1] == 5:
                    outcome27_list[i + j] = report_table_27_changed_5[0]
                    report_table_27_changed_5.remove(report_table_27_changed_5[0])
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
    player_list_28 = []
    for i in outcome28_list:
        if i[0] != 0:
            player_list_28.append(i[0])
    report_table_28_changed_1 = report_table_1[3:]
    report_table_28_changed_2 = report_table_2[1:]
    report_table_28_changed_5 = report_table_5[1:]
    for i in report_table_28_changed_1:
        if i[0] in player_list_28:
            report_table_28_changed_1.remove(i)
    for i in report_table_28_changed_2:
        if i[0] in player_list_28:
            report_table_28_changed_2.remove(i)
    for i in report_table_28_changed_5:
        if i[0] in player_list_28:
            report_table_28_changed_5.remove(i)
    for i in range(len(outcome28_list)):
        for j in range(1, (len(outcome28_list) - i)):
            if outcome28_list[i][0] == outcome28_list[i + j][0] != 0:
                if outcome28_list[i + j][1] == 1:
                    outcome28_list[i + j] = report_table_28_changed_1[0]
                    report_table_28_changed_1.remove(report_table_28_changed_1[0])
                elif outcome28_list[i + j][1] == 2:
                    outcome28_list[i + j] = report_table_28_changed_2[0]
                    report_table_28_changed_2.remove(report_table_28_changed_2[0])
                elif outcome28_list[i + j][1] == 5:
                    outcome28_list[i + j] = report_table_28_changed_5[0]
                    report_table_28_changed_5.remove(report_table_28_changed_5[0])
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
    player_list_29 = []
    for i in outcome29_list:
        if i[0] != 0:
            player_list_29.append(i[0])
    report_table_29_changed_1 = report_table_1[5:]
    report_table_29_changed_5 = report_table_5[1:]
    for i in report_table_29_changed_1:
        if i[0] in player_list_29:
            report_table_29_changed_1.remove(i)
    for i in report_table_29_changed_5:
        if i[0] in player_list_29:
            report_table_29_changed_5.remove(i)
    for i in range(len(outcome29_list)):
        for j in range(1, (len(outcome29_list) - i)):
            if outcome29_list[i][0] == outcome29_list[i + j][0] != 0:
                if outcome29_list[i + j][1] == 1:
                    outcome29_list[i + j] = report_table_29_changed_1[0]
                    report_table_29_changed_1.remove(report_table_29_changed_1[0])
                elif outcome29_list[i + j][1] == 5:
                    outcome29_list[i + j] = report_table_29_changed_5[0]
                    report_table_29_changed_5.remove(report_table_29_changed_5[0])
    for i in outcome29_list:
        value_29 = value_29 + i[3]
    # outcome for 6+4
    value_30 = 0
    outcome30_list = [report_table_6[0], report_table_4[0]]
    player_list_30 = []
    for i in outcome30_list:
        if i[0] != 0:
            player_list_30.append(i[0])
    report_table_30_changed_4 = report_table_4[1:]
    report_table_30_changed_6 = report_table_6[1:]
    for i in report_table_30_changed_4:
        if i[0] in player_list_30:
            report_table_30_changed_4.remove(i)
    for i in report_table_30_changed_6:
        if i[0] in player_list_30:
            report_table_30_changed_6.remove(i)
    for i in range(len(outcome30_list)):
        for j in range(1, (len(outcome30_list) - i)):
            if outcome30_list[i][0] == outcome30_list[i + j][0] != 0:
                if outcome30_list[i + j][1] == 4:
                    outcome30_list[i + j] = report_table_30_changed_4[0]
                    report_table_30_changed_4.remove(report_table_30_changed_4[0])
                elif outcome30_list[i + j][1] == 6:
                    outcome30_list[i + j] = report_table_30_changed_6[0]
                    report_table_30_changed_6.remove(report_table_30_changed_6[0])
    for i in outcome30_list:
        value_30 = value_30 + i[3]
    # outcome for 6+3+1
    value_31 = 0
    outcome31_list = [report_table_6[0], report_table_3[0], report_table_1[0]]
    player_list_31 = []
    for i in outcome31_list:
        if i[0] != 0:
            player_list_31.append(i[0])
    report_table_31_changed_1 = report_table_1[1:]
    report_table_31_changed_3 = report_table_3[1:]
    report_table_31_changed_6 = report_table_6[1:]
    for i in report_table_31_changed_1:
        if i[0] in player_list_31:
            report_table_31_changed_1.remove(i)
    for i in report_table_31_changed_3:
        if i[0] in player_list_31:
            report_table_31_changed_3.remove(i)
    for i in report_table_31_changed_6:
        if i[0] in player_list_31:
            report_table_31_changed_6.remove(i)
    for i in range(len(outcome31_list)):
        for j in range(1, (len(outcome31_list) - i)):
            if outcome31_list[i][0] == outcome31_list[i + j][0] != 0:
                if outcome31_list[i + j][1] == 1:
                    outcome31_list[i + j] = report_table_31_changed_1[0]
                    report_table_31_changed_1.remove(report_table_31_changed_1[0])
                elif outcome31_list[i + j][1] == 3:
                    outcome31_list[i + j] = report_table_31_changed_3[0]
                    report_table_31_changed_3.remove(report_table_31_changed_3[0])
                elif outcome31_list[i + j][1] == 6:
                    outcome31_list[i + j] = report_table_31_changed_6[0]
                    report_table_31_changed_6.remove(report_table_31_changed_6[0])
    for i in outcome31_list:
        value_31 = value_31 + i[3]
    # outcome for 6+2*2
    value_32 = 0
    outcome32_list = [report_table_6[0], report_table_2[0], report_table_2[1]]
    player_list_32 = []
    for i in outcome32_list:
        if i[0] != 0:
            player_list_32.append(i[0])
    report_table_32_changed_2 = report_table_2[2:]
    report_table_32_changed_6 = report_table_6[1:]
    for i in report_table_32_changed_2:
        if i[0] in player_list_32:
            report_table_32_changed_2.remove(i)
    for i in report_table_32_changed_6:
        if i[0] in player_list_32:
            report_table_32_changed_6.remove(i)
    for i in range(len(outcome32_list)):
        for j in range(1, (len(outcome32_list) - i)):
            if outcome32_list[i][0] == outcome32_list[i + j][0] != 0:
                if outcome32_list[i + j][1] == 2:
                    outcome32_list[i + j] = report_table_32_changed_2[0]
                    report_table_32_changed_2.remove(report_table_32_changed_2[0])
                elif outcome32_list[i + j][1] == 6:
                    outcome32_list[i + j] = report_table_32_changed_6[0]
                    report_table_32_changed_6.remove(report_table_32_changed_6[0])
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
    player_list_33 = []
    for i in outcome33_list:
        if i[0] != 0:
            player_list_33.append(i[0])
    report_table_33_changed_1 = report_table_1[2:]
    report_table_33_changed_2 = report_table_2[1:]
    report_table_33_changed_6 = report_table_6[1:]
    for i in report_table_33_changed_1:
        if i[0] in player_list_33:
            report_table_33_changed_1.remove(i)
    for i in report_table_33_changed_2:
        if i[0] in player_list_33:
            report_table_33_changed_2.remove(i)
    for i in report_table_33_changed_6:
        if i[0] in player_list_33:
            report_table_33_changed_6.remove(i)
    for i in range(len(outcome33_list)):
        for j in range(1, (len(outcome33_list) - i)):
            if outcome33_list[i][0] == outcome33_list[i + j][0] != 0:
                if outcome33_list[i + j][1] == 1:
                    outcome33_list[i + j] = report_table_33_changed_1[0]
                    report_table_33_changed_1.remove(report_table_33_changed_1[0])
                elif outcome33_list[i + j][1] == 2:
                    outcome33_list[i + j] = report_table_33_changed_2[0]
                    report_table_33_changed_2.remove(report_table_33_changed_2[0])
                elif outcome33_list[i + j][1] == 6:
                    outcome33_list[i + j] = report_table_33_changed_6[0]
                    report_table_33_changed_6.remove(report_table_33_changed_6[0])
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
    player_list_34 = []
    for i in outcome34_list:
        if i[0] != 0:
            player_list_34.append(i[0])
    report_table_34_changed_1 = report_table_1[4:]
    report_table_34_changed_6 = report_table_6[1:]
    for i in report_table_34_changed_1:
        if i[0] in player_list_34:
            report_table_34_changed_1.remove(i)
    for i in report_table_34_changed_6:
        if i[0] in player_list_34:
            report_table_34_changed_6.remove(i)
    for i in range(len(outcome34_list)):
        for j in range(1, (len(outcome34_list) - i)):
            if outcome34_list[i][0] == outcome34_list[i + j][0] != 0:
                if outcome34_list[i + j][1] == 1:
                    outcome34_list[i + j] = report_table_34_changed_1[0]
                    report_table_34_changed_1.remove(report_table_34_changed_1[0])
                elif outcome34_list[i + j][1] == 6:
                    outcome32_list[i + j] = report_table_34_changed_6[0]
                    report_table_34_changed_6.remove(report_table_34_changed_6[0])
    for i in outcome34_list:
        value_34 = value_34 + i[3]
    # outcome for 7+3
    value_35 = 0
    outcome35_list = [report_table_7[0], report_table_3[0]]
    player_list_35 = []
    for i in outcome35_list:
        if i[0] != 0:
            player_list_35.append(i[0])
    report_table_35_changed_3 = report_table_3[1:]
    report_table_35_changed_7 = report_table_7[1:]
    for i in report_table_35_changed_3:
        if i[0] in player_list_35:
            report_table_35_changed_3.remove(i)
    for i in report_table_35_changed_7:
        if i[0] in player_list_35:
            report_table_35_changed_7.remove(i)
    for i in range(len(outcome35_list)):
        for j in range(1, (len(outcome35_list) - i)):
            if outcome35_list[i][0] == outcome35_list[i + j][0] != 0:
                if outcome35_list[i + j][1] == 3:
                    outcome35_list[i + j] = report_table_35_changed_3[0]
                    report_table_35_changed_3.remove(report_table_35_changed_3[0])
                elif outcome35_list[i + j][1] == 7:
                    outcome35_list[i + j] = report_table_35_changed_7[0]
                    report_table_35_changed_7.remove(report_table_35_changed_7[0])
    for i in outcome35_list:
        value_35 = value_35 + i[3]
    # outcome for 7+2+1
    value_36 = 0
    outcome36_list = [report_table_7[0], report_table_2[0], report_table_1[0]]
    player_list_36 = []
    for i in outcome36_list:
        if i[0] != 0:
            player_list_36.append(i[0])
    report_table_36_changed_1 = report_table_1[2:]
    report_table_36_changed_2 = report_table_2[1:]
    report_table_36_changed_7 = report_table_7[1:]
    for i in report_table_36_changed_1:
        if i[0] in player_list_36:
            report_table_36_changed_1.remove(i)
    for i in report_table_36_changed_2:
        if i[0] in player_list_36:
            report_table_36_changed_2.remove(i)
    for i in report_table_36_changed_7:
        if i[0] in player_list_36:
            report_table_36_changed_7.remove(i)
    for i in range(len(outcome36_list)):
        for j in range(1, (len(outcome36_list) - i)):
            if outcome36_list[i][0] == outcome36_list[i + j][0] != 0:
                if outcome36_list[i + j][1] == 1:
                    outcome36_list[i + j] = report_table_36_changed_1[0]
                    report_table_36_changed_1.remove(report_table_36_changed_1[0])
                elif outcome36_list[i + j][1] == 2:
                    outcome36_list[i + j] = report_table_36_changed_2[0]
                    report_table_36_changed_2.remove(report_table_36_changed_2[0])
                elif outcome36_list[i + j][1] == 7:
                    outcome36_list[i + j] = report_table_36_changed_7[0]
                    report_table_36_changed_7.remove(report_table_36_changed_7[0])
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
    player_list_37 = []
    for i in outcome37_list:
        if i[0] != 0:
            player_list_37.append(i[0])
    report_table_37_changed_1 = report_table_1[3:]
    report_table_37_changed_7 = report_table_7[1:]
    for i in report_table_37_changed_1:
        if i[0] in player_list_37:
            report_table_37_changed_1.remove(i)
    for i in report_table_37_changed_7:
        if i[0] in player_list_37:
            report_table_37_changed_7.remove(i)
    for i in range(len(outcome37_list)):
        for j in range(1, (len(outcome37_list) - i)):
            if outcome37_list[i][0] == outcome37_list[i + j][0] != 0:
                if outcome37_list[i + j][1] == 1:
                    outcome37_list[i + j] = report_table_37_changed_1[0]
                    report_table_37_changed_1.remove(report_table_37_changed_1[0])
                elif outcome37_list[i + j][1] == 7:
                    outcome37_list[i + j] = report_table_37_changed_7[0]
                    report_table_37_changed_7.remove(report_table_37_changed_7[0])
    for i in outcome37_list:
        value_37 = value_37 + i[3]
    # outcome for 8+2
    value_38 = 0
    outcome38_list = [report_table_8[0], report_table_2[0]]
    player_list_38 = []
    for i in outcome38_list:
        if i[0] != 0:
            player_list_38.append(i[0])
    report_table_38_changed_2 = report_table_2[1:]
    report_table_38_changed_8 = report_table_8[1:]
    for i in report_table_38_changed_2:
        if i[0] in player_list_38:
            report_table_38_changed_2.remove(i)
    for i in report_table_38_changed_8:
        if i[0] in player_list_38:
            report_table_38_changed_8.remove(i)
    for i in range(len(outcome38_list)):
        for j in range(1, (len(outcome38_list) - i)):
            if outcome38_list[i][0] == outcome38_list[i + j][0] != 0:
                if outcome38_list[i + j][1] == 2:
                    outcome38_list[i + j] = report_table_38_changed_2[0]
                    report_table_38_changed_2.remove(report_table_38_changed_2[0])
                elif outcome38_list[i + j][1] == 8:
                    outcome38_list[i + j] = report_table_38_changed_8[0]
                    report_table_38_changed_8.remove(report_table_38_changed_8[0])
    for i in outcome38_list:
        value_38 = value_38 + i[3]
    # outcome for 8+1*2
    value_39 = 0
    outcome39_list = [report_table_8[0], report_table_1[0], report_table_1[1]]
    player_list_39 = []
    for i in outcome39_list:
        if i[0] != 0:
            player_list_39.append(i[0])
    report_table_39_changed_1 = report_table_1[2:]
    report_table_39_changed_8 = report_table_8[1:]
    for i in report_table_39_changed_1:
        if i[0] in player_list_39:
            report_table_39_changed_1.remove(i)
    for i in report_table_39_changed_8:
        if i[0] in player_list_39:
            report_table_39_changed_8.remove(i)
    for i in range(len(outcome39_list)):
        for j in range(1, (len(outcome39_list) - i)):
            if outcome39_list[i][0] == outcome39_list[i + j][0] != 0:
                if outcome39_list[i + j][1] == 1:
                    outcome39_list[i + j] = report_table_39_changed_1[0]
                    report_table_39_changed_1.remove(report_table_39_changed_1[0])
                elif outcome39_list[i + j][1] == 8:
                    outcome39_list[i + j] = report_table_39_changed_8[0]
                    report_table_39_changed_8.remove(report_table_39_changed_8[0])
    for i in outcome39_list:
        value_39 = value_39 + i[3]
    # outcome for 9+1
    value_40 = 0
    outcome40_list = [report_table_9[0], report_table_1[0]]
    player_list_40 = []
    for i in outcome40_list:
        if i[0] != 0:
            player_list_40.append(i[0])
    report_table_40_changed_1 = report_table_1[1:]
    report_table_40_changed_9 = report_table_9[1:]
    for i in report_table_40_changed_1:
        if i[0] in player_list_40:
            report_table_40_changed_1.remove(i)
    for i in report_table_40_changed_9:
        if i[0] in player_list_40:
            report_table_40_changed_9.remove(i)
    for i in range(len(outcome40_list)):
        for j in range(1, (len(outcome40_list) - i)):
            if outcome40_list[i][0] == outcome40_list[i + j][0] != 0:
                if outcome40_list[i + j][1] == 1:
                    outcome40_list[i + j] = report_table_40_changed_1[0]
                    report_table_40_changed_1.remove(report_table_40_changed_1[0])
                elif outcome40_list[i + j][1] == 9:
                    outcome40_list[i + j] = report_table_40_changed_9[0]
                    report_table_40_changed_9.remove(report_table_40_changed_9[0])
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
                            print(
                                z,
                                "----truth-telling-----" "allocate",
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
                            seplayer_list_1 = []
                            for i in seoutcome1_list:
                                if i[0] != 0:
                                    seplayer_list_1.append(i[0])
                            sereport_table_1_changed = sereport_table_1[9:]
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
                            # outcome for 2*5
                            sevalue_2 = 0
                            seoutcome2_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_2[3],
                                sereport_table_2[4],
                            ]
                            seplayer_list_2 = []
                            for i in seoutcome2_list:
                                if i[0] != 0:
                                    seplayer_list_2.append(i[0])
                            sereport_table_2_changed = sereport_table_2[5:]
                            for i in sereport_table_2_changed:
                                if i[0] in seplayer_list_2:
                                    sereport_table_2_changed.remove(i)
                            for i in range(len(seoutcome2_list)):
                                for j in range(1, (len(seoutcome2_list) - i)):
                                    if (
                                        seoutcome2_list[i][0]
                                        == seoutcome2_list[i + j][0]
                                        != 0
                                    ):
                                        seoutcome2_list[
                                            i + j
                                        ] = sereport_table_2_changed[0]
                                        sereport_table_2_changed.remove(
                                            sereport_table_2_changed[0]
                                        )
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
                            seplayer_list_3 = []
                            for i in seoutcome3_list:
                                if i[0] != 0:
                                    seplayer_list_3.append(i[0])
                            sereport_table_3_changed_1 = sereport_table_1[2:]
                            sereport_table_3_changed_2 = sereport_table_2[4:]
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
                            seplayer_list_4 = []
                            for i in seoutcome4_list:
                                if i[0] != 0:
                                    seplayer_list_4.append(i[0])
                            sereport_table_4_changed_1 = sereport_table_1[4:]
                            sereport_table_4_changed_2 = sereport_table_2[3:]
                            for i in sereport_table_4_changed_1:
                                if i[0] in seplayer_list_4:
                                    sereport_table_4_changed_1.remove(i)
                            for i in sereport_table_4_changed_2:
                                if i[0] in seplayer_list_4:
                                    sereport_table_4_changed_2.remove(i)
                            for i in range(len(seoutcome4_list)):
                                for j in range(1, (len(seoutcome4_list) - i)):
                                    if (
                                        seoutcome4_list[i][0]
                                        == seoutcome4_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome4_list[i + j][1] == 1:
                                            seoutcome4_list[
                                                i + j
                                            ] = sereport_table_4_changed_1[0]
                                            sereport_table_4_changed_1.remove(
                                                sereport_table_4_changed_1[0]
                                            )
                                        elif seoutcome4_list[i + j][1] == 2:
                                            seoutcome4_list[
                                                i + j
                                            ] = sereport_table_4_changed_2[0]
                                            sereport_table_4_changed_2.remove(
                                                sereport_table_4_changed_2[0]
                                            )
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
                            seplayer_list_5 = []
                            for i in seoutcome5_list:
                                if i[0] != 0:
                                    seplayer_list_5.append(i[0])
                            sereport_table_5_changed_1 = sereport_table_1[6:]
                            sereport_table_5_changed_2 = sereport_table_2[2:]
                            for i in sereport_table_5_changed_1:
                                if i[0] in seplayer_list_5:
                                    sereport_table_5_changed_1.remove(i)
                            for i in sereport_table_5_changed_2:
                                if i[0] in seplayer_list_5:
                                    sereport_table_5_changed_2.remove(i)
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
                                        elif seoutcome5_list[i + j][1] == 2:
                                            seoutcome5_list[
                                                i + j
                                            ] = sereport_table_5_changed_2[0]
                                            sereport_table_5_changed_2.remove(
                                                sereport_table_5_changed_2[0]
                                            )
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
                            seplayer_list_6 = []
                            for i in seoutcome6_list:
                                if i[0] != 0:
                                    seplayer_list_6.append(i[0])
                            sereport_table_6_changed_1 = sereport_table_1[8:]
                            sereport_table_6_changed_2 = sereport_table_2[1:]
                            for i in sereport_table_6_changed_1:
                                if i[0] in seplayer_list_6:
                                    sereport_table_6_changed_1.remove(i)
                            for i in sereport_table_6_changed_2:
                                if i[0] in seplayer_list_6:
                                    sereport_table_6_changed_2.remove(i)
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
                                        elif seoutcome6_list[i + j][1] == 2:
                                            seoutcome6_list[
                                                i + j
                                            ] = sereport_table_6_changed_2[0]
                                            sereport_table_6_changed_2.remove(
                                                sereport_table_6_changed_2[0]
                                            )
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
                            seplayer_list_7 = []
                            for i in seoutcome7_list:
                                if i[0] != 0:
                                    seplayer_list_7.append(i[0])
                            sereport_table_7_changed_1 = sereport_table_1[1:]
                            sereport_table_7_changed_3 = sereport_table_3[3:]
                            for i in sereport_table_7_changed_1:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_1.remove(i)
                            for i in sereport_table_7_changed_3:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_3.remove(i)
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
                                        elif seoutcome7_list[i + j][1] == 3:
                                            seoutcome7_list[
                                                i + j
                                            ] = sereport_table_7_changed_3[0]
                                            sereport_table_7_changed_3.remove(
                                                sereport_table_7_changed_3[0]
                                            )
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
                            seplayer_list_8 = []
                            for i in seoutcome8_list:
                                if i[0] != 0:
                                    seplayer_list_8.append(i[0])
                            sereport_table_8_changed_2 = sereport_table_2[2:]
                            sereport_table_8_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_8_changed_2:
                                if i[0] in seplayer_list_8:
                                    sereport_table_8_changed_2.remove(i)
                            for i in sereport_table_8_changed_3:
                                if i[0] in seplayer_list_8:
                                    sereport_table_8_changed_3.remove(i)
                            for i in range(len(seoutcome8_list)):
                                for j in range(1, (len(seoutcome8_list) - i)):
                                    if (
                                        seoutcome8_list[i][0]
                                        == seoutcome8_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome8_list[i + j][1] == 2:
                                            seoutcome8_list[
                                                i + j
                                            ] = sereport_table_8_changed_2[0]
                                            sereport_table_8_changed_2.remove(
                                                sereport_table_8_changed_2[0]
                                            )
                                        elif seoutcome8_list[i + j][1] == 3:
                                            seoutcome8_list[
                                                i + j
                                            ] = sereport_table_8_changed_3[0]
                                            sereport_table_8_changed_3.remove(
                                                sereport_table_8_changed_3[0]
                                            )
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
                            seplayer_list_9 = []
                            for i in seoutcome9_list:
                                if i[0] != 0:
                                    seplayer_list_9.append(i[0])
                            sereport_table_9_changed_1 = sereport_table_1[2:]
                            sereport_table_9_changed_2 = sereport_table_2[1:]
                            sereport_table_9_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_9_changed_1:
                                if i[0] in seplayer_list_9:
                                    sereport_table_9_changed_1.remove(i)
                            for i in sereport_table_9_changed_2:
                                if i[0] in seplayer_list_9:
                                    sereport_table_9_changed_2.remove(i)
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
                                        if seoutcome9_list[i + j][1] == 1:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_1[0]
                                            sereport_table_9_changed_1.remove(
                                                sereport_table_9_changed_1[0]
                                            )
                                        elif seoutcome9_list[i + j][1] == 2:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_2[0]
                                            sereport_table_9_changed_2.remove(
                                                sereport_table_9_changed_2[0]
                                            )
                                        elif seoutcome9_list[i + j][1] == 3:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_3[0]
                                            sereport_table_9_changed_3.remove(
                                                sereport_table_9_changed_3[0]
                                            )
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
                            seplayer_list_10 = []
                            for i in seoutcome10_list:
                                if i[0] != 0:
                                    seplayer_list_10.append(i[0])
                            sereport_table_10_changed_1 = sereport_table_1[4:]
                            sereport_table_10_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_10_changed_1:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_1.remove(i)
                            for i in sereport_table_10_changed_3:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_3.remove(i)
                            for i in range(len(seoutcome10_list)):
                                for j in range(1, (len(seoutcome10_list) - i)):
                                    if (
                                        seoutcome10_list[i][0]
                                        == seoutcome10_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome10_list[i + j][1] == 1:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_1[0]
                                            sereport_table_10_changed_1.remove(
                                                sereport_table_10_changed_1[0]
                                            )
                                        elif seoutcome10_list[i + j][1] == 3:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_3[0]
                                            sereport_table_10_changed_3.remove(
                                                sereport_table_10_changed_3[0]
                                            )
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
                            seplayer_list_11 = []
                            for i in seoutcome11_list:
                                if i[0] != 0:
                                    seplayer_list_11.append(i[0])
                            sereport_table_11_changed_1 = sereport_table_1[3:]
                            sereport_table_11_changed_2 = sereport_table_2[2:]
                            sereport_table_11_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_11_changed_1:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_1.remove(i)
                            for i in sereport_table_11_changed_2:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_2.remove(i)
                            for i in sereport_table_11_changed_3:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_3.remove(i)
                            for i in range(len(seoutcome11_list)):
                                for j in range(1, (len(seoutcome11_list) - i)):
                                    if (
                                        seoutcome11_list[i][0]
                                        == seoutcome11_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome11_list[i + j][1] == 1:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_1[0]
                                            sereport_table_11_changed_1.remove(
                                                sereport_table_11_changed_1[0]
                                            )
                                        elif seoutcome11_list[i + j][1] == 2:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_2[0]
                                            sereport_table_11_changed_2.remove(
                                                sereport_table_11_changed_2[0]
                                            )
                                        elif seoutcome11_list[i + j][1] == 3:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_3[0]
                                            sereport_table_11_changed_3.remove(
                                                sereport_table_11_changed_3[0]
                                            )
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
                            seplayer_list_12 = []
                            for i in seoutcome12_list:
                                if i[0] != 0:
                                    seplayer_list_12.append(i[0])
                            sereport_table_12_changed_1 = sereport_table_1[5:]
                            sereport_table_12_changed_2 = sereport_table_2[1:]
                            sereport_table_12_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_12_changed_1:
                                if i[0] in seplayer_list_12:
                                    sereport_table_12_changed_1.remove(i)
                            for i in sereport_table_12_changed_2:
                                if i[0] in seplayer_list_12:
                                    sereport_table_12_changed_2.remove(i)
                            for i in sereport_table_12_changed_3:
                                if i[0] in seplayer_list_12:
                                    sereport_table_12_changed_3.remove(i)
                            for i in range(len(seoutcome12_list)):
                                for j in range(1, (len(seoutcome12_list) - i)):
                                    if (
                                        seoutcome12_list[i][0]
                                        == seoutcome12_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome12_list[i + j][1] == 1:
                                            seoutcome12_list[
                                                i + j
                                            ] = sereport_table_12_changed_1[0]
                                            sereport_table_12_changed_1.remove(
                                                sereport_table_12_changed_1[0]
                                            )
                                        elif seoutcome12_list[i + j][1] == 2:
                                            seoutcome12_list[
                                                i + j
                                            ] = sereport_table_12_changed_2[0]
                                            sereport_table_12_changed_2.remove(
                                                sereport_table_12_changed_2[0]
                                            )
                                        elif seoutcome12_list[i + j][1] == 3:
                                            seoutcome12_list[
                                                i + j
                                            ] = sereport_table_12_changed_3[0]
                                            sereport_table_12_changed_3.remove(
                                                sereport_table_12_changed_3[0]
                                            )
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
                            seplayer_list_13 = []
                            for i in seoutcome13_list:
                                if i[0] != 0:
                                    seplayer_list_13.append(i[0])
                            sereport_table_13_changed_1 = sereport_table_1[7:]
                            sereport_table_13_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_13_changed_1:
                                if i[0] in seplayer_list_13:
                                    sereport_table_13_changed_1.remove(i)
                            for i in sereport_table_13_changed_3:
                                if i[0] in seplayer_list_13:
                                    sereport_table_13_changed_3.remove(i)
                            for i in range(len(seoutcome13_list)):
                                for j in range(1, (len(seoutcome13_list) - i)):
                                    if (
                                        seoutcome13_list[i][0]
                                        == seoutcome13_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome13_list[i + j][1] == 1:
                                            seoutcome13_list[
                                                i + j
                                            ] = sereport_table_13_changed_1[0]
                                            sereport_table_13_changed_1.remove(
                                                sereport_table_13_changed_1[0]
                                            )
                                        elif seoutcome13_list[i + j][1] == 3:
                                            seoutcome13_list[
                                                i + j
                                            ] = sereport_table_13_changed_3[0]
                                            sereport_table_13_changed_3.remove(
                                                sereport_table_13_changed_3[0]
                                            )
                            for i in seoutcome13_list:
                                sevalue_13 = sevalue_13 + i[3]
                            # outcome for 4*2+2
                            sevalue_14 = 0
                            seoutcome14_list = [
                                sereport_table_4[0],
                                sereport_table_4[1],
                                sereport_table_2[0],
                            ]
                            seplayer_list_14 = []
                            for i in seoutcome14_list:
                                if i[0] != 0:
                                    seplayer_list_14.append(i[0])
                            sereport_table_14_changed_2 = sereport_table_2[1:]
                            sereport_table_14_changed_4 = sereport_table_4[2:]
                            for i in sereport_table_14_changed_2:
                                if i[0] in seplayer_list_14:
                                    sereport_table_14_changed_2.remove(i)
                            for i in sereport_table_14_changed_4:
                                if i[0] in seplayer_list_14:
                                    sereport_table_14_changed_4.remove(i)
                            for i in range(len(seoutcome14_list)):
                                for j in range(1, (len(seoutcome14_list) - i)):
                                    if (
                                        seoutcome14_list[i][0]
                                        == seoutcome14_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome14_list[i + j][1] == 2:
                                            seoutcome14_list[
                                                i + j
                                            ] = sereport_table_14_changed_2[0]
                                            sereport_table_14_changed_2.remove(
                                                sereport_table_14_changed_2[0]
                                            )
                                        elif seoutcome14_list[i + j][1] == 4:
                                            seoutcome14_list[
                                                i + j
                                            ] = sereport_table_14_changed_4[0]
                                            sereport_table_14_changed_4.remove(
                                                sereport_table_14_changed_4[0]
                                            )
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
                            seplayer_list_15 = []
                            for i in seoutcome15_list:
                                if i[0] != 0:
                                    seplayer_list_15.append(i[0])
                            sereport_table_15_changed_1 = sereport_table_1[2:]
                            sereport_table_15_changed_4 = sereport_table_4[2:]
                            for i in sereport_table_15_changed_1:
                                if i[0] in seplayer_list_15:
                                    sereport_table_15_changed_1.remove(i)
                            for i in sereport_table_15_changed_4:
                                if i[0] in seplayer_list_15:
                                    sereport_table_15_changed_4.remove(i)
                            for i in range(len(seoutcome15_list)):
                                for j in range(1, (len(seoutcome15_list) - i)):
                                    if (
                                        seoutcome15_list[i][0]
                                        == seoutcome15_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome15_list[i + j][1] == 1:
                                            seoutcome15_list[
                                                i + j
                                            ] = sereport_table_15_changed_1[0]
                                            sereport_table_15_changed_1.remove(
                                                sereport_table_15_changed_1[0]
                                            )
                                        elif seoutcome15_list[i + j][1] == 4:
                                            seoutcome15_list[
                                                i + j
                                            ] = sereport_table_15_changed_4[0]
                                            sereport_table_15_changed_4.remove(
                                                sereport_table_15_changed_4[0]
                                            )
                            for i in seoutcome15_list:
                                sevalue_15 = sevalue_15 + i[3]
                            # outcome for 4+3*2
                            sevalue_16 = 0
                            seoutcome16_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_3[1],
                            ]
                            seplayer_list_16 = []
                            for i in seoutcome16_list:
                                if i[0] != 0:
                                    seplayer_list_16.append(i[0])
                            sereport_table_16_changed_3 = sereport_table_3[2:]
                            sereport_table_16_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_16_changed_3:
                                if i[0] in seplayer_list_16:
                                    sereport_table_16_changed_3.remove(i)
                            for i in sereport_table_16_changed_4:
                                if i[0] in seplayer_list_16:
                                    sereport_table_16_changed_4.remove(i)
                            for i in range(len(seoutcome16_list)):
                                for j in range(1, (len(seoutcome16_list) - i)):
                                    if (
                                        seoutcome16_list[i][0]
                                        == seoutcome16_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome16_list[i + j][1] == 3:
                                            seoutcome16_list[
                                                i + j
                                            ] = sereport_table_16_changed_3[0]
                                            sereport_table_16_changed_3.remove(
                                                sereport_table_16_changed_3[0]
                                            )
                                        elif seoutcome16_list[i + j][1] == 4:
                                            seoutcome16_list[
                                                i + j
                                            ] = sereport_table_16_changed_4[0]
                                            sereport_table_16_changed_4.remove(
                                                sereport_table_16_changed_4[0]
                                            )
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
                            seplayer_list_17 = []
                            for i in seoutcome17_list:
                                if i[0] != 0:
                                    seplayer_list_17.append(i[0])
                            sereport_table_17_changed_1 = sereport_table_1[1:]
                            sereport_table_17_changed_2 = sereport_table_2[1:]
                            sereport_table_17_changed_3 = sereport_table_3[1:]
                            sereport_table_17_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_17_changed_1:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_1.remove(i)
                            for i in sereport_table_17_changed_2:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_2.remove(i)
                            for i in sereport_table_17_changed_3:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_3.remove(i)
                            for i in sereport_table_17_changed_4:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_4.remove(i)
                            for i in range(len(seoutcome17_list)):
                                for j in range(1, (len(seoutcome17_list) - i)):
                                    if (
                                        seoutcome17_list[i][0]
                                        == seoutcome17_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome17_list[i + j][1] == 1:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_1[0]
                                            sereport_table_17_changed_1.remove(
                                                sereport_table_17_changed_1[0]
                                            )
                                        elif seoutcome17_list[i + j][1] == 2:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_2[0]
                                            sereport_table_17_changed_2.remove(
                                                sereport_table_17_changed_2[0]
                                            )
                                        elif seoutcome17_list[i + j][1] == 3:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_3[0]
                                            sereport_table_17_changed_3.remove(
                                                sereport_table_17_changed_3[0]
                                            )
                                        elif seoutcome17_list[i + j][1] == 4:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_4[0]
                                            sereport_table_17_changed_4.remove(
                                                sereport_table_17_changed_4[0]
                                            )
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
                            seplayer_list_18 = []
                            for i in seoutcome18_list:
                                if i[0] != 0:
                                    seplayer_list_18.append(i[0])
                            sereport_table_18_changed_1 = sereport_table_1[3:]
                            sereport_table_18_changed_3 = sereport_table_3[1:]
                            sereport_table_18_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_18_changed_1:
                                if i[0] in seplayer_list_18:
                                    sereport_table_18_changed_1.remove(i)
                            for i in sereport_table_18_changed_3:
                                if i[0] in seplayer_list_18:
                                    sereport_table_18_changed_3.remove(i)
                            for i in sereport_table_18_changed_4:
                                if i[0] in seplayer_list_18:
                                    sereport_table_18_changed_4.remove(i)
                            for i in range(len(seoutcome18_list)):
                                for j in range(1, (len(seoutcome18_list) - i)):
                                    if (
                                        seoutcome18_list[i][0]
                                        == seoutcome18_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome18_list[i + j][1] == 1:
                                            seoutcome18_list[
                                                i + j
                                            ] = sereport_table_18_changed_1[0]
                                            sereport_table_18_changed_1.remove(
                                                sereport_table_18_changed_1[0]
                                            )
                                        elif seoutcome18_list[i + j][1] == 3:
                                            seoutcome18_list[
                                                i + j
                                            ] = sereport_table_18_changed_3[0]
                                            sereport_table_18_changed_3.remove(
                                                sereport_table_18_changed_3[0]
                                            )
                                        elif seoutcome18_list[i + j][1] == 4:
                                            seoutcome18_list[
                                                i + j
                                            ] = sereport_table_18_changed_4[0]
                                            sereport_table_18_changed_4.remove(
                                                sereport_table_18_changed_4[0]
                                            )
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
                            seplayer_list_19 = []
                            for i in seoutcome19_list:
                                if i[0] != 0:
                                    seplayer_list_19.append(i[0])
                            sereport_table_19_changed_2 = sereport_table_2[3:]
                            sereport_table_19_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_19_changed_2:
                                if i[0] in seplayer_list_19:
                                    sereport_table_19_changed_2.remove(i)
                            for i in sereport_table_19_changed_4:
                                if i[0] in seplayer_list_19:
                                    sereport_table_19_changed_4.remove(i)
                            for i in range(len(seoutcome19_list)):
                                for j in range(1, (len(seoutcome19_list) - i)):
                                    if (
                                        seoutcome19_list[i][0]
                                        == seoutcome19_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome19_list[i + j][1] == 2:
                                            seoutcome19_list[
                                                i + j
                                            ] = sereport_table_19_changed_2[0]
                                            sereport_table_19_changed_2.remove(
                                                sereport_table_19_changed_2[0]
                                            )
                                        elif seoutcome19_list[i + j][1] == 4:
                                            seoutcome19_list[
                                                i + j
                                            ] = sereport_table_19_changed_4[0]
                                            sereport_table_19_changed_4.remove(
                                                sereport_table_19_changed_4[0]
                                            )
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
                            seplayer_list_20 = []
                            for i in seoutcome20_list:
                                if i[0] != 0:
                                    seplayer_list_20.append(i[0])
                            sereport_table_20_changed_1 = sereport_table_1[2:]
                            sereport_table_20_changed_2 = sereport_table_2[2:]
                            sereport_table_20_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_20_changed_1:
                                if i[0] in seplayer_list_20:
                                    sereport_table_20_changed_1.remove(i)
                            for i in sereport_table_20_changed_2:
                                if i[0] in seplayer_list_20:
                                    sereport_table_20_changed_2.remove(i)
                            for i in sereport_table_20_changed_4:
                                if i[0] in seplayer_list_20:
                                    sereport_table_20_changed_4.remove(i)
                            for i in range(len(seoutcome20_list)):
                                for j in range(1, (len(seoutcome20_list) - i)):
                                    if (
                                        seoutcome20_list[i][0]
                                        == seoutcome20_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome20_list[i + j][1] == 1:
                                            seoutcome20_list[
                                                i + j
                                            ] = sereport_table_20_changed_1[0]
                                            sereport_table_20_changed_1.remove(
                                                sereport_table_20_changed_1[0]
                                            )
                                        elif seoutcome20_list[i + j][1] == 2:
                                            seoutcome20_list[
                                                i + j
                                            ] = sereport_table_20_changed_2[0]
                                            sereport_table_20_changed_2.remove(
                                                sereport_table_20_changed_2[0]
                                            )
                                        elif seoutcome20_list[i + j][1] == 4:
                                            seoutcome20_list[
                                                i + j
                                            ] = sereport_table_20_changed_4[0]
                                            sereport_table_20_changed_4.remove(
                                                sereport_table_20_changed_4[0]
                                            )
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
                            seplayer_list_21 = []
                            for i in seoutcome21_list:
                                if i[0] != 0:
                                    seplayer_list_21.append(i[0])
                            sereport_table_21_changed_1 = sereport_table_1[4:]
                            sereport_table_21_changed_2 = sereport_table_2[1:]
                            sereport_table_21_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_21_changed_1:
                                if i[0] in seplayer_list_21:
                                    sereport_table_21_changed_1.remove(i)
                            for i in sereport_table_21_changed_2:
                                if i[0] in seplayer_list_21:
                                    sereport_table_21_changed_2.remove(i)
                            for i in sereport_table_21_changed_4:
                                if i[0] in seplayer_list_21:
                                    sereport_table_21_changed_4.remove(i)
                            for i in range(len(seoutcome21_list)):
                                for j in range(1, (len(seoutcome21_list) - i)):
                                    if (
                                        seoutcome21_list[i][0]
                                        == seoutcome21_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome21_list[i + j][1] == 1:
                                            seoutcome21_list[
                                                i + j
                                            ] = sereport_table_21_changed_1[0]
                                            sereport_table_21_changed_1.remove(
                                                sereport_table_21_changed_1[0]
                                            )
                                        elif seoutcome21_list[i + j][1] == 2:
                                            seoutcome21_list[
                                                i + j
                                            ] = sereport_table_21_changed_2[0]
                                            sereport_table_21_changed_2.remove(
                                                sereport_table_21_changed_2[0]
                                            )
                                        elif seoutcome21_list[i + j][1] == 4:
                                            seoutcome21_list[
                                                i + j
                                            ] = sereport_table_21_changed_4[0]
                                            sereport_table_21_changed_4.remove(
                                                sereport_table_21_changed_4[0]
                                            )
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
                            seplayer_list_22 = []
                            for i in seoutcome22_list:
                                if i[0] != 0:
                                    seplayer_list_22.append(i[0])
                            sereport_table_22_changed_1 = sereport_table_1[6:]
                            sereport_table_22_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_22_changed_1:
                                if i[0] in seplayer_list_22:
                                    sereport_table_22_changed_1.remove(i)
                            for i in sereport_table_22_changed_4:
                                if i[0] in seplayer_list_22:
                                    sereport_table_22_changed_4.remove(i)
                            for i in range(len(seoutcome22_list)):
                                for j in range(1, (len(seoutcome22_list) - i)):
                                    if (
                                        seoutcome22_list[i][0]
                                        == seoutcome22_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome22_list[i + j][1] == 1:
                                            seoutcome22_list[
                                                i + j
                                            ] = sereport_table_22_changed_1[0]
                                            sereport_table_22_changed_1.remove(
                                                sereport_table_22_changed_1[0]
                                            )
                                        elif seoutcome22_list[i + j][1] == 4:
                                            seoutcome22_list[
                                                i + j
                                            ] = sereport_table_22_changed_4[0]
                                            sereport_table_22_changed_4.remove(
                                                sereport_table_22_changed_4[0]
                                            )
                            for i in seoutcome22_list:
                                sevalue_22 = sevalue_22 + i[3]
                            # outcome for 5*2
                            sevalue_23 = 0
                            seoutcome23_list = [
                                sereport_table_5[0],
                                sereport_table_5[1],
                            ]
                            seplayer_list_23 = []
                            for i in seoutcome23_list:
                                if i[0] != 0:
                                    seplayer_list_23.append(i[0])
                            sereport_table_23_changed_5 = sereport_table_5[2:]
                            for i in sereport_table_23_changed_5:
                                if i[0] in seplayer_list_23:
                                    sereport_table_23_changed_5.remove(i)
                            for i in range(len(seoutcome23_list)):
                                for j in range(1, (len(seoutcome23_list) - i)):
                                    if (
                                        seoutcome23_list[i][0]
                                        == seoutcome23_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome23_list[i + j][1] == 5:
                                            seoutcome23_list[
                                                i + j
                                            ] = sereport_table_23_changed_5[0]
                                            sereport_table_23_changed_5.remove(
                                                sereport_table_23_changed_5[0]
                                            )
                            for i in seoutcome23_list:
                                sevalue_23 = sevalue_23 + i[3]
                            # outcome for 5+4+1
                            sevalue_24 = 0
                            seoutcome24_list = [
                                sereport_table_5[0],
                                sereport_table_4[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_24 = []
                            for i in seoutcome24_list:
                                if i[0] != 0:
                                    seplayer_list_24.append(i[0])
                            sereport_table_24_changed_1 = sereport_table_1[1:]
                            sereport_table_24_changed_4 = sereport_table_4[1:]
                            sereport_table_24_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_24_changed_1:
                                if i[0] in seplayer_list_24:
                                    sereport_table_24_changed_1.remove(i)
                            for i in sereport_table_24_changed_4:
                                if i[0] in seplayer_list_24:
                                    sereport_table_24_changed_4.remove(i)
                            for i in sereport_table_24_changed_5:
                                if i[0] in seplayer_list_24:
                                    sereport_table_24_changed_5.remove(i)
                            for i in range(len(seoutcome24_list)):
                                for j in range(1, (len(seoutcome24_list) - i)):
                                    if (
                                        seoutcome24_list[i][0]
                                        == seoutcome24_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome24_list[i + j][1] == 1:
                                            seoutcome24_list[
                                                i + j
                                            ] = sereport_table_24_changed_1[0]
                                            sereport_table_24_changed_1.remove(
                                                sereport_table_24_changed_1[0]
                                            )
                                        elif seoutcome24_list[i + j][1] == 4:
                                            seoutcome24_list[
                                                i + j
                                            ] = sereport_table_24_changed_4[0]
                                            sereport_table_24_changed_4.remove(
                                                sereport_table_24_changed_4[0]
                                            )
                                        elif seoutcome24_list[i + j][1] == 5:
                                            seoutcome24_list[
                                                i + j
                                            ] = sereport_table_24_changed_5[0]
                                            sereport_table_24_changed_5.remove(
                                                sereport_table_24_changed_5[0]
                                            )
                            for i in seoutcome24_list:
                                sevalue_24 = sevalue_24 + i[3]
                            # outcome for 5+3+2
                            sevalue_25 = 0
                            seoutcome25_list = [
                                sereport_table_5[0],
                                sereport_table_3[0],
                                sereport_table_2[0],
                            ]
                            seplayer_list_25 = []
                            for i in seoutcome25_list:
                                if i[0] != 0:
                                    seplayer_list_25.append(i[0])
                            sereport_table_25_changed_2 = sereport_table_2[1:]
                            sereport_table_25_changed_3 = sereport_table_3[1:]
                            sereport_table_25_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_25_changed_2:
                                if i[0] in seplayer_list_25:
                                    sereport_table_25_changed_2.remove(i)
                            for i in sereport_table_25_changed_3:
                                if i[0] in seplayer_list_25:
                                    sereport_table_25_changed_3.remove(i)
                            for i in sereport_table_25_changed_5:
                                if i[0] in seplayer_list_25:
                                    sereport_table_25_changed_5.remove(i)
                            for i in range(len(seoutcome25_list)):
                                for j in range(1, (len(seoutcome25_list) - i)):
                                    if (
                                        seoutcome25_list[i][0]
                                        == seoutcome25_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome25_list[i + j][1] == 2:
                                            seoutcome25_list[
                                                i + j
                                            ] = sereport_table_25_changed_2[0]
                                            sereport_table_25_changed_2.remove(
                                                sereport_table_25_changed_2[0]
                                            )
                                        elif seoutcome25_list[i + j][1] == 3:
                                            seoutcome25_list[
                                                i + j
                                            ] = sereport_table_25_changed_3[0]
                                            sereport_table_25_changed_3.remove(
                                                sereport_table_25_changed_3[0]
                                            )
                                        elif seoutcome25_list[i + j][1] == 5:
                                            seoutcome25_list[
                                                i + j
                                            ] = sereport_table_25_changed_5[0]
                                            sereport_table_25_changed_5.remove(
                                                sereport_table_25_changed_5[0]
                                            )
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
                            seplayer_list_26 = []
                            for i in seoutcome26_list:
                                if i[0] != 0:
                                    seplayer_list_26.append(i[0])
                            sereport_table_26_changed_1 = sereport_table_1[2:]
                            sereport_table_26_changed_3 = sereport_table_3[1:]
                            sereport_table_26_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_26_changed_1:
                                if i[0] in seplayer_list_26:
                                    sereport_table_26_changed_1.remove(i)
                            for i in sereport_table_26_changed_3:
                                if i[0] in seplayer_list_26:
                                    sereport_table_26_changed_3.remove(i)
                            for i in sereport_table_26_changed_5:
                                if i[0] in seplayer_list_26:
                                    sereport_table_26_changed_5.remove(i)
                            for i in range(len(seoutcome26_list)):
                                for j in range(1, (len(seoutcome26_list) - i)):
                                    if (
                                        seoutcome26_list[i][0]
                                        == seoutcome26_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome26_list[i + j][1] == 1:
                                            seoutcome26_list[
                                                i + j
                                            ] = sereport_table_26_changed_1[0]
                                            sereport_table_26_changed_1.remove(
                                                sereport_table_26_changed_1[0]
                                            )
                                        elif seoutcome26_list[i + j][1] == 3:
                                            seoutcome26_list[
                                                i + j
                                            ] = sereport_table_26_changed_3[0]
                                            sereport_table_26_changed_3.remove(
                                                sereport_table_26_changed_3[0]
                                            )
                                        elif seoutcome26_list[i + j][1] == 5:
                                            seoutcome26_list[
                                                i + j
                                            ] = sereport_table_26_changed_5[0]
                                            sereport_table_26_changed_5.remove(
                                                sereport_table_26_changed_5[0]
                                            )
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
                            seplayer_list_27 = []
                            for i in seoutcome27_list:
                                if i[0] != 0:
                                    seplayer_list_27.append(i[0])
                            sereport_table_27_changed_1 = sereport_table_1[1:]
                            sereport_table_27_changed_2 = sereport_table_2[2:]
                            sereport_table_27_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_27_changed_1:
                                if i[0] in seplayer_list_27:
                                    sereport_table_27_changed_1.remove(i)
                            for i in sereport_table_27_changed_2:
                                if i[0] in seplayer_list_27:
                                    sereport_table_27_changed_2.remove(i)
                            for i in sereport_table_27_changed_5:
                                if i[0] in seplayer_list_27:
                                    sereport_table_27_changed_5.remove(i)
                            for i in range(len(seoutcome27_list)):
                                for j in range(1, (len(seoutcome27_list) - i)):
                                    if (
                                        seoutcome27_list[i][0]
                                        == seoutcome27_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome27_list[i + j][1] == 1:
                                            seoutcome27_list[
                                                i + j
                                            ] = sereport_table_27_changed_1[0]
                                            sereport_table_27_changed_1.remove(
                                                sereport_table_27_changed_1[0]
                                            )
                                        elif seoutcome27_list[i + j][1] == 2:
                                            seoutcome27_list[
                                                i + j
                                            ] = sereport_table_27_changed_2[0]
                                            sereport_table_27_changed_2.remove(
                                                sereport_table_27_changed_2[0]
                                            )
                                        elif seoutcome27_list[i + j][1] == 5:
                                            seoutcome27_list[
                                                i + j
                                            ] = sereport_table_27_changed_5[0]
                                            sereport_table_27_changed_5.remove(
                                                sereport_table_27_changed_5[0]
                                            )
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
                            seplayer_list_28 = []
                            for i in seoutcome28_list:
                                if i[0] != 0:
                                    seplayer_list_28.append(i[0])
                            sereport_table_28_changed_1 = sereport_table_1[3:]
                            sereport_table_28_changed_2 = sereport_table_2[1:]
                            sereport_table_28_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_28_changed_1:
                                if i[0] in seplayer_list_28:
                                    sereport_table_28_changed_1.remove(i)
                            for i in sereport_table_28_changed_2:
                                if i[0] in seplayer_list_28:
                                    sereport_table_28_changed_2.remove(i)
                            for i in sereport_table_28_changed_5:
                                if i[0] in seplayer_list_28:
                                    sereport_table_28_changed_5.remove(i)
                            for i in range(len(seoutcome28_list)):
                                for j in range(1, (len(seoutcome28_list) - i)):
                                    if (
                                        seoutcome28_list[i][0]
                                        == seoutcome28_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome28_list[i + j][1] == 1:
                                            seoutcome28_list[
                                                i + j
                                            ] = sereport_table_28_changed_1[0]
                                            sereport_table_28_changed_1.remove(
                                                sereport_table_28_changed_1[0]
                                            )
                                        elif seoutcome28_list[i + j][1] == 2:
                                            seoutcome28_list[
                                                i + j
                                            ] = sereport_table_28_changed_2[0]
                                            sereport_table_28_changed_2.remove(
                                                sereport_table_28_changed_2[0]
                                            )
                                        elif seoutcome28_list[i + j][1] == 5:
                                            seoutcome28_list[
                                                i + j
                                            ] = sereport_table_28_changed_5[0]
                                            sereport_table_28_changed_5.remove(
                                                sereport_table_28_changed_5[0]
                                            )
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
                            seplayer_list_29 = []
                            for i in seoutcome29_list:
                                if i[0] != 0:
                                    seplayer_list_29.append(i[0])
                            sereport_table_29_changed_1 = sereport_table_1[5:]
                            sereport_table_29_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_29_changed_1:
                                if i[0] in seplayer_list_29:
                                    sereport_table_29_changed_1.remove(i)
                            for i in sereport_table_29_changed_5:
                                if i[0] in seplayer_list_29:
                                    sereport_table_29_changed_5.remove(i)
                            for i in range(len(seoutcome29_list)):
                                for j in range(1, (len(seoutcome29_list) - i)):
                                    if (
                                        seoutcome29_list[i][0]
                                        == seoutcome29_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome29_list[i + j][1] == 1:
                                            seoutcome29_list[
                                                i + j
                                            ] = sereport_table_29_changed_1[0]
                                            sereport_table_29_changed_1.remove(
                                                sereport_table_29_changed_1[0]
                                            )
                                        elif seoutcome29_list[i + j][1] == 5:
                                            seoutcome29_list[
                                                i + j
                                            ] = sereport_table_29_changed_5[0]
                                            sereport_table_29_changed_5.remove(
                                                sereport_table_29_changed_5[0]
                                            )
                            for i in seoutcome29_list:
                                sevalue_29 = sevalue_29 + i[3]
                            # outcome for 6+4
                            sevalue_30 = 0
                            seoutcome30_list = [
                                sereport_table_6[0],
                                sereport_table_4[0],
                            ]
                            seplayer_list_30 = []
                            for i in seoutcome30_list:
                                if i[0] != 0:
                                    seplayer_list_30.append(i[0])
                            sereport_table_30_changed_4 = sereport_table_4[1:]
                            sereport_table_30_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_30_changed_4:
                                if i[0] in seplayer_list_30:
                                    sereport_table_30_changed_4.remove(i)
                            for i in sereport_table_30_changed_6:
                                if i[0] in seplayer_list_30:
                                    sereport_table_30_changed_6.remove(i)
                            for i in range(len(seoutcome30_list)):
                                for j in range(1, (len(seoutcome30_list) - i)):
                                    if (
                                        seoutcome30_list[i][0]
                                        == seoutcome30_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome30_list[i + j][1] == 4:
                                            seoutcome30_list[
                                                i + j
                                            ] = sereport_table_30_changed_4[0]
                                            sereport_table_30_changed_4.remove(
                                                sereport_table_30_changed_4[0]
                                            )
                                        elif seoutcome30_list[i + j][1] == 6:
                                            seoutcome30_list[
                                                i + j
                                            ] = sereport_table_30_changed_6[0]
                                            sereport_table_30_changed_6.remove(
                                                sereport_table_30_changed_6[0]
                                            )
                            for i in seoutcome30_list:
                                sevalue_30 = sevalue_30 + i[3]
                            # outcome for 6+3+1
                            sevalue_31 = 0
                            seoutcome31_list = [
                                sereport_table_6[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_31 = []
                            for i in seoutcome31_list:
                                if i[0] != 0:
                                    seplayer_list_31.append(i[0])
                            sereport_table_31_changed_1 = sereport_table_1[1:]
                            sereport_table_31_changed_3 = sereport_table_3[1:]
                            sereport_table_31_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_31_changed_1:
                                if i[0] in seplayer_list_31:
                                    sereport_table_31_changed_1.remove(i)
                            for i in sereport_table_31_changed_3:
                                if i[0] in seplayer_list_31:
                                    sereport_table_31_changed_3.remove(i)
                            for i in sereport_table_31_changed_6:
                                if i[0] in seplayer_list_31:
                                    sereport_table_31_changed_6.remove(i)
                            for i in range(len(seoutcome31_list)):
                                for j in range(1, (len(seoutcome31_list) - i)):
                                    if (
                                        seoutcome31_list[i][0]
                                        == seoutcome31_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome31_list[i + j][1] == 1:
                                            seoutcome31_list[
                                                i + j
                                            ] = sereport_table_31_changed_1[0]
                                            sereport_table_31_changed_1.remove(
                                                sereport_table_31_changed_1[0]
                                            )
                                        elif seoutcome31_list[i + j][1] == 3:
                                            seoutcome31_list[
                                                i + j
                                            ] = sereport_table_31_changed_3[0]
                                            sereport_table_31_changed_3.remove(
                                                sereport_table_31_changed_3[0]
                                            )
                                        elif seoutcome31_list[i + j][1] == 6:
                                            seoutcome31_list[
                                                i + j
                                            ] = sereport_table_31_changed_6[0]
                                            sereport_table_31_changed_6.remove(
                                                sereport_table_31_changed_6[0]
                                            )
                            for i in seoutcome31_list:
                                sevalue_31 = sevalue_31 + i[3]
                            # outcome for 6+2*2
                            sevalue_32 = 0
                            seoutcome32_list = [
                                sereport_table_6[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                            ]
                            seplayer_list_32 = []
                            for i in seoutcome32_list:
                                if i[0] != 0:
                                    seplayer_list_32.append(i[0])
                            sereport_table_32_changed_2 = sereport_table_2[2:]
                            sereport_table_32_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_32_changed_2:
                                if i[0] in seplayer_list_32:
                                    sereport_table_32_changed_2.remove(i)
                            for i in sereport_table_32_changed_6:
                                if i[0] in seplayer_list_32:
                                    sereport_table_32_changed_6.remove(i)
                            for i in range(len(seoutcome32_list)):
                                for j in range(1, (len(seoutcome32_list) - i)):
                                    if (
                                        seoutcome32_list[i][0]
                                        == seoutcome32_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome32_list[i + j][1] == 2:
                                            seoutcome32_list[
                                                i + j
                                            ] = sereport_table_32_changed_2[0]
                                            sereport_table_32_changed_2.remove(
                                                sereport_table_32_changed_2[0]
                                            )
                                        elif seoutcome32_list[i + j][1] == 6:
                                            seoutcome32_list[
                                                i + j
                                            ] = sereport_table_32_changed_6[0]
                                            sereport_table_32_changed_6.remove(
                                                sereport_table_32_changed_6[0]
                                            )
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
                            seplayer_list_33 = []
                            for i in seoutcome33_list:
                                if i[0] != 0:
                                    seplayer_list_33.append(i[0])
                            sereport_table_33_changed_1 = sereport_table_1[2:]
                            sereport_table_33_changed_2 = sereport_table_2[1:]
                            sereport_table_33_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_33_changed_1:
                                if i[0] in seplayer_list_33:
                                    sereport_table_33_changed_1.remove(i)
                            for i in sereport_table_33_changed_2:
                                if i[0] in seplayer_list_33:
                                    sereport_table_33_changed_2.remove(i)
                            for i in sereport_table_33_changed_6:
                                if i[0] in seplayer_list_33:
                                    sereport_table_33_changed_6.remove(i)
                            for i in range(len(seoutcome33_list)):
                                for j in range(1, (len(seoutcome33_list) - i)):
                                    if (
                                        seoutcome33_list[i][0]
                                        == seoutcome33_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome33_list[i + j][1] == 1:
                                            seoutcome33_list[
                                                i + j
                                            ] = sereport_table_33_changed_1[0]
                                            sereport_table_33_changed_1.remove(
                                                sereport_table_33_changed_1[0]
                                            )
                                        elif seoutcome33_list[i + j][1] == 2:
                                            seoutcome33_list[
                                                i + j
                                            ] = sereport_table_33_changed_2[0]
                                            sereport_table_33_changed_2.remove(
                                                sereport_table_33_changed_2[0]
                                            )
                                        elif seoutcome33_list[i + j][1] == 6:
                                            seoutcome33_list[
                                                i + j
                                            ] = sereport_table_33_changed_6[0]
                                            sereport_table_33_changed_6.remove(
                                                sereport_table_33_changed_6[0]
                                            )
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
                            seplayer_list_34 = []
                            for i in seoutcome34_list:
                                if i[0] != 0:
                                    seplayer_list_34.append(i[0])
                            sereport_table_34_changed_1 = sereport_table_1[4:]
                            sereport_table_34_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_34_changed_1:
                                if i[0] in seplayer_list_34:
                                    sereport_table_34_changed_1.remove(i)
                            for i in sereport_table_34_changed_6:
                                if i[0] in seplayer_list_34:
                                    sereport_table_34_changed_6.remove(i)
                            for i in range(len(seoutcome34_list)):
                                for j in range(1, (len(seoutcome34_list) - i)):
                                    if (
                                        seoutcome34_list[i][0]
                                        == seoutcome34_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome34_list[i + j][1] == 1:
                                            seoutcome34_list[
                                                i + j
                                            ] = sereport_table_34_changed_1[0]
                                            sereport_table_34_changed_1.remove(
                                                sereport_table_34_changed_1[0]
                                            )
                                        elif seoutcome34_list[i + j][1] == 6:
                                            seoutcome32_list[
                                                i + j
                                            ] = sereport_table_34_changed_6[0]
                                            sereport_table_34_changed_6.remove(
                                                sereport_table_34_changed_6[0]
                                            )
                            for i in seoutcome34_list:
                                sevalue_34 = sevalue_34 + i[3]
                            # outcome for 7+3
                            sevalue_35 = 0
                            seoutcome35_list = [
                                sereport_table_7[0],
                                sereport_table_3[0],
                            ]
                            seplayer_list_35 = []
                            for i in seoutcome35_list:
                                if i[0] != 0:
                                    seplayer_list_35.append(i[0])
                            sereport_table_35_changed_3 = sereport_table_3[1:]
                            sereport_table_35_changed_7 = sereport_table_7[1:]
                            for i in sereport_table_35_changed_3:
                                if i[0] in seplayer_list_35:
                                    sereport_table_35_changed_3.remove(i)
                            for i in sereport_table_35_changed_7:
                                if i[0] in seplayer_list_35:
                                    sereport_table_35_changed_7.remove(i)
                            for i in range(len(seoutcome35_list)):
                                for j in range(1, (len(seoutcome35_list) - i)):
                                    if (
                                        seoutcome35_list[i][0]
                                        == seoutcome35_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome35_list[i + j][1] == 3:
                                            seoutcome35_list[
                                                i + j
                                            ] = sereport_table_35_changed_3[0]
                                            sereport_table_35_changed_3.remove(
                                                sereport_table_35_changed_3[0]
                                            )
                                        elif seoutcome35_list[i + j][1] == 7:
                                            seoutcome35_list[
                                                i + j
                                            ] = sereport_table_35_changed_7[0]
                                            sereport_table_35_changed_7.remove(
                                                sereport_table_35_changed_7[0]
                                            )
                            for i in seoutcome35_list:
                                sevalue_35 = sevalue_35 + i[3]
                            # outcome for 7+2+1
                            sevalue_36 = 0
                            seoutcome36_list = [
                                sereport_table_7[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_36 = []
                            for i in seoutcome36_list:
                                if i[0] != 0:
                                    seplayer_list_36.append(i[0])
                            sereport_table_36_changed_1 = sereport_table_1[2:]
                            sereport_table_36_changed_2 = sereport_table_2[1:]
                            sereport_table_36_changed_7 = sereport_table_7[1:]
                            for i in sereport_table_36_changed_1:
                                if i[0] in seplayer_list_36:
                                    sereport_table_36_changed_1.remove(i)
                            for i in sereport_table_36_changed_2:
                                if i[0] in seplayer_list_36:
                                    sereport_table_36_changed_2.remove(i)
                            for i in sereport_table_36_changed_7:
                                if i[0] in seplayer_list_36:
                                    sereport_table_36_changed_7.remove(i)
                            for i in range(len(seoutcome36_list)):
                                for j in range(1, (len(seoutcome36_list) - i)):
                                    if (
                                        seoutcome36_list[i][0]
                                        == seoutcome36_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome36_list[i + j][1] == 1:
                                            seoutcome36_list[
                                                i + j
                                            ] = sereport_table_36_changed_1[0]
                                            sereport_table_36_changed_1.remove(
                                                sereport_table_36_changed_1[0]
                                            )
                                        elif seoutcome36_list[i + j][1] == 2:
                                            seoutcome36_list[
                                                i + j
                                            ] = sereport_table_36_changed_2[0]
                                            sereport_table_36_changed_2.remove(
                                                sereport_table_36_changed_2[0]
                                            )
                                        elif seoutcome36_list[i + j][1] == 7:
                                            seoutcome36_list[
                                                i + j
                                            ] = sereport_table_36_changed_7[0]
                                            sereport_table_36_changed_7.remove(
                                                sereport_table_36_changed_7[0]
                                            )
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
                            seplayer_list_37 = []
                            for i in seoutcome37_list:
                                if i[0] != 0:
                                    seplayer_list_37.append(i[0])
                            sereport_table_37_changed_1 = sereport_table_1[3:]
                            sereport_table_37_changed_7 = sereport_table_7[1:]
                            for i in sereport_table_37_changed_1:
                                if i[0] in seplayer_list_37:
                                    sereport_table_37_changed_1.remove(i)
                            for i in sereport_table_37_changed_7:
                                if i[0] in seplayer_list_37:
                                    sereport_table_37_changed_7.remove(i)
                            for i in range(len(seoutcome37_list)):
                                for j in range(1, (len(seoutcome37_list) - i)):
                                    if (
                                        seoutcome37_list[i][0]
                                        == seoutcome37_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome37_list[i + j][1] == 1:
                                            seoutcome37_list[
                                                i + j
                                            ] = sereport_table_37_changed_1[0]
                                            sereport_table_37_changed_1.remove(
                                                sereport_table_37_changed_1[0]
                                            )
                                        elif outcome37_list[i + j][1] == 7:
                                            seoutcome37_list[
                                                i + j
                                            ] = sereport_table_37_changed_7[0]
                                            sereport_table_37_changed_7.remove(
                                                sereport_table_37_changed_7[0]
                                            )
                            for i in seoutcome37_list:
                                sevalue_37 = sevalue_37 + i[3]
                            # outcome for 8+2
                            sevalue_38 = 0
                            seoutcome38_list = [
                                sereport_table_8[0],
                                sereport_table_2[0],
                            ]
                            seplayer_list_38 = []
                            for i in seoutcome38_list:
                                if i[0] != 0:
                                    seplayer_list_38.append(i[0])
                            sereport_table_38_changed_2 = sereport_table_2[1:]
                            sereport_table_38_changed_8 = sereport_table_8[1:]
                            for i in sereport_table_38_changed_2:
                                if i[0] in seplayer_list_38:
                                    sereport_table_38_changed_2.remove(i)
                            for i in sereport_table_38_changed_8:
                                if i[0] in seplayer_list_38:
                                    sereport_table_38_changed_8.remove(i)
                            for i in range(len(seoutcome38_list)):
                                for j in range(1, (len(seoutcome38_list) - i)):
                                    if (
                                        seoutcome38_list[i][0]
                                        == seoutcome38_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome38_list[i + j][1] == 2:
                                            seoutcome38_list[
                                                i + j
                                            ] = sereport_table_38_changed_2[0]
                                            sereport_table_38_changed_2.remove(
                                                sereport_table_38_changed_2[0]
                                            )
                                        elif seoutcome38_list[i + j][1] == 8:
                                            seoutcome38_list[
                                                i + j
                                            ] = sereport_table_38_changed_8[0]
                                            sereport_table_38_changed_8.remove(
                                                sereport_table_38_changed_8[0]
                                            )
                            for i in seoutcome38_list:
                                sevalue_38 = sevalue_38 + i[3]
                            # outcome for 8+1*2
                            sevalue_39 = 0
                            seoutcome39_list = [
                                sereport_table_8[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            seplayer_list_39 = []
                            for i in seoutcome39_list:
                                if i[0] != 0:
                                    seplayer_list_39.append(i[0])
                            sereport_table_39_changed_1 = sereport_table_1[2:]
                            sereport_table_39_changed_8 = sereport_table_8[1:]
                            for i in sereport_table_39_changed_1:
                                if i[0] in seplayer_list_39:
                                    sereport_table_39_changed_1.remove(i)
                            for i in sereport_table_39_changed_8:
                                if i[0] in seplayer_list_39:
                                    sereport_table_39_changed_8.remove(i)
                            for i in range(len(seoutcome39_list)):
                                for j in range(1, (len(seoutcome39_list) - i)):
                                    if (
                                        seoutcome39_list[i][0]
                                        == seoutcome39_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome39_list[i + j][1] == 1:
                                            seoutcome39_list[
                                                i + j
                                            ] = sereport_table_39_changed_1[0]
                                            sereport_table_39_changed_1.remove(
                                                sereport_table_39_changed_1[0]
                                            )
                                        elif seoutcome39_list[i + j][1] == 8:
                                            seoutcome39_list[
                                                i + j
                                            ] = sereport_table_39_changed_8[0]
                                            sereport_table_39_changed_8.remove(
                                                sereport_table_39_changed_8[0]
                                            )
                            for i in seoutcome39_list:
                                sevalue_39 = sevalue_39 + i[3]
                            # outcome for 9+1
                            sevalue_40 = 0
                            seoutcome40_list = [
                                sereport_table_9[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_40 = []
                            for i in seoutcome40_list:
                                if i[0] != 0:
                                    seplayer_list_40.append(i[0])
                            sereport_table_40_changed_1 = sereport_table_1[1:]
                            sereport_table_40_changed_9 = sereport_table_9[1:]
                            for i in sereport_table_40_changed_1:
                                if i[0] in seplayer_list_40:
                                    sereport_table_40_changed_1.remove(i)
                            for i in sereport_table_40_changed_9:
                                if i[0] in seplayer_list_40:
                                    sereport_table_40_changed_9.remove(i)
                            for i in range(len(seoutcome40_list)):
                                for j in range(1, (len(seoutcome40_list) - i)):
                                    if (
                                        seoutcome40_list[i][0]
                                        == seoutcome40_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome40_list[i + j][1] == 1:
                                            seoutcome40_list[
                                                i + j
                                            ] = sereport_table_40_changed_1[0]
                                            sereport_table_40_changed_1.remove(
                                                sereport_table_40_changed_1[0]
                                            )
                                        elif seoutcome40_list[i + j][1] == 9:
                                            seoutcome40_list[
                                                i + j
                                            ] = sereport_table_40_changed_9[0]
                                            sereport_table_40_changed_9.remove(
                                                sereport_table_40_changed_9[0]
                                            )
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
    player_list_1 = []
    for i in random_outcome1_list:
        if i[0] != 0:
            player_list_1.append(i[0])
    random_table_1_changed = random_table_1[9:]
    for i in random_table_1_changed:
        if i[0] in player_list_1:
            random_table_1_changed.remove(i)
    for i in range(len(random_outcome1_list)):
        for j in range(1, (len(random_outcome1_list) - i)):
            if random_outcome1_list[i][0] == random_outcome1_list[i + j][0] != 0:
                random_outcome1_list[i + j] = random_table_1_changed[0]
                random_table_1_changed.remove(random_table_1_changed[0])
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
    player_list_2 = []
    for i in random_outcome2_list:
        if i[0] != 0:
            player_list_2.append(i[0])
    random_table_2_changed = random_table_2[5:]
    for i in random_table_2_changed:
        if i[0] in player_list_2:
            random_table_2_changed.remove(i)
    for i in range(len(random_outcome2_list)):
        for j in range(1, (len(random_outcome2_list) - i)):
            if random_outcome2_list[i][0] == random_outcome2_list[i + j][0] != 0:
                random_outcome2_list[i + j] = random_table_2_changed[0]
                random_table_2_changed.remove(random_table_2_changed[0])
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
    player_list_3 = []
    for i in random_outcome3_list:
        if i[0] != 0:
            player_list_3.append(i[0])
    random_table_3_changed_1 = random_table_1[2:]
    random_table_3_changed_2 = random_table_2[4:]
    for i in random_table_3_changed_1:
        if i[0] in player_list_3:
            random_table_3_changed_1.remove(i)
    for i in random_table_3_changed_2:
        if i[0] in player_list_3:
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
    player_list_4 = []
    for i in random_outcome4_list:
        if i[0] != 0:
            player_list_4.append(i[0])
    random_table_4_changed_1 = random_table_1[4:]
    random_table_4_changed_2 = random_table_2[3:]
    for i in random_table_4_changed_1:
        if i[0] in player_list_4:
            random_table_4_changed_1.remove(i)
    for i in random_table_4_changed_2:
        if i[0] in player_list_4:
            random_table_4_changed_2.remove(i)
    for i in range(len(random_outcome4_list)):
        for j in range(1, (len(random_outcome4_list) - i)):
            if random_outcome4_list[i][0] == random_outcome4_list[i + j][0] != 0:
                if random_outcome4_list[i + j][1] == 1:
                    random_outcome4_list[i + j] = random_table_4_changed_1[0]
                    random_table_4_changed_1.remove(random_table_4_changed_1[0])
                elif random_outcome4_list[i + j][1] == 2:
                    random_outcome4_list[i + j] = random_table_4_changed_2[0]
                    random_table_4_changed_2.remove(random_table_4_changed_2[0])
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
    player_list_5 = []
    for i in random_outcome5_list:
        if i[0] != 0:
            player_list_5.append(i[0])
    random_table_5_changed_1 = random_table_1[6:]
    random_table_5_changed_2 = random_table_2[2:]
    for i in random_table_5_changed_1:
        if i[0] in player_list_5:
            random_table_5_changed_1.remove(i)
    for i in random_table_5_changed_2:
        if i[0] in player_list_5:
            random_table_5_changed_2.remove(i)
    for i in range(len(random_outcome5_list)):
        for j in range(1, (len(random_outcome5_list) - i)):
            if random_outcome5_list[i][0] == random_outcome5_list[i + j][0] != 0:
                if random_outcome5_list[i + j][1] == 1:
                    random_outcome5_list[i + j] = random_table_5_changed_1[0]
                    random_table_5_changed_1.remove(random_table_5_changed_1[0])
                elif random_outcome5_list[i + j][1] == 2:
                    random_outcome5_list[i + j] = random_table_5_changed_2[0]
                    random_table_5_changed_2.remove(random_table_5_changed_2[0])
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
    player_list_6 = []
    for i in random_outcome6_list:
        if i[0] != 0:
            player_list_6.append(i[0])
    random_table_6_changed_1 = random_table_1[8:]
    random_table_6_changed_2 = random_table_2[1:]
    for i in random_table_6_changed_1:
        if i[0] in player_list_6:
            random_table_6_changed_1.remove(i)
    for i in random_table_6_changed_2:
        if i[0] in player_list_6:
            random_table_6_changed_2.remove(i)
    for i in range(len(random_outcome6_list)):
        for j in range(1, (len(random_outcome6_list) - i)):
            if random_outcome6_list[i][0] == random_outcome6_list[i + j][0] != 0:
                if random_outcome6_list[i + j][1] == 1:
                    random_outcome6_list[i + j] = random_table_6_changed_1[0]
                    random_table_6_changed_1.remove(random_table_6_changed_1[0])
                elif random_outcome6_list[i + j][1] == 2:
                    random_outcome6_list[i + j] = random_table_6_changed_2[0]
                    random_table_6_changed_2.remove(random_table_6_changed_2[0])
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
    player_list_7 = []
    for i in random_outcome7_list:
        if i[0] != 0:
            player_list_7.append(i[0])
    random_table_7_changed_1 = random_table_1[1:]
    random_table_7_changed_3 = random_table_3[3:]
    for i in random_table_7_changed_1:
        if i[0] in player_list_7:
            random_table_7_changed_1.remove(i)
    for i in random_table_7_changed_3:
        if i[0] in player_list_7:
            random_table_7_changed_3.remove(i)
    for i in range(len(random_outcome7_list)):
        for j in range(1, (len(random_outcome7_list) - i)):
            if random_outcome7_list[i][0] == random_outcome7_list[i + j][0] != 0:
                if random_outcome7_list[i + j][1] == 1:
                    random_outcome7_list[i + j] = random_table_7_changed_1[0]
                    random_table_7_changed_1.remove(random_table_7_changed_1[0])
                elif random_outcome7_list[i + j][1] == 3:
                    random_outcome7_list[i + j] = random_table_7_changed_3[0]
                    random_table_7_changed_3.remove(random_table_7_changed_3[0])
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
    player_list_8 = []
    for i in random_outcome8_list:
        if i[0] != 0:
            player_list_8.append(i[0])
    random_table_8_changed_2 = random_table_2[2:]
    random_table_8_changed_3 = random_table_3[2:]
    for i in random_table_8_changed_2:
        if i[0] in player_list_8:
            random_table_8_changed_2.remove(i)
    for i in random_table_8_changed_3:
        if i[0] in player_list_8:
            random_table_8_changed_3.remove(i)
    for i in range(len(random_outcome8_list)):
        for j in range(1, (len(random_outcome8_list) - i)):
            if random_outcome8_list[i][0] == random_outcome8_list[i + j][0] != 0:
                if random_outcome8_list[i + j][1] == 2:
                    random_outcome8_list[i + j] = random_table_8_changed_2[0]
                    random_table_8_changed_2.remove(random_table_8_changed_2[0])
                elif random_outcome8_list[i + j][1] == 3:
                    random_outcome8_list[i + j] = random_table_8_changed_3[0]
                    random_table_8_changed_3.remove(random_table_8_changed_3[0])
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
    player_list_9 = []
    for i in random_outcome9_list:
        if i[0] != 0:
            player_list_9.append(i[0])
    random_table_9_changed_1 = random_table_1[2:]
    random_table_9_changed_2 = random_table_2[1:]
    random_table_9_changed_3 = random_table_3[2:]
    for i in random_table_9_changed_1:
        if i[0] in player_list_9:
            random_table_9_changed_1.remove(i)
    for i in random_table_9_changed_2:
        if i[0] in player_list_9:
            random_table_9_changed_2.remove(i)
    for i in random_table_9_changed_3:
        if i[0] in player_list_9:
            random_table_9_changed_3.remove(i)
    for i in range(len(random_outcome9_list)):
        for j in range(1, (len(random_outcome9_list) - i)):
            if random_outcome9_list[i][0] == random_outcome9_list[i + j][0] != 0:
                if random_outcome9_list[i + j][1] == 1:
                    random_outcome9_list[i + j] = random_table_9_changed_1[0]
                    random_table_9_changed_1.remove(random_table_9_changed_1[0])
                elif random_outcome9_list[i + j][1] == 2:
                    random_outcome9_list[i + j] = random_table_9_changed_2[0]
                    random_table_9_changed_2.remove(random_table_9_changed_2[0])
                elif random_outcome9_list[i + j][1] == 3:
                    random_outcome9_list[i + j] = random_table_9_changed_3[0]
                    random_table_9_changed_3.remove(random_table_9_changed_3[0])
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
    player_list_10 = []
    for i in random_outcome10_list:
        if i[0] != 0:
            player_list_10.append(i[0])
    random_table_10_changed_1 = random_table_1[4:]
    random_table_10_changed_3 = random_table_3[2:]
    for i in random_table_10_changed_1:
        if i[0] in player_list_10:
            random_table_10_changed_1.remove(i)
    for i in random_table_10_changed_3:
        if i[0] in player_list_10:
            random_table_10_changed_3.remove(i)
    for i in range(len(random_outcome10_list)):
        for j in range(1, (len(random_outcome10_list) - i)):
            if random_outcome10_list[i][0] == random_outcome10_list[i + j][0] != 0:
                if random_outcome10_list[i + j][1] == 1:
                    random_outcome10_list[i + j] = random_table_10_changed_1[0]
                    random_table_10_changed_1.remove(random_table_10_changed_1[0])
                elif random_outcome10_list[i + j][1] == 3:
                    random_outcome10_list[i + j] = random_table_10_changed_3[0]
                    random_table_10_changed_3.remove(random_table_10_changed_3[0])
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
    player_list_11 = []
    for i in random_outcome11_list:
        if i[0] != 0:
            player_list_11.append(i[0])
    random_table_11_changed_1 = random_table_1[3:]
    random_table_11_changed_2 = random_table_2[2:]
    random_table_11_changed_3 = random_table_3[1:]
    for i in random_table_11_changed_1:
        if i[0] in player_list_11:
            random_table_11_changed_1.remove(i)
    for i in random_table_11_changed_2:
        if i[0] in player_list_11:
            random_table_11_changed_2.remove(i)
    for i in random_table_11_changed_3:
        if i[0] in player_list_11:
            random_table_11_changed_3.remove(i)
    for i in range(len(random_outcome11_list)):
        for j in range(1, (len(random_outcome11_list) - i)):
            if random_outcome11_list[i][0] == random_outcome11_list[i + j][0] != 0:
                if random_outcome11_list[i + j][1] == 1:
                    random_outcome11_list[i + j] = random_table_11_changed_1[0]
                    random_table_11_changed_1.remove(random_table_11_changed_1[0])
                elif random_outcome11_list[i + j][1] == 2:
                    random_outcome11_list[i + j] = random_table_11_changed_2[0]
                    random_table_11_changed_2.remove(random_table_11_changed_2[0])
                elif random_outcome11_list[i + j][1] == 3:
                    random_outcome11_list[i + j] = random_table_11_changed_3[0]
                    random_table_11_changed_3.remove(random_table_11_changed_3[0])
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
    player_list_12 = []
    for i in random_outcome12_list:
        if i[0] != 0:
            player_list_12.append(i[0])
    random_table_12_changed_1 = random_table_1[5:]
    random_table_12_changed_2 = random_table_2[1:]
    random_table_12_changed_3 = random_table_3[1:]
    for i in random_table_12_changed_1:
        if i[0] in player_list_12:
            random_table_12_changed_1.remove(i)
    for i in random_table_12_changed_2:
        if i[0] in player_list_12:
            random_table_12_changed_2.remove(i)
    for i in random_table_12_changed_3:
        if i[0] in player_list_12:
            random_table_12_changed_3.remove(i)
    for i in range(len(random_outcome12_list)):
        for j in range(1, (len(random_outcome12_list) - i)):
            if random_outcome12_list[i][0] == random_outcome12_list[i + j][0] != 0:
                if random_outcome12_list[i + j][1] == 1:
                    random_outcome12_list[i + j] = random_table_12_changed_1[0]
                    random_table_12_changed_1.remove(random_table_12_changed_1[0])
                elif random_outcome12_list[i + j][1] == 2:
                    random_outcome12_list[i + j] = random_table_12_changed_2[0]
                    random_table_12_changed_2.remove(random_table_12_changed_2[0])
                elif random_outcome12_list[i + j][1] == 3:
                    random_outcome12_list[i + j] = random_table_12_changed_3[0]
                    random_table_12_changed_3.remove(random_table_12_changed_3[0])
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
    player_list_13 = []
    for i in random_outcome13_list:
        if i[0] != 0:
            player_list_13.append(i[0])
    random_table_13_changed_1 = random_table_1[7:]
    random_table_13_changed_3 = random_table_3[1:]
    for i in random_table_13_changed_1:
        if i[0] in player_list_13:
            random_table_13_changed_1.remove(i)
    for i in random_table_13_changed_3:
        if i[0] in player_list_13:
            random_table_13_changed_3.remove(i)
    for i in range(len(random_outcome13_list)):
        for j in range(1, (len(random_outcome13_list) - i)):
            if random_outcome13_list[i][0] == random_outcome13_list[i + j][0] != 0:
                if random_outcome13_list[i + j][1] == 1:
                    random_outcome13_list[i + j] = random_table_13_changed_1[0]
                    random_table_13_changed_1.remove(random_table_13_changed_1[0])
                elif random_outcome13_list[i + j][1] == 3:
                    random_outcome13_list[i + j] = random_table_13_changed_3[0]
                    random_table_13_changed_3.remove(random_table_13_changed_3[0])
    for i in random_outcome13_list:
        random_value_13 = random_value_13 + i[3]
    # outcome for 4*2+2
    random_value_14 = 0
    random_outcome14_list = [random_table_4[0], random_table_4[1], random_table_2[0]]
    player_list_14 = []
    for i in random_outcome14_list:
        if i[0] != 0:
            player_list_14.append(i[0])
    random_table_14_changed_2 = random_table_2[1:]
    random_table_14_changed_4 = random_table_4[2:]
    for i in random_table_14_changed_2:
        if i[0] in player_list_14:
            random_table_14_changed_2.remove(i)
    for i in random_table_14_changed_4:
        if i[0] in player_list_14:
            random_table_14_changed_4.remove(i)
    for i in range(len(random_outcome14_list)):
        for j in range(1, (len(random_outcome14_list) - i)):
            if random_outcome14_list[i][0] == random_outcome14_list[i + j][0] != 0:
                if random_outcome14_list[i + j][1] == 2:
                    random_outcome14_list[i + j] = random_table_14_changed_2[0]
                    random_table_14_changed_2.remove(random_table_14_changed_2[0])
                elif random_outcome14_list[i + j][1] == 4:
                    random_outcome14_list[i + j] = random_table_14_changed_4[0]
                    random_table_14_changed_4.remove(random_table_14_changed_4[0])
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
    player_list_15 = []
    for i in random_outcome15_list:
        if i[0] != 0:
            player_list_15.append(i[0])
    random_table_15_changed_1 = random_table_1[2:]
    random_table_15_changed_4 = random_table_4[2:]
    for i in random_table_15_changed_1:
        if i[0] in player_list_15:
            random_table_15_changed_1.remove(i)
    for i in random_table_15_changed_4:
        if i[0] in player_list_15:
            random_table_15_changed_4.remove(i)
    for i in range(len(random_outcome15_list)):
        for j in range(1, (len(random_outcome15_list) - i)):
            if random_outcome15_list[i][0] == random_outcome15_list[i + j][0] != 0:
                if random_outcome15_list[i + j][1] == 1:
                    random_outcome15_list[i + j] = random_table_15_changed_1[0]
                    random_table_15_changed_1.remove(random_table_15_changed_1[0])
                elif random_outcome15_list[i + j][1] == 4:
                    random_outcome15_list[i + j] = random_table_15_changed_4[0]
                    random_table_15_changed_4.remove(random_table_15_changed_4[0])
    for i in random_outcome15_list:
        random_value_15 = random_value_15 + i[3]
    # outcome for 4+3*2
    random_value_16 = 0
    random_outcome16_list = [random_table_4[0], random_table_3[0], random_table_3[1]]
    player_list_16 = []
    for i in random_outcome16_list:
        if i[0] != 0:
            player_list_16.append(i[0])
    random_table_16_changed_3 = random_table_3[2:]
    random_table_16_changed_4 = random_table_4[1:]
    for i in random_table_16_changed_3:
        if i[0] in player_list_16:
            random_table_16_changed_3.remove(i)
    for i in random_table_16_changed_4:
        if i[0] in player_list_16:
            random_table_16_changed_4.remove(i)
    for i in range(len(random_outcome16_list)):
        for j in range(1, (len(random_outcome16_list) - i)):
            if random_outcome16_list[i][0] == random_outcome16_list[i + j][0] != 0:
                if random_outcome16_list[i + j][1] == 3:
                    random_outcome16_list[i + j] = random_table_16_changed_3[0]
                    random_table_16_changed_3.remove(random_table_16_changed_3[0])
                elif random_outcome16_list[i + j][1] == 4:
                    random_outcome16_list[i + j] = random_table_16_changed_4[0]
                    random_table_16_changed_4.remove(random_table_16_changed_4[0])
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
    player_list_17 = []
    for i in random_outcome17_list:
        if i[0] != 0:
            player_list_17.append(i[0])
    random_table_17_changed_1 = random_table_1[1:]
    random_table_17_changed_2 = random_table_2[1:]
    random_table_17_changed_3 = random_table_3[1:]
    random_table_17_changed_4 = random_table_4[1:]
    for i in random_table_17_changed_1:
        if i[0] in player_list_17:
            random_table_17_changed_1.remove(i)
    for i in random_table_17_changed_2:
        if i[0] in player_list_17:
            random_table_17_changed_2.remove(i)
    for i in random_table_17_changed_3:
        if i[0] in player_list_17:
            random_table_17_changed_3.remove(i)
    for i in random_table_17_changed_4:
        if i[0] in player_list_17:
            random_table_17_changed_4.remove(i)
    for i in range(len(random_outcome17_list)):
        for j in range(1, (len(random_outcome17_list) - i)):
            if random_outcome17_list[i][0] == random_outcome17_list[i + j][0] != 0:
                if random_outcome17_list[i + j][1] == 1:
                    random_outcome17_list[i + j] = random_table_17_changed_1[0]
                    random_table_17_changed_1.remove(random_table_17_changed_1[0])
                elif random_outcome17_list[i + j][1] == 2:
                    random_outcome17_list[i + j] = random_table_17_changed_2[0]
                    random_table_17_changed_2.remove(random_table_17_changed_2[0])
                elif random_outcome17_list[i + j][1] == 3:
                    random_outcome17_list[i + j] = random_table_17_changed_3[0]
                    random_table_17_changed_3.remove(random_table_17_changed_3[0])
                elif random_outcome17_list[i + j][1] == 4:
                    random_outcome17_list[i + j] = random_table_17_changed_4[0]
                    random_table_17_changed_4.remove(random_table_17_changed_4[0])
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
    player_list_18 = []
    for i in random_outcome18_list:
        if i[0] != 0:
            player_list_18.append(i[0])
    random_table_18_changed_1 = random_table_1[3:]
    random_table_18_changed_3 = random_table_3[1:]
    random_table_18_changed_4 = random_table_4[1:]
    for i in random_table_18_changed_1:
        if i[0] in player_list_18:
            random_table_18_changed_1.remove(i)
    for i in random_table_18_changed_3:
        if i[0] in player_list_18:
            random_table_18_changed_3.remove(i)
    for i in random_table_18_changed_4:
        if i[0] in player_list_18:
            random_table_18_changed_4.remove(i)
    for i in range(len(random_outcome18_list)):
        for j in range(1, (len(random_outcome18_list) - i)):
            if random_outcome18_list[i][0] == random_outcome18_list[i + j][0] != 0:
                if random_outcome18_list[i + j][1] == 1:
                    random_outcome18_list[i + j] = random_table_18_changed_1[0]
                    random_table_18_changed_1.remove(random_table_18_changed_1[0])
                elif random_outcome18_list[i + j][1] == 3:
                    random_outcome18_list[i + j] = random_table_18_changed_3[0]
                    random_table_18_changed_3.remove(random_table_18_changed_3[0])
                elif random_outcome18_list[i + j][1] == 4:
                    random_outcome18_list[i + j] = random_table_18_changed_4[0]
                    random_table_18_changed_4.remove(random_table_18_changed_4[0])
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
    player_list_19 = []
    for i in random_outcome19_list:
        if i[0] != 0:
            player_list_19.append(i[0])
    random_table_19_changed_2 = random_table_2[3:]
    random_table_19_changed_4 = random_table_4[1:]
    for i in random_table_19_changed_2:
        if i[0] in player_list_19:
            random_table_19_changed_2.remove(i)
    for i in random_table_19_changed_4:
        if i[0] in player_list_19:
            random_table_19_changed_4.remove(i)
    for i in range(len(random_outcome19_list)):
        for j in range(1, (len(random_outcome19_list) - i)):
            if random_outcome19_list[i][0] == random_outcome19_list[i + j][0] != 0:
                if random_outcome19_list[i + j][1] == 2:
                    random_outcome19_list[i + j] = random_table_19_changed_2[0]
                    random_table_19_changed_2.remove(random_table_19_changed_2[0])
                elif random_outcome19_list[i + j][1] == 4:
                    random_outcome19_list[i + j] = random_table_19_changed_4[0]
                    random_table_19_changed_4.remove(random_table_19_changed_4[0])
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
    player_list_20 = []
    for i in random_outcome20_list:
        if i[0] != 0:
            player_list_20.append(i[0])
    random_table_20_changed_1 = random_table_1[2:]
    random_table_20_changed_2 = random_table_2[2:]
    random_table_20_changed_4 = random_table_4[1:]
    for i in random_table_20_changed_1:
        if i[0] in player_list_20:
            random_table_20_changed_1.remove(i)
    for i in random_table_20_changed_2:
        if i[0] in player_list_20:
            random_table_20_changed_2.remove(i)
    for i in random_table_20_changed_4:
        if i[0] in player_list_20:
            random_table_20_changed_4.remove(i)
    for i in range(len(random_outcome20_list)):
        for j in range(1, (len(random_outcome20_list) - i)):
            if random_outcome20_list[i][0] == random_outcome20_list[i + j][0] != 0:
                if random_outcome20_list[i + j][1] == 1:
                    random_outcome20_list[i + j] = random_table_20_changed_1[0]
                    random_table_20_changed_1.remove(random_table_20_changed_1[0])
                elif random_outcome20_list[i + j][1] == 2:
                    random_outcome20_list[i + j] = random_table_20_changed_2[0]
                    random_table_20_changed_2.remove(random_table_20_changed_2[0])
                elif random_outcome20_list[i + j][1] == 4:
                    random_outcome20_list[i + j] = random_table_20_changed_4[0]
                    random_table_20_changed_4.remove(random_table_20_changed_4[0])
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
    player_list_21 = []
    for i in random_outcome21_list:
        if i[0] != 0:
            player_list_21.append(i[0])
    random_table_21_changed_1 = random_table_1[4:]
    random_table_21_changed_2 = random_table_2[1:]
    random_table_21_changed_4 = random_table_4[1:]
    for i in random_table_21_changed_1:
        if i[0] in player_list_21:
            random_table_21_changed_1.remove(i)
    for i in random_table_21_changed_2:
        if i[0] in player_list_21:
            random_table_21_changed_2.remove(i)
    for i in random_table_21_changed_4:
        if i[0] in player_list_21:
            random_table_21_changed_4.remove(i)
    for i in range(len(random_outcome21_list)):
        for j in range(1, (len(random_outcome21_list) - i)):
            if random_outcome21_list[i][0] == random_outcome21_list[i + j][0] != 0:
                if random_outcome21_list[i + j][1] == 1:
                    random_outcome21_list[i + j] = random_table_21_changed_1[0]
                    random_table_21_changed_1.remove(random_table_21_changed_1[0])
                elif random_outcome21_list[i + j][1] == 2:
                    random_outcome21_list[i + j] = random_table_21_changed_2[0]
                    random_table_21_changed_2.remove(random_table_21_changed_2[0])
                elif random_outcome21_list[i + j][1] == 4:
                    random_outcome21_list[i + j] = random_table_21_changed_4[0]
                    random_table_21_changed_4.remove(random_table_21_changed_4[0])
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
    player_list_22 = []
    for i in random_outcome22_list:
        if i[0] != 0:
            player_list_22.append(i[0])
    random_table_22_changed_1 = random_table_1[6:]
    random_table_22_changed_4 = random_table_4[1:]
    for i in random_table_22_changed_1:
        if i[0] in player_list_22:
            random_table_22_changed_1.remove(i)
    for i in random_table_22_changed_4:
        if i[0] in player_list_22:
            random_table_22_changed_4.remove(i)
    for i in range(len(random_outcome22_list)):
        for j in range(1, (len(random_outcome22_list) - i)):
            if random_outcome22_list[i][0] == random_outcome22_list[i + j][0] != 0:
                if random_outcome22_list[i + j][1] == 1:
                    random_outcome22_list[i + j] = random_table_22_changed_1[0]
                    random_table_22_changed_1.remove(random_table_22_changed_1[0])
                elif random_outcome22_list[i + j][1] == 4:
                    random_outcome22_list[i + j] = random_table_22_changed_4[0]
                    random_table_22_changed_4.remove(random_table_22_changed_4[0])
    for i in random_outcome22_list:
        random_value_22 = random_value_22 + i[3]
    # outcome for 5*2
    random_value_23 = 0
    random_outcome23_list = [random_table_5[0], random_table_5[1]]
    player_list_23 = []
    for i in random_outcome23_list:
        if i[0] != 0:
            player_list_23.append(i[0])
    random_table_23_changed_5 = random_table_5[2:]
    for i in random_table_23_changed_5:
        if i[0] in player_list_23:
            random_table_23_changed_5.remove(i)
    for i in range(len(random_outcome23_list)):
        for j in range(1, (len(random_outcome23_list) - i)):
            if random_outcome23_list[i][0] == random_outcome23_list[i + j][0] != 0:
                if random_outcome23_list[i + j][1] == 5:
                    random_outcome23_list[i + j] = random_table_23_changed_5[0]
                    random_table_23_changed_5.remove(random_table_23_changed_5[0])
    for i in random_outcome23_list:
        random_value_23 = random_value_23 + i[3]
    # outcome for 5+4+1
    random_value_24 = 0
    random_outcome24_list = [random_table_5[0], random_table_4[0], random_table_1[0]]
    player_list_24 = []
    for i in random_outcome24_list:
        if i[0] != 0:
            player_list_24.append(i[0])
    random_table_24_changed_1 = random_table_1[1:]
    random_table_24_changed_4 = random_table_4[1:]
    random_table_24_changed_5 = random_table_5[1:]
    for i in random_table_24_changed_1:
        if i[0] in player_list_24:
            random_table_24_changed_1.remove(i)
    for i in random_table_24_changed_4:
        if i[0] in player_list_24:
            random_table_24_changed_4.remove(i)
    for i in random_table_24_changed_5:
        if i[0] in player_list_24:
            random_table_24_changed_5.remove(i)
    for i in range(len(random_outcome24_list)):
        for j in range(1, (len(random_outcome24_list) - i)):
            if random_outcome24_list[i][0] == random_outcome24_list[i + j][0] != 0:
                if random_outcome24_list[i + j][1] == 1:
                    random_outcome24_list[i + j] = random_table_24_changed_1[0]
                    random_table_24_changed_1.remove(random_table_24_changed_1[0])
                elif random_outcome24_list[i + j][1] == 4:
                    random_outcome24_list[i + j] = random_table_24_changed_4[0]
                    random_table_24_changed_4.remove(random_table_24_changed_4[0])
                elif random_outcome24_list[i + j][1] == 5:
                    random_outcome24_list[i + j] = random_table_24_changed_5[0]
                    random_table_24_changed_5.remove(random_table_24_changed_5[0])
    for i in random_outcome24_list:
        random_value_24 = random_value_24 + i[3]
    # outcome for 5+3+2
    random_value_25 = 0
    random_outcome25_list = [random_table_5[0], random_table_3[0], random_table_2[0]]
    player_list_25 = []
    for i in random_outcome25_list:
        if i[0] != 0:
            player_list_25.append(i[0])
    random_table_25_changed_2 = random_table_2[1:]
    random_table_25_changed_3 = random_table_3[1:]
    random_table_25_changed_5 = random_table_5[1:]
    for i in random_table_25_changed_2:
        if i[0] in player_list_25:
            random_table_25_changed_2.remove(i)
    for i in random_table_25_changed_3:
        if i[0] in player_list_25:
            random_table_25_changed_3.remove(i)
    for i in random_table_25_changed_5:
        if i[0] in player_list_25:
            random_table_25_changed_5.remove(i)
    for i in range(len(random_outcome25_list)):
        for j in range(1, (len(random_outcome25_list) - i)):
            if random_outcome25_list[i][0] == random_outcome25_list[i + j][0] != 0:
                if random_outcome25_list[i + j][1] == 2:
                    random_outcome25_list[i + j] = random_table_25_changed_2[0]
                    random_table_25_changed_2.remove(random_table_25_changed_2[0])
                elif random_outcome25_list[i + j][1] == 3:
                    random_outcome25_list[i + j] = random_table_25_changed_3[0]
                    random_table_25_changed_3.remove(random_table_25_changed_3[0])
                elif random_outcome25_list[i + j][1] == 5:
                    random_outcome25_list[i + j] = random_table_25_changed_5[0]
                    random_table_25_changed_5.remove(random_table_25_changed_5[0])
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
    player_list_26 = []
    for i in random_outcome26_list:
        if i[0] != 0:
            player_list_26.append(i[0])
    random_table_26_changed_1 = random_table_1[2:]
    random_table_26_changed_3 = random_table_3[1:]
    random_table_26_changed_5 = random_table_5[1:]
    for i in random_table_26_changed_1:
        if i[0] in player_list_26:
            random_table_26_changed_1.remove(i)
    for i in random_table_26_changed_3:
        if i[0] in player_list_26:
            random_table_26_changed_3.remove(i)
    for i in random_table_26_changed_5:
        if i[0] in player_list_26:
            random_table_26_changed_5.remove(i)
    for i in range(len(random_outcome26_list)):
        for j in range(1, (len(random_outcome26_list) - i)):
            if random_outcome26_list[i][0] == random_outcome26_list[i + j][0] != 0:
                if random_outcome26_list[i + j][1] == 1:
                    random_outcome26_list[i + j] = random_table_26_changed_1[0]
                    random_table_26_changed_1.remove(random_table_26_changed_1[0])
                elif random_outcome26_list[i + j][1] == 3:
                    random_outcome26_list[i + j] = random_table_26_changed_3[0]
                    random_table_26_changed_3.remove(random_table_26_changed_3[0])
                elif random_outcome26_list[i + j][1] == 5:
                    random_outcome26_list[i + j] = random_table_26_changed_5[0]
                    random_table_26_changed_5.remove(random_table_26_changed_5[0])
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
    player_list_27 = []
    for i in random_outcome27_list:
        if i[0] != 0:
            player_list_27.append(i[0])
    random_table_27_changed_1 = random_table_1[1:]
    random_table_27_changed_2 = random_table_2[2:]
    random_table_27_changed_5 = random_table_5[1:]
    for i in random_table_27_changed_1:
        if i[0] in player_list_27:
            random_table_27_changed_1.remove(i)
    for i in random_table_27_changed_2:
        if i[0] in player_list_27:
            random_table_27_changed_2.remove(i)
    for i in random_table_27_changed_5:
        if i[0] in player_list_27:
            random_table_27_changed_5.remove(i)
    for i in range(len(random_outcome27_list)):
        for j in range(1, (len(random_outcome27_list) - i)):
            if random_outcome27_list[i][0] == random_outcome27_list[i + j][0] != 0:
                if random_outcome27_list[i + j][1] == 1:
                    random_outcome27_list[i + j] = random_table_27_changed_1[0]
                    random_table_27_changed_1.remove(random_table_27_changed_1[0])
                elif random_outcome27_list[i + j][1] == 2:
                    random_outcome27_list[i + j] = random_table_27_changed_2[0]
                    random_table_27_changed_2.remove(random_table_27_changed_2[0])
                elif random_outcome27_list[i + j][1] == 5:
                    random_outcome27_list[i + j] = random_table_27_changed_5[0]
                    random_table_27_changed_5.remove(random_table_27_changed_5[0])
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
    player_list_28 = []
    for i in random_outcome28_list:
        if i[0] != 0:
            player_list_28.append(i[0])
    random_table_28_changed_1 = random_table_1[3:]
    random_table_28_changed_2 = random_table_2[1:]
    random_table_28_changed_5 = random_table_5[1:]
    for i in random_table_28_changed_1:
        if i[0] in player_list_28:
            random_table_28_changed_1.remove(i)
    for i in random_table_28_changed_2:
        if i[0] in player_list_28:
            random_table_28_changed_2.remove(i)
    for i in random_table_28_changed_5:
        if i[0] in player_list_28:
            random_table_28_changed_5.remove(i)
    for i in range(len(random_outcome28_list)):
        for j in range(1, (len(random_outcome28_list) - i)):
            if random_outcome28_list[i][0] == random_outcome28_list[i + j][0] != 0:
                if random_outcome28_list[i + j][1] == 1:
                    random_outcome28_list[i + j] = random_table_28_changed_1[0]
                    random_table_28_changed_1.remove(random_table_28_changed_1[0])
                elif random_outcome28_list[i + j][1] == 2:
                    random_outcome28_list[i + j] = random_table_28_changed_2[0]
                    random_table_28_changed_2.remove(random_table_28_changed_2[0])
                elif random_outcome28_list[i + j][1] == 5:
                    random_outcome28_list[i + j] = random_table_28_changed_5[0]
                    random_table_28_changed_5.remove(random_table_28_changed_5[0])
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
    player_list_29 = []
    for i in random_outcome29_list:
        if i[0] != 0:
            player_list_29.append(i[0])
    random_table_29_changed_1 = random_table_1[5:]
    random_table_29_changed_5 = random_table_5[1:]
    for i in random_table_29_changed_1:
        if i[0] in player_list_29:
            random_table_29_changed_1.remove(i)
    for i in random_table_29_changed_5:
        if i[0] in player_list_29:
            random_table_29_changed_5.remove(i)
    for i in range(len(random_outcome29_list)):
        for j in range(1, (len(random_outcome29_list) - i)):
            if random_outcome29_list[i][0] == random_outcome29_list[i + j][0] != 0:
                if random_outcome29_list[i + j][1] == 1:
                    random_outcome29_list[i + j] = random_table_29_changed_1[0]
                    random_table_29_changed_1.remove(random_table_29_changed_1[0])
                elif random_outcome29_list[i + j][1] == 5:
                    random_outcome29_list[i + j] = random_table_29_changed_5[0]
                    random_table_29_changed_5.remove(random_table_29_changed_5[0])
    for i in random_outcome29_list:
        random_value_29 = random_value_29 + i[3]
    # outcome for 6+4
    random_value_30 = 0
    random_outcome30_list = [random_table_6[0], random_table_4[0]]
    player_list_30 = []
    for i in random_outcome30_list:
        if i[0] != 0:
            player_list_30.append(i[0])
    random_table_30_changed_4 = random_table_4[1:]
    random_table_30_changed_6 = random_table_6[1:]
    for i in random_table_30_changed_4:
        if i[0] in player_list_30:
            random_table_30_changed_4.remove(i)
    for i in random_table_30_changed_6:
        if i[0] in player_list_30:
            random_table_30_changed_6.remove(i)
    for i in range(len(random_outcome30_list)):
        for j in range(1, (len(random_outcome30_list) - i)):
            if random_outcome30_list[i][0] == random_outcome30_list[i + j][0] != 0:
                if random_outcome30_list[i + j][1] == 4:
                    random_outcome30_list[i + j] = random_table_30_changed_4[0]
                    random_table_30_changed_4.remove(random_table_30_changed_4[0])
                elif random_outcome30_list[i + j][1] == 6:
                    random_outcome30_list[i + j] = random_table_30_changed_6[0]
                    random_table_30_changed_6.remove(random_table_30_changed_6[0])
    for i in random_outcome30_list:
        random_value_30 = random_value_30 + i[3]
    # outcome for 6+3+1
    random_value_31 = 0
    random_outcome31_list = [random_table_6[0], random_table_3[0], random_table_1[0]]
    player_list_31 = []
    for i in random_outcome31_list:
        if i[0] != 0:
            player_list_31.append(i[0])
    random_table_31_changed_1 = random_table_1[1:]
    random_table_31_changed_3 = random_table_3[1:]
    random_table_31_changed_6 = random_table_6[1:]
    for i in random_table_31_changed_1:
        if i[0] in player_list_31:
            random_table_31_changed_1.remove(i)
    for i in random_table_31_changed_3:
        if i[0] in player_list_31:
            random_table_31_changed_3.remove(i)
    for i in random_table_31_changed_6:
        if i[0] in player_list_31:
            random_table_31_changed_6.remove(i)
    for i in range(len(random_outcome31_list)):
        for j in range(1, (len(random_outcome31_list) - i)):
            if random_outcome31_list[i][0] == random_outcome31_list[i + j][0] != 0:
                if random_outcome31_list[i + j][1] == 1:
                    random_outcome31_list[i + j] = random_table_31_changed_1[0]
                    random_table_31_changed_1.remove(random_table_31_changed_1[0])
                elif random_outcome31_list[i + j][1] == 3:
                    random_outcome31_list[i + j] = random_table_31_changed_3[0]
                    random_table_31_changed_3.remove(random_table_31_changed_3[0])
                elif random_outcome31_list[i + j][1] == 6:
                    random_outcome31_list[i + j] = random_table_31_changed_6[0]
                    random_table_31_changed_6.remove(random_table_31_changed_6[0])
    for i in random_outcome31_list:
        random_value_31 = random_value_31 + i[3]
    # outcome for 6+2*2
    random_value_32 = 0
    random_outcome32_list = [random_table_6[0], random_table_2[0], random_table_2[1]]
    player_list_32 = []
    for i in random_outcome32_list:
        if i[0] != 0:
            player_list_32.append(i[0])
    random_table_32_changed_2 = random_table_2[2:]
    random_table_32_changed_6 = random_table_6[1:]
    for i in random_table_32_changed_2:
        if i[0] in player_list_32:
            random_table_32_changed_2.remove(i)
    for i in random_table_32_changed_6:
        if i[0] in player_list_32:
            random_table_32_changed_6.remove(i)
    for i in range(len(random_outcome32_list)):
        for j in range(1, (len(random_outcome32_list) - i)):
            if random_outcome32_list[i][0] == random_outcome32_list[i + j][0] != 0:
                if random_outcome32_list[i + j][1] == 2:
                    random_outcome32_list[i + j] = random_table_32_changed_2[0]
                    random_table_32_changed_2.remove(random_table_32_changed_2[0])
                elif random_outcome32_list[i + j][1] == 6:
                    random_outcome32_list[i + j] = random_table_32_changed_6[0]
                    random_table_32_changed_6.remove(random_table_32_changed_6[0])
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
    player_list_33 = []
    for i in random_outcome33_list:
        if i[0] != 0:
            player_list_33.append(i[0])
    random_table_33_changed_1 = random_table_1[2:]
    random_table_33_changed_2 = random_table_2[1:]
    random_table_33_changed_6 = random_table_6[1:]
    for i in random_table_33_changed_1:
        if i[0] in player_list_33:
            random_table_33_changed_1.remove(i)
    for i in random_table_33_changed_2:
        if i[0] in player_list_33:
            random_table_33_changed_2.remove(i)
    for i in random_table_33_changed_6:
        if i[0] in player_list_33:
            random_table_33_changed_6.remove(i)
    for i in range(len(random_outcome33_list)):
        for j in range(1, (len(random_outcome33_list) - i)):
            if random_outcome33_list[i][0] == random_outcome33_list[i + j][0] != 0:
                if random_outcome33_list[i + j][1] == 1:
                    random_outcome33_list[i + j] = random_table_33_changed_1[0]
                    random_table_33_changed_1.remove(random_table_33_changed_1[0])
                elif random_outcome33_list[i + j][1] == 2:
                    random_outcome33_list[i + j] = random_table_33_changed_2[0]
                    random_table_33_changed_2.remove(random_table_33_changed_2[0])
                elif random_outcome33_list[i + j][1] == 6:
                    random_outcome33_list[i + j] = random_table_33_changed_6[0]
                    random_table_33_changed_6.remove(random_table_33_changed_6[0])
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
    player_list_34 = []
    for i in random_outcome34_list:
        if i[0] != 0:
            player_list_34.append(i[0])
    random_table_34_changed_1 = random_table_1[4:]
    random_table_34_changed_6 = random_table_6[1:]
    for i in random_table_34_changed_1:
        if i[0] in player_list_34:
            random_table_34_changed_1.remove(i)
    for i in random_table_34_changed_6:
        if i[0] in player_list_34:
            random_table_34_changed_6.remove(i)
    for i in range(len(random_outcome34_list)):
        for j in range(1, (len(random_outcome34_list) - i)):
            if random_outcome34_list[i][0] == random_outcome34_list[i + j][0] != 0:
                if random_outcome34_list[i + j][1] == 1:
                    random_outcome34_list[i + j] = random_table_34_changed_1[0]
                    random_table_34_changed_1.remove(random_table_34_changed_1[0])
                elif random_outcome34_list[i + j][1] == 6:
                    random_outcome32_list[i + j] = random_table_34_changed_6[0]
                    random_table_34_changed_6.remove(random_table_34_changed_6[0])
    for i in random_outcome34_list:
        random_value_34 = random_value_34 + i[3]
    # outcome for 7+3
    random_value_35 = 0
    random_outcome35_list = [random_table_7[0], random_table_3[0]]
    player_list_35 = []
    for i in random_outcome35_list:
        if i[0] != 0:
            player_list_35.append(i[0])
    random_table_35_changed_3 = random_table_3[1:]
    random_table_35_changed_7 = random_table_7[1:]
    for i in random_table_35_changed_3:
        if i[0] in player_list_35:
            random_table_35_changed_3.remove(i)
    for i in random_table_35_changed_7:
        if i[0] in player_list_35:
            random_table_35_changed_7.remove(i)
    for i in range(len(random_outcome35_list)):
        for j in range(1, (len(random_outcome35_list) - i)):
            if random_outcome35_list[i][0] == random_outcome35_list[i + j][0] != 0:
                if random_outcome35_list[i + j][1] == 3:
                    random_outcome35_list[i + j] = random_table_35_changed_3[0]
                    random_table_35_changed_3.remove(random_table_35_changed_3[0])
                elif random_outcome35_list[i + j][1] == 7:
                    random_outcome35_list[i + j] = random_table_35_changed_7[0]
                    random_table_35_changed_7.remove(random_table_35_changed_7[0])
    for i in random_outcome35_list:
        random_value_35 = random_value_35 + i[3]
    # outcome for 7+2+1
    random_value_36 = 0
    random_outcome36_list = [random_table_7[0], random_table_2[0], random_table_1[0]]
    player_list_36 = []
    for i in random_outcome36_list:
        if i[0] != 0:
            player_list_36.append(i[0])
    random_table_36_changed_1 = random_table_1[2:]
    random_table_36_changed_2 = random_table_2[1:]
    random_table_36_changed_7 = random_table_7[1:]
    for i in random_table_36_changed_1:
        if i[0] in player_list_36:
            random_table_36_changed_1.remove(i)
    for i in random_table_36_changed_2:
        if i[0] in player_list_36:
            random_table_36_changed_2.remove(i)
    for i in random_table_36_changed_7:
        if i[0] in player_list_36:
            random_table_36_changed_7.remove(i)
    for i in range(len(random_outcome36_list)):
        for j in range(1, (len(random_outcome36_list) - i)):
            if random_outcome36_list[i][0] == random_outcome36_list[i + j][0] != 0:
                if random_outcome36_list[i + j][1] == 1:
                    random_outcome36_list[i + j] = random_table_36_changed_1[0]
                    random_table_36_changed_1.remove(random_table_36_changed_1[0])
                elif random_outcome36_list[i + j][1] == 2:
                    random_outcome36_list[i + j] = random_table_36_changed_2[0]
                    random_table_36_changed_2.remove(random_table_36_changed_2[0])
                elif random_outcome36_list[i + j][1] == 7:
                    random_outcome36_list[i + j] = random_table_36_changed_7[0]
                    random_table_36_changed_7.remove(random_table_36_changed_7[0])
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
    player_list_37 = []
    for i in random_outcome37_list:
        if i[0] != 0:
            player_list_37.append(i[0])
    random_table_37_changed_1 = random_table_1[3:]
    random_table_37_changed_7 = random_table_7[1:]
    for i in random_table_37_changed_1:
        if i[0] in player_list_37:
            random_table_37_changed_1.remove(i)
    for i in random_table_37_changed_7:
        if i[0] in player_list_37:
            random_table_37_changed_7.remove(i)
    for i in range(len(random_outcome37_list)):
        for j in range(1, (len(random_outcome37_list) - i)):
            if random_outcome37_list[i][0] == random_outcome37_list[i + j][0] != 0:
                if random_outcome37_list[i + j][1] == 1:
                    random_outcome37_list[i + j] = random_table_37_changed_1[0]
                    random_table_37_changed_1.remove(random_table_37_changed_1[0])
                elif random_outcome37_list[i + j][1] == 7:
                    random_outcome37_list[i + j] = random_table_37_changed_7[0]
                    random_table_37_changed_7.remove(random_table_37_changed_7[0])
    for i in random_outcome37_list:
        random_value_37 = random_value_37 + i[3]
    # outcome for 8+2
    random_value_38 = 0
    random_outcome38_list = [random_table_8[0], random_table_2[0]]
    player_list_38 = []
    for i in random_outcome38_list:
        if i[0] != 0:
            player_list_38.append(i[0])
    random_table_38_changed_2 = random_table_2[1:]
    random_table_38_changed_8 = random_table_8[1:]
    for i in random_table_38_changed_2:
        if i[0] in player_list_38:
            random_table_38_changed_2.remove(i)
    for i in random_table_38_changed_8:
        if i[0] in player_list_38:
            random_table_38_changed_8.remove(i)
    for i in range(len(random_outcome38_list)):
        for j in range(1, (len(random_outcome38_list) - i)):
            if random_outcome38_list[i][0] == random_outcome38_list[i + j][0] != 0:
                if random_outcome38_list[i + j][1] == 2:
                    random_outcome38_list[i + j] = random_table_38_changed_2[0]
                    random_table_38_changed_2.remove(random_table_38_changed_2[0])
                elif random_outcome38_list[i + j][1] == 8:
                    random_outcome38_list[i + j] = random_table_38_changed_8[0]
                    random_table_38_changed_8.remove(random_table_38_changed_8[0])
    for i in random_outcome38_list:
        random_value_38 = random_value_38 + i[3]
    # outcome for 8+1*2
    random_value_39 = 0
    random_outcome39_list = [random_table_8[0], random_table_1[0], random_table_1[1]]
    player_list_39 = []
    for i in random_outcome39_list:
        if i[0] != 0:
            player_list_39.append(i[0])
    random_table_39_changed_1 = random_table_1[2:]
    random_table_39_changed_8 = random_table_8[1:]
    for i in random_table_39_changed_1:
        if i[0] in player_list_39:
            random_table_39_changed_1.remove(i)
    for i in random_table_39_changed_8:
        if i[0] in player_list_39:
            random_table_39_changed_8.remove(i)
    for i in range(len(random_outcome39_list)):
        for j in range(1, (len(random_outcome39_list) - i)):
            if random_outcome39_list[i][0] == random_outcome39_list[i + j][0] != 0:
                if random_outcome39_list[i + j][1] == 1:
                    random_outcome39_list[i + j] = random_table_39_changed_1[0]
                    random_table_39_changed_1.remove(random_table_39_changed_1[0])
                elif random_outcome39_list[i + j][1] == 8:
                    random_outcome39_list[i + j] = random_table_39_changed_8[0]
                    random_table_39_changed_8.remove(random_table_39_changed_8[0])
    for i in random_outcome39_list:
        random_value_39 = random_value_39 + i[3]
    # outcome for 9+1
    random_value_40 = 0
    random_outcome40_list = [random_table_9[0], random_table_1[0]]
    player_list_40 = []
    for i in random_outcome40_list:
        if i[0] != 0:
            player_list_40.append(i[0])
    random_table_40_changed_1 = random_table_1[1:]
    random_table_40_changed_9 = random_table_9[1:]
    for i in random_table_40_changed_1:
        if i[0] in player_list_40:
            random_table_40_changed_1.remove(i)
    for i in random_table_40_changed_9:
        if i[0] in player_list_40:
            random_table_40_changed_9.remove(i)
    for i in range(len(random_outcome40_list)):
        for j in range(1, (len(random_outcome40_list) - i)):
            if random_outcome40_list[i][0] == random_outcome40_list[i + j][0] != 0:
                if random_outcome40_list[i + j][1] == 1:
                    random_outcome40_list[i + j] = random_table_40_changed_1[0]
                    random_table_40_changed_1.remove(random_table_40_changed_1[0])
                elif random_outcome40_list[i + j][1] == 9:
                    random_outcome40_list[i + j] = random_table_40_changed_9[0]
                    random_table_40_changed_9.remove(random_table_40_changed_9[0])
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
                            print(
                                z,
                                "-------random-telling-------" "allocate table",
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
                            seplayer_list_1 = []
                            for i in seoutcome1_list:
                                if i[0] != 0:
                                    seplayer_list_1.append(i[0])
                            sereport_table_1_changed = sereport_table_1[9:]
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
                            # outcome for 2*5
                            sevalue_2 = 0
                            seoutcome2_list = [
                                sereport_table_2[0],
                                sereport_table_2[1],
                                sereport_table_2[2],
                                sereport_table_2[3],
                                sereport_table_2[4],
                            ]
                            seplayer_list_2 = []
                            for i in seoutcome2_list:
                                if i[0] != 0:
                                    seplayer_list_2.append(i[0])
                            sereport_table_2_changed = sereport_table_2[5:]
                            for i in sereport_table_2_changed:
                                if i[0] in seplayer_list_2:
                                    sereport_table_2_changed.remove(i)
                            for i in range(len(seoutcome2_list)):
                                for j in range(1, (len(seoutcome2_list) - i)):
                                    if (
                                        seoutcome2_list[i][0]
                                        == seoutcome2_list[i + j][0]
                                        != 0
                                    ):
                                        seoutcome2_list[
                                            i + j
                                        ] = sereport_table_2_changed[0]
                                        sereport_table_2_changed.remove(
                                            sereport_table_2_changed[0]
                                        )
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
                            seplayer_list_3 = []
                            for i in seoutcome3_list:
                                if i[0] != 0:
                                    seplayer_list_3.append(i[0])
                            sereport_table_3_changed_1 = sereport_table_1[2:]
                            sereport_table_3_changed_2 = sereport_table_2[4:]
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
                            seplayer_list_4 = []
                            for i in seoutcome4_list:
                                if i[0] != 0:
                                    seplayer_list_4.append(i[0])
                            sereport_table_4_changed_1 = sereport_table_1[4:]
                            sereport_table_4_changed_2 = sereport_table_2[3:]
                            for i in sereport_table_4_changed_1:
                                if i[0] in seplayer_list_4:
                                    sereport_table_4_changed_1.remove(i)
                            for i in sereport_table_4_changed_2:
                                if i[0] in seplayer_list_4:
                                    sereport_table_4_changed_2.remove(i)
                            for i in range(len(seoutcome4_list)):
                                for j in range(1, (len(seoutcome4_list) - i)):
                                    if (
                                        seoutcome4_list[i][0]
                                        == seoutcome4_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome4_list[i + j][1] == 1:
                                            seoutcome4_list[
                                                i + j
                                            ] = sereport_table_4_changed_1[0]
                                            sereport_table_4_changed_1.remove(
                                                sereport_table_4_changed_1[0]
                                            )
                                        elif seoutcome4_list[i + j][1] == 2:
                                            seoutcome4_list[
                                                i + j
                                            ] = sereport_table_4_changed_2[0]
                                            sereport_table_4_changed_2.remove(
                                                sereport_table_4_changed_2[0]
                                            )
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
                            seplayer_list_5 = []
                            for i in seoutcome5_list:
                                if i[0] != 0:
                                    seplayer_list_5.append(i[0])
                            sereport_table_5_changed_1 = sereport_table_1[6:]
                            sereport_table_5_changed_2 = sereport_table_2[2:]
                            for i in sereport_table_5_changed_1:
                                if i[0] in seplayer_list_5:
                                    sereport_table_5_changed_1.remove(i)
                            for i in sereport_table_5_changed_2:
                                if i[0] in seplayer_list_5:
                                    sereport_table_5_changed_2.remove(i)
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
                                        elif seoutcome5_list[i + j][1] == 2:
                                            seoutcome5_list[
                                                i + j
                                            ] = sereport_table_5_changed_2[0]
                                            sereport_table_5_changed_2.remove(
                                                sereport_table_5_changed_2[0]
                                            )
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
                            seplayer_list_6 = []
                            for i in seoutcome6_list:
                                if i[0] != 0:
                                    seplayer_list_6.append(i[0])
                            sereport_table_6_changed_1 = sereport_table_1[8:]
                            sereport_table_6_changed_2 = sereport_table_2[1:]
                            for i in sereport_table_6_changed_1:
                                if i[0] in seplayer_list_6:
                                    sereport_table_6_changed_1.remove(i)
                            for i in sereport_table_6_changed_2:
                                if i[0] in seplayer_list_6:
                                    sereport_table_6_changed_2.remove(i)
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
                                        elif seoutcome6_list[i + j][1] == 2:
                                            seoutcome6_list[
                                                i + j
                                            ] = sereport_table_6_changed_2[0]
                                            sereport_table_6_changed_2.remove(
                                                sereport_table_6_changed_2[0]
                                            )
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
                            seplayer_list_7 = []
                            for i in seoutcome7_list:
                                if i[0] != 0:
                                    seplayer_list_7.append(i[0])
                            sereport_table_7_changed_1 = sereport_table_1[1:]
                            sereport_table_7_changed_3 = sereport_table_3[3:]
                            for i in sereport_table_7_changed_1:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_1.remove(i)
                            for i in sereport_table_7_changed_3:
                                if i[0] in seplayer_list_7:
                                    sereport_table_7_changed_3.remove(i)
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
                                        elif seoutcome7_list[i + j][1] == 3:
                                            seoutcome7_list[
                                                i + j
                                            ] = sereport_table_7_changed_3[0]
                                            sereport_table_7_changed_3.remove(
                                                sereport_table_7_changed_3[0]
                                            )
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
                            seplayer_list_8 = []
                            for i in seoutcome8_list:
                                if i[0] != 0:
                                    seplayer_list_8.append(i[0])
                            sereport_table_8_changed_2 = sereport_table_2[2:]
                            sereport_table_8_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_8_changed_2:
                                if i[0] in seplayer_list_8:
                                    sereport_table_8_changed_2.remove(i)
                            for i in sereport_table_8_changed_3:
                                if i[0] in seplayer_list_8:
                                    sereport_table_8_changed_3.remove(i)
                            for i in range(len(seoutcome8_list)):
                                for j in range(1, (len(seoutcome8_list) - i)):
                                    if (
                                        seoutcome8_list[i][0]
                                        == seoutcome8_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome8_list[i + j][1] == 2:
                                            seoutcome8_list[
                                                i + j
                                            ] = sereport_table_8_changed_2[0]
                                            sereport_table_8_changed_2.remove(
                                                sereport_table_8_changed_2[0]
                                            )
                                        elif seoutcome8_list[i + j][1] == 3:
                                            seoutcome8_list[
                                                i + j
                                            ] = sereport_table_8_changed_3[0]
                                            sereport_table_8_changed_3.remove(
                                                sereport_table_8_changed_3[0]
                                            )
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
                            seplayer_list_9 = []
                            for i in seoutcome9_list:
                                if i[0] != 0:
                                    seplayer_list_9.append(i[0])
                            sereport_table_9_changed_1 = sereport_table_1[2:]
                            sereport_table_9_changed_2 = sereport_table_2[1:]
                            sereport_table_9_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_9_changed_1:
                                if i[0] in seplayer_list_9:
                                    sereport_table_9_changed_1.remove(i)
                            for i in sereport_table_9_changed_2:
                                if i[0] in seplayer_list_9:
                                    sereport_table_9_changed_2.remove(i)
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
                                        if seoutcome9_list[i + j][1] == 1:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_1[0]
                                            sereport_table_9_changed_1.remove(
                                                sereport_table_9_changed_1[0]
                                            )
                                        elif seoutcome9_list[i + j][1] == 2:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_2[0]
                                            sereport_table_9_changed_2.remove(
                                                sereport_table_9_changed_2[0]
                                            )
                                        elif seoutcome9_list[i + j][1] == 3:
                                            seoutcome9_list[
                                                i + j
                                            ] = sereport_table_9_changed_3[0]
                                            sereport_table_9_changed_3.remove(
                                                sereport_table_9_changed_3[0]
                                            )
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
                            seplayer_list_10 = []
                            for i in seoutcome10_list:
                                if i[0] != 0:
                                    seplayer_list_10.append(i[0])
                            sereport_table_10_changed_1 = sereport_table_1[4:]
                            sereport_table_10_changed_3 = sereport_table_3[2:]
                            for i in sereport_table_10_changed_1:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_1.remove(i)
                            for i in sereport_table_10_changed_3:
                                if i[0] in seplayer_list_10:
                                    sereport_table_10_changed_3.remove(i)
                            for i in range(len(seoutcome10_list)):
                                for j in range(1, (len(seoutcome10_list) - i)):
                                    if (
                                        seoutcome10_list[i][0]
                                        == seoutcome10_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome10_list[i + j][1] == 1:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_1[0]
                                            sereport_table_10_changed_1.remove(
                                                sereport_table_10_changed_1[0]
                                            )
                                        elif seoutcome10_list[i + j][1] == 3:
                                            seoutcome10_list[
                                                i + j
                                            ] = sereport_table_10_changed_3[0]
                                            sereport_table_10_changed_3.remove(
                                                sereport_table_10_changed_3[0]
                                            )
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
                            seplayer_list_11 = []
                            for i in seoutcome11_list:
                                if i[0] != 0:
                                    seplayer_list_11.append(i[0])
                            sereport_table_11_changed_1 = sereport_table_1[3:]
                            sereport_table_11_changed_2 = sereport_table_2[2:]
                            sereport_table_11_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_11_changed_1:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_1.remove(i)
                            for i in sereport_table_11_changed_2:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_2.remove(i)
                            for i in sereport_table_11_changed_3:
                                if i[0] in seplayer_list_11:
                                    sereport_table_11_changed_3.remove(i)
                            for i in range(len(seoutcome11_list)):
                                for j in range(1, (len(seoutcome11_list) - i)):
                                    if (
                                        seoutcome11_list[i][0]
                                        == seoutcome11_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome11_list[i + j][1] == 1:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_1[0]
                                            sereport_table_11_changed_1.remove(
                                                sereport_table_11_changed_1[0]
                                            )
                                        elif seoutcome11_list[i + j][1] == 2:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_2[0]
                                            sereport_table_11_changed_2.remove(
                                                sereport_table_11_changed_2[0]
                                            )
                                        elif seoutcome11_list[i + j][1] == 3:
                                            seoutcome11_list[
                                                i + j
                                            ] = sereport_table_11_changed_3[0]
                                            sereport_table_11_changed_3.remove(
                                                sereport_table_11_changed_3[0]
                                            )
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
                            seplayer_list_12 = []
                            for i in seoutcome12_list:
                                if i[0] != 0:
                                    seplayer_list_12.append(i[0])
                            sereport_table_12_changed_1 = sereport_table_1[5:]
                            sereport_table_12_changed_2 = sereport_table_2[1:]
                            sereport_table_12_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_12_changed_1:
                                if i[0] in seplayer_list_12:
                                    sereport_table_12_changed_1.remove(i)
                            for i in sereport_table_12_changed_2:
                                if i[0] in seplayer_list_12:
                                    sereport_table_12_changed_2.remove(i)
                            for i in sereport_table_12_changed_3:
                                if i[0] in seplayer_list_12:
                                    sereport_table_12_changed_3.remove(i)
                            for i in range(len(seoutcome12_list)):
                                for j in range(1, (len(seoutcome12_list) - i)):
                                    if (
                                        seoutcome12_list[i][0]
                                        == seoutcome12_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome12_list[i + j][1] == 1:
                                            seoutcome12_list[
                                                i + j
                                            ] = sereport_table_12_changed_1[0]
                                            sereport_table_12_changed_1.remove(
                                                sereport_table_12_changed_1[0]
                                            )
                                        elif seoutcome12_list[i + j][1] == 2:
                                            seoutcome12_list[
                                                i + j
                                            ] = sereport_table_12_changed_2[0]
                                            sereport_table_12_changed_2.remove(
                                                sereport_table_12_changed_2[0]
                                            )
                                        elif seoutcome12_list[i + j][1] == 3:
                                            seoutcome12_list[
                                                i + j
                                            ] = sereport_table_12_changed_3[0]
                                            sereport_table_12_changed_3.remove(
                                                sereport_table_12_changed_3[0]
                                            )
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
                            seplayer_list_13 = []
                            for i in seoutcome13_list:
                                if i[0] != 0:
                                    seplayer_list_13.append(i[0])
                            sereport_table_13_changed_1 = sereport_table_1[7:]
                            sereport_table_13_changed_3 = sereport_table_3[1:]
                            for i in sereport_table_13_changed_1:
                                if i[0] in seplayer_list_13:
                                    sereport_table_13_changed_1.remove(i)
                            for i in sereport_table_13_changed_3:
                                if i[0] in seplayer_list_13:
                                    sereport_table_13_changed_3.remove(i)
                            for i in range(len(seoutcome13_list)):
                                for j in range(1, (len(seoutcome13_list) - i)):
                                    if (
                                        seoutcome13_list[i][0]
                                        == seoutcome13_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome13_list[i + j][1] == 1:
                                            seoutcome13_list[
                                                i + j
                                            ] = sereport_table_13_changed_1[0]
                                            sereport_table_13_changed_1.remove(
                                                sereport_table_13_changed_1[0]
                                            )
                                        elif seoutcome13_list[i + j][1] == 3:
                                            seoutcome13_list[
                                                i + j
                                            ] = sereport_table_13_changed_3[0]
                                            sereport_table_13_changed_3.remove(
                                                sereport_table_13_changed_3[0]
                                            )
                            for i in seoutcome13_list:
                                sevalue_13 = sevalue_13 + i[3]
                            # outcome for 4*2+2
                            sevalue_14 = 0
                            seoutcome14_list = [
                                sereport_table_4[0],
                                sereport_table_4[1],
                                sereport_table_2[0],
                            ]
                            seplayer_list_14 = []
                            for i in seoutcome14_list:
                                if i[0] != 0:
                                    seplayer_list_14.append(i[0])
                            sereport_table_14_changed_2 = sereport_table_2[1:]
                            sereport_table_14_changed_4 = sereport_table_4[2:]
                            for i in sereport_table_14_changed_2:
                                if i[0] in seplayer_list_14:
                                    sereport_table_14_changed_2.remove(i)
                            for i in sereport_table_14_changed_4:
                                if i[0] in seplayer_list_14:
                                    sereport_table_14_changed_4.remove(i)
                            for i in range(len(seoutcome14_list)):
                                for j in range(1, (len(seoutcome14_list) - i)):
                                    if (
                                        seoutcome14_list[i][0]
                                        == seoutcome14_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome14_list[i + j][1] == 2:
                                            seoutcome14_list[
                                                i + j
                                            ] = sereport_table_14_changed_2[0]
                                            sereport_table_14_changed_2.remove(
                                                sereport_table_14_changed_2[0]
                                            )
                                        elif seoutcome14_list[i + j][1] == 4:
                                            seoutcome14_list[
                                                i + j
                                            ] = sereport_table_14_changed_4[0]
                                            sereport_table_14_changed_4.remove(
                                                sereport_table_14_changed_4[0]
                                            )
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
                            seplayer_list_15 = []
                            for i in seoutcome15_list:
                                if i[0] != 0:
                                    seplayer_list_15.append(i[0])
                            sereport_table_15_changed_1 = sereport_table_1[2:]
                            sereport_table_15_changed_4 = sereport_table_4[2:]
                            for i in sereport_table_15_changed_1:
                                if i[0] in seplayer_list_15:
                                    sereport_table_15_changed_1.remove(i)
                            for i in sereport_table_15_changed_4:
                                if i[0] in seplayer_list_15:
                                    sereport_table_15_changed_4.remove(i)
                            for i in range(len(seoutcome15_list)):
                                for j in range(1, (len(seoutcome15_list) - i)):
                                    if (
                                        seoutcome15_list[i][0]
                                        == seoutcome15_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome15_list[i + j][1] == 1:
                                            seoutcome15_list[
                                                i + j
                                            ] = sereport_table_15_changed_1[0]
                                            sereport_table_15_changed_1.remove(
                                                sereport_table_15_changed_1[0]
                                            )
                                        elif seoutcome15_list[i + j][1] == 4:
                                            seoutcome15_list[
                                                i + j
                                            ] = sereport_table_15_changed_4[0]
                                            sereport_table_15_changed_4.remove(
                                                sereport_table_15_changed_4[0]
                                            )
                            for i in seoutcome15_list:
                                sevalue_15 = sevalue_15 + i[3]
                            # outcome for 4+3*2
                            sevalue_16 = 0
                            seoutcome16_list = [
                                sereport_table_4[0],
                                sereport_table_3[0],
                                sereport_table_3[1],
                            ]
                            seplayer_list_16 = []
                            for i in seoutcome16_list:
                                if i[0] != 0:
                                    seplayer_list_16.append(i[0])
                            sereport_table_16_changed_3 = sereport_table_3[2:]
                            sereport_table_16_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_16_changed_3:
                                if i[0] in seplayer_list_16:
                                    sereport_table_16_changed_3.remove(i)
                            for i in sereport_table_16_changed_4:
                                if i[0] in seplayer_list_16:
                                    sereport_table_16_changed_4.remove(i)
                            for i in range(len(seoutcome16_list)):
                                for j in range(1, (len(seoutcome16_list) - i)):
                                    if (
                                        seoutcome16_list[i][0]
                                        == seoutcome16_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome16_list[i + j][1] == 3:
                                            seoutcome16_list[
                                                i + j
                                            ] = sereport_table_16_changed_3[0]
                                            sereport_table_16_changed_3.remove(
                                                sereport_table_16_changed_3[0]
                                            )
                                        elif seoutcome16_list[i + j][1] == 4:
                                            seoutcome16_list[
                                                i + j
                                            ] = sereport_table_16_changed_4[0]
                                            sereport_table_16_changed_4.remove(
                                                sereport_table_16_changed_4[0]
                                            )
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
                            seplayer_list_17 = []
                            for i in seoutcome17_list:
                                if i[0] != 0:
                                    seplayer_list_17.append(i[0])
                            sereport_table_17_changed_1 = sereport_table_1[1:]
                            sereport_table_17_changed_2 = sereport_table_2[1:]
                            sereport_table_17_changed_3 = sereport_table_3[1:]
                            sereport_table_17_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_17_changed_1:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_1.remove(i)
                            for i in sereport_table_17_changed_2:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_2.remove(i)
                            for i in sereport_table_17_changed_3:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_3.remove(i)
                            for i in sereport_table_17_changed_4:
                                if i[0] in seplayer_list_17:
                                    sereport_table_17_changed_4.remove(i)
                            for i in range(len(seoutcome17_list)):
                                for j in range(1, (len(seoutcome17_list) - i)):
                                    if (
                                        seoutcome17_list[i][0]
                                        == seoutcome17_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome17_list[i + j][1] == 1:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_1[0]
                                            sereport_table_17_changed_1.remove(
                                                sereport_table_17_changed_1[0]
                                            )
                                        elif seoutcome17_list[i + j][1] == 2:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_2[0]
                                            sereport_table_17_changed_2.remove(
                                                sereport_table_17_changed_2[0]
                                            )
                                        elif seoutcome17_list[i + j][1] == 3:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_3[0]
                                            sereport_table_17_changed_3.remove(
                                                sereport_table_17_changed_3[0]
                                            )
                                        elif seoutcome17_list[i + j][1] == 4:
                                            seoutcome17_list[
                                                i + j
                                            ] = sereport_table_17_changed_4[0]
                                            sereport_table_17_changed_4.remove(
                                                sereport_table_17_changed_4[0]
                                            )
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
                            seplayer_list_18 = []
                            for i in seoutcome18_list:
                                if i[0] != 0:
                                    seplayer_list_18.append(i[0])
                            sereport_table_18_changed_1 = sereport_table_1[3:]
                            sereport_table_18_changed_3 = sereport_table_3[1:]
                            sereport_table_18_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_18_changed_1:
                                if i[0] in seplayer_list_18:
                                    sereport_table_18_changed_1.remove(i)
                            for i in sereport_table_18_changed_3:
                                if i[0] in seplayer_list_18:
                                    sereport_table_18_changed_3.remove(i)
                            for i in sereport_table_18_changed_4:
                                if i[0] in seplayer_list_18:
                                    sereport_table_18_changed_4.remove(i)
                            for i in range(len(seoutcome18_list)):
                                for j in range(1, (len(seoutcome18_list) - i)):
                                    if (
                                        seoutcome18_list[i][0]
                                        == seoutcome18_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome18_list[i + j][1] == 1:
                                            seoutcome18_list[
                                                i + j
                                            ] = sereport_table_18_changed_1[0]
                                            sereport_table_18_changed_1.remove(
                                                sereport_table_18_changed_1[0]
                                            )
                                        elif seoutcome18_list[i + j][1] == 3:
                                            seoutcome18_list[
                                                i + j
                                            ] = sereport_table_18_changed_3[0]
                                            sereport_table_18_changed_3.remove(
                                                sereport_table_18_changed_3[0]
                                            )
                                        elif seoutcome18_list[i + j][1] == 4:
                                            seoutcome18_list[
                                                i + j
                                            ] = sereport_table_18_changed_4[0]
                                            sereport_table_18_changed_4.remove(
                                                sereport_table_18_changed_4[0]
                                            )
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
                            seplayer_list_19 = []
                            for i in seoutcome19_list:
                                if i[0] != 0:
                                    seplayer_list_19.append(i[0])
                            sereport_table_19_changed_2 = sereport_table_2[3:]
                            sereport_table_19_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_19_changed_2:
                                if i[0] in seplayer_list_19:
                                    sereport_table_19_changed_2.remove(i)
                            for i in sereport_table_19_changed_4:
                                if i[0] in seplayer_list_19:
                                    sereport_table_19_changed_4.remove(i)
                            for i in range(len(seoutcome19_list)):
                                for j in range(1, (len(seoutcome19_list) - i)):
                                    if (
                                        seoutcome19_list[i][0]
                                        == seoutcome19_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome19_list[i + j][1] == 2:
                                            seoutcome19_list[
                                                i + j
                                            ] = sereport_table_19_changed_2[0]
                                            sereport_table_19_changed_2.remove(
                                                sereport_table_19_changed_2[0]
                                            )
                                        elif seoutcome19_list[i + j][1] == 4:
                                            seoutcome19_list[
                                                i + j
                                            ] = sereport_table_19_changed_4[0]
                                            sereport_table_19_changed_4.remove(
                                                sereport_table_19_changed_4[0]
                                            )
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
                            seplayer_list_20 = []
                            for i in seoutcome20_list:
                                if i[0] != 0:
                                    seplayer_list_20.append(i[0])
                            sereport_table_20_changed_1 = sereport_table_1[2:]
                            sereport_table_20_changed_2 = sereport_table_2[2:]
                            sereport_table_20_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_20_changed_1:
                                if i[0] in seplayer_list_20:
                                    sereport_table_20_changed_1.remove(i)
                            for i in sereport_table_20_changed_2:
                                if i[0] in seplayer_list_20:
                                    sereport_table_20_changed_2.remove(i)
                            for i in sereport_table_20_changed_4:
                                if i[0] in seplayer_list_20:
                                    sereport_table_20_changed_4.remove(i)
                            for i in range(len(seoutcome20_list)):
                                for j in range(1, (len(seoutcome20_list) - i)):
                                    if (
                                        seoutcome20_list[i][0]
                                        == seoutcome20_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome20_list[i + j][1] == 1:
                                            seoutcome20_list[
                                                i + j
                                            ] = sereport_table_20_changed_1[0]
                                            sereport_table_20_changed_1.remove(
                                                sereport_table_20_changed_1[0]
                                            )
                                        elif seoutcome20_list[i + j][1] == 2:
                                            seoutcome20_list[
                                                i + j
                                            ] = sereport_table_20_changed_2[0]
                                            sereport_table_20_changed_2.remove(
                                                sereport_table_20_changed_2[0]
                                            )
                                        elif seoutcome20_list[i + j][1] == 4:
                                            seoutcome20_list[
                                                i + j
                                            ] = sereport_table_20_changed_4[0]
                                            sereport_table_20_changed_4.remove(
                                                sereport_table_20_changed_4[0]
                                            )
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
                            seplayer_list_21 = []
                            for i in seoutcome21_list:
                                if i[0] != 0:
                                    seplayer_list_21.append(i[0])
                            sereport_table_21_changed_1 = sereport_table_1[4:]
                            sereport_table_21_changed_2 = sereport_table_2[1:]
                            sereport_table_21_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_21_changed_1:
                                if i[0] in seplayer_list_21:
                                    sereport_table_21_changed_1.remove(i)
                            for i in sereport_table_21_changed_2:
                                if i[0] in seplayer_list_21:
                                    sereport_table_21_changed_2.remove(i)
                            for i in sereport_table_21_changed_4:
                                if i[0] in seplayer_list_21:
                                    sereport_table_21_changed_4.remove(i)
                            for i in range(len(seoutcome21_list)):
                                for j in range(1, (len(seoutcome21_list) - i)):
                                    if (
                                        seoutcome21_list[i][0]
                                        == seoutcome21_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome21_list[i + j][1] == 1:
                                            seoutcome21_list[
                                                i + j
                                            ] = sereport_table_21_changed_1[0]
                                            sereport_table_21_changed_1.remove(
                                                sereport_table_21_changed_1[0]
                                            )
                                        elif seoutcome21_list[i + j][1] == 2:
                                            seoutcome21_list[
                                                i + j
                                            ] = sereport_table_21_changed_2[0]
                                            sereport_table_21_changed_2.remove(
                                                sereport_table_21_changed_2[0]
                                            )
                                        elif seoutcome21_list[i + j][1] == 4:
                                            seoutcome21_list[
                                                i + j
                                            ] = sereport_table_21_changed_4[0]
                                            sereport_table_21_changed_4.remove(
                                                sereport_table_21_changed_4[0]
                                            )
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
                            seplayer_list_22 = []
                            for i in seoutcome22_list:
                                if i[0] != 0:
                                    seplayer_list_22.append(i[0])
                            sereport_table_22_changed_1 = sereport_table_1[6:]
                            sereport_table_22_changed_4 = sereport_table_4[1:]
                            for i in sereport_table_22_changed_1:
                                if i[0] in seplayer_list_22:
                                    sereport_table_22_changed_1.remove(i)
                            for i in sereport_table_22_changed_4:
                                if i[0] in seplayer_list_22:
                                    sereport_table_22_changed_4.remove(i)
                            for i in range(len(seoutcome22_list)):
                                for j in range(1, (len(seoutcome22_list) - i)):
                                    if (
                                        seoutcome22_list[i][0]
                                        == seoutcome22_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome22_list[i + j][1] == 1:
                                            seoutcome22_list[
                                                i + j
                                            ] = sereport_table_22_changed_1[0]
                                            sereport_table_22_changed_1.remove(
                                                sereport_table_22_changed_1[0]
                                            )
                                        elif seoutcome22_list[i + j][1] == 4:
                                            seoutcome22_list[
                                                i + j
                                            ] = sereport_table_22_changed_4[0]
                                            sereport_table_22_changed_4.remove(
                                                sereport_table_22_changed_4[0]
                                            )
                            for i in seoutcome22_list:
                                sevalue_22 = sevalue_22 + i[3]
                            # outcome for 5*2
                            sevalue_23 = 0
                            seoutcome23_list = [
                                sereport_table_5[0],
                                sereport_table_5[1],
                            ]
                            seplayer_list_23 = []
                            for i in seoutcome23_list:
                                if i[0] != 0:
                                    seplayer_list_23.append(i[0])
                            sereport_table_23_changed_5 = sereport_table_5[2:]
                            for i in sereport_table_23_changed_5:
                                if i[0] in seplayer_list_23:
                                    sereport_table_23_changed_5.remove(i)
                            for i in range(len(seoutcome23_list)):
                                for j in range(1, (len(seoutcome23_list) - i)):
                                    if (
                                        seoutcome23_list[i][0]
                                        == seoutcome23_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome23_list[i + j][1] == 5:
                                            seoutcome23_list[
                                                i + j
                                            ] = sereport_table_23_changed_5[0]
                                            sereport_table_23_changed_5.remove(
                                                sereport_table_23_changed_5[0]
                                            )
                            for i in seoutcome23_list:
                                sevalue_23 = sevalue_23 + i[3]
                            # outcome for 5+4+1
                            sevalue_24 = 0
                            seoutcome24_list = [
                                sereport_table_5[0],
                                sereport_table_4[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_24 = []
                            for i in seoutcome24_list:
                                if i[0] != 0:
                                    seplayer_list_24.append(i[0])
                            sereport_table_24_changed_1 = sereport_table_1[1:]
                            sereport_table_24_changed_4 = sereport_table_4[1:]
                            sereport_table_24_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_24_changed_1:
                                if i[0] in seplayer_list_24:
                                    sereport_table_24_changed_1.remove(i)
                            for i in sereport_table_24_changed_4:
                                if i[0] in seplayer_list_24:
                                    sereport_table_24_changed_4.remove(i)
                            for i in sereport_table_24_changed_5:
                                if i[0] in seplayer_list_24:
                                    sereport_table_24_changed_5.remove(i)
                            for i in range(len(seoutcome24_list)):
                                for j in range(1, (len(seoutcome24_list) - i)):
                                    if (
                                        seoutcome24_list[i][0]
                                        == seoutcome24_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome24_list[i + j][1] == 1:
                                            seoutcome24_list[
                                                i + j
                                            ] = sereport_table_24_changed_1[0]
                                            sereport_table_24_changed_1.remove(
                                                sereport_table_24_changed_1[0]
                                            )
                                        elif seoutcome24_list[i + j][1] == 4:
                                            seoutcome24_list[
                                                i + j
                                            ] = sereport_table_24_changed_4[0]
                                            sereport_table_24_changed_4.remove(
                                                sereport_table_24_changed_4[0]
                                            )
                                        elif seoutcome24_list[i + j][1] == 5:
                                            seoutcome24_list[
                                                i + j
                                            ] = sereport_table_24_changed_5[0]
                                            sereport_table_24_changed_5.remove(
                                                sereport_table_24_changed_5[0]
                                            )
                            for i in seoutcome24_list:
                                sevalue_24 = sevalue_24 + i[3]
                            # outcome for 5+3+2
                            sevalue_25 = 0
                            seoutcome25_list = [
                                sereport_table_5[0],
                                sereport_table_3[0],
                                sereport_table_2[0],
                            ]
                            seplayer_list_25 = []
                            for i in seoutcome25_list:
                                if i[0] != 0:
                                    seplayer_list_25.append(i[0])
                            sereport_table_25_changed_2 = sereport_table_2[1:]
                            sereport_table_25_changed_3 = sereport_table_3[1:]
                            sereport_table_25_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_25_changed_2:
                                if i[0] in seplayer_list_25:
                                    sereport_table_25_changed_2.remove(i)
                            for i in sereport_table_25_changed_3:
                                if i[0] in seplayer_list_25:
                                    sereport_table_25_changed_3.remove(i)
                            for i in sereport_table_25_changed_5:
                                if i[0] in seplayer_list_25:
                                    sereport_table_25_changed_5.remove(i)
                            for i in range(len(seoutcome25_list)):
                                for j in range(1, (len(seoutcome25_list) - i)):
                                    if (
                                        seoutcome25_list[i][0]
                                        == seoutcome25_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome25_list[i + j][1] == 2:
                                            seoutcome25_list[
                                                i + j
                                            ] = sereport_table_25_changed_2[0]
                                            sereport_table_25_changed_2.remove(
                                                sereport_table_25_changed_2[0]
                                            )
                                        elif seoutcome25_list[i + j][1] == 3:
                                            seoutcome25_list[
                                                i + j
                                            ] = sereport_table_25_changed_3[0]
                                            sereport_table_25_changed_3.remove(
                                                sereport_table_25_changed_3[0]
                                            )
                                        elif seoutcome25_list[i + j][1] == 5:
                                            seoutcome25_list[
                                                i + j
                                            ] = sereport_table_25_changed_5[0]
                                            sereport_table_25_changed_5.remove(
                                                sereport_table_25_changed_5[0]
                                            )
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
                            seplayer_list_26 = []
                            for i in seoutcome26_list:
                                if i[0] != 0:
                                    seplayer_list_26.append(i[0])
                            sereport_table_26_changed_1 = sereport_table_1[2:]
                            sereport_table_26_changed_3 = sereport_table_3[1:]
                            sereport_table_26_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_26_changed_1:
                                if i[0] in seplayer_list_26:
                                    sereport_table_26_changed_1.remove(i)
                            for i in sereport_table_26_changed_3:
                                if i[0] in seplayer_list_26:
                                    sereport_table_26_changed_3.remove(i)
                            for i in sereport_table_26_changed_5:
                                if i[0] in seplayer_list_26:
                                    sereport_table_26_changed_5.remove(i)
                            for i in range(len(seoutcome26_list)):
                                for j in range(1, (len(seoutcome26_list) - i)):
                                    if (
                                        seoutcome26_list[i][0]
                                        == seoutcome26_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome26_list[i + j][1] == 1:
                                            seoutcome26_list[
                                                i + j
                                            ] = sereport_table_26_changed_1[0]
                                            sereport_table_26_changed_1.remove(
                                                sereport_table_26_changed_1[0]
                                            )
                                        elif seoutcome26_list[i + j][1] == 3:
                                            seoutcome26_list[
                                                i + j
                                            ] = sereport_table_26_changed_3[0]
                                            sereport_table_26_changed_3.remove(
                                                sereport_table_26_changed_3[0]
                                            )
                                        elif seoutcome26_list[i + j][1] == 5:
                                            seoutcome26_list[
                                                i + j
                                            ] = sereport_table_26_changed_5[0]
                                            sereport_table_26_changed_5.remove(
                                                sereport_table_26_changed_5[0]
                                            )
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
                            seplayer_list_27 = []
                            for i in seoutcome27_list:
                                if i[0] != 0:
                                    seplayer_list_27.append(i[0])
                            sereport_table_27_changed_1 = sereport_table_1[1:]
                            sereport_table_27_changed_2 = sereport_table_2[2:]
                            sereport_table_27_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_27_changed_1:
                                if i[0] in seplayer_list_27:
                                    sereport_table_27_changed_1.remove(i)
                            for i in sereport_table_27_changed_2:
                                if i[0] in seplayer_list_27:
                                    sereport_table_27_changed_2.remove(i)
                            for i in sereport_table_27_changed_5:
                                if i[0] in seplayer_list_27:
                                    sereport_table_27_changed_5.remove(i)
                            for i in range(len(seoutcome27_list)):
                                for j in range(1, (len(seoutcome27_list) - i)):
                                    if (
                                        seoutcome27_list[i][0]
                                        == seoutcome27_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome27_list[i + j][1] == 1:
                                            seoutcome27_list[
                                                i + j
                                            ] = sereport_table_27_changed_1[0]
                                            sereport_table_27_changed_1.remove(
                                                sereport_table_27_changed_1[0]
                                            )
                                        elif seoutcome27_list[i + j][1] == 2:
                                            seoutcome27_list[
                                                i + j
                                            ] = sereport_table_27_changed_2[0]
                                            sereport_table_27_changed_2.remove(
                                                sereport_table_27_changed_2[0]
                                            )
                                        elif seoutcome27_list[i + j][1] == 5:
                                            seoutcome27_list[
                                                i + j
                                            ] = sereport_table_27_changed_5[0]
                                            sereport_table_27_changed_5.remove(
                                                sereport_table_27_changed_5[0]
                                            )
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
                            seplayer_list_28 = []
                            for i in seoutcome28_list:
                                if i[0] != 0:
                                    seplayer_list_28.append(i[0])
                            sereport_table_28_changed_1 = sereport_table_1[3:]
                            sereport_table_28_changed_2 = sereport_table_2[1:]
                            sereport_table_28_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_28_changed_1:
                                if i[0] in seplayer_list_28:
                                    sereport_table_28_changed_1.remove(i)
                            for i in sereport_table_28_changed_2:
                                if i[0] in seplayer_list_28:
                                    sereport_table_28_changed_2.remove(i)
                            for i in sereport_table_28_changed_5:
                                if i[0] in seplayer_list_28:
                                    sereport_table_28_changed_5.remove(i)
                            for i in range(len(seoutcome28_list)):
                                for j in range(1, (len(seoutcome28_list) - i)):
                                    if (
                                        seoutcome28_list[i][0]
                                        == seoutcome28_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome28_list[i + j][1] == 1:
                                            seoutcome28_list[
                                                i + j
                                            ] = sereport_table_28_changed_1[0]
                                            sereport_table_28_changed_1.remove(
                                                sereport_table_28_changed_1[0]
                                            )
                                        elif seoutcome28_list[i + j][1] == 2:
                                            seoutcome28_list[
                                                i + j
                                            ] = sereport_table_28_changed_2[0]
                                            sereport_table_28_changed_2.remove(
                                                sereport_table_28_changed_2[0]
                                            )
                                        elif seoutcome28_list[i + j][1] == 5:
                                            seoutcome28_list[
                                                i + j
                                            ] = sereport_table_28_changed_5[0]
                                            sereport_table_28_changed_5.remove(
                                                sereport_table_28_changed_5[0]
                                            )
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
                            seplayer_list_29 = []
                            for i in seoutcome29_list:
                                if i[0] != 0:
                                    seplayer_list_29.append(i[0])
                            sereport_table_29_changed_1 = sereport_table_1[5:]
                            sereport_table_29_changed_5 = sereport_table_5[1:]
                            for i in sereport_table_29_changed_1:
                                if i[0] in seplayer_list_29:
                                    sereport_table_29_changed_1.remove(i)
                            for i in sereport_table_29_changed_5:
                                if i[0] in seplayer_list_29:
                                    sereport_table_29_changed_5.remove(i)
                            for i in range(len(seoutcome29_list)):
                                for j in range(1, (len(seoutcome29_list) - i)):
                                    if (
                                        seoutcome29_list[i][0]
                                        == seoutcome29_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome29_list[i + j][1] == 1:
                                            seoutcome29_list[
                                                i + j
                                            ] = sereport_table_29_changed_1[0]
                                            sereport_table_29_changed_1.remove(
                                                sereport_table_29_changed_1[0]
                                            )
                                        elif seoutcome29_list[i + j][1] == 5:
                                            seoutcome29_list[
                                                i + j
                                            ] = sereport_table_29_changed_5[0]
                                            sereport_table_29_changed_5.remove(
                                                sereport_table_29_changed_5[0]
                                            )
                            for i in seoutcome29_list:
                                sevalue_29 = sevalue_29 + i[3]
                            # outcome for 6+4
                            sevalue_30 = 0
                            seoutcome30_list = [
                                sereport_table_6[0],
                                sereport_table_4[0],
                            ]
                            seplayer_list_30 = []
                            for i in seoutcome30_list:
                                if i[0] != 0:
                                    seplayer_list_30.append(i[0])
                            sereport_table_30_changed_4 = sereport_table_4[1:]
                            sereport_table_30_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_30_changed_4:
                                if i[0] in seplayer_list_30:
                                    sereport_table_30_changed_4.remove(i)
                            for i in sereport_table_30_changed_6:
                                if i[0] in seplayer_list_30:
                                    sereport_table_30_changed_6.remove(i)
                            for i in range(len(seoutcome30_list)):
                                for j in range(1, (len(seoutcome30_list) - i)):
                                    if (
                                        seoutcome30_list[i][0]
                                        == seoutcome30_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome30_list[i + j][1] == 4:
                                            seoutcome30_list[
                                                i + j
                                            ] = sereport_table_30_changed_4[0]
                                            sereport_table_30_changed_4.remove(
                                                sereport_table_30_changed_4[0]
                                            )
                                        elif seoutcome30_list[i + j][1] == 6:
                                            seoutcome30_list[
                                                i + j
                                            ] = sereport_table_30_changed_6[0]
                                            sereport_table_30_changed_6.remove(
                                                sereport_table_30_changed_6[0]
                                            )
                            for i in seoutcome30_list:
                                sevalue_30 = sevalue_30 + i[3]
                            # outcome for 6+3+1
                            sevalue_31 = 0
                            seoutcome31_list = [
                                sereport_table_6[0],
                                sereport_table_3[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_31 = []
                            for i in seoutcome31_list:
                                if i[0] != 0:
                                    seplayer_list_31.append(i[0])
                            sereport_table_31_changed_1 = sereport_table_1[1:]
                            sereport_table_31_changed_3 = sereport_table_3[1:]
                            sereport_table_31_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_31_changed_1:
                                if i[0] in seplayer_list_31:
                                    sereport_table_31_changed_1.remove(i)
                            for i in sereport_table_31_changed_3:
                                if i[0] in seplayer_list_31:
                                    sereport_table_31_changed_3.remove(i)
                            for i in sereport_table_31_changed_6:
                                if i[0] in seplayer_list_31:
                                    sereport_table_31_changed_6.remove(i)
                            for i in range(len(seoutcome31_list)):
                                for j in range(1, (len(seoutcome31_list) - i)):
                                    if (
                                        seoutcome31_list[i][0]
                                        == seoutcome31_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome31_list[i + j][1] == 1:
                                            seoutcome31_list[
                                                i + j
                                            ] = sereport_table_31_changed_1[0]
                                            sereport_table_31_changed_1.remove(
                                                sereport_table_31_changed_1[0]
                                            )
                                        elif seoutcome31_list[i + j][1] == 3:
                                            seoutcome31_list[
                                                i + j
                                            ] = sereport_table_31_changed_3[0]
                                            sereport_table_31_changed_3.remove(
                                                sereport_table_31_changed_3[0]
                                            )
                                        elif seoutcome31_list[i + j][1] == 6:
                                            seoutcome31_list[
                                                i + j
                                            ] = sereport_table_31_changed_6[0]
                                            sereport_table_31_changed_6.remove(
                                                sereport_table_31_changed_6[0]
                                            )
                            for i in seoutcome31_list:
                                sevalue_31 = sevalue_31 + i[3]
                            # outcome for 6+2*2
                            sevalue_32 = 0
                            seoutcome32_list = [
                                sereport_table_6[0],
                                sereport_table_2[0],
                                sereport_table_2[1],
                            ]
                            seplayer_list_32 = []
                            for i in seoutcome32_list:
                                if i[0] != 0:
                                    seplayer_list_32.append(i[0])
                            sereport_table_32_changed_2 = sereport_table_2[2:]
                            sereport_table_32_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_32_changed_2:
                                if i[0] in seplayer_list_32:
                                    sereport_table_32_changed_2.remove(i)
                            for i in sereport_table_32_changed_6:
                                if i[0] in seplayer_list_32:
                                    sereport_table_32_changed_6.remove(i)
                            for i in range(len(seoutcome32_list)):
                                for j in range(1, (len(seoutcome32_list) - i)):
                                    if (
                                        seoutcome32_list[i][0]
                                        == seoutcome32_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome32_list[i + j][1] == 2:
                                            seoutcome32_list[
                                                i + j
                                            ] = sereport_table_32_changed_2[0]
                                            sereport_table_32_changed_2.remove(
                                                sereport_table_32_changed_2[0]
                                            )
                                        elif seoutcome32_list[i + j][1] == 6:
                                            seoutcome32_list[
                                                i + j
                                            ] = sereport_table_32_changed_6[0]
                                            sereport_table_32_changed_6.remove(
                                                sereport_table_32_changed_6[0]
                                            )
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
                            seplayer_list_33 = []
                            for i in seoutcome33_list:
                                if i[0] != 0:
                                    seplayer_list_33.append(i[0])
                            sereport_table_33_changed_1 = sereport_table_1[2:]
                            sereport_table_33_changed_2 = sereport_table_2[1:]
                            sereport_table_33_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_33_changed_1:
                                if i[0] in seplayer_list_33:
                                    sereport_table_33_changed_1.remove(i)
                            for i in sereport_table_33_changed_2:
                                if i[0] in seplayer_list_33:
                                    sereport_table_33_changed_2.remove(i)
                            for i in sereport_table_33_changed_6:
                                if i[0] in seplayer_list_33:
                                    sereport_table_33_changed_6.remove(i)
                            for i in range(len(seoutcome33_list)):
                                for j in range(1, (len(seoutcome33_list) - i)):
                                    if (
                                        seoutcome33_list[i][0]
                                        == seoutcome33_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome33_list[i + j][1] == 1:
                                            seoutcome33_list[
                                                i + j
                                            ] = sereport_table_33_changed_1[0]
                                            sereport_table_33_changed_1.remove(
                                                sereport_table_33_changed_1[0]
                                            )
                                        elif seoutcome33_list[i + j][1] == 2:
                                            seoutcome33_list[
                                                i + j
                                            ] = sereport_table_33_changed_2[0]
                                            sereport_table_33_changed_2.remove(
                                                sereport_table_33_changed_2[0]
                                            )
                                        elif seoutcome33_list[i + j][1] == 6:
                                            seoutcome33_list[
                                                i + j
                                            ] = sereport_table_33_changed_6[0]
                                            sereport_table_33_changed_6.remove(
                                                sereport_table_33_changed_6[0]
                                            )
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
                            seplayer_list_34 = []
                            for i in seoutcome34_list:
                                if i[0] != 0:
                                    seplayer_list_34.append(i[0])
                            sereport_table_34_changed_1 = sereport_table_1[4:]
                            sereport_table_34_changed_6 = sereport_table_6[1:]
                            for i in sereport_table_34_changed_1:
                                if i[0] in seplayer_list_34:
                                    sereport_table_34_changed_1.remove(i)
                            for i in sereport_table_34_changed_6:
                                if i[0] in seplayer_list_34:
                                    sereport_table_34_changed_6.remove(i)
                            for i in range(len(seoutcome34_list)):
                                for j in range(1, (len(seoutcome34_list) - i)):
                                    if (
                                        seoutcome34_list[i][0]
                                        == seoutcome34_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome34_list[i + j][1] == 1:
                                            seoutcome34_list[
                                                i + j
                                            ] = sereport_table_34_changed_1[0]
                                            sereport_table_34_changed_1.remove(
                                                sereport_table_34_changed_1[0]
                                            )
                                        elif seoutcome34_list[i + j][1] == 6:
                                            seoutcome32_list[
                                                i + j
                                            ] = sereport_table_34_changed_6[0]
                                            sereport_table_34_changed_6.remove(
                                                sereport_table_34_changed_6[0]
                                            )
                            for i in seoutcome34_list:
                                sevalue_34 = sevalue_34 + i[3]
                            # outcome for 7+3
                            sevalue_35 = 0
                            seoutcome35_list = [
                                sereport_table_7[0],
                                sereport_table_3[0],
                            ]
                            seplayer_list_35 = []
                            for i in seoutcome35_list:
                                if i[0] != 0:
                                    seplayer_list_35.append(i[0])
                            sereport_table_35_changed_3 = sereport_table_3[1:]
                            sereport_table_35_changed_7 = sereport_table_7[1:]
                            for i in sereport_table_35_changed_3:
                                if i[0] in seplayer_list_35:
                                    sereport_table_35_changed_3.remove(i)
                            for i in sereport_table_35_changed_7:
                                if i[0] in seplayer_list_35:
                                    sereport_table_35_changed_7.remove(i)
                            for i in range(len(seoutcome35_list)):
                                for j in range(1, (len(seoutcome35_list) - i)):
                                    if (
                                        seoutcome35_list[i][0]
                                        == seoutcome35_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome35_list[i + j][1] == 3:
                                            seoutcome35_list[
                                                i + j
                                            ] = sereport_table_35_changed_3[0]
                                            sereport_table_35_changed_3.remove(
                                                sereport_table_35_changed_3[0]
                                            )
                                        elif seoutcome35_list[i + j][1] == 7:
                                            seoutcome35_list[
                                                i + j
                                            ] = sereport_table_35_changed_7[0]
                                            sereport_table_35_changed_7.remove(
                                                sereport_table_35_changed_7[0]
                                            )
                            for i in seoutcome35_list:
                                sevalue_35 = sevalue_35 + i[3]
                            # outcome for 7+2+1
                            sevalue_36 = 0
                            seoutcome36_list = [
                                sereport_table_7[0],
                                sereport_table_2[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_36 = []
                            for i in seoutcome36_list:
                                if i[0] != 0:
                                    seplayer_list_36.append(i[0])
                            sereport_table_36_changed_1 = sereport_table_1[2:]
                            sereport_table_36_changed_2 = sereport_table_2[1:]
                            sereport_table_36_changed_7 = sereport_table_7[1:]
                            for i in sereport_table_36_changed_1:
                                if i[0] in seplayer_list_36:
                                    sereport_table_36_changed_1.remove(i)
                            for i in sereport_table_36_changed_2:
                                if i[0] in seplayer_list_36:
                                    sereport_table_36_changed_2.remove(i)
                            for i in sereport_table_36_changed_7:
                                if i[0] in seplayer_list_36:
                                    sereport_table_36_changed_7.remove(i)
                            for i in range(len(seoutcome36_list)):
                                for j in range(1, (len(seoutcome36_list) - i)):
                                    if (
                                        seoutcome36_list[i][0]
                                        == seoutcome36_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome36_list[i + j][1] == 1:
                                            seoutcome36_list[
                                                i + j
                                            ] = sereport_table_36_changed_1[0]
                                            sereport_table_36_changed_1.remove(
                                                sereport_table_36_changed_1[0]
                                            )
                                        elif seoutcome36_list[i + j][1] == 2:
                                            seoutcome36_list[
                                                i + j
                                            ] = sereport_table_36_changed_2[0]
                                            sereport_table_36_changed_2.remove(
                                                sereport_table_36_changed_2[0]
                                            )
                                        elif seoutcome36_list[i + j][1] == 7:
                                            seoutcome36_list[
                                                i + j
                                            ] = sereport_table_36_changed_7[0]
                                            sereport_table_36_changed_7.remove(
                                                sereport_table_36_changed_7[0]
                                            )
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
                            seplayer_list_37 = []
                            for i in seoutcome37_list:
                                if i[0] != 0:
                                    seplayer_list_37.append(i[0])
                            sereport_table_37_changed_1 = sereport_table_1[3:]
                            sereport_table_37_changed_7 = sereport_table_7[1:]
                            for i in sereport_table_37_changed_1:
                                if i[0] in seplayer_list_37:
                                    sereport_table_37_changed_1.remove(i)
                            for i in sereport_table_37_changed_7:
                                if i[0] in seplayer_list_37:
                                    sereport_table_37_changed_7.remove(i)
                            for i in range(len(seoutcome37_list)):
                                for j in range(1, (len(seoutcome37_list) - i)):
                                    if (
                                        seoutcome37_list[i][0]
                                        == seoutcome37_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome37_list[i + j][1] == 1:
                                            seoutcome37_list[
                                                i + j
                                            ] = sereport_table_37_changed_1[0]
                                            sereport_table_37_changed_1.remove(
                                                sereport_table_37_changed_1[0]
                                            )
                                        elif outcome37_list[i + j][1] == 7:
                                            seoutcome37_list[
                                                i + j
                                            ] = sereport_table_37_changed_7[0]
                                            sereport_table_37_changed_7.remove(
                                                sereport_table_37_changed_7[0]
                                            )
                            for i in seoutcome37_list:
                                sevalue_37 = sevalue_37 + i[3]
                            # outcome for 8+2
                            sevalue_38 = 0
                            seoutcome38_list = [
                                sereport_table_8[0],
                                sereport_table_2[0],
                            ]
                            seplayer_list_38 = []
                            for i in seoutcome38_list:
                                if i[0] != 0:
                                    seplayer_list_38.append(i[0])
                            sereport_table_38_changed_2 = sereport_table_2[1:]
                            sereport_table_38_changed_8 = sereport_table_8[1:]
                            for i in sereport_table_38_changed_2:
                                if i[0] in seplayer_list_38:
                                    sereport_table_38_changed_2.remove(i)
                            for i in sereport_table_38_changed_8:
                                if i[0] in seplayer_list_38:
                                    sereport_table_38_changed_8.remove(i)
                            for i in range(len(seoutcome38_list)):
                                for j in range(1, (len(seoutcome38_list) - i)):
                                    if (
                                        seoutcome38_list[i][0]
                                        == seoutcome38_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome38_list[i + j][1] == 2:
                                            seoutcome38_list[
                                                i + j
                                            ] = sereport_table_38_changed_2[0]
                                            sereport_table_38_changed_2.remove(
                                                sereport_table_38_changed_2[0]
                                            )
                                        elif seoutcome38_list[i + j][1] == 8:
                                            seoutcome38_list[
                                                i + j
                                            ] = sereport_table_38_changed_8[0]
                                            sereport_table_38_changed_8.remove(
                                                sereport_table_38_changed_8[0]
                                            )
                            for i in seoutcome38_list:
                                sevalue_38 = sevalue_38 + i[3]
                            # outcome for 8+1*2
                            sevalue_39 = 0
                            seoutcome39_list = [
                                sereport_table_8[0],
                                sereport_table_1[0],
                                sereport_table_1[1],
                            ]
                            seplayer_list_39 = []
                            for i in seoutcome39_list:
                                if i[0] != 0:
                                    seplayer_list_39.append(i[0])
                            sereport_table_39_changed_1 = sereport_table_1[2:]
                            sereport_table_39_changed_8 = sereport_table_8[1:]
                            for i in sereport_table_39_changed_1:
                                if i[0] in seplayer_list_39:
                                    sereport_table_39_changed_1.remove(i)
                            for i in sereport_table_39_changed_8:
                                if i[0] in seplayer_list_39:
                                    sereport_table_39_changed_8.remove(i)
                            for i in range(len(seoutcome39_list)):
                                for j in range(1, (len(seoutcome39_list) - i)):
                                    if (
                                        seoutcome39_list[i][0]
                                        == seoutcome39_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome39_list[i + j][1] == 1:
                                            seoutcome39_list[
                                                i + j
                                            ] = sereport_table_39_changed_1[0]
                                            sereport_table_39_changed_1.remove(
                                                sereport_table_39_changed_1[0]
                                            )
                                        elif seoutcome39_list[i + j][1] == 8:
                                            seoutcome39_list[
                                                i + j
                                            ] = sereport_table_39_changed_8[0]
                                            sereport_table_39_changed_8.remove(
                                                sereport_table_39_changed_8[0]
                                            )
                            for i in seoutcome39_list:
                                sevalue_39 = sevalue_39 + i[3]
                            # outcome for 9+1
                            sevalue_40 = 0
                            seoutcome40_list = [
                                sereport_table_9[0],
                                sereport_table_1[0],
                            ]
                            seplayer_list_40 = []
                            for i in seoutcome40_list:
                                if i[0] != 0:
                                    seplayer_list_40.append(i[0])
                            sereport_table_40_changed_1 = sereport_table_1[1:]
                            sereport_table_40_changed_9 = sereport_table_9[1:]
                            for i in sereport_table_40_changed_1:
                                if i[0] in seplayer_list_40:
                                    sereport_table_40_changed_1.remove(i)
                            for i in sereport_table_40_changed_9:
                                if i[0] in seplayer_list_40:
                                    sereport_table_40_changed_9.remove(i)
                            for i in range(len(seoutcome40_list)):
                                for j in range(1, (len(seoutcome40_list) - i)):
                                    if (
                                        seoutcome40_list[i][0]
                                        == seoutcome40_list[i + j][0]
                                        != 0
                                    ):
                                        if seoutcome40_list[i + j][1] == 1:
                                            seoutcome40_list[
                                                i + j
                                            ] = sereport_table_40_changed_1[0]
                                            sereport_table_40_changed_1.remove(
                                                sereport_table_40_changed_1[0]
                                            )
                                        elif seoutcome40_list[i + j][1] == 9:
                                            seoutcome40_list[
                                                i + j
                                            ] = sereport_table_40_changed_9[0]
                                            sereport_table_40_changed_9.remove(
                                                sereport_table_40_changed_9[0]
                                            )
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
bug = 448
average utility changed under truth-telling strategy: 3.6416
"""

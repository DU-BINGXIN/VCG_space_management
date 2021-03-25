import pandas as pd
import numpy as np
import random

# table = 9, course = 3, consumer = 30


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


def getIndexesrandom(p, p_report):
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
            listOfPos.append((row, col, random.randint(0, 20)))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos


res_revenue_total_1 = 0
social_value_total_1 = 0
res_revenue_total_2 = 0
social_value_total_2 = 0
res_revenue_total_3 = 0
social_value_total_3 = 0
res_revenue_total_4 = 0
social_value_total_4 = 0
res_revenue_total_5 = 0
social_value_total_5 = 0
res_revenue_total_6 = 0
social_value_total_6 = 0
res_revenue_total_7 = 0
social_value_total_7 = 0
res_revenue_total_8 = 0
social_value_total_8 = 0
res_revenue_total_9 = 0
social_value_total_9 = 0
res_revenue_total_10 = 0
social_value_total_10 = 0
for z in range(10000):
    consumer = 20
    report_1_table = []
    report_2_table = []
    report_3_table = []
    report_4_table = []
    report_5_table = []
    report_6_table = []
    report_7_table = []
    report_8_table = []
    report_9_table = []
    report_10_table = []
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
        pi_report_1 = [i + 1,] + getIndexes(pi, pi_value_1)[0]
        report_1_table = report_1_table + [pi_report_1]
        # two reported situation
        pi_value_2 = pi_value_list[1]
        if pi_value_1 == pi_value_2:
            pi_report_2 = [i + 1,] + getIndexes(pi, pi_value_2)[1]
        else:
            pi_report_2 = [i + 1,] + getIndexes(pi, pi_value_2)[0]
        report_2_table = report_2_table + [pi_report_1] + [pi_report_2]
        # three reported situation
        pi_value_3 = pi_value_list[2]
        if pi_value_3 == pi_value_1:
            pi_report_3 = [i + 1,] + getIndexes(pi, pi_value_3)[2]
        elif pi_value_3 == pi_value_2 != pi_value_1:
            pi_report_3 = [i + 1,] + getIndexes(pi, pi_value_3)[1]
        else:
            pi_report_3 = [i + 1,] + getIndexes(pi, pi_value_3)[0]
        report_3_table = report_3_table + [pi_report_1] + [pi_report_2] + [pi_report_3]
        # four reported situation
        pi_value_4 = pi_value_list[3]
        if pi_value_4 == pi_value_1:
            pi_report_4 = [i + 1,] + getIndexes(pi, pi_value_4)[3]
        elif pi_value_4 == pi_value_2 != pi_value_1:
            pi_report_4 = [i + 1,] + getIndexes(pi, pi_value_4)[2]
        elif pi_value_4 == pi_value_3 != pi_value_2:
            pi_report_4 = [i + 1,] + getIndexes(pi, pi_value_4)[1]
        else:
            pi_report_4 = [i + 1,] + getIndexes(pi, pi_value_4)[0]
        report_4_table = (
            report_4_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
        )
        # five reported situation
        pi_value_5 = pi_value_list[4]
        if pi_value_5 == pi_value_1:
            pi_report_5 = [i + 1,] + getIndexes(pi, pi_value_5)[4]
        elif pi_value_5 == pi_value_2 != pi_value_1:
            pi_report_5 = [i + 1,] + getIndexes(pi, pi_value_5)[3]
        elif pi_value_5 == pi_value_3 != pi_value_2:
            pi_report_5 = [i + 1,] + getIndexes(pi, pi_value_5)[2]
        elif pi_value_5 == pi_value_4 != pi_value_3:
            pi_report_5 = [i + 1,] + getIndexes(pi, pi_value_5)[1]
        else:
            pi_report_5 = [i + 1,] + getIndexes(pi, pi_value_5)[0]
        report_5_table = (
            report_5_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
            + [pi_report_5]
        )
        # six reported situation
        pi_value_6 = pi_value_list[5]
        if pi_value_6 == pi_value_1:
            pi_report_6 = [i + 1,] + getIndexes(pi, pi_value_6)[5]
        elif pi_value_6 == pi_value_2 != pi_value_1:
            pi_report_6 = [i + 1,] + getIndexes(pi, pi_value_6)[4]
        elif pi_value_6 == pi_value_3 != pi_value_2:
            pi_report_6 = [i + 1,] + getIndexes(pi, pi_value_6)[3]
        elif pi_value_6 == pi_value_4 != pi_value_3:
            pi_report_6 = [i + 1,] + getIndexes(pi, pi_value_6)[2]
        elif pi_value_6 == pi_value_5 != pi_value_4:
            pi_report_6 = [i + 1,] + getIndexes(pi, pi_value_6)[1]
        else:
            pi_report_6 = [i + 1,] + getIndexes(pi, pi_value_6)[0]
        report_6_table = (
            report_6_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
            + [pi_report_5]
            + [pi_report_6]
        )
        # seven reported situation
        pi_value_7 = pi_value_list[6]
        if pi_value_7 == pi_value_1:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[6]
        elif pi_value_7 == pi_value_2 != pi_value_1:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[5]
        elif pi_value_7 == pi_value_3 != pi_value_2:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[4]
        elif pi_value_7 == pi_value_4 != pi_value_3:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[3]
        elif pi_value_7 == pi_value_5 != pi_value_4:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[2]
        elif pi_value_7 == pi_value_6 != pi_value_5:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[1]
        else:
            pi_report_7 = [i + 1,] + getIndexes(pi, pi_value_7)[0]
        report_7_table = (
            report_7_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
            + [pi_report_5]
            + [pi_report_6]
            + [pi_report_7]
        )
        # eight reported situation
        pi_value_8 = pi_value_list[7]
        if pi_value_8 == pi_value_1:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[7]
        elif pi_value_8 == pi_value_2 != pi_value_1:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[6]
        elif pi_value_8 == pi_value_3 != pi_value_2:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[5]
        elif pi_value_8 == pi_value_4 != pi_value_3:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[4]
        elif pi_value_8 == pi_value_5 != pi_value_4:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[3]
        elif pi_value_8 == pi_value_6 != pi_value_5:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[2]
        elif pi_value_8 == pi_value_7 != pi_value_6:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[1]
        else:
            pi_report_8 = [i + 1,] + getIndexes(pi, pi_value_8)[0]
        report_8_table = (
            report_8_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
            + [pi_report_5]
            + [pi_report_6]
            + [pi_report_7]
            + [pi_report_8]
        )
        # nine reported situation
        pi_value_9 = pi_value_list[8]
        if pi_value_9 == pi_value_1:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[8]
        elif pi_value_9 == pi_value_2 != pi_value_1:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[7]
        elif pi_value_9 == pi_value_3 != pi_value_2:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[6]
        elif pi_value_9 == pi_value_4 != pi_value_3:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[5]
        elif pi_value_9 == pi_value_5 != pi_value_4:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[4]
        elif pi_value_9 == pi_value_6 != pi_value_5:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[3]
        elif pi_value_9 == pi_value_7 != pi_value_6:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[2]
        elif pi_value_9 == pi_value_8 != pi_value_7:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[1]
        else:
            pi_report_9 = [i + 1,] + getIndexes(pi, pi_value_9)[0]
        report_9_table = (
            report_9_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
            + [pi_report_5]
            + [pi_report_6]
            + [pi_report_7]
            + [pi_report_8]
            + [pi_report_9]
        )
        # ten reported situation
        pi_value_10 = pi_value_list[9]
        if pi_value_10 == pi_value_1:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[9]
        elif pi_value_10 == pi_value_2 != pi_value_1:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[8]
        elif pi_value_10 == pi_value_3 != pi_value_2:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[7]
        elif pi_value_10 == pi_value_4 != pi_value_3:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[6]
        elif pi_value_10 == pi_value_5 != pi_value_4:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[5]
        elif pi_value_10 == pi_value_6 != pi_value_5:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[4]
        elif pi_value_10 == pi_value_7 != pi_value_6:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[3]
        elif pi_value_10 == pi_value_8 != pi_value_7:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[2]
        elif pi_value_10 == pi_value_9 != pi_value_8:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[1]
        else:
            pi_report_10 = [i + 1,] + getIndexes(pi, pi_value_10)[0]
        report_10_table = (
            report_10_table
            + [pi_report_1]
            + [pi_report_2]
            + [pi_report_3]
            + [pi_report_4]
            + [pi_report_5]
            + [pi_report_6]
            + [pi_report_7]
            + [pi_report_8]
            + [pi_report_9]
            + [pi_report_10]
        )
    print(
        "----------------truth telling with one reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_1_table)):
        if report_1_table[i][1] == 1:
            report_table_1.append(report_1_table[i])
        elif report_1_table[i][1] == 2:
            report_table_2.append(report_1_table[i])
        elif report_1_table[i][1] == 3:
            report_table_3.append(report_1_table[i])
        elif report_1_table[i][1] == 4:
            report_table_4.append(report_1_table[i])
        elif report_1_table[i][1] == 5:
            report_table_5.append(report_1_table[i])
        elif report_1_table[i][1] == 6:
            report_table_6.append(report_1_table[i])

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_1 = res_revenue_total_1 + res_revenue
    social_value_total_1 = social_value_total_1 + social_value

    print(
        "----------------truth telling with two reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_2_table)):
        if report_2_table[i][1] == 1:
            report_table_1.append(report_2_table[i])
        elif report_2_table[i][1] == 2:
            report_table_2.append(report_2_table[i])
        elif report_2_table[i][1] == 3:
            report_table_3.append(report_2_table[i])
        elif report_2_table[i][1] == 4:
            report_table_4.append(report_2_table[i])
        elif report_2_table[i][1] == 5:
            report_table_5.append(report_2_table[i])
        elif report_2_table[i][1] == 6:
            report_table_6.append(report_2_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_2 = res_revenue_total_2 + res_revenue
    social_value_total_2 = social_value_total_2 + social_value

    print(
        "----------------truth telling with three reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_3_table)):
        if report_3_table[i][1] == 1:
            report_table_1.append(report_3_table[i])
        elif report_3_table[i][1] == 2:
            report_table_2.append(report_3_table[i])
        elif report_3_table[i][1] == 3:
            report_table_3.append(report_3_table[i])
        elif report_3_table[i][1] == 4:
            report_table_4.append(report_3_table[i])
        elif report_3_table[i][1] == 5:
            report_table_5.append(report_3_table[i])
        elif report_3_table[i][1] == 6:
            report_table_6.append(report_3_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_3 = res_revenue_total_3 + res_revenue
    social_value_total_3 = social_value_total_3 + social_value

    print(
        "----------------truth telling with four reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_4_table)):
        if report_4_table[i][1] == 1:
            report_table_1.append(report_4_table[i])
        elif report_4_table[i][1] == 2:
            report_table_2.append(report_4_table[i])
        elif report_4_table[i][1] == 3:
            report_table_3.append(report_4_table[i])
        elif report_4_table[i][1] == 4:
            report_table_4.append(report_4_table[i])
        elif report_4_table[i][1] == 5:
            report_table_5.append(report_4_table[i])
        elif report_4_table[i][1] == 6:
            report_table_6.append(report_4_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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
    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_4 = res_revenue_total_4 + res_revenue
    social_value_total_4 = social_value_total_4 + social_value

    print(
        "----------------truth telling with five reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_5_table)):
        if report_5_table[i][1] == 1:
            report_table_1.append(report_5_table[i])
        elif report_5_table[i][1] == 2:
            report_table_2.append(report_5_table[i])
        elif report_5_table[i][1] == 3:
            report_table_3.append(report_5_table[i])
        elif report_5_table[i][1] == 4:
            report_table_4.append(report_5_table[i])
        elif report_5_table[i][1] == 5:
            report_table_5.append(report_5_table[i])
        elif report_5_table[i][1] == 6:
            report_table_6.append(report_5_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_5 = res_revenue_total_5 + res_revenue
    social_value_total_5 = social_value_total_5 + social_value

    print(
        "----------------truth telling with six reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_6_table)):
        if report_6_table[i][1] == 1:
            report_table_1.append(report_6_table[i])
        elif report_6_table[i][1] == 2:
            report_table_2.append(report_6_table[i])
        elif report_6_table[i][1] == 3:
            report_table_3.append(report_6_table[i])
        elif report_6_table[i][1] == 4:
            report_table_4.append(report_6_table[i])
        elif report_6_table[i][1] == 5:
            report_table_5.append(report_6_table[i])
        elif report_6_table[i][1] == 6:
            report_table_6.append(report_6_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_6 = res_revenue_total_6 + res_revenue
    social_value_total_6 = social_value_total_6 + social_value

    print(
        "----------------truth telling with seven reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_7_table)):
        if report_7_table[i][1] == 1:
            report_table_1.append(report_7_table[i])
        elif report_7_table[i][1] == 2:
            report_table_2.append(report_7_table[i])
        elif report_7_table[i][1] == 3:
            report_table_3.append(report_7_table[i])
        elif report_7_table[i][1] == 4:
            report_table_4.append(report_7_table[i])
        elif report_7_table[i][1] == 5:
            report_table_5.append(report_7_table[i])
        elif report_7_table[i][1] == 6:
            report_table_6.append(report_7_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_7 = res_revenue_total_7 + res_revenue
    social_value_total_7 = social_value_total_7 + social_value

    print(
        "----------------truth telling with eight reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_8_table)):
        if report_8_table[i][1] == 1:
            report_table_1.append(report_8_table[i])
        elif report_8_table[i][1] == 2:
            report_table_2.append(report_8_table[i])
        elif report_8_table[i][1] == 3:
            report_table_3.append(report_8_table[i])
        elif report_8_table[i][1] == 4:
            report_table_4.append(report_8_table[i])
        elif report_8_table[i][1] == 5:
            report_table_5.append(report_8_table[i])
        elif report_8_table[i][1] == 6:
            report_table_6.append(report_8_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_8 = res_revenue_total_8 + res_revenue
    social_value_total_8 = social_value_total_8 + social_value

    print(
        "----------------truth telling with nine reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_9_table)):
        if report_9_table[i][1] == 1:
            report_table_1.append(report_9_table[i])
        elif report_9_table[i][1] == 2:
            report_table_2.append(report_9_table[i])
        elif report_9_table[i][1] == 3:
            report_table_3.append(report_9_table[i])
        elif report_9_table[i][1] == 4:
            report_table_4.append(report_9_table[i])
        elif report_9_table[i][1] == 5:
            report_table_5.append(report_9_table[i])
        elif report_9_table[i][1] == 6:
            report_table_6.append(report_9_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]
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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_9 = res_revenue_total_9 + res_revenue
    social_value_total_9 = social_value_total_9 + social_value

    print(
        "----------------truth telling with ten reported combination-------------------"
    )
    # classify tables with table numbers
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    report_table_6 = []
    for i in range(len(report_10_table)):
        if report_10_table[i][1] == 1:
            report_table_1.append(report_10_table[i])
        elif report_10_table[i][1] == 2:
            report_table_2.append(report_10_table[i])
        elif report_10_table[i][1] == 3:
            report_table_3.append(report_10_table[i])
        elif report_10_table[i][1] == 4:
            report_table_4.append(report_10_table[i])
        elif report_10_table[i][1] == 5:
            report_table_5.append(report_10_table[i])
        elif report_10_table[i][1] == 6:
            report_table_6.append(report_10_table[i])

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

    report_table_1.sort(key=takeValue, reverse=True)
    report_table_2.sort(key=takeValue, reverse=True)
    report_table_3.sort(key=takeValue, reverse=True)
    report_table_4.sort(key=takeValue, reverse=True)
    report_table_5.sort(key=takeValue, reverse=True)
    report_table_6.sort(key=takeValue, reverse=True)

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

    # find the optimal outcome
    for v in range(len(values)):
        value_v = values[v]
        if value_v == max(values):
            social_value = value_v
            res_revenue = 0
            for m in range(len(outcomes_list)):
                outcome_m = outcomes_list[m]
                if m == v:
                    for p in outcome_m:
                        if p[0] == 0:
                            pass
                        else:
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
                            sereport_table_1 = [
                                k for k in report_table_1 if k[0] != p[0]
                            ]
                            sereport_table_2 = [
                                k for k in report_table_2 if k[0] != p[0]
                            ]
                            sereport_table_3 = [
                                k for k in report_table_3 if k[0] != p[0]
                            ]
                            sereport_table_4 = [
                                k for k in report_table_4 if k[0] != p[0]
                            ]
                            sereport_table_5 = [
                                k for k in report_table_5 if k[0] != p[0]
                            ]
                            sereport_table_6 = [
                                k for k in report_table_6 if k[0] != p[0]
                            ]

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
                                    utility = p[3] - monetary_transfer
                                    res_revenue = res_revenue + monetary_transfer
                                    print("utility for", p[0], ":", utility)
                                    break
                                else:
                                    pass
            print("social value:", social_value, "restaurant revenue:", res_revenue)
            break
        else:
            pass
    res_revenue_total_10 = res_revenue_total_10 + res_revenue
    social_value_total_10 = social_value_total_10 + social_value

ave_res_revenue_1 = res_revenue_total_1 / 10000
ave_social_value_1 = social_value_total_1 / 10000
print(
    "一つ入札:",
    "average social value:",
    ave_social_value_1,
    "average restaurant revenue:",
    ave_res_revenue_1,
)
ave_res_revenue_2 = res_revenue_total_2 / 10000
ave_social_value_2 = social_value_total_2 / 10000
print(
    "二つ入札:",
    "average social value:",
    ave_social_value_2,
    "average restaurant revenue:",
    ave_res_revenue_2,
)
ave_res_revenue_3 = res_revenue_total_3 / 10000
ave_social_value_3 = social_value_total_3 / 10000
print(
    "三つ入札:",
    "average social value:",
    ave_social_value_3,
    "average restaurant revenue:",
    ave_res_revenue_3,
)
ave_res_revenue_4 = res_revenue_total_4 / 10000
ave_social_value_4 = social_value_total_4 / 10000
print(
    "四つ入札:",
    "average social value:",
    ave_social_value_4,
    "average restaurant revenue:",
    ave_res_revenue_4,
)
ave_res_revenue_5 = res_revenue_total_5 / 10000
ave_social_value_5 = social_value_total_5 / 10000
print(
    "五つ入札:",
    "average social value:",
    ave_social_value_5,
    "average restaurant revenue:",
    ave_res_revenue_5,
)
ave_res_revenue_6 = res_revenue_total_6 / 10000
ave_social_value_6 = social_value_total_6 / 10000
print(
    "六つ入札:",
    "average social value:",
    ave_social_value_6,
    "average restaurant revenue:",
    ave_res_revenue_6,
)
ave_res_revenue_7 = res_revenue_total_7 / 10000
ave_social_value_7 = social_value_total_7 / 10000
print(
    "七つ入札:",
    "average social value:",
    ave_social_value_7,
    "average restaurant revenue:",
    ave_res_revenue_7,
)
ave_res_revenue_8 = res_revenue_total_8 / 10000
ave_social_value_8 = social_value_total_8 / 10000
print(
    "八つ入札:",
    "average social value:",
    ave_social_value_8,
    "average restaurant revenue:",
    ave_res_revenue_8,
)
ave_res_revenue_9 = res_revenue_total_9 / 10000
ave_social_value_9 = social_value_total_9 / 10000
print(
    "九つ入札:",
    "average social value:",
    ave_social_value_9,
    "average restaurant revenue:",
    ave_res_revenue_9,
)
ave_res_revenue_10 = res_revenue_total_10 / 10000
ave_social_value_10 = social_value_total_10 / 10000
print(
    "十つ入札:",
    "average social value:",
    ave_social_value_10,
    "average restaurant revenue:",
    ave_res_revenue_10,
)
"""
Result:
一つ入札: average social value: 95.3444 average restaurant revenue: 79.9487
二つ入札: average social value: 98.9953 average restaurant revenue: 95.4707
三つ入札: average social value: 99.1822 average restaurant revenue: 96.7917
四つ入札: average social value: 99.2012 average restaurant revenue: 96.8923
五つ入札: average social value: 99.2041 average restaurant revenue: 96.9115
六つ入札: average social value: 99.2045 average restaurant revenue: 96.9152
七つ入札: average social value: 99.2046 average restaurant revenue: 96.915
八つ入札: average social value: 99.2046 average restaurant revenue: 96.915
九つ入札: average social value: 99.2046 average restaurant revenue: 96.915
十つ入札: average social value: 99.2046 average restaurant revenue: 96.915
"""

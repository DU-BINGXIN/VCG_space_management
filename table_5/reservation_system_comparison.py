from numpy.lib.function_base import average
import pandas as pd
import random
import copy
# table = 5, course = 3


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
#random.seed(0)
bug=0
total_res_rev_1=0
total_res_rev_2=0
total_utility_1=0
total_utility_2=0
for z in range(1):
    print("----------- round", z, "-----------")
    consumer = 10
    fixed_price = 15
    report_table1 = []
    report_table = []
    random_table = []
    res_revenue1 = 0
    res_revenue2 = 0
    utility1=0
    utility2=0
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
        pi_table1_list=[pi["A"].tolist()[0],pi["B"].tolist()[0],pi["C"].tolist()[0]]
        pi_table1_value_set=sorted(set(pi_table1_list),key=pi_table1_list.index)
        pi_table1_value=max(pi_table1_value_set)
        if pi_table1_value >= fixed_price:
            pi_table_1=getIndexes(pi, pi_table1_value)
            for table_1 in pi_table_1:
                if table_1[0] == 1:
                    pi_table1 = [i + 1,] + table_1
                    break
            report_table1 = report_table1 + [pi_table1]
        pi_value_list.sort(reverse=True)
        pi_value_list2 = sorted(set(pi_value_list),key=pi_value_list.index)
        for value2 in pi_value_list2:
            for j in range(pi_value_list.count(value2)):
                pi_report = [i + 1,] + getIndexes(pi, value2)[j]
                report_table = report_table + [pi_report]
    print("first come first serve comsumer list : ", report_table1)
    if len(report_table1)<4:
        res_revenue1=fixed_price*len(report_table1)
    else:
        res_revenue1=fixed_price*4
    while len(report_table1)<4:
        report_table1.append([0, 1, 0, 0])
    for onetablevalue in report_table1[:4]:
        if onetablevalue[3] != 0:
            utility1=utility1+onetablevalue[3]-fixed_price
    social_value1=res_revenue1+utility1
    print("res_revenue1 : ", res_revenue1, "utility1 : ", utility1, "social value 1 : ", social_value1)
    report_table_1 = []
    report_table_2 = []
    report_table_3 = []
    report_table_4 = []
    report_table_5 = []
    for com in report_table:
        if com[1] == 1:
            report_table_1.append(com)
        elif com[1] == 2:
            report_table_2.append(com)
        elif com[1] == 3:
            report_table_3.append(com)
        elif com[1] == 4:
            report_table_4.append(com)
        elif com[1] == 5:
            report_table_5.append(com)

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
    report_table_1_changed_copy1 = copy.deepcopy(report_table_1_changed)
    for i in report_table_1_changed_copy1:
        if i[0] in player_list_1:
            report_table_1_changed.remove(i)
    for i in range(len(outcome1_list)):
        for j in range(1, (len(outcome1_list) - i)):
            report_table_1_changed_copy2 = copy.deepcopy(report_table_1_changed)
            if outcome1_list[i][0] == outcome1_list[i + j][0] != 0:
                outcome1_list[i + j] = report_table_1_changed[0]
                for k in report_table_1_changed_copy2:
                    if outcome1_list[i + j][0] == k[0]:
                        report_table_1_changed.remove(k)
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
    report_table_2_changed_1_copy1 = copy.deepcopy(report_table_2_changed_1)
    report_table_2_changed_2_copy1 = copy.deepcopy(report_table_2_changed_2)
    for i in report_table_2_changed_1_copy1:
        if i[0] in player_list_2:
            report_table_2_changed_1.remove(i)
    for i in report_table_2_changed_2_copy1:
        if i[0] in player_list_2:
            report_table_2_changed_2.remove(i)    
    for i in range(len(outcome2_list)):
        for j in range(1, (len(outcome2_list) - i)):
            report_table_2_changed_1_copy2 = copy.deepcopy(report_table_2_changed_1)
            report_table_2_changed_2_copy2 = copy.deepcopy(report_table_2_changed_2)
            if outcome2_list[i][0] == outcome2_list[i + j][0] != 0:
                if outcome2_list[i + j][1] == 2:
                    outcome2_list[i + j] = report_table_2_changed_1[0]
                    for k in report_table_2_changed_1_copy2:
                        if k[0]==outcome2_list[i + j][0]:
                            report_table_2_changed_1.remove(k)
                elif outcome2_list[i + j][1] == 1:
                    a=outcome2_list[i + j][3] - report_table_2_changed_1[0][3]
                    b=outcome2_list[i][3] - report_table_2_changed_2[0][3]
                    if a>b:
                        outcome2_list[i] = report_table_2_changed_2[0]
                        for k in report_table_2_changed_2_copy2:
                            if k[0]==outcome2_list[i][0]:
                                report_table_2_changed_2.remove(k)
                        for l in report_table_2_changed_1_copy2:
                            if l[0]==outcome2_list[i+j][0]:
                                report_table_2_changed_1.remove(l)                                                         
                    else:
                        outcome2_list[i+j] = report_table_2_changed_1[0]
                        for k in report_table_2_changed_1_copy2:
                            if k[0]==outcome2_list[i+j][0]:
                                report_table_2_changed_1.remove(k)
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
    report_table_3_changed_1_copy1 = copy.deepcopy(report_table_3_changed_1)
    report_table_3_changed_2_copy1 = copy.deepcopy(report_table_3_changed_2)     
    for i in report_table_3_changed_1_copy1:
        if i[0] in player_list_3:
            report_table_3_changed_1.remove(i)
    for i in report_table_3_changed_2_copy1:
        if i[0] in player_list_3:
            report_table_3_changed_2.remove(i) 
    for i in range(len(outcome3_list)):
        for j in range(1, (len(outcome3_list) - i)):
            report_table_3_changed_1_copy2 = copy.deepcopy(report_table_3_changed_1)
            report_table_3_changed_2_copy2 = copy.deepcopy(report_table_3_changed_2)                
            if outcome3_list[i][0] == outcome3_list[i + j][0] != 0:
                a=outcome3_list[i + j][3] - report_table_3_changed_1[0][3]
                b=outcome3_list[i][3] - report_table_3_changed_2[0][3]
                if a>b:
                    if outcome3_list[i][1]==2:
                        outcome3_list[i] = report_table_3_changed_2[0]
                        for k in report_table_3_changed_2_copy2:
                            if k[0]==outcome3_list[i][0]:
                                report_table_3_changed_2.remove(k)
                        for l in report_table_3_changed_1_copy2:
                            if l[0]==outcome3_list[i][0]:
                                report_table_3_changed_1.remove(l)       
                    else:     
                        outcome3_list[i] = report_table_3_changed_1[0]
                        for k in report_table_3_changed_1_copy2:
                            if k[0]==outcome3_list[i][0]:
                                report_table_3_changed_1.remove(k)                  
                else:
                    outcome3_list[i+j] = report_table_3_changed_1[0]
                    for k in report_table_3_changed_1_copy2:
                        if k[0]==outcome3_list[i+j][0]:
                            report_table_3_changed_1.remove(k)  
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
    report_table_4_changed_2_copy1 = copy.deepcopy(report_table_4_changed_2)
    report_table_4_changed_3_copy1 = copy.deepcopy(report_table_4_changed_3)    
    for i in report_table_4_changed_2_copy1:
        if i[0] in player_list_4:
            report_table_4_changed_2.remove(i)
    for i in report_table_4_changed_3_copy1:
        if i[0] in player_list_4:
            report_table_4_changed_3.remove(i)   
    for i in range(len(outcome4_list)):
        for j in range(1, (len(outcome4_list) - i)):
            report_table_4_changed_2_copy2 = copy.deepcopy(report_table_4_changed_2)
            report_table_4_changed_3_copy2 = copy.deepcopy(report_table_4_changed_3) 
            if outcome4_list[i][0] == outcome4_list[i + j][0] != 0:
                a=outcome4_list[i + j][3] - report_table_4_changed_2[0][3]
                b=outcome4_list[i][3] - report_table_4_changed_3[0][3]
                if a>b:
                    outcome4_list[i] = report_table_4_changed_3[0]
                    for k in report_table_4_changed_3_copy2:
                        if k[0]==outcome4_list[i][0]:
                            report_table_4_changed_3.remove(k)        
                else:
                    outcome4_list[i+j] = report_table_4_changed_2[0]
                    for k in report_table_4_changed_2_copy2:
                        if k[0]==outcome4_list[i][0]:
                            report_table_4_changed_2.remove(k)  
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
    report_table_5_changed_1_copy1 = copy.deepcopy(report_table_5_changed_1)
    report_table_5_changed_3_copy1 = copy.deepcopy(report_table_5_changed_3)  
    for i in report_table_5_changed_1_copy1:
        if i[0] in player_list_5:
            report_table_5_changed_1.remove(i)
    for i in report_table_5_changed_3_copy1:
        if i[0] in player_list_5:
            report_table_5_changed_3.remove(i)           
    for i in range(len(outcome5_list)):
        for j in range(1, (len(outcome5_list) - i)):
            report_table_5_changed_1_copy2 = copy.deepcopy(report_table_5_changed_1)
            report_table_5_changed_3_copy2 = copy.deepcopy(report_table_5_changed_3) 
            if outcome5_list[i][0] == outcome5_list[i + j][0] != 0:
                a=outcome5_list[i + j][3] - report_table_5_changed_1[0][3]
                b=outcome5_list[i][3] - report_table_5_changed_3[0][3]
                if a>b:
                    if outcome5_list[i][1]==3:
                        outcome5_list[i] = report_table_5_changed_3[0]
                        for k in report_table_5_changed_3_copy2:
                            if k[0]==outcome5_list[i][0]:
                                report_table_5_changed_3.remove(k)
                        for l in report_table_5_changed_1_copy2:
                            if l[0]==outcome5_list[i][0]:
                                report_table_5_changed_1.remove(l)  
                    else:            
                        outcome5_list[i] = report_table_5_changed_1[0]
                        for k in report_table_5_changed_1_copy2:
                            if k[0]==outcome5_list[i][0]:
                                report_table_5_changed_1.remove(k)                
                else:
                    outcome5_list[i+j] = report_table_5_changed_1[0]
                    for k in report_table_5_changed_1_copy2:
                        if k[0]==outcome5_list[i][0]:
                            report_table_5_changed_1.remove(k)  
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
    report_table_6_changed_1_copy1 = copy.deepcopy(report_table_6_changed_1)
    report_table_6_changed_4_copy1 = copy.deepcopy(report_table_6_changed_4)    
    for i in report_table_6_changed_1_copy1:
        if i[0] in player_list_6:
            report_table_6_changed_1.remove(i)
    for i in report_table_6_changed_4_copy1:
        if i[0] in player_list_6:
            report_table_6_changed_4.remove(i) 
    for i in range(len(outcome6_list)):
        for j in range(1, (len(outcome6_list) - i)):
            report_table_6_changed_1_copy2 = copy.deepcopy(report_table_6_changed_1)
            report_table_6_changed_4_copy2 = copy.deepcopy(report_table_6_changed_4) 
            if outcome6_list[i][0] == outcome6_list[i + j][0] != 0:
                a=outcome6_list[i + j][3] - report_table_6_changed_1[0][3]
                b=outcome6_list[i][3] - report_table_6_changed_4[0][3]
                if a>b:
                    outcome6_list[i] = report_table_6_changed_4[0]
                    for k in report_table_6_changed_4_copy2:
                        if k[0]==outcome6_list[i][0]:
                            report_table_6_changed_4.remove(k)
                else:
                    outcome6_list[i+j] = report_table_6_changed_1[0]
                    for k in report_table_6_changed_1_copy2:
                        if k[0]==outcome6_list[i][0]:
                            report_table_6_changed_1.remove(k)  
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
    values = [
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
                        sereport_table_1_changed_copy1=copy.deepcopy(sereport_table_1_changed)
                        for i in sereport_table_1_changed_copy1:
                            if i[0] in seplayer_list_1:
                                sereport_table_1_changed.remove(i)
                        for i in range(len(seoutcome1_list)):
                            for j in range(1, (len(seoutcome1_list) - i)):
                                sereport_table_1_changed_copy2=copy.deepcopy(sereport_table_1_changed)
                                if (
                                    seoutcome1_list[i][0]
                                    == seoutcome1_list[i + j][0]
                                    != 0
                                ):
                                    seoutcome1_list[
                                        i + j
                                    ] = sereport_table_1_changed[0]
                                    for k in sereport_table_1_changed_copy2:
                                        if k[0]==seoutcome1_list[i+j][0]:
                                            sereport_table_1_changed.remove(k)
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
                        sereport_table_2_changed_1_copy1 = copy.deepcopy(sereport_table_2_changed_1)
                        sereport_table_2_changed_2_copy1 = copy.deepcopy(sereport_table_2_changed_2)
                        for i in sereport_table_2_changed_1_copy1:
                            if i[0] in seplayer_list_2:
                                sereport_table_2_changed_1.remove(i)
                        for i in sereport_table_2_changed_2_copy1:
                            if i[0] in seplayer_list_2:
                                sereport_table_2_changed_2.remove(i)   
                        for i in range(len(seoutcome2_list)):
                            for j in range(1, (len(seoutcome2_list) - i)):
                                sereport_table_2_changed_1_copy2 = copy.deepcopy(sereport_table_2_changed_1)
                                sereport_table_2_changed_2_copy2 = copy.deepcopy(sereport_table_2_changed_2) 
                                if seoutcome2_list[i][0] == seoutcome2_list[i + j][0] != 0:
                                    if seoutcome2_list[i + j][1] == 2:
                                        seoutcome2_list[i + j] = sereport_table_2_changed_1[0]
                                        for k in sereport_table_2_changed_1_copy2:
                                            if k[0]==seoutcome2_list[i + j][0]:
                                                sereport_table_2_changed_1.remove(k)
                                    elif seoutcome2_list[i + j][1] == 1:
                                        a=seoutcome2_list[i + j][3] - sereport_table_2_changed_1[0][3]
                                        b=seoutcome2_list[i][3] - sereport_table_2_changed_2[0][3]
                                        if a>b:
                                            seoutcome2_list[i] = sereport_table_2_changed_2[0]
                                            for k in sereport_table_2_changed_2_copy2:
                                                if k[0]==seoutcome2_list[i][0]:
                                                    sereport_table_2_changed_2.remove(k)
                                            for l in sereport_table_2_changed_1_copy2:
                                                if l[0]==seoutcome2_list[i+j][0]:
                                                    sereport_table_2_changed_1.remove(l)                                                      
                                        else:
                                            seoutcome2_list[i+j] = sereport_table_2_changed_1[0]
                                            for k in sereport_table_2_changed_1_copy2:
                                                if k[0]==seoutcome2_list[i+j][0]:
                                                    sereport_table_2_changed_1.remove(k)            
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
                        sereport_table_3_changed_1_copy1 = copy.deepcopy(sereport_table_3_changed_1)
                        sereport_table_3_changed_2_copy1 = copy.deepcopy(sereport_table_3_changed_2)     
                        for i in sereport_table_3_changed_1_copy1:
                            if i[0] in seplayer_list_3:
                                sereport_table_3_changed_1.remove(i)
                        for i in sereport_table_3_changed_2_copy1:
                            if i[0] in seplayer_list_3:
                                sereport_table_3_changed_2.remove(i)
                        for i in range(len(seoutcome3_list)):
                            for j in range(1, (len(seoutcome3_list) - i)):
                                sereport_table_3_changed_1_copy2 = copy.deepcopy(sereport_table_3_changed_1)
                                sereport_table_3_changed_2_copy2 = copy.deepcopy(sereport_table_3_changed_2) 
                                if seoutcome3_list[i][0] == seoutcome3_list[i + j][0] != 0:
                                    a=seoutcome3_list[i + j][3] - sereport_table_3_changed_1[0][3]
                                    b=seoutcome3_list[i][3] - sereport_table_3_changed_2[0][3]
                                    if a>b:
                                        if seoutcome3_list[i][1]==2:
                                            seoutcome3_list[i] = sereport_table_3_changed_2[0]
                                            for k in sereport_table_3_changed_2_copy2:
                                                if k[0]==seoutcome3_list[i][0]:
                                                    sereport_table_3_changed_2.remove(k)
                                            for l in sereport_table_3_changed_1_copy2:
                                                if l[0]==seoutcome3_list[i][0]:
                                                    sereport_table_3_changed_1.remove(l)      
                                        else:      
                                            seoutcome3_list[i] = sereport_table_3_changed_1[0]
                                            for k in sereport_table_3_changed_1_copy2:
                                                if k[0]==seoutcome3_list[i][0]:
                                                    sereport_table_3_changed_1.remove(k)                                     
                                    else:
                                        seoutcome3_list[i+j] = sereport_table_3_changed_1[0]
                                        for k in sereport_table_3_changed_1_copy2:
                                            if k[0]==seoutcome3_list[i+j][0]:
                                                sereport_table_3_changed_1.remove(k)
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
                        sereport_table_4_changed_2_copy1 = copy.deepcopy(sereport_table_4_changed_2)
                        sereport_table_4_changed_3_copy1 = copy.deepcopy(sereport_table_4_changed_3)    
                        for i in sereport_table_4_changed_2_copy1:
                            if i[0] in seplayer_list_4:
                                sereport_table_4_changed_2.remove(i)
                        for i in sereport_table_4_changed_3_copy1:
                            if i[0] in seplayer_list_4:
                                sereport_table_4_changed_3.remove(i)   
                        for i in range(len(seoutcome4_list)):
                            for j in range(1, (len(seoutcome4_list) - i)):
                                sereport_table_4_changed_2_copy2 = copy.deepcopy(sereport_table_4_changed_2)
                                sereport_table_4_changed_3_copy2 = copy.deepcopy(sereport_table_4_changed_3) 
                                if seoutcome4_list[i][0] == seoutcome4_list[i + j][0] != 0:
                                    a=seoutcome4_list[i + j][3] - sereport_table_4_changed_2[0][3]
                                    b=seoutcome4_list[i][3] - sereport_table_4_changed_3[0][3]
                                    if a>b:
                                        seoutcome4_list[i] = sereport_table_4_changed_3[0]
                                        for k in sereport_table_4_changed_3_copy2:
                                            if k[0]==seoutcome4_list[i][0]:
                                                sereport_table_4_changed_3.remove(k)
                                    else:
                                        seoutcome4_list[i+j] = sereport_table_4_changed_2[0]
                                        for k in sereport_table_4_changed_2_copy2:
                                            if k[0]==seoutcome4_list[i][0]:
                                                sereport_table_4_changed_2.remove(k)  
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
                        sereport_table_5_changed_1_copy1 = copy.deepcopy(sereport_table_5_changed_1)
                        sereport_table_5_changed_3_copy1 = copy.deepcopy(sereport_table_5_changed_3)  
                        for i in sereport_table_5_changed_1_copy1:
                            if i[0] in seplayer_list_5:
                                sereport_table_5_changed_1.remove(i)
                        for i in sereport_table_5_changed_3_copy1:
                            if i[0] in seplayer_list_5:
                                sereport_table_5_changed_3.remove(i)           
                        for i in range(len(seoutcome5_list)):
                            for j in range(1, (len(seoutcome5_list) - i)):
                                sereport_table_5_changed_1_copy2 = copy.deepcopy(sereport_table_5_changed_1)
                                sereport_table_5_changed_3_copy2 = copy.deepcopy(sereport_table_5_changed_3) 
                                if seoutcome5_list[i][0] == seoutcome5_list[i + j][0] != 0:
                                    a=seoutcome5_list[i + j][3] - sereport_table_5_changed_1[0][3]
                                    b=seoutcome5_list[i][3] - sereport_table_5_changed_3[0][3]
                                    if a>b:
                                        if seoutcome5_list[i][1]==3:
                                            seoutcome5_list[i] = sereport_table_5_changed_3[0]
                                            for k in sereport_table_5_changed_3_copy2:
                                                if k[0]==seoutcome5_list[i][0]:
                                                    sereport_table_5_changed_3.remove(k)
                                            for l in sereport_table_5_changed_1_copy2:
                                                if l[0]==seoutcome5_list[i][0]:
                                                    sereport_table_5_changed_1.remove(l)    
                                        else:    
                                            seoutcome5_list[i] = sereport_table_5_changed_1[0]
                                            for k in sereport_table_5_changed_1_copy2:
                                                if k[0]==seoutcome5_list[i][0]:
                                                    sereport_table_5_changed_1.remove(k)                                          
                                    else:
                                        seoutcome5_list[i+j] = sereport_table_5_changed_1[0]
                                        for k in sereport_table_5_changed_1_copy2:
                                            if k[0]==seoutcome5_list[i][0]:
                                                sereport_table_5_changed_1.remove(k)  
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
                        sereport_table_6_changed_1_copy1 = copy.deepcopy(sereport_table_6_changed_1)
                        sereport_table_6_changed_4_copy1 = copy.deepcopy(sereport_table_6_changed_4)    
                        for i in sereport_table_6_changed_1_copy1:
                            if i[0] in seplayer_list_6:
                                sereport_table_6_changed_1.remove(i)
                        for i in sereport_table_6_changed_4_copy1:
                            if i[0] in seplayer_list_6:
                                sereport_table_6_changed_4.remove(i)  
                        for i in range(len(seoutcome6_list)):
                            for j in range(1, (len(seoutcome6_list) - i)):
                                sereport_table_6_changed_1_copy2 = copy.deepcopy(sereport_table_6_changed_1)
                                sereport_table_6_changed_4_copy2 = copy.deepcopy(sereport_table_6_changed_4)
                                if seoutcome6_list[i][0] == seoutcome6_list[i + j][0] != 0:
                                    a=seoutcome6_list[i + j][3] - sereport_table_6_changed_1[0][3]
                                    b=seoutcome6_list[i][3] - sereport_table_6_changed_4[0][3]
                                    if a>b:
                                        seoutcome6_list[i] = sereport_table_6_changed_4[0]
                                        for k in sereport_table_6_changed_4_copy2:
                                            if k[0]==seoutcome6_list[i][0]:
                                                sereport_table_6_changed_4.remove(k)
                                    else:
                                        seoutcome6_list[i+j] = sereport_table_6_changed_1[0]
                                        for k in sereport_table_6_changed_1_copy2:
                                            if k[0]==seoutcome6_list[i][0]:
                                                sereport_table_6_changed_1.remove(k)  
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
                        seoutcomes_list=[seoutcome1_list,seoutcome2_list,seoutcome3_list,seoutcome4_list,seoutcome5_list,seoutcome6_list,seoutcome7_list]
                        for n in range(len(sevalues)):
                            if sevalues[n] == max(sevalues):
                                second_value = sevalues[n]
                                for o in range(len(seoutcomes_list)):
                                    if o == n:
                                        print(
                                            "second best allocation : ",
                                            seoutcomes_list[o],
                                        )
                                        monetary_transfer = -(social_value - p[3] - second_value)
                                        res_revenue2=res_revenue2+monetary_transfer
                                        utility2=utility2+p[3]-monetary_transfer
                                break
                            else:
                                pass
                    break
            social_value2=res_revenue2+utility2
            print("res_revenue2 : ", res_revenue2, "total utility2 : ", utility2, "social value 2 : ", social_value2)    
            break
        else:
            pass
    if social_value1>social_value2:
        bug=bug+1
    total_res_rev_1=total_res_rev_1+res_revenue1
    total_res_rev_2=total_res_rev_2+res_revenue2
    total_utility_1=total_utility_1+utility1
    total_utility_2=total_utility_2+utility2
average_res_rev_1=total_res_rev_1/100
average_res_rev_2=total_res_rev_2/100
average_utility_1=total_utility_1/100
average_utility_2=total_utility_2/100
print("times when FCFS gives higher social value : ", bug)
print("average restaurant revenue for FCFS : ", average_res_rev_1, "average consumer utility for FCFS : ", average_utility_1)
print("average restaurant revenue for VCG : ", average_res_rev_2, "average consumer utility for VCG : ", average_utility_2)
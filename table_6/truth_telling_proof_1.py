import pandas as pd
import random
import itertools

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


utility_change = 0
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

        truth_table = random_table.copy()
        for j in truth_table:
            if j[0] == 1:
                truth_table.remove(j)
        truth_table.append(p1_report)
    # テーブル数
    seats = 6
    print("--------------------random-telling---------------------------")
    max_outcome = 0
    max_social_value = 0
    sec_social_value = 0
    best_mu = 0
    sec_mu = 0
    utility_random = 0

    for k in range(1, seats):
        mus = list(itertools.combinations(random_table, k))
        for mu in mus:
            player_list = []
            for bid in mu:
                player_list.append(bid[0])
            if len(set(player_list)) != len(player_list):
                mus.remove(mu)
        for mu in mus:
            tmp_social_value = 0
            tmp_seats = 0
            for bid in mu:
                tmp_social_value = tmp_social_value + bid[3]
                tmp_seats = tmp_seats + bid[1]
            if max_social_value < tmp_social_value:
                if tmp_seats <= seats:
                    max_social_value = tmp_social_value
                    best_mu = mu
    for allo in best_mu:
        if allo[0] == 1:
            for j in random_table:
                if j[0] == 1:
                    random_table.remove(j)
            for k in range(1, seats):
                mus = list(itertools.combinations(random_table, k))
                for mu in mus:
                    player_list = []
                    for bid in mu:
                        player_list.append(bid[0])
                    if len(set(player_list)) != len(player_list):
                        mus.remove(mu)
                for mu in mus:
                    tmp_social_value = 0
                    tmp_seats = 0
                    for bid in mu:
                        tmp_social_value = tmp_social_value + bid[3]
                        tmp_seats = tmp_seats + bid[1]
                    if sec_social_value < tmp_social_value:
                        if tmp_seats <= seats:
                            sec_social_value = tmp_social_value
                            sec_mu = mu
            monetary_transfer = -(max_social_value - allo[3] - sec_social_value)
            true_value = p1.loc[allo[1], allo[2]]
            utility_random = true_value - monetary_transfer
    print("best_mu：" + str(best_mu))
    print("max_social_value：" + str(max_social_value))
    print("sec_mu：" + str(sec_mu))
    print("sec_social_value：" + str(sec_social_value))
    print("utility for palyer 1: " + str(utility_random))
    print("---------------------truth-telling----------------------")
    max_outcome = 0
    max_social_value = 0
    sec_social_value = 0
    best_mu = 0
    sec_mu = 0
    utility_truth = 0
    for k in range(1, seats):
        mus = list(itertools.combinations(truth_table, k))
        for mu in mus:
            player_list = []
            for bid in mu:
                player_list.append(bid[0])
            if len(set(player_list)) != len(player_list):
                mus.remove(mu)
        for mu in mus:
            tmp_social_value = 0
            tmp_seats = 0
            for bid in mu:
                tmp_social_value = tmp_social_value + bid[3]
                tmp_seats = tmp_seats + bid[1]
            if max_social_value < tmp_social_value:
                if tmp_seats <= seats:
                    max_social_value = tmp_social_value
                    best_mu = mu
    for allo in best_mu:
        if allo[0] == 1:
            for j in truth_table:
                if j[0] == 1:
                    truth_table.remove(j)
            for k in range(1, seats):
                mus = list(itertools.combinations(truth_table, k))
                for mu in mus:
                    player_list = []
                    for bid in mu:
                        player_list.append(bid[0])
                    if len(set(player_list)) != len(player_list):
                        mus.remove(mu)
                for mu in mus:
                    tmp_social_value = 0
                    tmp_seats = 0
                    for bid in mu:
                        tmp_social_value = tmp_social_value + bid[3]
                        tmp_seats = tmp_seats + bid[1]
                    if sec_social_value < tmp_social_value:
                        if tmp_seats <= seats:
                            sec_social_value = tmp_social_value
                            sec_mu = mu
            monetary_transfer = -(max_social_value - allo[3] - sec_social_value)
            true_value = p1.loc[allo[1], allo[2]]
            utility_truth = true_value - monetary_transfer
    print("best_mu：" + str(best_mu))
    print("max_social_value：" + str(max_social_value))
    print("sec_mu：" + str(sec_mu))
    print("sec_social_value：" + str(sec_social_value))
    print("utility for palyer 1: " + str(utility_truth))

    utility_change = utility_change + (utility_truth - utility_random)
    if utility_random > utility_truth:
        bug = bug + 1

print("bug =", bug)

utility_change = utility_change / 10000
print("average utility changed:", utility_change)
"""
bug = 162
average utility changed: 2.529
"""

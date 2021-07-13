
import itertools
import numpy as np
import random
import copy

revenue_difference = 0
full_capacity_larger=0
for z in range (100):
    print("-----------round", z, "--------------")
    #入札リスト[player, course, number_of_talbes, utility]
    o_l = [['p1', 'C_A', 1, random.randint(0, 20)], ['p1', 'C_A', 2, random.randint(0, 20)], ['p1', 'C_A', 3, random.randint(0, 20)], ['p1', 'C_A', 4, random.randint(0, 20)],['p1', 'C_A', 5, random.randint(0, 20)],
            ['p2', 'C_A', 1, random.randint(0, 20)], ['p2', 'C_A', 2, random.randint(0, 20)], ['p2', 'C_A', 3, random.randint(0, 20)], ['p2', 'C_A', 4, random.randint(0, 20)],['p2', 'C_A', 5, random.randint(0, 20)],
            ['p3', 'C_A', 1, random.randint(0, 20)], ['p3', 'C_A', 2, random.randint(0, 20)], ['p3', 'C_A', 3, random.randint(0, 20)], ['p3', 'C_A', 4, random.randint(0, 20)],['p3', 'C_A', 5, random.randint(0, 20)],
            ['p4', 'C_A', 1, random.randint(0, 20)], ['p4', 'C_A', 2, random.randint(0, 20)], ['p4', 'C_A', 3, random.randint(0, 20)], ['p4', 'C_A', 4, random.randint(0, 20)],['p4', 'C_A', 5, random.randint(0, 20)],
            ['p5', 'C_A', 1, random.randint(0, 20)], ['p5', 'C_A', 2, random.randint(0, 20)], ['p5', 'C_A', 3, random.randint(0, 20)], ['p5', 'C_A', 4, random.randint(0, 20)],['p5', 'C_A', 5, random.randint(0, 20)],
            ['p6', 'C_A', 1, random.randint(0, 20)], ['p6', 'C_A', 2, random.randint(0, 20)], ['p6', 'C_A', 3, random.randint(0, 20)], ['p6', 'C_A', 4, random.randint(0, 20)],['p6', 'C_A', 5, random.randint(0, 20)],
            ]
    #テーブル数
    seats = 5
    max_outcome_wfc = 0
    max_outcome_nfc = 0
    max_social_value_wfc = 0
    max_social_value_nfc = 0
    best_mu_wfc = 0
    best_mu_nfc = 0
    max_social_value_wfc_2 = 0
    max_social_value_nfc_2 = 0
    money_transfer_wfc = 0
    money_transfer_nfc = 0
    for i in range(1,seats+1):
        mus_wfc = list(itertools.combinations(o_l, i))
        mus_wfc_copy = copy.deepcopy(mus_wfc)
        for mu_wfc in mus_wfc:
            player_list_wfc = []
            for bid_wfc in mu_wfc:
                player_list_wfc.append(bid_wfc[0])
            if len(set(player_list_wfc)) != len(player_list_wfc):
                mus_wfc_copy.remove(mu_wfc)
        for mu_wfc_copy in mus_wfc_copy:
            tmp_social_value_wfc = 0
            tmp_seats_wfc = 0
            for bid_wfc_copy in mu_wfc_copy:
                tmp_social_value_wfc = tmp_social_value_wfc + bid_wfc_copy[3]
                tmp_seats_wfc = tmp_seats_wfc + bid_wfc_copy[2]
            if max_social_value_wfc < tmp_social_value_wfc:
                if tmp_seats_wfc <= seats:
                    max_social_value_wfc = tmp_social_value_wfc
                    best_mu_wfc = mu_wfc_copy

    print('best_mu_wfc：'+str(best_mu_wfc))
    print('max_social_value_wfc：' + str(max_social_value_wfc))

    o_l_wfc=copy.deepcopy(o_l)
    for j in range(len(best_mu_wfc)):
        max_social_value_wfc_2_j = 0
        player_wfc_j = best_mu_wfc[j][0]
        value_wfc_j = best_mu_wfc[j][3]
        for allo_wfc in o_l:
            if allo_wfc[0] == player_wfc_j:
                o_l_wfc.remove(allo_wfc)
        for k in range(1,seats+1):
            mus2_wfc_j = list(itertools.combinations(o_l_wfc, k))
            mus2_wfc_j_copy = copy.deepcopy(mus2_wfc_j)
            for mu2_wfc in mus2_wfc_j:
                player_list_wfc_j = []
                for bid2_wfc in mu2_wfc:
                    player_list_wfc_j.append(bid2_wfc[0])
                if len(set(player_list_wfc_j)) != len(player_list_wfc_j):
                    mus2_wfc_j_copy.remove(mu2_wfc)
            for mu2_wfc_copy in mus2_wfc_j_copy:
                tmp_social_value_2_wfc_j = 0
                tmp_seats_2_wfc_j = 0
                for bid2_wfc_copy in mu2_wfc_copy:
                    tmp_social_value_2_wfc_j = tmp_social_value_2_wfc_j + bid2_wfc_copy[3]
                    tmp_seats_2_wfc_j = tmp_seats_2_wfc_j + bid2_wfc_copy[2]
                if max_social_value_wfc_2_j < tmp_social_value_2_wfc_j:
                    if tmp_seats_2_wfc_j <= seats:
                        max_social_value_wfc_2_j = tmp_social_value_2_wfc_j
                        best_mu2_wfc_j = mu2_wfc_copy
        print('best_mu2_wfc：'+str(best_mu2_wfc_j))
        print('max_social_value_2_wfc：' + str(max_social_value_wfc_2_j))       
        money_transfer_wfc = money_transfer_wfc + max_social_value_wfc_2_j - max_social_value_wfc + value_wfc_j
        o_l_wfc=copy.deepcopy(o_l)
    print('money_transfer_wfc：' + str(money_transfer_wfc))

    for l in range(1,seats):
        mus_nfc = list(itertools.combinations(o_l, l))
        mus_nfc_copy = copy.deepcopy(mus_nfc)
        for mu_nfc in mus_nfc:
            player_list_nfc = []
            for bid_nfc in mu_nfc:
                player_list_nfc.append(bid_nfc[0])
            if len(set(player_list_nfc)) != len(player_list_nfc):
                mus_nfc_copy.remove(mu_nfc)
        for mu_nfc_copy in mus_nfc_copy:
            tmp_social_value_nfc = 0
            tmp_seats_nfc = 0
            for bid_nfc_copy in mu_nfc_copy:
                tmp_social_value_nfc = tmp_social_value_nfc + bid_nfc_copy[3]
                tmp_seats_nfc = tmp_seats_nfc + bid_nfc_copy[2]
            if max_social_value_nfc < tmp_social_value_nfc:
                if tmp_seats_nfc <= seats:
                    max_social_value_nfc = tmp_social_value_nfc
                    best_mu_nfc = mu_nfc_copy

    print('best_mu_nfc：'+str(best_mu_nfc))
    print('max_social_value_nfc：' + str(max_social_value_nfc))

    o_l_nfc=copy.deepcopy(o_l)
    for m in range(len(best_mu_nfc)):
        max_social_value_nfc_2_m = 0
        player_nfc_m = best_mu_nfc[m][0]
        value_nfc_m = best_mu_nfc[m][3]
        for allo_nfc in o_l:
            if allo_nfc[0] == player_nfc_m:
                o_l_nfc.remove(allo_nfc)
        for n in range(1,seats):
            mus2_nfc_m = list(itertools.combinations(o_l_nfc, n))
            mus2_nfc_m_copy = copy.deepcopy(mus2_nfc_m)
            for mu2_nfc in mus2_nfc_m:
                player_list_nfc_m = []
                for bid2_nfc in mu2_nfc:
                    player_list_nfc_m.append(bid2_nfc[0])
                if len(set(player_list_nfc_m)) != len(player_list_nfc_m):
                    mus2_nfc_m_copy.remove(mu2_nfc)
            for mu2_nfc_copy in mus2_nfc_m_copy:
                tmp_social_value_2_nfc_m = 0
                tmp_seats_2_nfc_m = 0
                for bid2_nfc_copy in mu2_nfc_copy:
                    tmp_social_value_2_nfc_m = tmp_social_value_2_nfc_m + bid2_nfc_copy[3]
                    tmp_seats_2_nfc_m = tmp_seats_2_nfc_m + bid2_nfc_copy[2]
                if max_social_value_nfc_2_m < tmp_social_value_2_nfc_m:
                    if tmp_seats_2_nfc_m <= seats:
                        max_social_value_nfc_2_m = tmp_social_value_2_nfc_m
                        best_mu2_nfc_m = mu2_nfc_copy
        print('best_mu2_nfc：'+str(best_mu2_nfc_m))
        print('max_social_value_2_nfc：' + str(max_social_value_nfc_2_m))       
        money_transfer_nfc = money_transfer_nfc + max_social_value_nfc_2_m - max_social_value_nfc + value_nfc_m
        o_l_nfc=copy.deepcopy(o_l)
    print('money_transfer_nfc：' + str(money_transfer_nfc))

    if money_transfer_wfc>money_transfer_nfc:
        full_capacity_larger = full_capacity_larger + 1
    revenue_difference = revenue_difference + money_transfer_nfc - money_transfer_wfc

revenue_difference = revenue_difference/100
print('revenue_difference:', revenue_difference)
print('revenue with full capacity is larger:', full_capacity_larger)
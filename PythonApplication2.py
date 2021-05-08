
The_final_array = []
 
 
# step_1
def low_complexity_regions():
    string = "PQGEFRYRYRYG"
    Array = []
    New_Array = []
 
    Array = list(string)
    New_Array = list(string)
    var = 2
    for i in range(len(Array)):
        if Array[i] == Array[var]:
            index1 = i
            index2 = var
            New_Array[index1] = 'X'
            New_Array[index2] = 'X'
            if var == len(Array) - 1:
                var = len(Array) - 1
                New_Array[i] = Array[var]
            else:
                var = var + 1
            continue
        if var == len(Array) - 1:
            var = len(Array) - 1
        else:
            var = var + 1
 
    for i in range(len(New_Array)):
        if New_Array[i] != 'X':
            The_final_array.append(New_Array[i])
 
    print("******************************step_1*************************************")
    for i in The_final_array:
        print(i)
 
 
low_complexity_regions()
 
Array3 = []
 
 
# step_2
def W_letter_word_list():
    for i in range(len(The_final_array)):
        if i <= len(The_final_array) - 3:
            Array3.append(The_final_array[i] + The_final_array[i + 1] + The_final_array[i + 2])
 
    print("**********************************step_2***************************************")
    for i in Array3:
        print(i)
 
 
W_letter_word_list()
 
score_dic = {}
Amino_acid = {"AV": 0, "AY": -2, "AW": -3, "AT": 0, "AS": 1, "AP": -1, "AF": -2, "AM": -1, "AK": -1, "AL": -1, "AI": -1,
              "AH": -2, "AG": 0, "AE": -1, "AQ": -1, "AC": 0, "AD": -2, "AN": -2, "AR": -1, "AA": 4, "RV": -3, "RY": -2,
              "RW": -3, "RT": -1, "RS": -1, "RP": -2, "RF": -3, "RM": -1, "RK": 2, "RL": -2, "RI": -3, "RH": 0,
              "RG": -2, "RE": 0, "RQ": 1, "RC": -3, "RD": -2, "RN": 0, "RR": 5, "RA": -1, "NV": -3, "NY": -2, "NW": -4,
              "NT": 0, "NS": 1, "NP": -2, "NF": -3, "NM": -2, "NK": 0, "NL": -3, "NI": -3, "NH": 1, "NG": 0, "NE": 0,
              "NQ": 0, "NC": -3, "ND": 1, "NN": 6, "NR": 0, "NA": -2, "DV": -3, "DY": -3, "DW": -4, "DT": -1, "DS": 0,
              "DP": -1, "DF": -3, "DM": -3, "DK": -1, "DL": -4, "DI": -3, "DH": -1, "DG": -1, "DE": 2, "DQ": 0,
              "DC": -3, "DD": 6, "DN": 1, "DR": -2, "DA": -2, "CV": -1, "CY": -2, " CW": -2, "CT": -1, "CS": -1,
              "CP": -3, "CF": -2, "CM": -1, "CK": -3, "CL": -1, "CI": -1, "CH": -3, "CG": -3, "CE": -4, "CQ": -3,
              "CC": 9, "CD": -3, "CN": -3, "CR": -3, "CA": 0, "QV": -2, "QY": -1, "QW": -2, "QT": -1, "QS": 0, "QP": -1,
              "QF": -3, "QM": 0, "QK": 1, "QL": -2, "QI": -3, "QH": 0, "QG": -2, "QE": 2, "QQ": 5, "QC": -3, "QD": 0,
              "QN": 0, "QR": 1, "QA": -1, "EV": -2, "EY": -2, "EW": -3, "ET": -1, "ES": 0, "EP": -1, "EF": -3, "EM": -2,
              "EK": 1, "EL": -3, "EI": -3, "EH": 0, "EG": -2, "EE": 5, "EQ": 2, "EC": -4, "ED": 2, "EN": 0, "ER": 0,
              "EA": -1, "GV": -3, "GY": -3, "GW": -2, "GT": -2, "GS": 0, "GP": -2, "GF": -3, "GM": -3, "GK": -2,
              "GL": -4, "GI": -4, "GH": -2, "GG": 6, "GE": -2, "GQ": -2, "GC": -3, "GD": -1, "GN": 0, "GR": -2, "GA": 0,
              "HV": -3, "HY": 2, "HW": -2, "HT": -2, "HS": -1, "HP": -2, "HF": -1, "HM": -2, "HK": -1, "HL": -3,
              "HI": -3, "HH": 8, "HG": -2, "HE": 0, "HQ": 0, "HC": -3, "HD": -1, "HN": 1, "HR": 0, "HA": -2, "IC": -1,
              "IS": -2, "IT": -2, "IP": -3, "IA": -1, "IG": -4, "IN": -3, "ID": -3, "IE": -3, "IQ": -3, "IH": -3,
              "IR": -3, "IK": -3, "IM": 1, "II": 4, "IL": 2, "IV": 3, "IF": 0, "IY": -1, "IW": -3, "LC": -1, "LS": -2,
              "LT": -2, "LP": -3, "LA": -1, "LG": -4, "LN": -3, "LD": -4, "LE": -3, "LQ": -2, "LH": -3, "LR": -2,
              "LK": -2, "LM": 2, "LI": 2, "LL": 4, "LV": 1, "LF": 0, "LY": -1, "LW": -2, "KC": -3, "KS": 0, "KT": 0,
              "KP": -1, "KA": -1, "KG": -2, "KN": 0, "KD": -1, "KE": 1, "KQ": 1, "KH": -1, "KR": 2, "KK": 5, "KM": -1,
              "KI": -3, "KL": -2, "KV": -2, "KF": -3, "KY": -2, "KW": -3, "MC": -1, "MS": -1, "MT": -1, "MP": -2,
              "MA": -1, "MG": -3, "MN": -2, "MD": -3, "ME": -2, "MQ": 0, "MH": -2, "MR": -1, "MK": -1, "MM": 5, "MI": 1,
              "ML": 2, "MV": 1, "MF": 0, "MY": -1, "MW": -1, "FC": -2, "FS": -2, "FT": -2, "FP": -4, "FA": -2, "FG": -3,
              "FN": -3, "FD": -3, "FE": -3, "FQ": -3, "FH": -1, "FR": -3, "FK": -3, "FM": 0, "FI": 0, "FL": 0, "FV": -1,
              "FF": 6, "FY": 3, "FW": 1, "PC": -3, "PS": -1, "PT": 1, "PP": 7, "PA": -1, "PG": -2, "PN": -2, "PD": -1,
              "PE": -1, "PQ": -1, "PH": -2, "PR": -2, "PK": -1, "PM": -2, "PI": -3, "PL": -3, "PV": -2, "PF": -4,
              "PY": -3, "PW": -4, "SC": -1, "SS": 4, "ST": 1, "SP": -1, "SA": 1, "SG": 0, "SN": 1, "SD": 0, "SE": 0,
              "SQ": 0, "SH": -1, "SR": -1, "SK": 0, "SM": -1, "SI": -2, "SL": -2, "SV": -2, "SF": -2, "SY": -2,
              "SW": -3, "TC": -1, "TS": 1, "TT": 4, "TP": 1, "TA": -1, "TG": 1, "TN": 0, "TD": 1, "TE": 0, "TQ": 0,
              "TH": 0, "TR": -1, "TK": 0, "TM": -1, "TI": -2, "TL": -2, "TV": -2, "TF": -2, "TY": -2, "TW": -3,
              "WC": -2, "WS": -3, "WT": -3, "WP": -4, "WA": -3, "WG": -2, "WN": -4, "WD": -4, "WE": -3, "WQ": -2,
              "WH": -2, "WR": -3, "WK": -3, "WM": -1, "WI": -3, "WL": -2, "WV": -3, "WF": 1, "WY": 2, "WW": 11,
              "YC": -2, "YS": -2, "YT": -2, "YP": -3, "YA": -2, "YG": -3, "YN": -2, "YD": -3, "YE": -2, "YQ": -1,
              "YH": 2, "YR": -2, "YK": -2, "YM": -1, "YI": -1, "YL": -1, "YV": -1, "YF": 3, "YY": 7, "YW": 2, "VC": -1,
              "VS": -2, "VT": -2, "VP": -2, "VA": -2, "VG": 0, "VN": -3, "VD": -3, "VE": -3, "VQ": -2, "VH": -2,
              "VR": -3, "VK": -3, "VM": -2, "VI": 1, "VL": 3, "VV": 4, "VF": -1, "VY": -1, "VW": -3}
 
 
# step_3
def neighborhood_words():
    temp = []
    for i in range(len(Array3)):
        for j in range(3):
            temp_string = Array3[i]
            temp = list(temp_string)
            if j == 0:
 
                var1 = "A" + temp[1] + temp[2]
                tmp1 = var1[0] + temp[0]
                tmp2 = var1[1] + temp[1]
                tmp3 = var1[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var1 != temp:
                    score_dic.update({var1: temp_score})
 
                var2 = "R" + temp[1] + temp[2]
                tmp1 = var2[0] + temp[0]
                tmp2 = var2[1] + temp[1]
                tmp3 = var2[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var2 != temp:
                    score_dic.update({var2: temp_score})
 
                var3 = "N" + temp[1] + temp[2]
                tmp1 = var3[0] + temp[0]
                tmp2 = var3[1] + temp[1]
                tmp3 = var3[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var3 != temp:
                    score_dic.update({var3: temp_score})
 
                var4 = "D" + temp[1] + temp[2]
                tmp1 = var4[0] + temp[0]
                tmp2 = var4[1] + temp[1]
                tmp3 = var4[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var4 != temp:
                    score_dic.update({var4: temp_score})
 
                var5 = "C" + temp[1] + temp[2]
                tmp1 = var5[0] + temp[0]
                tmp2 = var5[1] + temp[1]
                tmp3 = var5[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var5 != temp:
                    score_dic.update({var5: temp_score})
 
                var6 = "Q" + temp[1] + temp[2]
                tmp1 = var6[0] + temp[0]
                tmp2 = var6[1] + temp[1]
                tmp3 = var6[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var6 != temp:
                    score_dic.update({var6: temp_score})
 
                var7 = "E" + temp[1] + temp[2]
                tmp1 = var7[0] + temp[0]
                tmp2 = var7[1] + temp[1]
                tmp3 = var7[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var7 != temp:
                    score_dic.update({var7: temp_score})
 
                var8 = "G" + temp[1] + temp[2]
                tmp1 = var8[0] + temp[0]
                tmp2 = var8[1] + temp[1]
                tmp3 = var8[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var8 != temp:
                    score_dic.update({var8: temp_score})
 
                var9 = "H" + temp[1] + temp[2]
                tmp1 = var9[0] + temp[0]
                tmp2 = var9[1] + temp[1]
                tmp3 = var9[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var9 != temp:
                    score_dic.update({var9: temp_score})
 
                var10 = "I" + temp[1] + temp[2]
                tmp1 = var10[0] + temp[0]
                tmp2 = var10[1] + temp[1]
                tmp3 = var10[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var10 != temp:
                    score_dic.update({var10: temp_score})
 
                var11 = "L" + temp[1] + temp[2]
                tmp1 = var11[0] + temp[0]
                tmp2 = var11[1] + temp[1]
                tmp3 = var11[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var11 != temp:
                    score_dic.update({var11: temp_score})
 
                var12 = "K" + temp[1] + temp[2]
                tmp1 = var12[0] + temp[0]
                tmp2 = var12[1] + temp[1]
                tmp3 = var12[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var12 != temp:
                    score_dic.update({var12: temp_score})
 
                var13 = "M" + temp[1] + temp[2]
                tmp1 = var13[0] + temp[0]
                tmp2 = var13[1] + temp[1]
                tmp3 = var13[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var13 != temp:
                    score_dic.update({var13: temp_score})
 
                var14 = "F" + temp[1] + temp[2]
                tmp1 = var14[0] + temp[0]
                tmp2 = var14[1] + temp[1]
                tmp3 = var14[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var14 != temp:
                    score_dic.update({var14: temp_score})
 
                var15 = "P" + temp[1] + temp[2]
                tmp1 = var15[0] + temp[0]
                tmp2 = var15[1] + temp[1]
                tmp3 = var15[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var15 != temp:
                    score_dic.update({var15: temp_score})
 
                var16 = "S" + temp[1] + temp[2]
                tmp1 = var16[0] + temp[0]
                tmp2 = var16[1] + temp[1]
                tmp3 = var16[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var16 != temp:
                    score_dic.update({var16: temp_score})
 
                var17 = "T" + temp[1] + temp[2]
                tmp1 = var17[0] + temp[0]
                tmp2 = var17[1] + temp[1]
                tmp3 = var17[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var17 != temp:
                    score_dic.update({var17: temp_score})
 
                var18 = "W" + temp[1] + temp[2]
                tmp1 = var18[0] + temp[0]
                tmp2 = var18[1] + temp[1]
                tmp3 = var18[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var18 != temp:
                    score_dic.update({var18: temp_score})
 
                var19 = "Y" + temp[1] + temp[2]
                tmp1 = var19[0] + temp[0]
                tmp2 = var19[1] + temp[1]
                tmp3 = var19[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var19 != temp:
                    score_dic.update({var19: temp_score})
 
                var20 = "V" + temp[1] + temp[2]
                tmp1 = var20[0] + temp[0]
                tmp2 = var20[1] + temp[1]
                tmp3 = var20[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var20 != temp:
                    score_dic.update({var20: temp_score})
 
 
 
            elif j == 1:
 
                var1 = temp[0] + "R" + temp[2]
                tmp1 = var1[0] + temp[0]
                tmp2 = var1[1] + temp[1]
                tmp3 = var1[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var1 != temp:
                    score_dic.update({var1: temp_score})
 
                var2 = temp[0] + "R" + temp[2]
                tmp1 = var2[0] + temp[0]
                tmp2 = var2[1] + temp[1]
                tmp3 = var2[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var2 != temp:
                    score_dic.update({var2: temp_score})
 
                var3 = temp[0] + "N" + temp[2]
                tmp1 = var3[0] + temp[0]
                tmp2 = var3[1] + temp[1]
                tmp3 = var3[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var3 != temp:
                    score_dic.update({var3: temp_score})
 
                var4 = temp[0] + "D" + temp[2]
                tmp1 = var4[0] + temp[0]
                tmp2 = var4[1] + temp[1]
                tmp3 = var4[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var4 != temp:
                    score_dic.update({var4: temp_score})
 
                var5 = temp[0] + "C" + temp[2]
                tmp1 = var5[0] + temp[0]
                tmp2 = var5[1] + temp[1]
                tmp3 = var5[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var5 != temp:
                    score_dic.update({var5: temp_score})
 
                var6 = temp[0] + "Q" + temp[2]
                tmp1 = var6[0] + temp[0]
                tmp2 = var6[1] + temp[1]
                tmp3 = var6[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var6 != temp:
                    score_dic.update({var6: temp_score})
 
                var7 = temp[0] + "E" + temp[2]
                tmp1 = var7[0] + temp[0]
                tmp2 = var7[1] + temp[1]
                tmp3 = var7[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var7 != temp:
                    score_dic.update({var7: temp_score})
 
                var8 = temp[0] + "G" + temp[2]
                tmp1 = var8[0] + temp[0]
                tmp2 = var8[1] + temp[1]
                tmp3 = var8[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var8 != temp:
                    score_dic.update({var8: temp_score})
 
                var9 = temp[0] + "H" + temp[2]
                tmp1 = var9[0] + temp[0]
                tmp2 = var9[1] + temp[1]
                tmp3 = var9[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var9 != temp:
                    score_dic.update({var9: temp_score})
 
                var10 = temp[0] + "I" + temp[2]
                tmp1 = var10[0] + temp[0]
                tmp2 = var10[1] + temp[1]
                tmp3 = var10[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var10 != temp:
                    score_dic.update({var10: temp_score})
 
                var11 = temp[0] + "L" + temp[2]
                tmp1 = var11[0] + temp[0]
                tmp2 = var11[1] + temp[1]
                tmp3 = var11[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var11 != temp:
                    score_dic.update({var11: temp_score})
 
                var12 = temp[0] + "K" + temp[2]
                tmp1 = var12[0] + temp[0]
                tmp2 = var12[1] + temp[1]
                tmp3 = var12[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var12 != temp:
                    score_dic.update({var12: temp_score})
 
                var13 = temp[0] + "M" + temp[2]
                tmp1 = var13[0] + temp[0]
                tmp2 = var13[1] + temp[1]
                tmp3 = var13[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var13 != temp:
                    score_dic.update({var13: temp_score})
 
                var14 = temp[0] + "F" + temp[2]
                tmp1 = var14[0] + temp[0]
                tmp2 = var14[1] + temp[1]
                tmp3 = var14[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var14 != temp:
                    score_dic.update({var14: temp_score})
 
                var15 = temp[0] + "P" + temp[2]
                tmp1 = var15[0] + temp[0]
                tmp2 = var15[1] + temp[1]
                tmp3 = var15[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var15 != temp:
                    score_dic.update({var15: temp_score})
 
                var16 = temp[0] + "S" + temp[2]
                tmp1 = var16[0] + temp[0]
                tmp2 = var16[1] + temp[1]
                tmp3 = var16[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var16 != temp:
                    score_dic.update({var16: temp_score})
 
                var17 = temp[0] + "T" + temp[2]
                tmp1 = var17[0] + temp[0]
                tmp2 = var17[1] + temp[1]
                tmp3 = var17[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var17 != temp:
                    score_dic.update({var17: temp_score})
 
                var18 = temp[0] + "W" + temp[2]
                tmp1 = var18[0] + temp[0]
                tmp2 = var18[1] + temp[1]
                tmp3 = var18[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var18 != temp:
                    score_dic.update({var18: temp_score})
 
                var19 = temp[0] + "Y" + temp[2]
                tmp1 = var19[0] + temp[0]
                tmp2 = var19[1] + temp[1]
                tmp3 = var19[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var19 != temp:
                    score_dic.update({var19: temp_score})
 
                var20 = temp[0] + "V" + temp[2]
                tmp1 = var20[0] + temp[0]
                tmp2 = var20[1] + temp[1]
                tmp3 = var20[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var20 != temp:
                    score_dic.update({var20: temp_score})
 
 
 
            elif j == 2:
 
                var1 = temp[0] + temp[1] + "A"
                tmp1 = var1[0] + temp[0]
                tmp2 = var1[1] + temp[1]
                tmp3 = var1[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var1 != temp:
                    score_dic.update({var1: temp_score})
 
                var2 = temp[0] + temp[1] + "R"
                tmp1 = var2[0] + temp[0]
                tmp2 = var2[1] + temp[1]
                tmp3 = var2[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var2 != temp:
                    score_dic.update({var2: temp_score})
 
                var3 = temp[0] + temp[1] + "N"
                tmp1 = var3[0] + temp[0]
                tmp2 = var3[1] + temp[1]
                tmp3 = var3[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var3 != temp:
                    score_dic.update({var3: temp_score})
 
                var4 = temp[0] + temp[1] + "D"
                tmp1 = var4[0] + temp[0]
                tmp2 = var4[1] + temp[1]
                tmp3 = var4[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var4 != temp:
                    score_dic.update({var4: temp_score})
 
                var5 = temp[0] + temp[1] + "C"
                tmp1 = var5[0] + temp[0]
                tmp2 = var5[1] + temp[1]
                tmp3 = var5[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var5 != temp:
                    score_dic.update({var5: temp_score})
 
                var6 = temp[0] + temp[1] + "Q"
                tmp1 = var6[0] + temp[0]
                tmp2 = var6[1] + temp[1]
                tmp3 = var6[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var6 != temp:
                    score_dic.update({var6: temp_score})
 
                var7 = temp[0] + temp[1] + "E"
                tmp1 = var7[0] + temp[0]
                tmp2 = var7[1] + temp[1]
                tmp3 = var7[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var7 != temp:
                    score_dic.update({var7: temp_score})
 
                var8 = temp[0] + temp[1] + "G"
                tmp1 = var8[0] + temp[0]
                tmp2 = var8[1] + temp[1]
                tmp3 = var8[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var8 != temp:
                    score_dic.update({var8: temp_score})
 
                var9 = temp[0] + temp[1] + "H"
                tmp1 = var9[0] + temp[0]
                tmp2 = var9[1] + temp[1]
                tmp3 = var9[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var9 != temp:
                    score_dic.update({var9: temp_score})
 
                var10 = temp[0] + temp[1] + "I"
                tmp1 = var10[0] + temp[0]
                tmp2 = var10[1] + temp[1]
                tmp3 = var10[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var10 != temp:
                    score_dic.update({var10: temp_score})
 
                var11 = temp[0] + temp[1] + "L"
                tmp1 = var11[0] + temp[0]
                tmp2 = var11[1] + temp[1]
                tmp3 = var11[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var11 != temp:
                    score_dic.update({var11: temp_score})
 
                var12 = temp[0] + temp[1] + "K"
                tmp1 = var12[0] + temp[0]
                tmp2 = var12[1] + temp[1]
                tmp3 = var12[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var12 != temp:
                    score_dic.update({var12: temp_score})
 
                var13 = temp[0] + temp[1] + "M"
                tmp1 = var13[0] + temp[0]
                tmp2 = var13[1] + temp[1]
                tmp3 = var13[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var13 != temp:
                    score_dic.update({var13: temp_score})
 
                var14 = temp[0] + temp[1] + "F"
                tmp1 = var14[0] + temp[0]
                tmp2 = var14[1] + temp[1]
                tmp3 = var14[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var14 != temp:
                    score_dic.update({var14: temp_score})
 
                var15 = temp[0] + temp[1] + "P"
                tmp1 = var15[0] + temp[0]
                tmp2 = var15[1] + temp[1]
                tmp3 = var15[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var15 != temp:
                    score_dic.update({var15: temp_score})
 
                var16 = temp[0] + temp[1] + "S"
                tmp1 = var16[0] + temp[0]
                tmp2 = var16[1] + temp[1]
                tmp3 = var16[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var16 != temp:
                    score_dic.update({var16: temp_score})
 
                var17 = temp[0] + temp[1] + "T"
                tmp1 = var17[0] + temp[0]
                tmp2 = var17[1] + temp[1]
                tmp3 = var17[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var17 != temp:
                    score_dic.update({var17: temp_score})
 
                var18 = temp[0] + temp[1] + "W"
                tmp1 = var18[0] + temp[0]
                tmp2 = var18[1] + temp[1]
                tmp3 = var18[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var18 != temp:
                    score_dic.update({var18: temp_score})
 
                var19 = temp[0] + temp[1] + "Y"
                tmp1 = var19[0] + temp[0]
                tmp2 = var19[1] + temp[1]
                tmp3 = var19[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var19 != temp:
                    score_dic.update({var19: temp_score})
 
                var20 = temp[0] + temp[1] + "V"
                tmp1 = var20[0] + temp[0]
                tmp2 = var20[1] + temp[1]
                tmp3 = var20[2] + temp[2]
                temp_score = Amino_acid[tmp1] + Amino_acid[tmp2] + Amino_acid[tmp3]
                if var20 != temp:
                    score_dic.update({var20: temp_score})
 
 
neighborhood_words()
print("*****************************step_3***********************************")
print(score_dic)
 
T = 13
Seeds = []
 
 
# step_4
def neighborhood_compere():
    for key in list(score_dic.keys()):
        if score_dic[key] >= T:
            Seeds.append(key)
    print("**********************step_4*****************************")
    for key in Seeds:
        print(key)
 
 
neighborhood_compere()
blosum62 = {
    ('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0,
    ('Q', 'Q'): 5, ('N', 'A'): -2, ('Z', 'Y'): -2, ('W', 'R'): -3,
    ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1,
    ('H', 'D'): -1, ('L', 'N'): -3, ('W', 'A'): -3, ('Y', 'M'): -1,
    ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
    ('Y', 'A'): -2, ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7,
    ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
    ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2,
    ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3, ('V', 'S'): -2,
    ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2,
    ('K', 'K'): 5, ('P', 'D'): -1, ('I', 'H'): -3, ('I', 'D'): -3,
    ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
    ('P', 'H'): -2, ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1,
    ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1, ('D', 'R'): -2,
    ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2,
    ('Z', 'W'): -3, ('F', 'E'): -3, ('D', 'N'): 1, ('B', 'K'): 0,
    ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0,
    ('F', 'M'): 0, ('B', 'C'): -3, ('Z', 'I'): -3, ('Z', 'V'): -2,
    ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
    ('N', 'N'): 6, ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3,
    ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0, ('L', 'E'): -3,
    ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0,
    ('N', 'R'): 0, ('H', 'C'): -3, ('Y', 'N'): -2, ('G', 'Q'): -2,
    ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2,
    ('G', 'A'): 0, ('K', 'R'): 2, ('E', 'D'): 2, ('Y', 'R'): -2,
    ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
    ('T', 'A'): 0, ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1,
    ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1, ('K', 'H'): -1,
    ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2,
    ('V', 'V'): 4, ('M', 'I'): 1, ('T', 'Q'): -1, ('I', 'G'): -4,
    ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1,
    ('Z', 'D'): 1, ('F', 'R'): -3, ('X', 'K'): -1, ('Q', 'D'): 0,
    ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
    ('B', 'L'): -4, ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2,
    ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
    ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1,
    ('W', 'L'): -2, ('H', 'R'): 0, ('W', 'H'): -2, ('H', 'N'): 1,
    ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4,
    ('L', 'D'): -4, ('B', 'I'): -3, ('L', 'H'): -3, ('S', 'N'): 1,
    ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
    ('Y', 'G'): -3, ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1,
    ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2, ('E', 'E'): 5,
    ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2,
    ('P', 'R'): -2, ('V', 'G'): -3, ('T', 'L'): -1, ('V', 'K'): -2,
    ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1,
    ('P', 'F'): -4, ('I', 'N'): -3, ('K', 'I'): -3, ('M', 'D'): -3,
    ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
    ('K', 'A'): -1, ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4,
    ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1, ('X', 'F'): -1,
    ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3,
    ('F', 'C'): -2, ('Z', 'Q'): 3, ('X', 'Z'): -1, ('F', 'G'): -3,
    ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2,
    ('X', 'R'): -1, ('D', 'D'): 6, ('W', 'G'): -2, ('Z', 'F'): -3,
    ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
    ('L', 'C'): -1, ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4,
    ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0, ('S', 'I'): -2,
    ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2,
    ('Y', 'D'): -3, ('E', 'R'): 0, ('X', 'P'): -2, ('G', 'G'): 6,
    ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3,
    ('T', 'K'): -1, ('A', 'A'): 4, ('P', 'Q'): -1, ('T', 'C'): -1,
    ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
    ('C', 'R'): -3, ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1,
    ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1, ('M', 'G'): -3,
    ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1,
    ('I', 'A'): -1, ('P', 'I'): -3, ('R', 'R'): 5, ('X', 'M'): -1,
    ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1,
    ('Z', 'N'): 0, ('X', 'A'): 0, ('B', 'R'): -1, ('B', 'N'): 3,
    ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
    ('B', 'F'): -3, ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4
}
 
# List = ["PQG", "PEG", "QGE", "GEF"]
 
# Quary_dic = {"PQG":18, "PEG":15, "QGE":16, "GEF":17}
 
Quary = "PQGEFG"
 
emptyDict = {}
 
 
# step_5
def search():
    with open("project_file.txt", 'r') as read_obj:
        for line in read_obj:
            for item in Seeds:
                if item in line:
                    emptyDict[item] = line.index(item)
                    print("seed match", item)
 
print("******************step_5**********************")
 
search()
 
scores = blosum62
 
 
# step_6_7
 
 
def extend():
    index = 0
    with open("project_file.txt", 'r') as read_obj:
 
        for line in read_obj:
            eof = read_obj.read()
 
            for q in emptyDict:
 
                sco = score_dic[q]
                key_list=list(emptyDict)
 
 
                x = emptyDict[q]
                print("seed ", index+1, key_list[index])
 
                index=index+1
 
                print("index of first letter =",x)
 
                y = x - 1
                j = x + 3
                for i in range(len(line)):
 
                    if line[j] == eof:
                        tleft = 0
                        tright = 0
                        for i in range(y, x, 1):
                            tleft = tleft + scores[line[i], line[i]]
                        for i in range(x + 3, j + 1, 1):
 
                            tright = tright + scores[line[i], line[i]]
 
                        print("seqence =", line[y:j + 1])
                        print("this is stopping score =", sco)
                        print("tleft = ",tleft)
                        print("tright = ", tright)
                        print("total = ", tright + tleft)
                        print("____________________________________________________________")
                        break
                    if (line[y], line[j]) not in scores:
                        sum = scores[line[j], line[y]]
                    else:
                        sum = scores[line[y], line[j]]
 
 
 
                    sco += sum
 
                    if sco < T:
                        tleft = 0
                        tright = 0
                        for i in range(y, x, 1):
                            tleft = tleft + scores[line[i], line[i]]
                        for i in range(x+3, j+1, 1):
                            tright = tright + scores[line[i], line[i]]
                        print("seqence =", line[y:j + 1])
                        print("this is stopping score =", sco)
                        print("tleft = ", tleft)
                        print("tright = ", tright)
                        print("total = ", tright + tleft)
                        print("____________________________________________________________")
 
                        break
                    else:
 
                        if y == 0 or j == line.index(eof):
                            tleft = 0
                            tright = 0
                            for i in range(y, x, 1):
                                tleft = tleft + scores[line[i], line[i]]
                            for i in range(x + 3, j + 1, 1):
                                tright = tright + scores[line[i], line[i]]
                            print("seqence =",line[y:j + 1])
                            print("this is stopping score =",sco)
                            print("tleft = ", tleft)
                            print("tright = ", tright)
 
                            print("total = " ,tright+tleft)
                            print("____________________________________________________________")
                            break
                        else:
                            y = y - 1
                            j = j + 1
 
 
print("*******************step_6_7**********************")
extend()
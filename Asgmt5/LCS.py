str1 = input("Please input the 1st str：")
str2 = input("Please input the 2nd str：")

def LCStr(s1, s2):
    DParray = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    LCS_len = 0
    endpos = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                DParray[i][j] = DParray[i - 1][j - 1] + 1
                if DParray[i][j] > LCS_len:
                    LCS_len = DParray[i][j]
                    endpos = i + 1
    # 返回值依次为：最大子串, 开始位置, 最大子串长度
    return s1[endpos-LCS_len:endpos], endpos-LCS_len, LCS_len

#“吴亦凡竟然回复了李雪琴，我也是醉了”，“她说我不照顾孩子，好吧，我也是醉了”
LCS, start, maxlen = LCStr(str1, str2)
if start == 0:
    if str1[start+maxlen-1] == "，" or str1[start+maxlen-1] == ",":
        print("The template being matched: ", LCS, "\w+")
    else:
        print("The template being matched: ", LCS + ",", "\w+")
else:
    if str1[start-1] == "，" or str1[start-1] == ",":
        print("The template being matched: ", "\w+,", LCS)
    else:
        print("The template being matched: ", "\w+", LCS)
str3 = input("Please input the 3rd str：")
if LCS.lstrip("，").rstrip("，") in str3:
    print("The 3rd string is in line with the template.")
else:
    print("The 3rd string is not in line with the template.")
    print("The 3rd string is not in line with the template.")
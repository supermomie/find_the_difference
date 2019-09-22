def findTheDifference(s, t):
        l_s = len(s)
        l_t = len(t)
        bigger_arr = s if l_s > l_t else t
        smaller_arr = t if l_t < l_s else s
        for i in list(bigger_arr):
            matches = [x for x in list(smaller_arr) if i == x]#TODO prendre aussi la position de chaque lettres
            #print("matches : ", matches)
            #print("i : ", i)
            #if [i] != matches:
            #    return i

print(findTheDifference("a", "aa"))


#https://leetcode.com/contest/leetcode-weekly-contest-2/problems/find-the-difference/

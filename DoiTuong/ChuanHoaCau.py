# def chuanhoa(s):
#     s = s.strip().capitalize().split()
#     s = " ".join(s)
#     if s[-1]=="." or s[-1]=="!" or s[-1]=="?":
#         if s[-2]==" ":
#             return s[:-2]+s[-1]
#         else: return s
#     else:
#         return s +"."
# lst = []
# while True:
#     try:
#         lst += [chuanhoa(input())]
#     except : break
# for i in lst:
#     print(i)

import re
while True:
    try:
        s=input()
        s=re.sub('\s+',' ',s)
        if s[len(s)-1]!='.' and s[len(s)-1]!='?' and s[len(s)-1]!='!': s+='.'
        s=s.strip(' ')
        ss=''
        for i in s.split():
            if i!='.' and i!='?' and i!='!':
                ss+=" "+i
            else:
                ss+=i
            if ss[len(ss)-1]=='.' or ss[len(ss)-1]=='?' or ss[len(ss)-1]=='!':
                ss=ss.strip().capitalize()
                print(ss)
                ss=''
    except EOFError: 
        break
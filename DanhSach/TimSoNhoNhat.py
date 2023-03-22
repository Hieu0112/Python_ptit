for x in range(int(input())):
  s=input()
  for i in range(len(s)):
    if s[i]<"0" or s[i]>"9":
      s=s.replace(s[i]," ")
  s=[int(x) for x in s.split()]
  print(int(min(s)))
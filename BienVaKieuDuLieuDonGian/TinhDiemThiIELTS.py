Moc=[3,5,7,10,13,16,20,23,27,30,33,35,37,39,41]
for _ in range(int(input())):
    diem=[float(x)  for x in input().split()]
    doc,nghe=diem[0],diem[1]
    for i in range(len(Moc)):
        if doc>=Moc[i] :
            diem[0] = 2+(i+1)*0.5
        if nghe>=Moc[i] :
            diem[1] = 2+(i+1)*0.5
    total=sum(diem)/4
    if total-int(total)<0.25: 
        total = int(total)+0.0
    elif total - int(total) < 0.75: 
        total = int(total)+0.5
    else: total = int(total)+1.0
    print(total)



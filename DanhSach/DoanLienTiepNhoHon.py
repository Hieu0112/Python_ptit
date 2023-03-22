for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    st=[]
    print(1,end=' ')
    st.append(0)
    for i in range(1,len(a)):
        while len(st)>0 and a[i]>=a[st[-1]]:
            st.pop()
        if len(st)==0:
            print(i+1,end=' ')
        else:
            print(i-st[-1],end=' ')
        st.append(i)
    print('')

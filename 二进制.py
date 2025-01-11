while True:
    need=int(input('整数：'))
    out=[]
    if need==0 or need==1:
        print(need)
    else:
        while need>=1:
            need=need//2
            b=need%2
            out.append(b)
    print(str(out)[::-1])

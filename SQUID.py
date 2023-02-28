n = int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    count = 0
    
    lists = list(map(int,input().split()))
    for j in lists:
        if j>b:
            count += 1
            
    print(count)
    

def arranging_Coins(number):
    res=0
    while num>=res:
        num-=res
        res+=1
    return res-1

number=int(input())
print(arranging_Coins(number))
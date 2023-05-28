n=18
i=0
print("LET THE GAME BEGIN","  - YOU WILL GET 9 ATTEMPTS TO FINISH THIS GAME")
d=9
while (i<9):
    m=int(d-i)
    print(m ,"ATTEMPTS LEFT", " - Type Your Number Please : ")
    a=int(input())
        

    if a<18 and m!=1:
        print("OHHO! SMALL")
        
    elif a>18 and m!=1:
        print("OHHO! LARGE")
        
    elif a==18 and m!=1:
        print("WOW! YOU WON")
        print("YOU TOOK ",i+1, "ATTEMPTS TO FINISH")
        break
    elif m==1:
        print("YOU LOOSE")
        break
    

    i=i+1
    

     







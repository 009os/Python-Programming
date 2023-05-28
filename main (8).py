import random
print("LET's PLAY SNAKE WATER GUN"," - NUMBER OF ROUNDS = 10 ")
i=1
d=10
a=0
c=0
while(i<=10):
    game=["snake","water","gun"]
    choice = random.choice(game)
    print("ROUND : ",i,"\nPLEASE ENTER YOUR CHOICE")
    choice1= input()
    if choice==choice1:
        print("\nOHHHO! No Result\n")
    elif choice=="snake" and choice1=="water":
        print("\nYOU LOOSE\n")
    elif choice=="snake" and choice1=="gun":
        print("\nYOU WON\n")
    elif choice=="water" and choice1=="gun":
        print("\nYOU LOOSE\n")
    elif choice=="water" and choice1=="snake":
        print("\nYOU WON\n")
    a=a+1    
    elif choice=="gun" and choice1=="snake":
        print("\nYOU LOOSE\n")
    elif choice=="gun" and choice1=="water":
        print("\nYOU WON\n")
    a=a+1
    i=i+1

print("RESULTS : YOUR POINTS ARE: ",a)
b=int(10-a-c)
if a>b:
    print("YOU WON OVERALL")
elif a==b:
    print("TIED")
elif a<b:
    print("YOU LOOSE OVERALL")








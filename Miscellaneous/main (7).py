import random
print("LET's PLAY SNAKE WATER GUN"," - NUMBER OF ROUNDS = 10 ")
i=1
d=10
a=0
c=0
while(i<=10):
    game=["snake","water","gun"]
    choice = random.choice(game)
    print("\nROUND : ",i," - PLEASE ENTER YOUR CHOICE :")
    choice1= input()
    if choice==choice1:
        print("OHHHO! No Result")
        c=c+1
    elif (choice=="snake" and choice1=="water") or(choice=="water" and choice1=="gun")or (choice=="gun" and choice1=="snake") :
        print("NOOOO! YOU LOOSE THIS ROUND ")
    elif (choice=="snake" and choice1=="gun")or (choice=="water" and choice1=="snake")or (choice=="gun" and choice1=="water"):
        print("CONGO!YOU WON")
        a=a+1
  
    i=i+1

print("\nRESULTS : YOUR POINTS ARE: ",a)
b=int(10-a-c)
if a>b:
    print("YOU WON OVERALL")
elif a==b:
    print("TIED")
elif a<b:
    print("YOU LOOSE OVERALL")




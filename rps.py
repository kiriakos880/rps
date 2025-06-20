import random

ai_choices =["rock","paper","scissors"]
ai=random.choice(ai_choices)
print(ai)

rps =input("choose from rock,paper ,scissors:")
if rps == "rock"and ai == "rock":
    print("tie")
elif rps== "rock"and ai =="paper":
    print("lose")
elif rps== "rock"and ai =="scissors":
    print("win")
elif rps =="paper"and ai =="paper":
    print("tie")
elif rps== "paper"and ai=="rock":
    print("win")
elif rps== "paper"and ai =="scissors":
    print("lose")
elif (rps =="scissors"and ai =="scissors"):
    print("tie")
elif rps== "scissors"and ai =="rock":
    print("lose")
elif rps== "scissors"and ai =="paper":
    print("win")
else:
    print("chose a valid option")



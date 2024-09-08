import random

list_cpu = ["scissors","paper","rock"]
random_index= random.randint(0,2)


choice1 = (list_cpu[random_index])
print(f"cpu chose {choice1}")

user = ["scissors","paper","rock"]
random_index= random.randint(0,2)


choice2 = (user[random_index])
print(f"user chose {choice2}")

if choice1 == choice2:
    print("draw")
elif choice1 == "scissors" and choice2 == "paper":
    print("cpu wins ")
elif choice1 == "paper" and choice2 == "rock" :
    print("cpu wins ")
elif choice1 == "rock" and choice2 == "scissors":
    print("cpu wins ")
else:
    print("user wins")

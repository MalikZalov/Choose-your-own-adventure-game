name = input("Please, type your name: ").capitalize()

print(f"Welcome to the adventure game, {name}!")

answer = input("You are too drunk and in front of a nightclub at 2 am. All of a sudden, you remember that you have an exam tomorrow early in the morning. You can enter the nightclub, or you can head back home to take rest. Which option would you like to choose (enter/back)? ").lower()

if answer == "enter":
    answer = input(f"Nice choice! Yes, you had lots of fun in the nightclub, but guess what?! You failed the exam, {name}! Now you can go to the university to beg for a mark from your teacher, or smoke a cigarette and drink some beer (beg/smoke)! ").lower()
    if answer == "beg":
        answer = input("You lose! Never beg for such worthless things, you pussy! ").lower()
    elif answer == "smoke":
        answer = input(f"You win, my man! That's what I expected from you! Proud of you, {name}! ").lower()
    else:
        print("Not valid option. You lost")

elif answer == "back":
    answer = input("Oh, man! That's too boring. Now you are home. Would you like to go to sleep, or call the girl you met on your way home (sleep/call)? ").lower()
    if answer == "sleep":
        answer = input(f"You lost, {name}! Even though you passed the exam, you did not have fun last night! ").lower()
    elif answer == "call":
        answer = input(f"Nice choice, legend, you won! Yeah, you failed the exam, but you had fun last night, {name}! ").lower()
    else:
        print("Not valid option. You lost!")
else:
    print("Not valid option! You lost!")

print("Thank you for playing my game!")
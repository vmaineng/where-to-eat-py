import random

options = ['sushi', 'thai', 'italian']

def play():
    user_choice = input(f"What do you want to eat today? Chose from {', '.join(options)}\n")
  
    while user_choice not in options:
        return f"{user_choice} is not in the list of the options. Please pick again"
        continue
    
        computer_choice = random.choice(options)
    
        if user_choice == computer_choice:
            return "Let's eat"
            break
        else:
            return f"You chose {user_choice}, but the computer suggested {computer_choice}"
            break

print(play())


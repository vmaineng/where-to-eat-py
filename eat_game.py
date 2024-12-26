def play():
    user = input("What do you want to eat today? 's' for sushi, 't' for thai food, or 'd' for desserts\n")
    computer = random.choice(['s', 't', 'd'])

    if user == computer:
        return 'please make a choice'

    if chose_eat(user, computer):
        return 'You get to eat'
    
    return 'Let\'s play again'

    def chose_eat(eater, computer):
        #return true if eater makes a selection
        if (eater == 't' and computer == 's') or (eater == 'd' and computer =='s') or (eater == 't' and computer == 'd'):
            return True

    print(play)
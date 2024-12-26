def play():
    user = input("'s' for sushi, 't' for thai food, or 'd' for desserts")
    computer = random.choice(['s', 't', 'd'])

    if user == computer:
        return 'please make a choice'

    if chose_eat(user, computer):
        return 'You get to eat'
    
    return 'Let\'s play again

    def chose_eat(eater, computer):
        if (eater == 't' and computer == 's') or (eater == 'd' and computer =='s') or (eater == 't' and computer == 'd'):
            return True

    print(play)
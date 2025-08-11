import random
import os

def num_die():
    while True:
        try:
            num_dice = input('Number of dice (1, 2, or 3): ')
            valid_responses = ['1', 'one', '2', 'two', '3', 'three']
            if num_dice not in valid_responses:
                raise ValueError('1, 2, or 3 only')
            else:
                return num_dice
        except ValueError as err:
            print(err)

def roll_dice():
    min_val = 1
    max_val = 6
    roll_again = 'y'

    while roll_again.lower() in ['yes', 'y']:
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = num_die()

        if amount in ['3', 'three']:
            print('Rolling three dice...')
            dice = [random.randint(min_val, max_val) for _ in range(3)]
            print('The values are:')
            for i, val in enumerate(dice, start=1):
                print(f'Dice {i}:', val)
            print('Total:', sum(dice))

        elif amount in ['2', 'two']:
            print('Rolling two dice...')
            dice = [random.randint(min_val, max_val) for _ in range(2)]
            print('The values are:')
            print('Dice One:', dice[0])
            print('Dice Two:', dice[1])
            print('Total:', sum(dice))

        else:
            print('Rolling one die...')
            dice_1 = random.randint(min_val, max_val)
            print(f'The value is: {dice_1}')

        roll_again = input('Roll Again? ')

if __name__ == '__main__':
    roll_dice()

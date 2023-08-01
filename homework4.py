import random
def roll_dice():
    return random.randint(1,6)
def simulate_dice_rol():
    prize_count=0
    for i in range (1):
        dice_result=roll_dice()
        print("Dice result:",dice_result)
        if dice_result == 6:
            prize_count+=1
            if prize_count == 2:
                print("Congratulations! You won a prize!")
                prize_count = 0
            else:
                prize_count = 0
simulate_dice_rol()
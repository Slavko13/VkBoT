import random
def flip():
    coinValues = ["Орел","Решка"]
    return random.choice(coinValues)

def roll():
    return random.randint(1,100)
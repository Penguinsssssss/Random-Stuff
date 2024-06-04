#Mining simulator
import random
import time

#initialize variables
money = 0
commonItems = ["Stone", "Coal", "Copper"]
rareItems = ["Iron", "Gold", "Silver"]
epicItems = ["Ruby", "Sapphire", "Topaz"]
legendaryItems = ["Diamond", "Emerald", "Amythest"]
commonValues = [1, 2, 3]
rareValues = [5, 25, 10]
epicValues = [100, 150, 50]
legendaryValues = [250, 200, 500]

print("Press Enter to begin!")
enter = input()

while 1 == 1:
    print("You begin mining")
    time.sleep(1)
    conti = 1
    while conti == 1:
        itemRarity = 0
        itemQuantity = 0
        itemName = 0
        item = 0
        itemTotalWorth = 0
        if random.randint(1, 2) == 1:
            itemRarity = 1
            item = random.randint(0, len(commonItems) - 1)
            itemName = commonItems[item]
            itemQuantity = random.randint(1, 100)
            itemTotalWorth = commonValues[item] * itemQuantity
        elif random.randint(1, 2) == 1:
            itemRarity = 2
            item = random.randint(0, len(rareItems) - 1)
            itemName = rareItems[item]
            itemQuantity = random.randint(1, 50)
            itemTotalWorth = rareValues[item] * itemQuantity
        elif random.randint(1, 2) == 1:
            itemRarity = 3
            item = random.randint(0, len(epicItems) - 1)
            itemName = epicItems[item]
            itemQuantity = random.randint(1, 25)
            itemTotalWorth = epicValues[item] * itemQuantity
        else:
            itemRarity = 4
            item = random.randint(0, len(legendaryItems) - 1)
            itemName = legendaryItems[item]
            itemQuantity = random.randint(1, 10)
            itemTotalWorth = legendaryValues[item] * itemQuantity
        print("You got " + str(itemQuantity) + " " + str(itemName) + " (worth: " + str(itemTotalWorth) + ")")
        money += itemTotalWorth
        time.sleep(0.25)
        conti = random.randint(1, 2) == 1
    time.sleep(2)
    print("You now have $" + str(money))
    time.sleep(2)
    print("Press enter to continue")
    enter = input()
    
        


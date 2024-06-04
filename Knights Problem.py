#Knights Problem
import random
import time
def Average(lst): 
    return sum(lst) / len(lst)

#VVV Number of iterations to get a run of 100 VVV
#times = 2598801700000000000000000000000000000000000000000000000

totalTimes = []
times = 1000000
bestScore = 0
print("Started " + str(times) + " iterations")
estimatedTimeSeconds = times * 0.0000110018
unit = "seconds"
if estimatedTimeSeconds > 60:
    estimatedTimeSeconds /= 60
    unit = "minutes"
    if estimatedTimeSeconds > 60:
        estimatedTimeSeconds /= 60
        unit = "hours"
        if estimatedTimeSeconds > 24:
            estimatedTimeSeconds /= 24
            unit = "days"
            if estimatedTimeSeconds > 365:
                estimatedTimeSeconds /= 365
                unit = "years"
                if estimatedTimeSeconds > 1000:
                    estimatedTimeSeconds /= 1000
                    unit = "milenia"
print("Estimated time is " + str(estimatedTimeSeconds) + " " + str(unit))

start = time.time()
while times > 0:
    KnightX = random.randint(1,8)
    KnightY = random.randint(1,8)
    moves = 0
    while 9 > KnightX > 0 and 9 > KnightY > 0:
        chosenDir = random.randint(1,2)
        distance = random.randint(1,2)
        distance *= 4
        distance -= 6
        smallDistance = random.randint(1,2)
        smallDistance *= 2
        smallDistance -= 3
        if chosenDir == 1:
            KnightX += distance
            KnightY += smallDistance
        else:
            KnightY += distance
            KnightX += smallDistance
        #print(KnightX)
        #print(KnightY)
        #print()
        moves += 1
    totalTimes.append(moves)
    times -= 1
    #print("\nfallen\n")
    #print("Finished iteration " + str(times))
    #if moves > bestScore:
        #bestScore = moves
end = time.time()
print()
#print(totalTimes)
average = Average(totalTimes)
print("Average moves taken is " + str(average))
#print("The best score is " + str(bestScore))
print(f"Code executed in {end-start} seconds")
percentage = 1 / average
print("Chance to fall per move " + str(percentage))
print()

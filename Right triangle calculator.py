#Right triangle calculator
import math

#45 45 known leg calc
if 1 == 2:
    while 1 == 1:
        print("leg whole is")
        whole = input()
        print("leg root is")
        root = input()
        root = math.sqrt(float(root))
        #print(root)
        #print(whole)
        leg1 = float(root) * float(whole)
        #print(leg1)
        leg2 = leg1
        print("Leg 2 = " + str(leg2))
        leg1sq = leg1 * leg1
        leg2sq = leg2 * leg2
        hypot = leg1sq + leg2sq
        hypot = math.sqrt(hypot)
        print("Hypot = " + str(hypot))
        
if 1 == 1:
    while 1 == 1:
        print("hypot whole is")
        whole = input()
        print("hypot root is")
        root = input()
        root = math.sqrt(float(root))
        #print(root)
        #print(whole)
        hypot = float(root) * float(whole)
        hypot /= 2
        hypot = math.sqrt(hypot)
        #print(leg1);
        print("Hypot = " + str(hypot))
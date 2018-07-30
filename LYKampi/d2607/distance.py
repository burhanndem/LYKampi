from math import sqrt, pow

dot = []
dot1 = []


def uzaklik(*args):
    dotx = args[0]
    doty = args[1]
    dot1x = args[2]
    dot1y = args[3]

    dot.insert(0, dotx)
    dot.insert(1, doty)

    dot1.insert(0, dot1x)
    dot1.insert(1, dot1y)

    distance = (pow((dot[0] - dot1[0]), 2) + pow((dot[1] - dot1[1]), 2))
    sqrt(distance)

    print(sqrt(distance))


dotx = int(input("dot'in x girin: "))
doty = int(input("dot'in y :"))

dot1x = int(input("dot1'in x girin: "))
dot1y = int(input("dot1'in y :"))

uzaklik(dotx, doty, dot1x, dot1y)

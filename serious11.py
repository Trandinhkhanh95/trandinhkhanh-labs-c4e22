def is_insight(t,l):
    if t[0]<= (l[0]+l[2]) and t[1] <= (l[1]+l[3]):
        print("Point is insight a rectangle")
        return True
    else:
        print("point is not inside a rectangle")
        return False
is_insight([200, 120], [140, 60, 100, 200])
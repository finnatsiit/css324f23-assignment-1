def init_state():
    return 8, 0, 0

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def success(s):
    act = []
    a, b, c = s

    # 8-liters to 5-liters
    if a > 0 and b < 5:
        amt = min(a, 5 - b)
        act.append(((a - amt, b + amt, c), amt))

    # 8-liters to 3-liters
    if a > 0 and c < 3:
        amt = min(a, 3 - c)
        act.append(((a - amt, b, c + amt), amt))

    # 5-liters to 8-liters
    if b > 0 and a < 8:
        amt = min(b, 8 - a)
        act.append(((a + amt, b - amt, c), amt))

    # 5-liters to 3-liters
    if b > 0 and c < 3:
        amt = min(b, 3 - c)
        act.append(((a, b - amt, c + amt), amt))

    # 3-liters to 8-liters
    if c > 0 and a < 8:
        amt = min(c, 8 - a)
        act.append(((a + amt, b, c - amt), amt))

    # 3-liters to 5-liters
    if c > 0 and b < 5:
        amt = min(c, 5 - b)
        act.append(((a, b + amt, c - amt), amt))

    return act

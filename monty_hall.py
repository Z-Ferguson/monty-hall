import random


def no_switch():
    successes = 0
    for i in range(1000):
        winning_door = random.randint(1, 3)
        user_door = random.randint(1, 3)
        if user_door == winning_door:
            successes += 1
        else:
            continue
    print("\nNever switch first selection:\n")
    print("{} out of 1000. success rate {}%".format(successes, successes / 10))
    return(successes/10)


def _switch():
    successes = 0
    for i in range(1000):
        winning_door = random.randint(1, 3)
        user_door = random.randint(1, 3)
        if user_door == winning_door:
            continue
        else:
            successes += 1
    print("\nAlways switch first selection:\n")
    print("{} out of 1000. success rate {}%".format(successes, successes / 10))
    return(successes/10)


def fifty_fifty():
    successes = 0
    for i in range(1000):
        winning_door = random.randint(1, 3)
        user_door = random.randint(1, 3)
        switch = random.randint(0, 1)
        if switch:
            if user_door == winning_door:
                continue
            else:
                successes += 1
        else:
            if user_door == winning_door:
                successes += 1
            else:
                continue
    print("\nFifty/Fifty chance of switching:\n")
    print("{} out of 1000. success rate {}%".format(successes, successes / 10))
    return(successes/10)


def main():
    no_switch()
    _switch()
    fifty_fifty()

main()

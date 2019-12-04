#!/usr/bin/python3

start_input = 272091
end_input = 815432
passwords = 0


def is_double(cur, pre):
    if cur == pre:
        return True
    else:
        return False


def is_valid(cur, pre):
    if cur < pre:
        return True
    else:
        return False


for i in range(start_input, end_input):
    decrease = False
    double = False

    pre = 0

    for cur in str(i):
        cur = int(cur)

        if double is False:
            double = is_double(cur, pre)

        if decrease is False:
            decrease = is_valid(cur, pre)

        pre = cur

    if decrease is False and double is True:
        passwords += 1

print("Passwords:", passwords)

# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [
    msg_0,
    msg_1,
    msg_2,
    msg_3,
    msg_4,
    msg_5,
    msg_6,
    msg_7,
    msg_8,
    msg_9,
    msg_10,
    msg_11,
    msg_12,
]
operations = ["+", "-", "*", "/"]


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_one_digit(v):
    if (-10 < v < 10) and v.is_integer():
        return True
    else:
        return False


def math_operation(v1, v2, v3):
    if v3 == "+":
        return v1 + v2
    elif v3 == "-":
        return v1 - v2
    elif v3 == "*":
        return v1 * v2
    elif v3 == "/":
        return v1 / v2


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(float(v1)) and is_one_digit(float(v2)):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


memory = 0
while True:
    print(msg_0)
    calc = input().split(" ")
    x = calc[0]
    oper = calc[1]
    y = calc[2]

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    if not is_number(x) or not is_number(y):
        print(msg_1)
    elif oper not in operations:
        print(msg_2)
    else:
        try:
            check(float(x), float(y), oper)
            result = math_operation(float(x), float(y), oper)
            print(result)
            while True:
                print(msg_4)
                answer = input().strip()
                if answer == "y":
                    if is_one_digit(result):
                        msg_index = 10
                        while True:
                            print(msg_[msg_index])
                            answer3 = input().strip()
                            if answer3 == "y":
                                if msg_index < 12:
                                    msg_index += 1
                                    continue
                                else:
                                    memory = result
                                    break
                            elif answer3 == "n":
                                break
                            else:
                                continue
                    else:
                        memory = result
                        break
                    break
                elif answer == "n":
                    break
                else:
                    continue
            while True:
                print(msg_5)
                answer2 = input().strip()
                if answer2 == "y" or answer2 == "n":
                    break
                else:
                    continue

            if answer2 == "y":
                continue
            if answer2 == "n":
                break

        except ZeroDivisionError:
            print(msg_3)

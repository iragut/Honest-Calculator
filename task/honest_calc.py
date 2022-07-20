msg_ = ["Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]


def isfloat(num):  # check if input is a float
    try:
        float(num)
        return False
    except ValueError:
        return True


def is_one_digit(v):              # if number is integer
    if -10 < v < 10 and v == int(v):
        return True
    else:
        return False


def check(v1, v2, v3):               # Laziness test
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


x, oper, y = input("Enter an equation\n").split()
memory = 0
msg_index = 0
while True:
    if x == 'M':               # check if calculate from memory
        x = memory
    elif y == "M":
        y = memory
    elif isfloat(x) or isfloat(y) and not (x == "M" or y == "M"):          # check if input is a number
        print("Do you even know what numbers are? Stay focused!")
        x, oper, y = input("Enter an equation\n").split()

    elif not (oper == "+" or oper == "-" or oper == "*" or oper == "/"):         # check if oper is a mathematics symbol
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        x, oper, y = input("Enter an equation\n").split()

    elif oper == "+":                    # Block for arithmetic calculation "+"
        check(float(x), float(y), oper)
        print(float(x) + float(y))
        answer = float(x) + float(y)
        resp = input("Do you want to store the result? (y / n):")

        if resp == 'y':           # if you want to save energy
            if is_one_digit(answer):
                msg_index = 0
                resp = input(msg_[msg_index])
                if resp == "y" and msg_index < 3:
                    msg_index += 1
                    resp = input(msg_[msg_index])
                    if resp == "y" and msg_index < 3:
                        msg_index += 1
                        resp = input(msg_[msg_index])
                        if resp == "y" and msg_index < 3:
                            memory = answer
            else:
                memory = answer

        resp = input("Do you want to continue calculations? (y / n):")
        if resp == 'y':
            x, oper, y = input("Enter an equation\n").split()
        else:
            break

    elif oper == "-":                       # Block for arithmetic calculation "-"
        check(float(x), float(y), oper)
        print(float(x) - float(y))
        answer = float(x) - float(y)
        resp = input("Do you want to store the result? (y / n):")

        if resp == 'y':                  # if you want to save energy
            if is_one_digit(answer):
                msg_index = 0
                resp = input(msg_[msg_index])
                if resp == "y" and msg_index < 3:
                    msg_index += 1
                    resp = input(msg_[msg_index])
                    if resp == "y" and msg_index < 3:
                        msg_index += 1
                        resp = input(msg_[msg_index])
                        if resp == "y" and msg_index < 3:
                            memory = answer
            else:
                memory = answer

        resp = input("Do you want to continue calculations? (y / n):")
        if resp == 'y':
            x, oper, y = input("Enter an equation\n").split()
        else:
            break

    elif oper == "*":                     # Block for arithmetic calculation "*"
        check(float(x), float(y), oper)
        print(float(x) * float(y))
        answer = float(x) * float(y)
        resp = input("Do you want to store the result? (y / n):")

        if resp == 'y':                # if you want to save energy
            if is_one_digit(answer):
                msg_index = 0
                resp = input(msg_[msg_index])
                if resp == "y" and msg_index < 3:
                    msg_index += 1
                    resp = input(msg_[msg_index])
                    if resp == "y" and msg_index < 3:
                        msg_index += 1
                        resp = input(msg_[msg_index])
                        if resp == "y" and msg_index < 3:
                            memory = answer
            else:
                memory = answer

        resp = input("Do you want to continue calculations? (y / n):")
        if resp == 'y':
            x, oper, y = input("Enter an equation\n").split()
        else:
            break

    elif oper == "/" and int(y) != 0:        # Block for arithmetic calculation "/"
        check(float(x), float(y), oper)
        print(float(x) / float(y))
        answer = float(x) / float(y)
        resp = input("Do you want to store the result? (y / n):")

        if resp == 'y':                  # if you want to save energy
            if is_one_digit(answer):
                msg_index = 0
                resp = input(msg_[msg_index])
                if resp == "y" and msg_index < 3:
                    msg_index += 1
                    resp = input(msg_[msg_index])
                    if resp == "y" and msg_index < 3:
                        msg_index += 1
                        resp = input(msg_[msg_index])
                        if resp == "y" and msg_index < 3:
                            memory = answer
            else:
                memory = answer

        resp = input("Do you want to continue calculations? (y / n):")
        if resp == 'y':
            x, oper, y = input("Enter an equation\n").split()
        else:
            break

    else:                                # if y == 0
        check(float(x), float(y), oper)
        print("Yeah... division by zero. Smart move...")
        x, oper, y = input("Enter an equation\n").split()

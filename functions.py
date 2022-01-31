import messages
import variables

def is_one_digit(v):
    if isinstance(v, int) and v > -10 and v < 10:
        output = True
    else:
        output = False
    return output

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages.msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += messages.msg_7
    if (v1 == 0 or v2 == 0) and v3 in variables.lazy:
        msg += messages.msg_8
    if msg:
        msg = messages.msg_9 + msg
        print(msg)

def is_int(a):
    copy = str(a)
    if copy[len(copy) - 1] == '0':
        return 1
    else:
        return 0
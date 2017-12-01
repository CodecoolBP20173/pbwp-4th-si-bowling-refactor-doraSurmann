def score(roll):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(roll)):
        if roll[i] == '/':
            result += 10 - last
        else:
            result += get_value(roll[i])
        if frame < 10  and get_value(roll[i]) == 10:
            if roll[i] == '/':
                result += get_value(roll[i+1])
            elif roll[i] == 'X' or roll[i] == 'x':
                result += get_value(roll[i+1])
                if roll[i+2] == '/':
                    result += 10 - get_value(roll[i+1])
                else:
                    result += get_value(roll[i+2])
        last = get_value(roll[i])
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if roll[i] == 'X' or roll[i] == 'x':
            in_first_half = True
            frame += 1
    return result

def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

print(score("11111111112222222222"))
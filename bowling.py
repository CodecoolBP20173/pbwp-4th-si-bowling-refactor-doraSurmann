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
        in_first_half = not in_first_half
        if roll[i] == 'X' or roll[i] == 'x':
            in_first_half = True
            frame += 1
    return result

def get_value(pins):
    if pins in "123456789":
        return int(pins)
    elif pins == 'X' or pins == 'x' or pins == '/':
        return 10
    elif pins == '-':
        return 0
    else:
        raise ValueError()

print(score("11111111112222222222"))
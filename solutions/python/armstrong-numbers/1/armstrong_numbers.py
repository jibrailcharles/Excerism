def is_armstrong_number(number):
    new = str(number)
    sum = 0
    for i in range(len(new)):
        sum = int(new[i]) ** len(new) + sum
    if sum == number:
        return True
    else:
        return False

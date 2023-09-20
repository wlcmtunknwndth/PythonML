from datetime import date


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# THE FIRST TASK
def triplets(stroke):
    tripletsArr = []
    i = 0
    if stroke[-1] == '?' or stroke[-1] == '!' or stroke[-1] == '.':
        stroke = stroke[0: len(stroke) - 1]
    while i < len(stroke) - 2:
        if stroke[i + 2] == ',':
            i = i + 4
            continue
        elif stroke[i + 2] == ' ':
            i = i + 3
            continue
        tripletsArr.append(stroke[i:i + 3])
        print(stroke[i:i + 3])
        i = i + 1

    return tripletsArr


# THE SECOND TASK
def datetime_parse(text):
    i = 0
    dateArr = []
    while i < len(text):
        if i + 10 > len(text): break
        if text[i + 2] == '.' and text[i + 5] == '.':
            dateArr.append(date(int(text[i + 6:i + 10]), int(text[i + 3:i + 5]), int(text[i:i + 2])))
            print(dateArr[-1])
            i = i + 10
            # arr[i] = datetime(text[6:10], text[3:5], text[0:2])
        else:
            i = i + 1
            continue

    return dateArr


# THE THIRD TASK
def __apple_problem(pupils: int, apples: int):
    if pupils <= 0 or apples < 0:
        return
    elif 10000 > apples > 0 and 10000 > pupils > 0:
        return int(apples / pupils)
    elif apples == 0:
        return 0
    return


# THE FOURTH TASK
def theLastDigit(Number):
    return Number % 10


# THE FIFTH TASK
def mins_to_time(minutes_past):
    hours = minutes_past // 60
    minutes = minutes_past % 60
    if minutes < 10:
        print(str(hours) + ':' + '0' + str(minutes))
    else:
        print(str(hours) + ':' + str(minutes))


# THE SIXTH TASK
def equal_of_three(first, second, third):
    if first == second and second == third:
        return 3
    elif first == second or second == third or third == first:
        return 2
    else:
        return 0

# THE SEVENTH TASK
    def can_contain(A1, B1, C1, A2, B2, C2):
        A_box = [A1, B1, C1]
        B_box = [A2, B2, C2]
        A_size = A1 * B1 * C1
        B_size = A2 * B2 * C2
        A_box.sort()
        B_box.sort()
        if A_size <= B_size and A_box[0] == B_box[0] and A_box[1] == B_box[1]:
            print('Ящики равны')
        elif A_size < B_size and A_box[0] < B_box[0] and A_box[1] < B_box[1]:
            print('Первое поле меньше второго')
        elif A_size > B_size and A_box[0] > B_box[0] and A_box[1] > B_box[1]:
            print('Первое поле больше второго')
        else:
            print('Ящики несопоставимы')

    can_contain(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))

# THE EIGHT TASK
def cows(num):
    if num % 10 == 1:
        print('На лугу пасется ' + str(num) + ' корова')
    elif num % 10 == 2 or num % 10 == 3 or num % 10 == 4:
        print('На лугу пасется ' + str(num) + ' коровы')
    else:
        print('На лугу пасется ' + str(num) + ' коров')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(triplets('Мама, мыла раму?'))  # 1st
    # print(datetime_parse(
    #     '01.09.1939 Третий Рейх вторгается в Польшу, а 09.03.2021 Шуфутинский переворачивает календарь.'))
    print('Each gets ' + str(__apple_problem(10, 45)) + ' apples')  # 3rd
    print(__apple_problem(10000, 10001))
    # print(theLastDigit(102325))  # 4th
    # mins_to_time(130)  # 5th
    # print('The sixth task:')  # 6th
    # print(equal_of_three(1, 2, 3))
    # print(equal_of_three(10, 10, 10))
    # print(equal_of_three(2, 2, 3))
    # 
    # print('COWS:')  # 8th
    # cows(31)
    # cows(67)
    # cows(22)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

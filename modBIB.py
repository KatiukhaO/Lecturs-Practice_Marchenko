from random import randint, random


def randList(start, stop, quantity):  # формує список з рендомних елементів
    r_list = [randint(start, stop) for i in range(quantity)]
    return r_list


def remVow(slv):  # функція видалення голосних з стрічки
    slv = list(map(str, slv))
    i = 0
    while i < len(slv):
        if slv[i] == 'a' or slv[i] == 'e' or slv[i] == 'u' or slv[i] == 'o' or slv[i] == 'y' or slv[i] == 'i':
            del slv[i]
        else:
            i = i + 1
    slv = ''.join(slv)  # переведення списка в строку
    return slv


def poli(string):  # первіряє чи є слово поліндромом
    string = list(map(str, string))
    revert_string = string[::-1]
    if string == revert_string:
        print(string, " - Вітаємо!!! Це слово поліндром!")
        # return string
    else:
        print(string, " - Нажаль, це НЕ слово поліндром!")


def multiplication(start, stop):  # добуток послідовнисті чисел
    if start > stop:
        start, stop = stop, start
    if start == 0 or stop == 0:
        return 0
    mult = 1
    i = start
    while i <= stop:
        mult = mult * i
        i += 1
    return mult


def maxminLi(array):  # повертає кортеж з максимального і мінімального елемента списка
    minimum = array[0]
    maximum = array[0]
    for i in array:
        if i < minimum:
            minimum = i
        elif i > maximum:
            maximum = i
    return maximum, minimum


def revArray(array):  # повертає перевернутий список
    n = int(len(array))
    i = 0
    while i < (n - 1) // 2:
        b = array[i]
        array[i] = array[n - 1 - i]
        array[n - 1 - i] = b
        i = i + 1
    return array


def x2list(n, m, start, stop):  # повертає створений та заповнений рандомними значеннями в
    # певному діапазоні матрицю позміром m на n
    x2list = list()
    i = 0
    while i < n:
        x2list.append([0] * m)
        j = 0
        while j < m:
            x2list[i][j] = randint(start, stop)
            j += 1
        i += 1
    return x2list


def show_matrix(array):
    for row in array:
        for elem in row:
            print(str(elem).center(3, ' '), end='')
        print()


def rnd_intORfloat(left, right, intORfloat):
    if intORfloat.lower() == 'int' or intORfloat.lower() == 'i':
        random_int_numeric = randint(left, right)
        return random_int_numeric
    elif intORfloat.lower() == 'float' or intORfloat.lower() == 'float':
        random_float_numeric = random() * (right - left) + left
        return round(random_float_numeric, 4)

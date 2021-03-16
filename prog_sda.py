"""Обчислити значення кусочно неперервної ф-ї у, або видпти повідомлення про неіснування даної ф=ї"""
while True:
    x = int(input('x = '))

    if -10 < x <= 0:
        y = x ** 2
        print('y1 = ', y)
    elif 20 <= x <= 30:
        y = 2 * x - 3
        print('y1 = ', y)
    else:
        print("Ф-я неіснує")

    """2 variant"""

    if x <= (-10):
        print("Ф-я неіснує")
    else:
        if x <= 0:
            y = x ** 2
            print('y2 = ', y)
        else:
            if x < 20:
                print('Ф-я неіснує')
            else:
                if x <= 30:
                    y = 2 * x - 3
                    print('y2 = ', y)
                else:
                    print('Ф-я неіснує')

    '''3 варіант (інші функції і проміжки)'''

    if x < -4:
        y = 7 * x
        print('y3 = ', y)
    else:
        if x > -1:
            if x < 2:
                y = x ** 2 - x
                print('y3 = ', y)
            else:
                if x > 8:
                    if x <= 20:
                        y = 7 * x
                        print('y3 = ', y)
                    else:
                        if x >= 32:
                            if x < 64:
                                y = 3 * x + 2
                                print('y3 = ', y)
                            else:
                                print('Неіснує')
                        else:
                            print('Неіснує')
                else:
                    print('Неіснує')
        else:
            print('Неіснує')

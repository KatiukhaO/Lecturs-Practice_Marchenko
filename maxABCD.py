while True:
    A = int(input("A="))
    B = int(input("B="))
    C = int(input("C="))
    D = int(input('D='))

    if A > B:
        if A > C:
            if A > D:
                print("max A ", A)
            else:
                print("max D ", D)
        else:
            if C > D:
                print("max C ", C)
            else:
                print("max D ", D)
    else:
        if B > C:
            if B > D:
                print("max B ", B)
            else:
                print("max D ", D)
        else:
            if C > D:
                print("max C ", C)
            else:
                print("max D ", D)

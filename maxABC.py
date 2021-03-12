while True:
    A = int(input("A="))
    B = int(input("B="))
    C = int(input("C="))

    if A > C:
        if A > B:
            print("max A ", A)
        else:
            print("max B ", B)
    else:
        if B > C:
            print("max B ", B)
        else:
            print("max C ", C)

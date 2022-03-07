import ctypes ,os
ctypes.windll.kernel32.SetConsoleTitleW(f'Δ ↔ λ converter | made by piombacciaio')

while True:
    print("Please choose one of the following options:\n[1] Star to Delta converter\n[2] Delta to Star converter")
    user = input(">> ")
   
    if user == "1": #STAR - DELTA
        r1 = input("Input the value of the resistor R1 [Ω] >> ")
        r2 = input("Input the value of the resistor R2 [Ω] >> ")
        r3 = input("Input the value of the resistor R3 [Ω] >> ")
        rAB = ((int(r1) * int(r2)) + (int(r2) * int(r3)) + (int(r1) * int(r3))) / int(r3)
        rBC = ((int(r1) * int(r2)) + (int(r2) * int(r3)) + (int(r1) * int(r3))) / int(r1)
        rAC = ((int(r1) * int(r2)) + (int(r2) * int(r3)) + (int(r1) * int(r3))) / int(r2)
        print(f"Rab = {round(rAB, 2)}Ω; Rbc = {round(rBC, 2)}Ω; Rac = {round(rAC, 2)}Ω\nWhen done, press [ENTER] to continue")
        input()

    elif user == "2": #DELTA - STAR
        r1 = input("Input the value of the resistor R1 [Ω] >> ")
        r2 = input("Input the value of the resistor R2 [Ω] >> ")
        r3 = input("Input the value of the resistor R3 [Ω] >> ")
        rA = (int(r1) * int(r2))/(int(r1) + int(r2) + int(r3))
        rB = (int(r2) * int(r3))/(int(r1) + int(r2) + int(r3))
        rC = (int(r1) * int(r3))/(int(r1) + int(r2) + int(r3))
        print(f"Ra = {round(rA, 2)}Ω; Rb = {round(rB, 2)}Ω; Rc = {round(rC, 2)}Ω\nWhen done, press [ENTER] to continue")
        input()

    else:
        print("Wrong choice, press [ENTER] to continue...")
        input()
    os.system("cls")

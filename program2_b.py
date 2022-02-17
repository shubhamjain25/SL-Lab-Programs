def ctof(c):
    return c*(9/5) + 32

def ftoc(f):
    return (f-32)*(5/9)


def ctok(c):
    return c+273.15


def ktoc(c):
    return c-273.15


def ftok(f):
    return ctok(ftoc(f))


def ktof(k):
    return ctof(ktoc(k))


def main():

    op1=[]
    op2=[]
    op3=[]
    op4=[]
    op5=[]
    op6=[]

    ch = "Y"
    while ch == "Y" or ch == "y":
        op = input("Enter the selection: 1.C->F  2.F->C  3.C->K  4.K->C  5.F->K  6.K->F \n")
        if op == "1":
            temp = float(input("Enter temperature in Celsius: "))
            print("Temperature in F: ", ctof(temp))
            op1 = op1+[(temp, ctof(temp))]
            print("Celsius to Fahrenheit List:\n")
            print(sorted(op1))
        elif op == "2":
            temp = float(input("Enter temperature in Fahrenheit: "))
            print("Temperature in C: ", ftoc(temp))
            op2 = op2+[(temp, ftoc(temp))]
            print("Fahrenheit to Celsius List:\n")
            print(sorted(op2))
        elif op == "3":
            temp = float(input("Enter temperature in Celsius: "))
            print("Temperature in K: ", ctok(temp))
            op3 = op3+[(temp, ctok(temp))]
            print("Celsius to Kelvin List:\n")
            print(sorted(op3))
        elif op == "4":
            temp = float(input("Enter temperature in Kelvin: "))
            print("Temperature in C: ", ktoc(temp))
            op4 = op4+[(temp, ktoc(temp))]
            print("Kelvin to Celsius List:\n")
            print(sorted(op4))
        elif op == "5":
            temp = float(input("Enter temperature in Fahrenheit"))
            print("Temperature in K: ", ftok(temp))
            op5 = op5+[(temp, ftok(temp))]
            print("Fahrenheit to Kelvin List:\n")
            print(sorted(op5))
        elif op == "6":
            temp = float(input("Enter temperature in Kelvin"))
            print("Temperature in F: ", ktof(temp))
            op6 = op6+[(temp, ktof(temp))]
            print("Kelvin to Fahrenheit List:\n")
            print(sorted(op6))
        else:
            print("Invalid Choice")

        ch = input("Enter Y to continue and N to terminate\n")


main()
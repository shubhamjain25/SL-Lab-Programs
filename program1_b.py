from collections import Counter

def first_part():
    a = []
    b = []
    c = []
    try:
        a = eval(input("Enter the numbers:"))
        for x in a:
            if x not in b:
                b.append(x)

        c = [x for x in b if x % 2 == 0]
        print("List A equals ", a)
        print("List B equals ", b)
        print("List C equals ", c)
        c.reverse()
        print("Reversed List C equals ", c)
    except:
        print("Enter numbers seperated with a comma")


def second_part(fname):
    with open(fname) as f:
        return Counter(f.read().split())


def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    m = find_max(arr[1:])
    return m if m > arr[0] else arr[0]


def third_part():
    arr = []
    try:
        arr = eval(input("Enter the numbers:"))
        res = find_max(arr)
        print("Maximum value equals ",res)
    except:
        print("Enter numbers seperated with a comma")


def main():
    first_part()
    print("Number of words in the file :", second_part("temp.txt"))
    third_part()

main()

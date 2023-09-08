def isEven(num):
    return num % 2 == 0


randomNumbers = [20, 5, 60, 70, 30, 80]

for num in randomNumbers:
    if isEven(num):
        print(str(num)  + ": is Even")
    else:
        print(str(num)  + ": is ODD")


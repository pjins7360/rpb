def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        print("Error: cannot divide by zero.")
    else:
        return x / y

def main():
    print("더하기 실행")
    x = int(input("x > "))
    y = int(input("y > "))
    print("%d+%d=%d" % (x, y, add(x, y)))

    print("나누기 실행")
    x = int(input("x > "))
    y = int(input("y > "))
    
    result = divide(x, y)
    if result is not None:
        print("%d/%d=%d" % (x, y, result))

if __name__ == "__main__":
    main()
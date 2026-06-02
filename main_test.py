from calSum import calSum

def Info(name, age):
    print(f"Nickname: {name}")
    print(f"Age: {age}")

def main():
    name = input("Enter your nickname: ")
    age = input("Enter your age: ")
    Info(name, age)

    a, b = map(int, input("Enter two numbers separated by space: ").split())
    res = calSum(a, b)
    print(f"The sum of {a} and {b} is: {res}")

main()
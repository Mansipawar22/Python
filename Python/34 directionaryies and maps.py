n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {name : cell for name,cell in name_numbers}

while True:
    name = input()
    if name in phone_book:
        print(f"{name}={phone_book[name]}")
    else:
        print("Not Found")

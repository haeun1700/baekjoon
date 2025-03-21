words = [input() for i in range(3)]
for idx, val in enumerate(words):
    if val.isdigit():
        result = int(val) + (3-idx)

        if result % 3 == 0 and result % 5 == 0:
            print("FizzBuzz")
        elif result % 3 == 0:
            print("Fizz")
        elif result % 5 == 0:
            print("Buzz")
        else:
            print(result)
        break
def summa():
    current_sum = 0
    while True:
        next_number = yield current_sum
        if next_number == 0:
            print(f"Summation complete. Final sum: {current_sum}")
            break
        current_sum += next_number
        print(f"Current sum: {current_sum}")


sum_generator = summa()
next(sum_generator)

while True:
    try:
        user_input = int(input("Enter a number (enter 0 to exit): "))
        sum_generator.send(user_input)
    except StopIteration:
        break 
    except ValueError:
        print("Invalid input. Please enter an integer.")
       
        
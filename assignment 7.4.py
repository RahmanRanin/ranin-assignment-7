numbers = []

while True:
    user_input = input("Enter an integer (type 'done' to exit): ")

    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print(f"Current average: {average}")
    except ValueError:
        print("Please enter a valid integer.")

print("Program terminated.")

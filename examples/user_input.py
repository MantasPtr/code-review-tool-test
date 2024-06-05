def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    user_input = input("Enter numbers separated by comma: ")
    numbers = user_input.split(",")
    print(calculate_average(numbers))

if __name__ == "__main__":
    main()

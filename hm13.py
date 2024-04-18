def analyze_input(input_str):
    if input_str.lower() in ["вихід", "exit", "quit", "e", "q"]:
        return 'exit'
    elif input_str.replace('.', '', 1).replace(',', '', 1).replace('-', '', 1).isdigit():
        number = float(input_str.replace(',', '.'))
        if number == 0:
            return "Ви ввели нуль"
        elif number < 0:
            if '.' in input_str or ',' in input_str:
                return f"Ви ввели негативне дробове число: {number}"
            else:
                return f"Ви ввели негативне ціле число {int(number)}"
        else:
            if '.' in input_str or ',' in input_str:
                return f"Ви ввели додатнє дробове число: {number}"
            else:
                return f"Ви ввели додатнє ціле число: {int(number)}"
    else:
        return f"Ви ввели не коректне число: {input_str}"


while True:
    user_input = input("Введіть число або 'вихід', 'exit', 'quit', 'e', або 'q': ")
    result = analyze_input(user_input)
    if result == 'exit':
        print("Дякую за використання програми!")
        break
    else:
        print(result)


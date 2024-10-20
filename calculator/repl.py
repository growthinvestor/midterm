import sys
from calculator.core import Calculator
from calculator.history import HistoryManager

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager('data/history.csv')
        self.history_manager.load_history()

    def start(self):
        print("Welcome to the Advanced Calculator!")
        while True:
            command = input("Enter command (add, subtract, multiply, divide, history, quit): ")
            if command.lower() == 'quit':
                print("Exiting...")
                sys.exit()
            elif command.lower() == 'history':
                print(self.history_manager.get_history())
                continue

            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if command.lower() == 'add':
                    result = self.calculator.add(a, b)
                    self.history_manager.add_record(f"{a} + {b}", result)
                elif command.lower() == 'subtract':
                    result = self.calculator.subtract(a, b)
                    self.history_manager.add_record(f"{a} - {b}", result)
                elif command.lower() == 'multiply':
                    result = self.calculator.multiply(a, b)
                    self.history_manager.add_record(f"{a} * {b}", result)
                elif command.lower() == 'divide':
                    result = self.calculator.divide(a, b)
                    self.history_manager.add_record(f"{a} / {b}", result)
                else:
                    print("Invalid command.")
                    continue

                print(f"Result: {result}")
            except ValueError as e:
                print(f"Error: {e}")

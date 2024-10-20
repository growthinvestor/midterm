import sys
import logging
from dotenv import load_dotenv  # Import load_dotenv
import os  # Import os to access environment variables
from calculator.core import Calculator
from calculator.history import HistoryManager

# Set up logging
LOG_FILE = 'logs/app.log'
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # You can set this to DEBUG for more detailed logs
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class REPL:
    def __init__(self):
        self.calculator = Calculator()
        self.history_manager = HistoryManager('data/history.csv')
        self.history_manager.load_history()
        logging.info("Calculator REPL initialized, history loaded.")

    def start(self):
        print("Welcome to the Advanced Calculator!")
        logging.info("REPL session started.")

        while True:
            # Display the menu
            print("\nAvailable commands:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. History")
            print("6. Quit")
            
            command = input("Select an option (1-6): ")
            logging.info(f"User selected command: {command}")

            if command == '6':  # Quit
                print("Exiting...")
                logging.info("User exited the calculator.")
                sys.exit()
            elif command == '5':  # Show history
                print("Calculation History:")
                print(self.history_manager.get_history())
                logging.info("Displayed calculation history.")
                continue

            try:
                if command in ['1', '2', '3', '4']:
                    a = float(input("Enter first number: "))
                    b = float(input("Enter second number: "))
                    logging.info(f"User inputs: a={a}, b={b}")

                    if command == '1':  # Add
                        result = self.calculator.add(a, b)
                        operation = f"{a} + {b}"
                    elif command == '2':  # Subtract
                        result = self.calculator.subtract(a, b)
                        operation = f"{a} - {b}"
                    elif command == '3':  # Multiply
                        result = self.calculator.multiply(a, b)
                        operation = f"{a} * {b}"
                    elif command == '4':  # Divide
                        if b == 0:
                            print("Error: Cannot divide by zero.")
                            logging.warning("Attempted division by zero.")
                            continue
                        result = self.calculator.divide(a, b)
                        operation = f"{a} / {b}"

                    # Record the operation in history
                    self.history_manager.add_record(operation, result)
                    print(f"Result: {result}")
                    logging.info(f"Operation performed: {operation}, result: {result}")
                else:
                    print("Invalid command. Please select a valid option.")
                    logging.warning(f"Invalid command entered: {command}")
            except ValueError as e:
                print(f"Error: {e}")
                logging.error(f"ValueError encountered: {e}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()

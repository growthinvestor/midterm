import pandas as pd
import os  # Import the os module

class HistoryManager:
    def __init__(self, history_file):
        self.history_file = history_file
        self.history = pd.DataFrame(columns=["operation", "result"])
        self.ensure_history_file_exists()

    def ensure_history_file_exists(self):
        # Get the directory name from the history file path
        directory = os.path.dirname(self.history_file)
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)

    def load_history(self):
        try:
            self.history = pd.read_csv(self.history_file)
        except FileNotFoundError:
            self.history = pd.DataFrame(columns=["operation", "result"])

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "result"])
        self.save_history()

    def add_record(self, operation, result):
        # Create a new DataFrame to append
        new_record = pd.DataFrame({"operation": [operation], "result": [result]})
        # Use pd.concat to add the new record to the history DataFrame
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()

    def get_history(self):
        return self.history

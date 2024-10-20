import pandas as pd

class HistoryManager:
    def __init__(self, history_file):
        self.history_file = history_file
        self.history = pd.DataFrame(columns=["operation", "result"])

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
        self.history = self.history.append({"operation": operation, "result": result}, ignore_index=True)
        self.save_history()

    def get_history(self):
        return self.history

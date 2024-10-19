import pandas as pd
import os

HISTORY_FILE = 'calculation_history.csv'

def load_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)
    return pd.DataFrame(columns=['operation', 'result'])

def save_history(operation, result):
    df = load_history()
    new_record = pd.DataFrame([[operation, result]], columns=['operation', 'result'])
    df = pd.concat([df, new_record])
    df.to_csv(HISTORY_FILE, index=False)

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

def get_history():
    return load_history()

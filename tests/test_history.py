from calculator import history
import pandas as pd
import os

def test_save_history():
    history.save_history("add 2 3", 5)
    df = pd.read_csv("calculation_history.csv")
    assert df.iloc[-1]['operation'] == "add 2 3"
    assert df.iloc[-1]['result'] == 5

def test_clear_history():
    history.clear_history()
    assert not os.path.exists("calculation_history.csv")

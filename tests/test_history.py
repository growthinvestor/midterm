import os
import pytest
from calculator.history import HistoryManager

@pytest.fixture
def history_manager(tmpdir):
    history_file = tmpdir.join("history.csv")
    hm = HistoryManager(str(history_file))
    return hm

def test_load_history(history_manager):
    history_manager.load_history()
    assert history_manager.history.empty

def test_add_record(history_manager):
    history_manager.add_record("2 + 3", 5)
    assert len(history_manager.history) == 1
    assert history_manager.history.iloc[0]["operation"] == "2 + 3"
    assert history_manager.history.iloc[0]["result"] == 5

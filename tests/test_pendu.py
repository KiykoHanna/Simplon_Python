import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from pendu import func_add, input_lettre

@pytest.mark.parametrize(a, b, rez, [
    (1, 2, 3),
    (2, 5, 7),
    ()
] )
def test_func_add(a, b, rez):
    assert func_add(2, 3) == 5

def test_input_lettre(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "a")
    assert input_lettre() == "a"
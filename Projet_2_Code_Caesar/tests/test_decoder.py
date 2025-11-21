import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/components")))

import pytest
from app.components import decode_text

@pytest.mark.parametrize("text, cle, rez", [
    ("ABC", 5, "VWX"),
    ("Lipps, Asvph!", 4, "Hello, World!"),
    ("Édpmf", 1, "École")
])
def test_decoder(text, cle, rez):
    assert decode_text(text, cle) == rez
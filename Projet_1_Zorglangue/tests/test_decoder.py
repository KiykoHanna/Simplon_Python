import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/components")))

import pytest
from app.components import decode_text

@pytest.mark.parametrize("a, rez", [
    ("azertyuiop", "poiuytreza"),
    ("Azer Azer", "rezA rezA"),
    ("1234 1234", "1234 1234")
] )
def test_decoder(a, rez):
    assert decode_text(a) == rez
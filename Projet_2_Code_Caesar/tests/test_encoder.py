import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../app/components")))

import pytest
from app.components import encode_text

@pytest.mark.parametrize("text, cle, rez", [
    ("VWX", 5, "ABC"),
    ("XYZ", 3, "ABC"),
    ("bonjour", 5, "gtsuzwt")
])
def test_encoder(text, cle, rez):
    assert encode_text(text, cle) == rez
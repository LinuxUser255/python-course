#!/usr/bin/env python3

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from lesson_4.just_playin import drink_age
import pytest
from unittest.mock import patch, Mock


def test_drink_age_greater_than_21(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '25')
    drink_age()
    captured = capsys.readouterr()
    assert "You can drink." in captured.out
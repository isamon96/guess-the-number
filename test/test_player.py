import pytest
from unittest.mock import patch
from io import StringIO
from player import Player

def test_guess():
    with patch('builtins.input', return_value='5'):
        player = Player()
        assert player.guess() == 5

def test_receive_hint():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        player = Player()
        player.receive_hint('higher', 5)
        assert fake_out.getvalue().strip() == 'The secret number is higher than 5.'
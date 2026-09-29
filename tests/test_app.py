import sys
sys.path.append("src")

from app import add_bid, get_winner


def test_add_bid():
    assert add_bid(1000, 1500) == 1500


def test_reject_lower_bid():
    assert add_bid(1500, 1200) == 1500


def test_get_winner():
    assert get_winner("Rohitha", 1500) == {
        "winner": "Rohitha",
        "amount": 1500
    }
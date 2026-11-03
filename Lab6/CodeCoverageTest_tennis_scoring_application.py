"""Tests for the first, line-coverage stage of Lab 6."""

import pytest

from tennis_scoring import game_score, match_status, set_winner


@pytest.mark.parametrize(
    ("points_a", "points_b", "expected"),
    [
        (0, 0, "0-0"),
        (2, 1, "30-15"),
        (3, 3, "deuce"),
        (5, 5, "deuce"),
        (5, 3, "game A"),
        (3, 5, "game B"),
        (4, 3, "advantage A"),
        (4, 0, "game A"),
        (0, 4, "game B"),
    ],
)
def test_game_scores(points_a, points_b, expected):
    assert game_score(points_a, points_b) == expected


def test_negative_points_are_rejected():
    with pytest.raises(ValueError, match="negative points"):
        game_score(-1, 0)


@pytest.mark.parametrize(
    ("games_a", "games_b", "expected"),
    [
        (3, 2, None),
        (6, 4, "A"),
        (4, 6, "B"),
        (7, 6, "A"),
    ],
)
def test_set_results(games_a, games_b, expected):
    assert set_winner(games_a, games_b) == expected


@pytest.mark.parametrize(
    ("sets_a", "sets_b", "best_of", "expected"),
    [
        (0, 0, 3, "in progress"),
        (2, 0, 3, "A wins"),
        (0, 2, 3, "B wins"),
        (1, 1, 3, "decider"),
    ],
)
def test_match_results(sets_a, sets_b, best_of, expected):
    assert match_status(sets_a, sets_b, best_of) == expected

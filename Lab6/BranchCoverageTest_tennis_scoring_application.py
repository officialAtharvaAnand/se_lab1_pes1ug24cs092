"""Decision and boundary tests for the branch-coverage stage of Lab 6."""

import pytest

from tennis_scoring import game_score, match_status, set_winner


@pytest.mark.parametrize("points_a,points_b", [(-1, 0), (0, -1)])
def test_either_negative_point_is_rejected(points_a, points_b):
    with pytest.raises(ValueError, match="negative points"):
        game_score(points_a, points_b)


@pytest.mark.parametrize(
    ("points_a", "points_b", "expected"),
    [
        (0, 0, "0-0"),
        (2, 3, "30-40"),
        (3, 3, "deuce"),
        (4, 4, "deuce"),
        (5, 3, "game A"),
        (3, 5, "game B"),
        (4, 3, "advantage A"),
        (3, 4, "advantage B"),
        (4, 2, "game A"),
        (2, 4, "game B"),
    ],
)
def test_game_decision_outcomes(points_a, points_b, expected):
    assert game_score(points_a, points_b) == expected


@pytest.mark.parametrize(
    ("games_a", "games_b", "expected"),
    [
        (5, 5, None),
        (6, 5, None),
        (6, 4, "A"),
        (4, 6, "B"),
        (7, 5, "A"),
        (5, 7, "B"),
        (7, 6, "A"),
        (6, 7, "B"),
    ],
)
def test_set_decision_outcomes(games_a, games_b, expected):
    assert set_winner(games_a, games_b) == expected


@pytest.mark.parametrize(
    ("sets_a", "sets_b", "best_of", "expected"),
    [
        (0, 0, 3, "in progress"),
        (2, 0, 3, "A wins"),
        (0, 2, 3, "B wins"),
        (1, 1, 3, "decider"),
        (2, 2, 5, "decider"),
        (3, 1, 5, "A wins"),
        (1, 3, 5, "B wins"),
    ],
)
def test_match_decision_outcomes(sets_a, sets_b, best_of, expected):
    assert match_status(sets_a, sets_b, best_of) == expected

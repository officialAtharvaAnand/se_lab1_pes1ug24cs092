import os
from types import SimpleNamespace

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame
import pytest

import game


def test_radar_uses_absolute_world_positions(monkeypatch):
    drawn_rectangles = []

    def record_rect(_screen, color, rect, width=0):
        drawn_rectangles.append((color, rect, width))

    monkeypatch.setattr(pygame.draw, "rect", record_rect)
    instance = game.Game.__new__(game.Game)
    instance.player = SimpleNamespace(x=1600, y=250)
    instance.humanoids = [SimpleNamespace(x=800, y=500)]
    instance.landers = [SimpleNamespace(x=2400, y=100, mutant=False)]

    instance.draw_radar(None)

    blip_x_positions = [entry[1][0] + 2 for entry in drawn_rectangles[-3:]]
    assert blip_x_positions == [200, 600, 400]


def test_sky_colour_changes_safely_with_wave():
    assert game.sky_color(1) == (5, 5, 20)
    assert game.sky_color(5) != game.sky_color(1)
    assert all(0 <= channel <= 255 for channel in game.sky_color(1000))


def test_rescue_feedback_is_timed():
    humanoid = game.Humanoid(100)
    game.on_humanoid_rescued(humanoid)
    assert humanoid.rescue_timer == 1.4
    humanoid.update(0.4)
    assert humanoid.rescue_timer == pytest.approx(1.0)
    humanoid.update(5.0)
    assert humanoid.rescue_timer == 0.0


def test_bonus_life_threshold():
    assert game.bonus_life_threshold() == 10_000

import pytest

@pytest.mark.parametrize("point1, point2, x, expected", [
    [(0, 0), (1, 1), 2, 2],
    [(0, 0), (1, 2), 2, 4],
    [(-1, -0.5), (-2, 1), 0, 0],
    ])
def test_in_line(point1, point2, x, expected):
    from in_line import in_line
    y = in_line(point1, point2, x)
    assert y == expected





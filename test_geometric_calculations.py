from geometric_calculation import triangular_surface_area
from geometric_calculation import circular_surface_area
from geometric_calculation import cylinder_volume

def test_triangular_surface_area():
    assert triangular_surface_area(1, 2) == 1
    assert triangular_surface_area(12, 20) == 120
    assert triangular_surface_area(4, 10) == 20


def test_circular_surface_area():
    assert circular_surface_area(4) == 50.265472
    assert circular_surface_area(13) == 530.929048
    assert circular_surface_area(99) == 30790.743192


def test_cylinder_volume():
    assert cylinder_volume(2, 5) == 62.83184
    assert cylinder_volume(3, 8) == 226.194624
    assert cylinder_volume(9, 7) == 1781.282664

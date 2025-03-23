def triangular_surface_area(s, h):
    """This function calculates the surface area of a triangle."""
    A = s * h / 2
    print("triangular_surface_area =", A)
    return A


def circular_surface_area(radius, pi=3.141592):
    """This function calculates the surface area of a circle."""
    A = radius**2 * pi
    print("circular_surface_area =", A)
    return A


def cylinder_volume(radius, height, pi=3.141592):
    """This function calculates the volume of a cylinder."""
    V = radius**2 * height * pi
    print("cylinder_volume =", V)
    return V


if __name__ == "__main__":
    s = 4
    h = 3
    triangular_surface_area(s, h)

    r = 10
    circular_surface_area(r)

    height = 20
    cylinder_volume(r, height)

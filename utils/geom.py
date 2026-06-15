import math

def rectangle_area(
    edge_a: int | float,
    edge_b: int | float
) -> int | float:
    return edge_a * edge_b


def circle_area(
    radius: int | float
):
    return radius ** 2 * math.pi

import math
import copy


class point:
    """Point in 2D Space"""
    x = 0.0
    y = 0.0


def distance_bet_points(p1, p2):
    dist = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return dist


def print_point(p):
    print(p.x, p.y)


class rectangle:
    """Indicaates a rectangle"""


class circle:
    """Indicates a circle"""


def point_in_circle(point, circle):
    d = distance_bet_points(point, circle.center)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False
    p.x = p.x + rect.width
    if not point_in_circle(p, circle):
        return True
    p.y += rect.height
    if not point_in_circle(p, circle):
        return False
    p.x = rect.width
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    p = copy.copy(rect.corner)
    if point_in_circle(p, circle):
        return True
    p.x = p.x + rect.width
    if point_in_circle(p, circle):
        return True
    p.y += rect.height
    if point_in_circle(p, circle):
        return True
    p.x = rect.width
    if point_in_circle(p, circle):
        return True
    return False


def main():
    box = rectangle()
    box.height = 30
    box.width = 40
    box.corner = point()
    box.corner.x = 50
    box.corner.y = 50
    c = circle()
    c.radius = 75
    c.center = point()
    c.center.x = 150
    c.center.y = 100
    p = point()
    print("Enter a point co-ordinate")
    p.x = float(input("Enter X co-ordinate"))
    p.y = float(input("Enter Y co-ordinate"))
    print_point(p)
    print("Point inside Circle:", point_in_circle(p, c))
    print("Rectangle inside circle:", rect_in_circle(box, c))
    print("Rectangle overlapiping with circle", rect_circle_overlap(box, c))


main()


from solutions.day12 import apply_gravity
from solutions.day12 import apply_velocity
from solutions.day12 import calculate_energy
from solutions.day12 import create_hashable_string
from solutions.day12 import Moon
from common.Point3D import Point3D


def test_apply_gravity():
    moons = [
        Moon(Point3D(-1, 0, 2)),
        Moon(Point3D(2, -10, -7)),
        Moon(Point3D(4, -8, 8)),
        Moon(Point3D(3, 5, -1)),
    ]
    moons = apply_gravity(moons)
    assert moons[0].vel == (3, -1, -1)


def test_apply_velocity():
    moon = Moon(Point3D(-1, 0, 2), Point3D(3, -1, -1))
    apply_velocity([moon])
    assert moon.pos == (2, -1, 1)


def test_create_hashable_string():
    list1 = [
        Moon(Point3D(-1, 0, 2)),
        Moon(Point3D(2, -10, -7)),
        Moon(Point3D(4, -8, 8)),
        Moon(Point3D(3, 5, -1)),
    ]
    apply_gravity(list1)
    apply_velocity(list1)
    hash1 = hash(create_hashable_string(list1))
    list2 = [
        Moon(Point3D(-1, 0, 2)),
        Moon(Point3D(2, -10, -7)),
        Moon(Point3D(4, -8, 8)),
        Moon(Point3D(3, 5, -1)),
    ]
    apply_gravity(list2)
    apply_velocity(list2)
    hash2 = hash(create_hashable_string(list2))
    assert hash1 == hash2


def test_simulation():
    moons = [
        Moon(Point3D(-1, 0, 2)),
        Moon(Point3D(2, -10, -7)),
        Moon(Point3D(4, -8, 8)),
        Moon(Point3D(3, 5, -1)),
    ]
    for _ in range(10):
        apply_gravity(moons)
        apply_velocity(moons)
    assert moons[0].pos == (2, 1, -3)
    assert moons[0].vel == (-3, -2, 1)
    assert calculate_energy(moons) == 179

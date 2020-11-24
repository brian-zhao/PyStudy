import attr


@attr.s(auto_attribs=True)
class Point:
    x: float
    y: float
    z: float = 0.0
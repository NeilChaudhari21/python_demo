"""Small numeric helpers."""


def percent(value: float, rate: float) -> float:
    return round(float(value) * float(rate), 2)


def clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))

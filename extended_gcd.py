def extended_gcd(a: int, b: int, positive_x: bool) -> tuple[int, int, int]:
    original_a = a
    original_b = b
    x0, y0 = 1, 0
    x1, y1 = 0, 1

    while b != 0:
        quotient = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - quotient * x1
        y0, y1 = y1, y0 - quotient * y1

    if positive_x and x0 < 0:
        shift_k = (abs(x0) + (original_b // a) - 1) // (original_b // a)
        x0 += shift_k * (original_b // a)
        y0 -= shift_k * (original_a // a)

    return a, x0, y0
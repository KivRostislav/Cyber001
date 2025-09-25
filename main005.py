from math import pi, acos, sqrt


def main():
    s0, v0, g, t = 1, 1, 1, 1
    s = s0 + v0*t + (g*t**2)/2

    PV, INT, YRS = 1, 1, 1
    FV = PV * (1 + INT/100)**YRS

    a, p, m1, m2 = 1, 1, 1, 1
    G = 4 * pi**2 * (a**3 / (p**2 * (m1 + m2)))

    a, b, gamma = 1, 1, 1
    c = sqrt(a**2 + b**2 - (2 * acos(gamma)))

if __name__ == '__main__':
    main()
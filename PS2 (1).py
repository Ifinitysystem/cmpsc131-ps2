"""
Course     : CMPSC 131, Summer 2025
File       : PS2.py 

Name       : Jonathan Reese
GitHub User:  Ifinitysystem
Collaboration Statement:
"""

#-YOUR CODE STARTS HERE  (TODO) 
#Part 1
def math_func_1(x: float) -> float:
    numerator1 = 5 * x - 3
    denominator1 = 4
    numerator2 = 3
    denominator2 = 4 * x - 3

    return (numerator1 / denominator1) * (numerator2 / denominator2)

def math_func_2(x: float, y: float) -> float:
    part1 = (3 + 4 * x) / 5
    numerator = (y ** 2 - 8) % (x ** 3 - 1)
    denominator = (4 / 9) * ((y + x) / (x + y))

    return part1 - (numerator / denominator)

def math_func_3(x: float, y: float, z: float) -> float:
    numerator = 2 % x - 3
    denominator = z * y
    part1 = numerator / denominator

    part2 = (4 // z) - y

    return part1 + part2
#Part 2
def get_total_cost(value: float, rate: float, months: int) -> float:
    numerator = value * rate
    denominator = 1 - (1 + rate) ** (-months)
    return (numerator / denominator) * months
#Part 2.2
def get_digit(number: int, pos: int) -> int:
    return (number // (10 ** pos)) % 10 if pos < len(str(number)) else 0

#Part 2.3
def is_between(x: int, y: int, z: int) -> bool:
    return (x > y and x < z) or (x < y and x > z)

def get_middle(a: int, b: int, c: int) -> int:
    if is_between(a, b, c):
        return a
    elif is_between(b, a, c):
        return b
    else:
        return c


#Part 2.4
def get_min(a: int, b: int, c: int) -> int:
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

def remove_base(r: int, g: int, b: int) -> str:
    base = get_min(r, g, b)
    return f'rgb({r - base}, {g - base}, {b - base})'

#Part 3.1
def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

#Part 3.2 
def is_right_triangle(x1: float, y1: float,
                      x2: float, y2: float,
                      x3: float, y3: float) -> bool:
    a = get_distance(x1, y1, x2, y2)
    b = get_distance(x2, y2, x3, y3)
    c = get_distance(x1, y1, x3, y3)
    
    sides = sorted([a, b, c])
    return almost_equal(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)



################################################################################

def main():
    #-YOUR TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)
    print(math_func_1(2))
    print(math_func_2(2, 3))
    print(math_func_3(3, 2, 1))

    print(get_total_cost(10000.0, 0.01, 12))
    print(get_digit(3589, 2))
    print(get_digit(3589, 10))

    print(get_middle(5, 1, 3))
    print(get_middle(9, 12, 11))
    print(get_middle(0, -5, -2))

    print(remove_base(130, 50, 130))
    print(remove_base(100, 100, 100))
    print(remove_base(255, 0, 255))

    print(get_distance(-8, 5.95, 5, 0))
    print(is_right_triangle(0, 0, 3, 0, 0, 4))
    print(is_right_triangle(3, 0, 1.5, 2.6, 0, 0))



if __name__ == "__main__":
    main()

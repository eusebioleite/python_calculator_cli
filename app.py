import argparse

def add(x, y):
    """Addition function."""
    return x + y

def sub(x, y):
    """Subtraction function."""
    return x - y

def div(x, y):
    """Division function."""
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y

def mul(x, y):
    """Multiplication function."""
    return x * y

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple python CLI calculator.")
    parser.add_argument('operation', choices=['a', 's', 'd', 'm'], help='Operation to perform (a: addition, s: subtraction, d: division, m: multiplication)')
    parser.add_argument('x', type=float, help='First argument.')
    parser.add_argument('y', type=float, help='Second argument.')
    
    args = parser.parse_args()

    if args.operation == 'a':
        result = add(args.x, args.y)
    elif args.operation == 's':
        result = sub(args.x, args.y)
    elif args.operation == 'd':
        result = div(args.x, args.y)
    elif args.operation == 'm':
        result = mul(args.x, args.y)

    print("Result:", result)

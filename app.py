import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple python CLI calculator.")
    parser.add_argument('operation', choices=['a', 's', 'd', 'm'], help='Operation to perform (a: addition, s: subtraction, d: division, m: multiplication)')
    parser.add_argument('x', type=float, help='First argument.')
    parser.add_argument('y', type=float, help='Second argument.')
    
    args = parser.parse_args()

    match args.operation:
        case 'a':
            result = args.x + args.y
            print("Result:", result)
        case 's':
            result = args.x - args.y
            print("Result:", result)
        case 'd':
            if args.y == 0 or args.x == 0:
                print("Division by zero is not allowed.")
            else:
                result = args.x / args.y
                print("Result:", result)
        case 'm':
            result = args.x * args.y
            print("Result:", result)
        case _  : 
            print('Operation to perform (a: addition, s: subtraction, d: division, m: multiplication)')

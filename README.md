# pycalc

pycalc is a simple Python command-line calculator application that performs basic arithmetic operations.

## Usage

To use pycalc, run the `app.py` script with the following command-line arguments:
```bash
python app.py <operation> <x> <y>
```
- `<operation>`: The operation to perform. Choose from 'a' (addition), 's' (subtraction), 'd' (division), or 'm' (multiplication).
- `<x>`: The first argument (operand).
- `<y>`: The second argument (operand).

## Example

To add two numbers:
```bash
python app.py a 10 5
```
This will output:
```bash
Result: 15
```
## Functions

- `add(x, y)`: Addition function.
- `sub(x, y)`: Subtraction function.
- `div(x, y)`: Division function.
- `mul(x, y)`: Multiplication function.

Each function takes two arguments (`x` and `y`) and returns the result of the corresponding arithmetic operation.

## Requirements

- Python 3.10+
- argparse (standard library)

## License

This project is licensed under the MIT License - see the LICENSE file for details.


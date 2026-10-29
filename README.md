# DATA STRUCTURE & ALGORITHM

## PAssignment Overview

This assignment implements a Python program that evaluates mathematical expressions using a stack-based algorithm.

The program reads expressions from `input.txt`, evaluates them, and writes the results to `output.txt`.

It was developed for the DCOMP320 Data Structures and Algorithm assignment at Limkokwing University of Creative Technology, Sierra Leone.

## Features

* Implements a Stack class.
* Supports push, pop, peek, is_empty, and size operations.
* Evaluates addition, subtraction, multiplication, and division.
* Supports parentheses and operator precedence.
* Supports decimal numbers and unary positive and negative signs.
* Reads multiple expressions from a text file.
* Preserves separator lines in the output file.
* Handles invalid expressions and division by zero.
* Uses exception handling for file operations.

## Project Structure

Stack-Implementation/
├── main.py
├── input.txt
├── output.txt
└── README.md

## Requirements

* Python 3
* A text editor or Python IDE
* A terminal or command prompt

No external Python libraries are required.

## Input File Format

The `input.txt` file contains one mathematical expression per line.

Expressions can be separated by lines containing hyphens.

Example:

```text
3 + 5 * 2
-----
(8 / 4) + 7 * 2
-----
10 - (2 + 3) * 4
```

## How to Run

1. Place `main.py` and `input.txt` in the same directory.
2. Open a terminal in that directory.
3. Execute the following command:

```bash
python main.py
```

Alternatively, on Windows, use:

```bash
py main.py
```

4. Open `output.txt` to view the results.

## Output File Format

The output file contains the result of each expression on a separate line. Separator lines from the input file are preserved.

Expected output:

```text
13
-----
16
-----
-10
```

## Data Structure

The program implements a Stack class using Python lists.

The stack follows the Last-In, First-Out (LIFO) principle.

The algorithm converts infix expressions to postfix notation and evaluates the postfix expressions using a stack.

## Assumptions and Limitations

* Input expressions must use valid arithmetic syntax.
* Supported binary operators are `+`, `-`, `*`, and `/`.
* Parentheses may be used to control evaluation order.
* Decimal numbers are supported.
* Division by zero is rejected.
* Invalid expressions produce error messages in the output file.
* The program does not support exponentiation, modulo, or mathematical functions.
* Floating-point arithmetic may introduce small rounding differences for some decimal calculations.

## Author

Solomon Gibrilla Munu

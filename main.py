import re


class Stack:
    """A last-in, first-out (LIFO) stack."""

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack underflow.")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def tokenize(expression):
    """Tokenize a mathematical expression."""

    pattern = r"\d+(?:\.\d*)?|\.\d+|[+\-*/()]"
    tokens = re.findall(pattern, expression)

    if not tokens or "".join(tokens) != re.sub(r"\s+", "", expression):
        raise ValueError("Invalid or empty expression.")

    return tokens


def to_postfix(expression):
    """Convert an infix expression to postfix notation."""

    output = []
    operators = Stack()
    tokens = tokenize(expression)

    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "u+": 3,
        "u-": 3
    }

    expect_operand = True

    for token in tokens:

        if re.fullmatch(r"\d+(?:\.\d*)?|\.\d+", token):
            if not expect_operand:
                raise ValueError("Missing operator between operands.")

            output.append(float(token))
            expect_operand = False

        elif token == "(":
            if not expect_operand:
                raise ValueError("Missing operator before '('.")
            operators.push(token)
            expect_operand = True

        elif token == ")":
            if expect_operand:
                raise ValueError("Invalid expression before ')'.")

            while (
                not operators.is_empty()
                and operators.peek() != "("
            ):
                output.append(operators.pop())

            if operators.is_empty():
                raise ValueError("Mismatched parentheses.")

            operators.pop()
            expect_operand = False

        elif token in ("+", "-", "*", "/"):

            if expect_operand:
                if token not in ("+", "-"):
                    raise ValueError("Unexpected operator.")

                token = "u+" if token == "+" else "u-"

            else:
                expect_operand = True

            # Unary operators are right-associative.
            while (
                not operators.is_empty()
                and operators.peek() != "("
                and (
                    precedence[operators.peek()] > precedence[token]
                    or (
                        precedence[operators.peek()] == precedence[token]
                        and token not in ("u+", "u-")
                    )
                )
            ):
                output.append(operators.pop())

            operators.push(token)

    if expect_operand:
        raise ValueError("Expression ends unexpectedly.")

    while not operators.is_empty():
        operator = operators.pop()

        if operator == "(":
            raise ValueError("Mismatched parentheses.")

        output.append(operator)

    return output


def evaluate_expression(expression):
    """Evaluate an expression using postfix notation and a stack."""

    postfix = to_postfix(expression)
    values = Stack()

    for token in postfix:

        if isinstance(token, float):
            values.push(token)

        elif token in ("u+", "u-"):
            if values.is_empty():
                raise ValueError("Missing unary operand.")

            value = values.pop()
            values.push(value if token == "u+" else -value)

        else:
            if values.size() < 2:
                raise ValueError("Insufficient operands.")

            right = values.pop()
            left = values.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                if right == 0:
                    raise ValueError("Division by zero.")
                result = left / right
            else:
                raise ValueError(f"Unsupported operator: {token}")

            values.push(result)

    if values.size() != 1:
        raise ValueError("Invalid mathematical expression.")

    return values.pop()


def format_result(value):
    """Format whole-number results without a decimal suffix."""

    if value.is_integer():
        return str(int(value))

    return str(value)


def process_files(input_file="input.txt", output_file="output.txt"):
    """Read expressions from a file and write evaluated results."""

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} was not found.")
        return

    output_lines = []

    for line_number, line in enumerate(lines, start=1):
        expression = line.strip()

        if not expression:
            output_lines.append("")
            continue

        if re.fullmatch(r"-+", expression):
            output_lines.append(expression)
            continue

        try:
            result = evaluate_expression(expression)
            output_lines.append(format_result(result))
        except (ValueError, OverflowError) as error:
            output_lines.append(f"Error on line {line_number}: {error}")

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write("\n".join(output_lines))

            if output_lines:
                file.write("\n")

        print("Evaluation completed.")
        print(f"Results written to {output_file}.")

    except OSError as error:
        print(f"Error writing output file: {error}")


if __name__ == "__main__":
    process_files()
    
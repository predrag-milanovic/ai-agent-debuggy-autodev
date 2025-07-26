class Calculator:   # A basic calculator that evaluates infix mathematical expressions. Supports +, -, *, / operations.

    def __init__(self):
        # Operator to function mapping with lambda expressions
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,   # Lowest precedence
            "-": 1,
            "*": 2,
            "/": 2,   # Highest precedence
        }

    def evaluate(self, expression):                     # Public method to evaluate an expression string.
        if not expression or expression.isspace():      # expression: String containing math expression (e.g. "3 + 5").
            return None                                 # ValueError: For invalid expressions or operators.
        tokens = expression.strip().split()             # Tokenize and process.
        return self._evaluate_infix(tokens)             # float/int: Result of calculation. Delegate to infix processor.

    def _evaluate_infix(self, tokens):    # Algorithm implementation for infix notation. Uses two stacks (values and operators) to handle precedence.
        values = []       # Stack for operands
        operators = []    # Stack for operators

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
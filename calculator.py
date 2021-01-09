class Equation:
    PRECEDENCE = 0
    EVAL = 1
    operators = {
        "-": (2000, lambda x, y: x-y),
        "+": (1000, lambda x, y: x+y),
        "*": (3000, lambda x, y: x*y),
        "/": (4000, lambda x, y: x/y),
        "^": (5000, lambda x, y: x**y),
    }
    
    def __init__(self):
        self.equation = []
        self.operator_list = []

    def eval_operator_list(self, equation):
        operator_list = []
        for i in range(0, len(equation)):
            if type(equation[i]) == list:
                operator_list.append(self.eval_operator_list(equation[i]))
            elif equation[i] in Equation.operators:
                operator_list.append(i)
        return operator_list

    def _order_operators(self, operator):
        if type(operator) == list:
            return 10000
        return Equation.operators[self.equation[operator]][Equation.PRECEDENCE] - operator

    def sort_operators(self):
        self.operator_list = sorted(self.operator_list, key=self._order_operators)
        return self.operator_list
    
    def simple_eval_equation(self, equation_string):        
        self.equation = self._string_to_equation(equation_string)
        if len(self.equation) == 1:
            return self.equation[0]
        self.operator_list = self.eval_operator_list(self.equation)
        self.sort_operators()
        while len(self.equation) > 1:
            operator = self.operator_list.pop()
            result = Equation.operators[self.equation[operator]][Equation.EVAL](self.equation[operator-1], self.equation[operator+1])
            self.equation = self.equation[:operator-1] + [result] + self.equation[operator+2:]
            self.operator_list = self.eval_operator_list(self.equation)
            self.sort_operators()
        return result
    
    def _string_to_equation(self, equation_string):
        self.equation = []
        num_start = 0
        for i in range(len(equation_string)):
            if equation_string[i] in Equation.operators:
                if num_start != i:
                    self.equation.append(float(equation_string[num_start:i]))
                    self.equation.append(equation_string[i])
                    num_start = i+1
        self.equation.append(float(equation_string[num_start:]))
        return self.equation
    
    def eval_equation(self, equation=""):
        new_string = '('+equation+')'
        eq_stack = ['(', ""]
        i = 1
        j = 1
        while eq_stack and i <= len(equation)+1:
            if new_string[i] == ')':
                eq = eq_stack[-1]
                simple_equation = ""
                while eq != '(':
                    if eq != "(":
                        simple_equation = eq + simple_equation
                        eq_stack.pop()
                    eq = eq_stack[-1]
                solved = self.simple_eval_equation(simple_equation)
                eq_stack[len(eq_stack)-1] = str(solved)

            elif new_string[i] == '(':
                if eq_stack[-1] != "":
                    eq_stack.append('(')
                else:
                    eq_stack[-1] = '('
                eq_stack.append("")

            else:
                eq_stack[-1] += new_string[i]

#             print(i, j, len(eq_stack), eq_stack)
            i += 1
        return float(eq_stack[0])


def eval_var_equation(equation, variables):
    for var in variables:
        if (type(variables[var]) == float or type(variables[var]) == int):
            equation = equation.replace(var, f"({variables[var]})")
        else:
            equation = equation.replace(var, f"(0)")
    a = Equation()
    try:
        return a.eval_equation(equation)
    except (ZeroDivisionError):
        return None

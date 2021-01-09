# eval_string
Evaluate string containing mathmatical equation without using python's eval() function.

### Usage
## 1. Simple Equation containing no variables
First import function Equation from calculator.py file.
```
eq = Equation()
eq.eval_var_equation("1+2-3*4/5^6")
```
## 2. Equation with variables
First import function eval_equation from calculator.py file.
```
eval_equation("1+2-A*4/5^6", {"A": 4})
```
where A is a variable with value 4.

### Support
1. Equation currently support 5 operations +,-,*,/,^. You can add new operator in the operators dictionary of Equation, make sure to specify the precendence of the operator in the first position of tuple, and at the second position specify the function which evaluate the operation. 
2. Brackets are also supported.


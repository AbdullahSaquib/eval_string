# eval_string
Evaluate string containing mathematical expression without using python's eval() function.

### Usage
## 1. Simple expression without variables
Import function eval_equation from calculator.py file, pass mathematical expression in string format as parameter
```
eval_equation("1+2-3*4/5^6")
```
## 2. Equation with variables
Import function eval_equation from calculator.py file, pass mathematical expression in string format as parameter, mathematical expression can contain multiple variables, pass a dictionary with variable values
```
eval_equation("1+2-A*4/5^6", {"A": 4})
```
In the above expression, A is a variable with value 4.

### Support
1. Expression currently support 5 operations +,-,*,/,^. You can add new operator in the operators dictionary of Equation, make sure to specify the precendence of the operator in the first position of tuple, and at the second position specify the function which evaluate the operation. 
2. Brackets are also supported.


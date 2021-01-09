from calculator import eval_var_equation, Equation

print(eval_var_equation("1+A", {"A":2}))

a = Equation()
test_eval = [
    ("1+2", "3.0"),
    ("5+4-3+2", "8.0"),
    ("5+4/4*3", "8.0"),
    ("(5+4)/4*3", "6.75"),
    ("2^3", "8.0"),
    ("2^3*4", "32.0"),
    ("(-1)", "-1.0"),
    ("-1*3", "-3.0"),
    ("1+2+3+4", "10.0"),
    ("1*2*3*4", "24.0"),
    ("8/4/2/1", "1.0"), # check operation left to right
    ("8-4-2-1", "1.0"), # check operation left to right
    ("(8-4)-(2-1)-(1-4)", "6.0"), # check bracket operation left to right
    ("4/2*3+1-2", str(4/2*3+1-2)),
    ("-2+1+3*4/2", str(-2+1+3*4/2)),
]
for eq, res in test_eval:
    eval_res = a.eval_equation(eq)
    print(eq, res, eval_res, str(eval_res)==res)

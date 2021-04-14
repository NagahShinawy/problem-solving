'''
Given few lines of code inside a string variable and execute the code inside the string.

Examples:

Input:
code = """ a = 6+5
           print(a)"""
Output:
11
Explanation:
Mind it that "code" is a variable and
not python code. It contains another code,
which we need to execute.

Input:
code = """ def factorial(num):
               for i in range(1,num+1):
                   fact = fact*i
               return fact
           print(factorial(5))"""
Output:
120
Explanation:
On executing the program cantoning the
variable in Python we must get the result
after executing the content of the variable.
'''


def run(text_as_code: str):
    exec(text_as_code)


run("print('Hello World')")
run("name = 'John'; print(name)")
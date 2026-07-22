def function1():
    print(" function 1 is executed")
def function2(some_function):
    print(" function 2 is executed")
    some_function()
function2(function1)
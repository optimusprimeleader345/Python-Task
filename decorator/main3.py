def cool():
    def super_cool():
        return "i am super cool"
    return super_cool

some_func = cool()
print(some_func())
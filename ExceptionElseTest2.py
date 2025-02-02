a= 20
b= 5
def tests_exception(c):
    try:
        print("Before Exception")
        divide = a / c
        print("After Exception", divide)
    except ZeroDivisionError:
        print("Anumber cn't be divided by Zero")
        print("Retry | Any other logic")
    else:
        print("Else Block Excecuted")
    finally:
        print("Finally Block will allways executed")

tests_exception(10)
#tests_exception(0)
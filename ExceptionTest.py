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

tests_exception(5)
tests_exception(0)
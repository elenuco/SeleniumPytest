number=[1,2,3]
#if(number)>3:
 #   print("Before Exception")
  #  raise Exception("Exception is Raised")
   # print("After Exception")
a = 20
b = 5
def test_exception():
    print("Before Exception")
    divide = a/b
    print("After Exception", divide)

test_exception()
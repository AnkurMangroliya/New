# This is try and except example
try:
    result = 10 / 4
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"An error occured: {e}")
#  else will run if no exception occurs
else:
    print("No exception occurred, result is:", result)
finally:
    print("this must run after above cases.")


# Exception and base Exception
try:
    result = 10 / 2
except Exception as e:
    print(e)
except BaseException as e:
    print("BaseException caught:", e)




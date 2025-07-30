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

import asyncio

async def async_function():
    print("started")
    await asyncio.sleep(3)
    print("finished")

async def main():
    print("Main started")
    await async_function()
    print("Main finished")

if __name__ == "__main__":
    asyncio.run(main())
    print("Program finished")




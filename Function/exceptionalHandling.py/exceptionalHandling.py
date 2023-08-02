



try:
    a = 10
    print(a/0)
except NameError:
    print("Check the variables")
except ZeroDivisionError:
    print("Can't divide by 0")



try:
    a = int(input("Enter a value ="))
    b = int(input("Enter a value ="))
    print(a+b)
except ValueError:
    print("Cannot add a String")
    raise ValueError("Cannot add a String")
except:
    print("Something went wrong")

else:
    print("Errorless Code")
finally:
    print("End of the Program")
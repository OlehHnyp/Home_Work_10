age = input("Enter your age:")

def even_odd(inf):
    try:
        inf = int(inf)
        if inf < 1:
            raise IndexError
        status = "odd"
        if inf%2 == 0:
            status = 'even'
        print(f"Your age is {status}")
    except ValueError:
        print("It's not a number")
    except IndexError:
        print("Age should be positive number")

even_odd(age)
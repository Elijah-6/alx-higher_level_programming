def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        print("Inside result: {}".format(result))

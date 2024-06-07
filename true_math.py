from math import inf

def divide (first, second):
    if second == 0:
        return float("inf")
    else:
        result = first / second
        return result


# print(divide(5,87))
# print(divide(4,0))
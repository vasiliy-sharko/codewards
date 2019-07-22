# Square Every Digit

# The function accepts an integer and returns an integer

# If we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.


def square_digits(num):
    return int(''.join([str(int(x) ** 2) for x in str(num)]))


print(square_digits(9119))

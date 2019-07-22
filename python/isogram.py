# Isograms

# Return True if input is an empty string or a string that has no duplicate letters, case-insensitive


def is_isogram(string):
    return not string or not bool([x for x in string.lower() if string.lower().count(x) > 1])


print(is_isogram(''))
print(is_isogram('isogram'))
print(is_isogram('isograms'))

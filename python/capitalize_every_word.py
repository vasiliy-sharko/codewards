# Jaden Casing Strings

# Jaden Smith is known for some of his philosophy that he delivers via Twitter.
# When writing on Twitter, he is known for almost always capitalizing every word.

# Your task is to convert strings to how they would be written by Jaden.


def to_jaden_case(string):
    return ' '.join([x.capitalize() for x in string.split(' ')])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))

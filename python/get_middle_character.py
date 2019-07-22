# Get Middle Character

# Input: string with number of character 0 < n < 1000

# Returns middle char if the len is odd, 2 middle chars if len is even


def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        return s[len(s) // 2]


print(get_middle('middle'))

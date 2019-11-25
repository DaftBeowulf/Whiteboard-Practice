import math


def find_rotation_point(words):
    index = 0
    while words[index] < words[index+1]:
        index += 1
    return index + 1

# first pass, takes O(n)


def find_rotation_point_bs(words):
    first_word = words[0]

    floor_index = 0
    ceiling_index = len(words) - 1

    while floor_index < ceiling_index:
        guess_index = math.floor(
            floor_index + ((ceiling_index - floor_index) / 2))
        if words[guess_index] >= first_word:
            floor_index = guess_index
        else:
            ceiling_index = guess_index
        if floor_index + 1 == ceiling_index:
            break

    return ceiling_index

# cutting problem in half with each iteration, so O(log N)


example = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
print(find_rotation_point_bs(example))  # should be 5

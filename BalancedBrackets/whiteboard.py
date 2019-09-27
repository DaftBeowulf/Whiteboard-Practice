def balancedBrackets(brackets):
    # when finding opening bracket, it needs to be inserted into a queue list
    # when finding a closer, we should be able to look at the most recent opener and it should match
    # if it does not match, return false and kill function
    # if it does match, pop opener from queue and continue iterating over input string
    # if iterate over entire string with 0 "false" returns, return true

    matches = {')': '(', '}': '{', ']': '['}
    openers = []
    for bracket in brackets:
        if bracket in matches:  # is closer
            # check if the last opener in the openers list is the match for the closer
            if openers[-1] != matches[bracket]:
                return False
            openers.pop()  # if it was a match, remove it from end of openers list
        else:  # is opener
            openers.append(bracket)

    return True


print(balancedBrackets('[]{}()'))   # should return true
print(balancedBrackets('[{[()]}]'))   # should return true
print(balancedBrackets('[({}}]'))  # should return false

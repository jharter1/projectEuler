def leastCommonDenominator(valsList):
    currentAnswer = max(valsList)
    # in case it just happens to be 1 & 2;
    while(True):
        # should the current answer against all values in the valsList divide evenly out to zero... we've won
        if all(currentAnswer % allvalues == 0 for allvalues in valsList):
            break
        # if not, let's try the next number. this works; it isn't very elegant.
        currentAnswer = currentAnswer + 1
        pass
    return currentAnswer

print(leastCommonDenominator([11,12,13,14,15,16,17,18,19,20]))
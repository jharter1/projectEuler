def isPalindrome(s):
    return str(s) == str(s)[::-1]

palindromeList=[]

for i in range(900,999):
    for j in range (900,999):
        product = i*j
        if isPalindrome(product):
            palindromeList.append(product)
            pass
        pass
    pass
print(max(palindromeList))
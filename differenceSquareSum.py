sumSquare = 0
squareSum = 0
justSum = 0


for i in range(1,101):
    sumSquare = sumSquare + i**2

for i in range(1,101):
    justSum = justSum + i
    squareSum = justSum ** 2

diffSuSqSqSu = squareSum - sumSquare

print(diffSuSqSqSu)

# holy shit i wrote this entire fucking thing on my own. 
# 
# and i actually know how it worked.
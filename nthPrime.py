n = int(input('Gib mir : '))
primes = [2,3]
i=3

if(0<n<3):
    # this mostly deals with primes being 1 or 2, definitely some edge cases
    print(n,'ste Prime Nummer ist :',primes[n-1])
elif(n>2):
    # however, if we go higher, we start out a while loop
    while (True):
        # increment i to 4
        i+=1
        # create a status condition
        status = True
        # if any numbers between 2 and anything beyond it (because everything is divisible by 1,)
        for j in range(2,int(i/2)+1):
            # if those numbers cannot evenly divide,
            if(i%j==0):
                # then forget about it, and go back to the re-incrementing phase
                status = False
                break
        # now, if this number cannot be divided evenly by any number that came before it,
        if(status==True):
            # add it to the old list
            primes.append(i)
            # but if we got to that phase of the list when we can finish,
        if(len(primes)==n):
            # close out
            break
        # provide the people with what they love
    print(n,'ste Prime Nummer ist :', primes[n-1])
else:
    print('Das ist nicht so gut')

# this shit was not so straightforward and i had to google an 'nth prime # generator'
#
# after that, I translated it into german so it would look or feel less cheaty
def primer(x):
    for i in range(1,x):
        for t in range(2,x):
            if (x%t==0):
                k=x/t
                print(x,"equals",t,"*",k) ## 
                break
        else:
            print(x, "is a Prime Number")
        break ## without this break the code would repeat for the range of 1 to x-1 
    ##small test code I wrote to find small primes

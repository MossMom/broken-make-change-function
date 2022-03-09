def makeChange(amount):
    q = 0
    n = 0
    d = 0
    p = 0
    ran = 0 # use this later to stop the function if it breaks
    
    print("Running")
    maxRun = amount*5 # limit the max number of times to run change based on initial amount
    
    while amount > 0:
        
        print("Amount is", amount)
        
        ran += 1
        if ran > maxRun: # check how many times the code ran
            print("ERROR: WEIRD FLOAT ISSUE AGAIN?")
            print("Amount was", amount)
            amount = 0
        
        if amount >= 0.25: # if amount is more than a quarter, remove a quarter
            q += 1
            print(q, "q")
            amount -= 0.25
            
        elif amount >= 0.10: # if amount is more than a dime, remove a dime
            d += 1
            print(d, "d")
            amount -= 0.10
            
        elif amount >= 0.05: # if amount is more than a nickel, remove a nickel
            n += 1
            print(n, "n")
            amount -= 0.05
            
        elif amount >= 0.01: # if amount is more than a penny, remove a penny
            p += 1
            print(p, "p")
            amount -= 0.01
            
    print("\nQuarters:", q, "\nDimes:", d, "\nNickels:", n, "\nPennies:", p)

while True:
    print("\nHow much is change being made for?\n")
    userInput = input()
    makeChange(float(userInput))
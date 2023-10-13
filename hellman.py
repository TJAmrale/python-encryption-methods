import random

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
              47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #list of all prime numbers between 1-100 for random selection

def square_and_multiply(a, b, n): #based on provided pseudocode
    d = 1
    k = len(bin(b)) - 2 #convert to binary, -2 used because python adds 0b 

    for i in range(k, -1, -1): #first -1 goes to the highest bit, second -1 decrements i 
        d = (d * d) % n  

        if (b >> i) & 1:  #shift selected bit and shift it all the way to the right, then check and retain on the 1
            d = (d * a) % n

    return d

def check_prime(num):
    if num <= 1: #numbers less than or 1 cannot be prime
        return False

    for x in range(2, num): #check numbers 2 to the selected Prime
        if not num % x: #checks if P is divisble by any number in the range
            return False
    return True

def check_primitive(g,p):
    primitive_roots = [] #store all primitive roots in list
    for g in range(2,p):  
        nums = set() #store values 
        primitive = True #assuming g is a primitive root, unless updated

        for i in range(1,p): 
            out = pow(g,i,p) #g^i mod p
            if out in nums: # is result already in set?
                primitive = False #if it is then g becomes false
                break
            nums.add(out) # add value to the set
        
        if primitive and len(nums) == p-1: #checks if all values have been checked excluding the prime
            primitive_roots.append(g) #if g is still true then add it to the list
    return primitive_roots

while True:
    print("Diffie-Hellman Algorithm")
    print("1. Manual Inputs")
    print("2. Automatic Inputs")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == '1':

        while True:
            P = int(input("Enter P: "))
            if check_prime(P) == True:
                break
            else:
                print("This number is not a prime please enter again")

        while True: 
            G = int(input(f"Enter the Primitive root of {P}:"))
            primitive_roots = check_primitive(G,P)
            if G in primitive_roots:
                break 
            else:
                print(f"This is not a primitive root of {P}, try again.\n")
                print(f"These are the primitive roots for prime {P}\n", primitive_roots)
        
        while True: 
            Xa = int(input("Enter the key for User A: "))
            if 1 <= Xa < P:
                break  
            else:
                print(f"User A  key has to be between 1 and {P}")

        while True:  
            Xb = int(input("Enter the key for User B: "))
            if 1 <= Xb < P:
                break  
            else:
                print(f"User B  key has to be between 1 and {P}")

        
        Ya = square_and_multiply(G,Xa, P) #calculating the Ya and Yb using the square multiply algorithm
        Yb = square_and_multiply(G,Xb, P) 
        
        final_key1 = square_and_multiply(Yb,Xa, P) #final key calculated using Ya and Yb
        final_key2 = square_and_multiply(Ya,Xb, P)

        print("The key for User A is: ", final_key1)
        print("The key for User B is: ", final_key2)

    
    elif choice == '2':
        P = random.choice(prime_numbers) #random module used to get a random number from the defined list
        G = random.choice(check_primitive(2,P)) #picks a random number from the primitive_roots list
        Xa = random.randint(1, P - 1)
        Xb = random.randint(1, P - 1)

        print("\nRandom Values")
        print("Prime Number:", P)
        print("Primitive Root:", G)
        print("User A key:", Xa)
        print("User B key:", Xb)

        Ya = square_and_multiply(G,Xa, P)
        Yb = square_and_multiply(G,Xb, P)
        
        final_key1 = square_and_multiply(Yb,Xa, P)
        final_key2 = square_and_multiply(Ya,Xb, P)

        print("The key for User A is: ", final_key1)
        print("The key for User B is: ", final_key2)
        print("\n")

    elif choice == '3':
        break
    else:
        print("Invalid choice")

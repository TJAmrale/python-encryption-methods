#SDES functions
IP = [2,6,3,1,4,8,5,7]
inv_IP = [4,1,3,5,7,2,8,6]

P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]

E_P = [4,1,2,3,2,3,4,1]
P4 = [2,4,3,1]

#S Boxes
S0 = [[1, 0, 3, 2], 
      [3, 2, 1, 0], 
      [0, 2, 1, 3], 
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3], 
      [2, 0, 1, 3], 
      [3, 0, 1, 0], 
      [2, 1, 0, 3]]

K1 = ""
K2 = ""
cipher = ""
plain = ""
tenkey = ""
msg = ""

def shiftL(list): #removes the first element in the list and adds it back to the end
    return list[1:] + list[0] 
#suppose list is [1,2,3,4] then list[1:] would be everything including index 1 so list[1:]=[2,3,4]
#now list[0] is the first index so 1, after adding 1 back to the list it will be [2,3,4,1] esentially doing a left shift

def reorder(input, function): #this reorders the input depeding on which permutation function has been selected
      out = "" #storing the output
      for i in function:
        out +=input[i-1] #i-1 is used to get back to 0
      return out


def xor(list, function):
    out = ""
    for i in range(len(list)): #gets the length of the list, range will create indices 
        if list[i] == function[i]: #only if both are the same size, the function proceeds
            out += "0" #if both bits match make it a 0 and append 
        else:
            out += "1" #if not matching make it a 1 and append
    return out

     

def sbox(box, input):
    row = int(input[0] + input[3], 2) #gets the first and last input from EP XOR split, and determines them as row, int(,2) converts them to decimal via base 2 
    col = int(input[1] + input[2], 2) #gets the middle two bits and makes them column coordinates 
    return '{0:02b}'.format(box[row][col]) #converts the output back to binary from decimal, 0 corresponds to box[row][col],  02 means it will be have atleast 2 binary characters


def encryption(msg, K1, K2):
    temp = reorder(msg, IP) #reorder using according to IP 
    temp = FK(K1, temp) #generate fk 1
    temp = temp[4:] + temp[:4] # put the first 4 at the end and last 4 at the start
    temp = FK(K2, temp) # generate fk 2
    cipher = reorder(temp, inv_IP) #create the cipher by reordering using inverse IP
    return cipher


def decryption(): #to decrypt the keys are reversed
    cipher = input("Enter 8 bit cipher: ")  
    tenkey = input("Enter 10 bit key: ")
    K1, K2 = gen_keys(tenkey) #generate both keys
    temp = reorder(cipher, IP) #reorder cipher using IP
    temp = FK(K2, temp) #generate fk2
    temp = temp[4:] + temp[:4] #first 4 go to end last 4 go to start
    temp = FK(K1, temp) #generate fk2
    plain = reorder(temp, inv_IP) # reorder to create the plain text
    return plain, K1, K2

def FK(ten_key, msg): # order is Split->E/P->XOR->Split->S-Boxes->P4->XOR and swap 
    left = msg[:4] #split user 8 bit into two halfs 
    right = msg[4:]
    temp = reorder(right, E_P) #reorder the right half according to the E/P list
    temp = xor(temp, ten_key) # apply XOR to the reordered right half and the 10bit key the user entered
    left_bits = sbox(S0, temp[:4])  #apply the S0 box to the first 4 bits
    right_bits = sbox(S1, temp[4:]) #apply the S1 box to the last 4 bits
    left_bits = "0" * (2 - len(left_bits)) + left_bits  #makes sure values have exactly 2 binary values
    right_bits = "0" * (2 - len(right_bits)) + right_bits #if one side has value of 1 then we get 2-1=1 which means one 0 will be added giving us 01 after the bit is readded
    temp = reorder(left_bits + right_bits, P4) # the left and right split are combined and reorderd using P4
    temp = xor(left, temp) # XOR is applied to the rordered list and the first left split
    return temp + right #they are combined again with the first right split.

def gen_keys(ten_key): # order is P10->split->Left Shift 1->P8=K1->Left Shift 2->P8=K2
    temp = reorder(ten_key, P10) # reorder list according to P10 
    left = temp[:5] #split into left and right side
    right = temp[5:]
    left = shiftL(left) #shift sides to left by 1
    right = shiftL(right)
    K1 = reorder(left+right, P8 ) #create key 1
    left = shiftL(left) #shift to left by 2
    right = shiftL(right)
    left = shiftL(left)
    right = shiftL(right)
    K2 = reorder(left+right, P8 ) #create key 2
    return K1, K2

while True:
    print("S-DES Encryption and Decryption")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == '1':
        msg = input("Enter 8 bit message: ")
        tenkey = input("Enter 10 bit key: ")
        K1, K2 = gen_keys(tenkey)
        cipher = encryption(msg, K1, K2)
        print("Key 1 is: ", K1)
        print("Key 2 is: ", K2)
        print("Cipher text is:", cipher)
    elif choice == '2':
        plain, K1, K2 = decryption()
        print("Key 1 is: ", K1)
        print("Key 2 is: ", K2)
        print("Plain text is:", plain)
    elif choice == '3':
        break
    else:
        print("Invalid choice")

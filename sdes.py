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


def reorder(input, function): #this reorders the input depeding on which permutation function has been selected
      out = "" #storing the output
      for i in function:
        out +=input[i-1] #i-1 is used to get back to 0
      return out

def shiftL(list): #removes the first element in the list and adds it back to the end
    return list[1:] + list[0] 
#suppose list is [1,2,3,4] then list[1:] would be everything including index 1 so list[1:]=[2,3,4]
#now list[0] is the first index so 1, after adding 1 back to the list it will be [2,3,4,1] esentially doing a left shift

def shiftR(list): #removes the last element in the list and adds it back to the front
    return list[-1] + list[:-1]
#list[-1] goes backwards in the index and selects the last element which would be 4, this is easier than calculating the length of the list
#list[:-1] would be everything to the left of 5 so [1,2,3,4], then 5 is added to this list becoming [4,1,2,3], doing a right shift

def xor(list, function):
    out = ""
    for i in range(len(list)): #gets the length of the list, range will create indices 
        if list[i] == function[i]: #only if both are the same size, the function proceeds
            out += "0" #if both bits match make it a 0 and append 
        else:
            out += "1" #if not matching make it a 1 and append
    return out


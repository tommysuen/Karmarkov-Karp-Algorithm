import random

#array1 = [10,8,7,6,5]
array1 =[]
for i in range(100):
    apples1 = random.randint(1,10 **12)
    array1.append(apples1)

#print(array1)

def KK(array):
    
    #Copies array to another array for manipulation without altering the original array
    KK_array = array[:]
    
    #Checker Flags to avoid changing values more than once
    Flag1 = 1
    Flag2 = 1
    
    array_length = len(array)
    KK_array = array[:]
    
    #Checks that if the array is <= 1, return the array
    if len(array) <= 1:
        return array

    #Finds first and second max
    first = max(KK_array)
    KK_array.remove(first)
    second = max(KK_array)
    
    while(second != 0): #Checks that there is at least one non-zero value:
        for i in range(array_length):
            if (Flag1 != 0 or Flag2 != 0):
                if (array[i] == first and Flag1 == 1): #Finds Max Value and then replacing it with the difference
                    array[i] = abs(first - second)
                    Flag1 = 0                          #Checks that a value has already been changed and no more valids should be changed
                elif (array[i] == second and Flag2 == 1): #Looks for second max value and turning it to 0
                    array[i] = 0
                    Flag2 = 0                         #Checks that a value has already been changed and no more valids should be changed
        Flag1 = 1
        Flag2 = 1
        KK_array = array[:]
        first = max(KK_array)
        KK_array.remove(first)
        second = max(KK_array)
        
    return array

print(KK(array1))


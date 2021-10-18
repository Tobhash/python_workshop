print("Hello, this script will generate the Fibonacci Sequence.")
print("Please type how many elements you want to be generated?")

num_of_elements = input()
num_of_elements = int(num_of_elements)

#preparing two first elements for the sequence
n0 = 0
n1 = 1

#Checking to determine given input
if num_of_elements <= 1:
    print("0")

elif num_of_elements == 2:
    print("0, 1")

else:
    print("0 , 1", end=", ")
    #every next element will be stored in result variable
    result = 0
    #calculating the sequence without first, second and the last element
    for i in range(num_of_elements - 3):
        result  = n0 + n1
        print(result, end=", ")
        n0 = n1
        n1 = result
    #last element of the sequence
    print(n0 + n1)

#End message
print("\nSequence finished.")
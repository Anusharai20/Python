#ALGORITHM:
#STEP 1: Declare and initialize an array.
#STEP 2: Store first element in variable max.
#STEP 3: Loop through the array from 0 to length of the array and compare the value of max with elements of the array.
#STEP 4: If any element is greater than max, max will hold the value of that element.
#STEP 5: At last, max will hold the largest element in the array.
#initializing an array.
a = [23,45,2,150,189,54]
#Storing  the first variable of the list in variable max
max = a[0]
# Loop through the array from 0 to length of the array and compare the value of max with elements of the array.
for i in range (len(a)):
    if(a[i] > max):
        max = a[i]
print("The largest element of the list is: " +str(max))
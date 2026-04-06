arr=[1,22,5,55,32]
max_number=arr[0]
secondmax_number=arr[0]

for x in arr:
    if x>max_number:
       secondmax_number=max_number
       max_number=x
    elif x>secondmax_number and x!=secondmax_number:
       secondmax_number=x
print("secondmax_number")


#list comprehensions is used to print list in single line code

l=[]
x = int(input())
y = int(input())
z = int(input())
n = int(input())
for i in range(0,x+1): # neasted loop in this type we can print pairs
 for j in range(0,y+1):
  for k in range(0,z+1):
   if i+j+k!=n:
    l.append([i,j,k])
print(l)

print("withouth using list comprehension:")
numbers=[]
for i in range(1,11):
  numbers.append(i)
print(numbers)
          

print("using list comprehension:")
numbers=[num for num  in range(1,11)]
print(numbers)

print("gretest number in list:")
numbers=[10,4,5,9,35,78]
result=[num for num in numbers if num>10]
print(result)








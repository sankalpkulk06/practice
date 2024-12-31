# Code with Harry: https://www.youtube.com/watch?v=eF6nK5bSlmg

l = [1,2,3]
print(type(l), l)

# indexing similar to strings

marks = [3,5,7,"Snk", True, 8, 72]
print(marks[len(marks)-3])
print(marks[-3])
print(marks[2])

# Check if ele exists in list
if 7 in marks:
    print("Yes")
else:   
    print("No")

# print ele within a range
print(marks[2:5])

print(marks[2:7:2])

# List Comprehension: creating a lis ton the fly
names = ["1A", "1B", "2C", "2D", "3E", "3F"]
namesWith_0 = [item for item in names if "3" in item]
print(namesWith_0)

list = [i*i for i in range(4)]
print(list)

list = [i*i for i in range(10) if i%2==0]
print(list)
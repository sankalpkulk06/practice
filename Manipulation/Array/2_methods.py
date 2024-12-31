# Code with Harry: https://www.youtube.com/watch?v=scWc3F8LbOo

l = [1,2,4,6]
print(l)

# append(), adds at end of a list
l.append(7)
print(l)

# list.sort(), by default it is ascending
# list.sort(resverse=True), is descending

# list.index(<int>): (item in list)
# print(l.index(3))

# copy(): list, returns a copy of a list (change in the original) - memory reference (NOT RECOMMENDED)
m = l.copy()
m[0] = 0
print(l)

m = l
m[0] = 0
print(l)

# insert(index, value)
l.insert(1, 899)
print(l)

# extend(list), adds entire list to existing list
m = [900,1000,11100]
l.extend(m)
print(l)

# concat(), joins list
k = l + m
print(k)


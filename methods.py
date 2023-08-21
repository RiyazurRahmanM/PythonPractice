list = ['hello',1,"world"]
list.append("by python")
print(list)

nested = [2,3]
joining = [4,5,6]
nested.extend(joining)
another_joining = (7,8)
nested.extend(another_joining)
print(nested)

list.append(nested)
print(list)


list.clear()
print(list)

original = [1,2,3,"three",3]

copied = original.copy()

print(copied)
print(copied.count(3))
print(copied.count("three"))

print("index of value 3:")
print(copied.index(3))

x = input("Enter the value to Insert in copied list:")
index =  int(input("enter the index to insert:"))

copied.insert(index,x)
print(copied)
copied.reverse()
print(f"Copied list in reverse order:{copied}")

alphabets = ['a','z','d','b']
alphabets.sort()

print(alphabets)

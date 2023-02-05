thisList = ["apple", "banana", "cherry"]
print(thisList[1])
print(thisList[1:2])
thisList[1] = "kiwi"
print(thisList)
thisList[1:2] = ["watermelon"]
print(thisList)
thisList.append("orange")
thisList.insert(1, "orange")
print(thisList)
thisList.remove("cherry")
print(thisList)
# Remove index
del thisList[0]
thisList.pop(1)
print(thisList)
# Remove end
thisList.pop()
print(thisList)
# Clear list
thisList.clear()
# Remove all
del thisList
thisList = ["apple", "banana", "cherry"]
# Loop
for x in thisList:
    print(x)
for i in range(len(thisList)):
    print(thisList[i])

i = 0
while i < len(thisList):
    print(thisList[i])
    i += 1
print("----------")
#Sort
thisList.sort()
print(thisList)
thisList.sort(reverse=True)
print(thisList)


def myfunc(n):
    return abs(n-50)
thisList = [100,50,65,82,23]
thisList.sort(key=myfunc)
thisList = ["apple", "banana", "cherry"]
thisList.sort(key=str.lower)
thisList.reverse()
print(thisList)

#method
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list
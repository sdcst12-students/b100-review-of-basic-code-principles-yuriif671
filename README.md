# 201-list-comprehension

Objectives
* create lists from lists using list comprehension

List comprehension is a shortcut; it is not strictly necessary, but is worth knowing because you will often run into examples that use it to make code more concise.  List comprehension is used to make a list from an existing list.  Consider the following code:

```
oldList = [3,4,5,6,9,10]
newList = []
for i in oldList:
  newList.append(i)
```

This code interates through the old list, and each entry is added to the new list.  With list comprehension, the code can be simplified to the following:
```
oldList = [3,4,5,6,9,10]
newList = [i for i in oldList]
```

List comprehension can also be used to use conditional operators to choose specific values from a list:
```
# finds all even numbers from the oldList
oldList = [3,4,5,6,9,10]
newList = [i for i in oldList if i%2==0]
```


The syntax for list comprehension is:

newlist = [*expression* for *item* in *iterable* if *condition* == True]
 
A great resource for looking at list comprehension includes the w3schools page at https://www.w3schools.com/python/python_lists_comprehension.asp

List comprehension can also be used to handle nested for loops.  Consider:
```
timestables = []
for i in range(1,11):
  for j in range(1,11):
    timestables.append(f"{i} x {j} = {i*j}")
```
the same could be done with 2 lists in your list comprehension
```
timestables = [f"{i} x {j} = {i*j}" for i in range(1,11) for j in range(1,11)]
print(timestables)
```
or even consider:
```
for x in [f"{i} x {j} = {i*j}" for i in range(1,11) for j in range(1,11)]:
  print(x)
```

# Assignment
* Work through the assignments in assignment.py to convert your code from your previous assignment to use list comprehension
* Open up deck.py.  Use list comprehension with the 2 lists to create a new list that shows all 52 possible cards in a deck of cards, and then print the first 5 cards in thd deck.

# Further Practice
* expand on your deck assignment. Some function ideas:
    * shuffle the deck
    * deal x number of cards, where x is an input parameter that can be set during the function call
    * sort the cards in a list by suit and by rank (this one is challenging!)

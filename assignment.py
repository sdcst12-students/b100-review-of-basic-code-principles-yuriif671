#!python3
# Use list comprehension to make each of these assignments work
# You can use the test functions with assertion statements to see if your code is working properly

def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = []

    return integers

def getFactors(myList,number):
    # myList : expected list or tuple
    # number : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []

    return factors

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives = []

    return negatives


def test1():
  l1 = [x * .5 for x in range(20)]
  assert getIntegers(l1) == [i for i in range(10)]
  l2 = [x /3 for x in range(12)]
  assert getIntegers(l2) == [i for i in range(4)]

def test2():
  l1 = range(1,10)
  assert getFactors(l1,12) == [1,2,3,4,6]
  assert getFactors(l1,21) == [1,3,7]
  assert getFactors(l1,18) == [1,2,3,6,9]

def test3():
  easy1 = [5,10,15,2,4,6,8]
  easy2 = [-2,-4,-6,2,4,6,0.1]
  numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
  numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
  assert getNegatives(easy2) == [-2,-4,-6]
  assert getNegatives(numbers1) == [-3]

def main():
  test1()
  test2()
  test3()


if __name__ == "__main__":
    main()

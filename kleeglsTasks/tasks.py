#Task 1
Arr = input("Task #1\nPress array:\n")
intArr = list(map(int, Arr.split()))
print("Index of max:",intArr.index(max(intArr)))

#Task 2
Arr2 = input("\n -----------------------------------------------\nTask #2\nPress fucked array: \n").split()
Per1 = input("\nPress ur value for search: \n")
print("Ur value",Per1,"and index:", Arr2.index(Per1))

#Task 3
Arr3 = input("\n------------------------------------------------Task #3\nPress array for reverse:").split()
print(Arr3[::-1])

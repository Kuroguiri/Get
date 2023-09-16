#
#
# inter = [1,2,43,5,2]
# inter2 = 5,4,6,2,2,2
# inter.extend(inter2)          #exted list
# inter.pop(0)                  #remove value on "0" index
# print(inter.index(5))         #give index of "5" value
# print(inter)
# stringer = ["Mass", "Effect", "Mast have"]
# inter.insert(2,56)            #swap value on "2"-index to "56"
# print(inter.index(5))
# print(inter.count(2))         #Counter of values in list
# print(inter[2])
#
# print(stringer[0],stringer[1]," - ",stringer[2])

# listik = "Tom", "Kruz", 999, 5.2      #lists can be with diff types of values
# print()
# print(listik)
#
# list1 = [2]*4                   #multypliy of values in list
# list2 = 5,6,7,"Tom"*2,"n"+"e"*3+"d", ["Dima"]*3
# list1+=list2                    #easyst path to extend list
# print(list1)
# print(list1[-2])                # "[-2]" negative index adressed to reverse part of the list,
#                                 # "[-1]" the index of last value in list
'''
list3 = [64,5,43,2,57]

l1,l2,l3,l4,l5=list3
print(l5)
print(len(list3))                 #length of list3, count of all values
print(list3[:2])
print(list3[1:-1:1])              #slice of list "start:end:step"
print(list3[0:-1:2])

print("--------------------------------------")
def sortByFract (intC):         # sortByFract - key for "sort." returning value, who change list value
    return int(str(intC)[-1])

list3.sort(key=sortByFract)
print(list3)
print(max(list3))
list3=[64,5,43,2,57]
print("method \"sorted()\" without \".sort\"\n",sorted(list3,key=sortByFract))

if 4 in list3:
    list3.remove(4)       #test for "valueError"
del list3[2]
print(list3)
'''

rownum = [  ["Zero"],
            ["First", 1],
            ["Second",2],
            ["Third",3],
            ["Fourth",4],
            ["Fifth",5]]
print(rownum[3],"\n",rownum[3][0])
rownum[3].append("Wednesday")       #adding an element into inner-list ["Third",3]
print(rownum[3][2])
rownum.pop(3)
print(rownum)
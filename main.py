# ans = input("Ivan, r u gay?")
# if ans == "Yes.": print("No, im just pythonist")
# else: print("Yes.")
# line comment
'''
ans2 = input()
if ans2 =="What" : print("CHlen cherez plecho")
else: print("Aga")
''' # ''' - block comment
#
# ans3 = "To the china Lord"
# if ans3 == "To princess" : print("Here your stupid bitch")
# else:
#     if ans3=="To the china Lord": print("Here ur sexy Cat-wife")
#     else: print("Here ur normis wofe")
#
# if ans3 == "To princess":
#     print('Привет,', ans3, '!', sep='::', end='uebiok\n') #sep - parameter witch swap " " between words
#     # end - parameter witch swap "\n" in the end of printing line
#     print('Привет,'+ans3+ '!', end='bez probelov') # "+" connecting words without space
#     print("\n Привет", "че за ебала ка", "кие нахуй пробелы между словами")
#
# print(0b111) # binnary
# print(0o111) # octo
# print(0x111) # sixteen
#
# queenComplex=2+3j;
# queenComplex+=2
# print(queenComplex)

# text = '''
# У Лукоморья дуб зеленый
# Златая цепь на дубе том
# И кот...'''
# print(text)
#
# print("У Лукоморья дуб зеленый\nЗлатая \"цепь\" на дубе том\n\tИ кот...") # \ backslash add ability of adding leng sign.
# print("My \neibor is \near \try  to keep \"kalm\", \\please")             # this ability may does troubles
# print(r"My \neibor is \near \try  to keep \"kalm\", \\please")            # and this leng sign easy to turn off by using "r" word before the line.
#
# print("\nHi, this is a WRONG per injection: {text}\n")
# print(f"Hi, this is a per injection: {text}") #it's need a "f" word to work
#
# nameOfNature = "Pahom"
# numberOfCosmos = 42
# secretOfLife = "fap before she's come"
# print(f'''\nthis is the greatest secrets of humanity:
# Name of nature is {nameOfNature}
# Answer for all questions is {numberOfCosmos}
# And the greatest secret of life: {secretOfLife}
# ''')
#
# print("\nnameOfNature type is "+nameOfNature,type(nameOfNature),"\nnumberOfCosmos type is ",numberOfCosmos,type(numberOfCosmos),"\nsecretOfLife type is "+secretOfLife,type(secretOfLife))
#
# Ass = input("Check ur ass: ")
# print(Ass+".")

# print(1*2+3-5)
print(3/2)
print(3//2,"\"//\" operator get result without fraction") # // result without fraction
print(2.5%2, " % operator gets fraction truly in float, and rounded in integer")
# print(5**3)
# greatNum = 50
# greatNum += greatNum
# print(greatNum)
# Num_1 = 3.5//3
# Num_1 += 3.5%3
# print(Num_1)
# print(round(Num_1))
# Num_1 -=0.1
# print(round(Num_1)) # "round" is rounding number up if its fraction greater then 0,51 or its equal 0,5 and close to even number
# Num_2 = 1.1254
# print(round(Num_2,2)) # second parameter set the count of numbers after dot for round

# int1 = 3
# print(f"{int1:0b}") #set a system for print numbers

# TrulyBool = True
# FalseBool = "true"
# print(f"TrulyBool -{TrulyBool} is {type(TrulyBool)}")
# print(f"\nTrulyBool -{FalseBool} is {type(FalseBool)}")
# bool1 = False
# bool2 = True
# print("\n",bool1&bool2, sep="")
# print(bool1|bool2)
# print(bool1^bool2)
# bool2 =not bool2
# print(bool2,", it was \"True\"", sep="")
# str1="Tr"
# str2="True"
# print(str1 in str2)

# int1=5
# if int1==5:
#     print("YOS")
#     print("HUOOS") # its stayng in the IF-instructions area
# else:
#     print("puk~")
#
def main():
    trying(7)

def trying (inter): #de func
    def goodBuy(): print("\nDat a good buy") #local func, not allowed outside de main func
    goodBuy()
    if inter==7:
        print("First try")
        print("puk~")
    elif inter==8:
        print("Second try")
        print("puk#2~")
    elif inter==9:
        print("Congrat comrad", )
        print("<3")
    else:
        print("You lose.")

trying(9)
main()

# inter=1
# while inter<=5:
#     print(f"inter is - {inter}")
#     inter+=1
# else:
#     print("You reached the Five\n")
#
# streng = "Bonfire reached.\n"
# count=0
# for w in streng:
#     if count==7:
#         continue
#     print(w," ",sep="", end="")
#     count+=1
# else:
#     print(f"\n{count} words reached.")

def counter (*ct, count=0):
    for n in ct:
      count+=1
    print(count)

per_a = counter
per_a(1,2,3)
per_a(1)
per_a(5,67,12,7,234,7,3)

def do (a,b,operation):     #func as a per in another func
    return operation(a,b)
def sum(a,b):
    return a+b
def mult(a,b):
    return a*b
print()
print(do(5,6,lambda a,b:a*b)) #lambda func as a one-line func without name, which can transfer in another func
print("Hi pidarmot")

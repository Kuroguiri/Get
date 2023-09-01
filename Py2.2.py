

# print(int(float("1.1"))) #str lines can be translate only if type clearly matched
# print()
# print("Unknown person: ", str(550))
#
# def func1 (a,b,operation):
#     print(operation(a,b))
#
# func1(5,6,lambda a,b:a*b)      #blyambda transpher operation is less
#
# a=5
# b=7
# def outer ():
#     a=3
#     global b    #initial of "b" per global in func
#     def inner():
#         print("\n",a, sep="")   #print local per nearest to func
#                                 # global -> outer(that is nearest) -> inner (here we are)
#         b=10                    #prints local per b initials in that func, not global
#         def inner_2():
#             nonlocal b          #change value of "b" per in "inner" func, dont create new per
#             b=12
#         inner_2()
#         print(b)
#     inner()
#     print(a)
#     print(b)
# outer()

# def incr(a): return lambda b:a+b
#
# fn=incr(10)     #there we get "a" per in "incr" func
# print(fn(2))    #there and further we use inner func with "a" per inside
# print(fn(12))
# print(fn(5))
# print(fn(50))

def gloriosity(glorylessFunc):      #initialising of decorator
    def gloryosFunc():
        print("\n___**GlOrYoS**ReDeMpTioN**___")
        glorylessFunc()
        print("___**GlOrYoS**ReDeMpTioN**___")
    return gloryosFunc

@gloriosity     #decorator active
def hyer():     #on dat func
    print("             Hayer")

hyer()

def Nullifyer(greatNum):
    def Nullifer(*args):
        a=0
        b=args[1]
        c=0
        greatNum(a,b,c)
    return Nullifer

@Nullifyer
def massivePrinter(a,b,c):
    print(f'''\nFirst num: {a}
Second num: {b}
Third num: {c}''')

massivePrinter(5,67,1)
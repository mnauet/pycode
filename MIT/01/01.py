import random
""" x =  random.randint(22,222)
print (x)
type(3)
type(3.0)
type("hi")
float(3.0)
hi = "hallo there"
name = "ana"
greet = hi + " " + name
print(greet)
silly = hi + (" " + name)*3
print (silly)

x=1
print(x)
x_str = str(x)
print("my fav num is ", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x= " + x_str)


text = input("enter some text")
print(5*text)

num= int("enter a num")
print(num)

"a" == "a"
"a" != "b"


x = float(input("Enter a num for x: "))
y = float(input("Enter a num for y: "))
if x==y :
    print("x & y are equal")
elif x < y :
    print("x is kliener als y ")
else :
    print("y is smaller")
print(" Thanks")


 # iterate
n = 0
while n < 5 :
    print(n)
    n = n+1
for n in range(5):
    print(n)

mysum = 0
for i in range(0,10,2):
    mysum +=i
    print(i)
print("sum : " + str(mysum))

 # Lecture 3 , string manipulations, guess & check, Approximation, Bisection

 #strings
s = 'abc'
x=len(s)
print (x)
print ("0: " + s[0])
print ("1: " + s[1])
print ("2: " + s[2])
print ("-1: " + s[-1])
print ("-2: " + s[-2])
print ("-3: " + s[-3])
 
#sub string slice[start:stop:step]
s = "abcdefgh"
print(s)
print("s[3:6] - " + s[3:6])
print("s[3:6:2] - " + s[3:6:2])
print("s[::] - " + s[::])
print("s[::-1] - " + s[::-1])
print("s[::-2] - " + s[::-2])
print("s[4:1:-2] - " + s[4:1:-2])
print("s[4:1:-1] - " + s[4:1:-1])
print("s[6:1:-1] - " + s[6:1:-1])
print("s[7:1:-1] - " + s[7:1:-1])
print("s[:1:-1] - " + s[:1:-1])

s="abcdefghu"
for char in s:
    if char== 'i' or char== 'u' :
        print(char + " - there is an i or u"  )
    else:
        print(char +  " - no i or u")


# Guess & Check cube root
cube = -8
for guess in range(abs(cube)+1):
    if guess**3 == abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print("cube root of ", str(cube), "is ", str(guess))


#Approximation solution - cube root
#cube = 27
#cube = 8120601
cube = 10000
epsilon = 0.01
guess=0.0
increment= 0.001
num_guessess=0
while abs(guess**3 - cube) >= epsilon and guess < cube:
    guess += increment
    num_guessess +=1

print('num_guesses =', num_guessess)

if abs(guess**3 - cube) >= epsilon :
    print('failed on cube root of = ', cube)
else:
    print(guess, 'is close to the cube root of ', cube)



# Bisection Search - cube root
cube =27
epsilon = 0.01
num_guessess = 0
low = 0
high = cube
guess = (high + low)/2
while abs(guess**3 - cube) >= epsilon :
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (low+high)/2.0
    num_guessess += 1

print("num of guesses : ", num_guessess)
print(guess, 'is cube root of', cube)




# Lecture 4 Decomposition, Abstraction & Function

def f(x) :
    x = x+1
    print('in f(x):x =',x)
    return x
x=3
z = f(x)

def is_even(i):
    remainder = i%2
    return remainder==0
    
print('all numbers, betwenn 0-20 even or odd')
for i in range(20):
    if is_even(i):
        print(i, 'is even')
    else:
        print(i, 'is odd')


#functions as arguments
def func_a():
    print ('inside func_a')

def func_b(y):
    print ('inside func_b')
    return y

def func_c(z):
    print ('inside func_c')
    return z()

print (func_a())
print (5 + func_b(2))
print (func_c(func_a))


# scope example
# ###############################################
def f(y):
    x= 1
    x +=1
    print(x)

x=5 
f(x) # prints 2
print(x) # prints 5
print('=================')

def g(y):
    print(x)
    print(x+1)
x=5
g(x)    # prints 5&6 , x from global scope
print(x) # prints 5 
print('=================')

def h(y):
    #x +=1
    print(x+1)
x=5
h(x)    # error, x can not be modified inside function
print(x) # prints 5 
print('=================')



def g(x):
    def h():
        x = 'abc'
        print('h: x=',x)
    x= x+1
    print('g: x=',x)
    h()
    return x
x=3
z = g(x)
print ('g return :',z)

# Tuples, List, Aliasing, mutability & Cloning
#  ###########################################
te = ()
t = (2, "mit", 3)
print(t)
print(t[0])
print(len(t))
t=t+(4,5,6)
print(t)
print(len(t))
print(t[1:4])


# Tuples - Immutable 
def quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    return (q,r)

(quot,rem) = quotient_and_remainder(4,5)
print(quot,rem)
t= (quot,rem)
print(t)
r= (rem,quot)
print(r)


# Manipulationg Tuples
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n,max_n,unique_words)

test = ((1,"a"),(2,"b"),(3,"c"),(4,"d"),(5,"e"))
(a,b,c) = get_data(test)
t= (a,b,c)
print(t)


# Lists -  Mutable, changeable - []

# indices & ordering
a_list = []
L = [2,'a',3,4,[1,2]]
print( len(L) )
print ( L[0])
print ( L[2] + 1)
print ( L[3])
print ( L[4])
i=2
print ( L[i-1] )

# Lists mutable
L = [1,2,3]
L[1]=5
print ( L )



# Operations on Lists
L = [2,1,3,6,3,7,0]
print(L)
L.remove(2)
print(L)
L.remove(3) # removes first 3
print (L)
del (L[1])  # removes 6
print(L)
print( L.pop() ) # shows last deleted digit, 0
print(L)
L.insert(0,2)
print(L)
L.insert(0,4)
print(L)

# Convert Lists to string and back
s = "I<3 cs"
print(s)
l=list(s)
print(l)
ss=s.split('<') # splits to two strings 
print(ss)
print(s)
l=list(s)
print(l)
L= ['a','b','c']
print(L)
LL= ''.join(L)
print(LL)
LL='_'.join(L)
print(LL)


# list parameter sort
L=[9,6,0,3]
print(L)
LL=sorted(L)    # not mutate L, unchanged L
print(LL)
print(L)
L.sort()    # mutates L
print(L)
L.reverse()
print(L)


# Alias
a=1
b=a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(warm)
print(hot)

# clone lists, original remains unchanged
cool = ['blue','green','grey']
chill = cool[:]
chill.append('black') # cool remains unchanged
print(cool)
print(chill)


# sorting list
warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cool = ['blue','green','black']
sortedcool = sorted(cool)
print(cool)
print(sortedcool)



# Lecture 6 - Recursions, dictionaires mutable
# Multiplication - iteration
def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

result = mult_iter(2,5)
print(result)


def mult(a , b):
    print('mult - a,b', a, b)
    if b==1 :
        print('if - a,b',a, b)
        return a    
    else:
        print('else - a,b',a, b) 
        aa = a + mult(a,b-1)
        print('else - aa,b',aa, b)   
        return aa

result = mult(2,5)
print(result)

def factorial(n):
    if n==1: 
        return 1
    else:
        # we really create a local scope for recursive call
        return n * factorial(n-1) 
fac = factorial(5)
print(fac)

def printMove(fr,to):
    print('prinMmove - from: ' + str(fr) + ' to: ' + str(to) + '  ===============')
# a-b; a-c;b-c;a-b;c-a;c-b;a-b;
def Towers(n,fr,to,spare,nr):
    print('n:',n, 'fr:',fr, 'to:',to,'spare:',spare, 'callingFunction:',nr)
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to,1)
        Towers(1,fr,to,spare,2)
        Towers(n-1,spare,to,fr,3)
fr = 'A'
to = 'B'
spare = 'C'
Towers(3,fr,to,spare,0)

# Fibonachi 
def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
# 1->1; 2->2; 3->3; 4->5; 5->8; 6->12; 7->21; 8->34;;
print (fib(8))

# Palindrome

def isPalindrome(s):
    def toChars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    
    return isPal(toChars(s))

s1= 'Able was I, ere i saw Elba'
s2= 'Are we not drawn onward, we few, drawn onward to new era? xxx '
print (isPalindrome(s2))

# Dictinaary

my_dict = {}
grades =  {'Ana' : 'B', 'John' : 'A', 'Denise' : 'A', 'Kate' : 'A' }
print(grades)
print(grades['Ana'])
grades['sylves'] = 'C'  # insert
print(grades)
del(grades['sylves'])   # delete
print(grades)  
print( grades.keys())
print( grades.values()) 


she_loves_you = [ 'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'You', 'think', "you've", 'lost', 'your','love',
'Well', 'I', 'saw', 'her', 'yesterday','-yi-yay',
"It's", 'you', "she's", 'thinking', 'of',
'And', 'she', 'told', 'me', 'what', 'to', 'say','-yi-yay',
'She', 'says', 'she', 'loves', 'you',
'And', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'And', 'you', 'know', 'you', 'should', 'be', 'glad',
'She', 'said', 'you', 'hurt', 'her', 'so',
'She', 'almost', 'lost', 'her', 'mind',
'And', 'now', 'she', 'says', 'she', 'knows',
"You're", 'not', 'the', 'hurting', 'kind',
'She', 'says', 'she', 'loves', 'you',
'And', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'And', 'you', 'know', 'you', 'should', 'be', 'glad',
'Oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'She', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'With', 'a', 'love', 'like', 'that',
'You', 'know', 'you', 'should', 'be', 'glad',
'You', 'know', "it's", 'up', 'to', 'you',
'I', 'think', "it's", 'only', 'fair',
'Pride', 'can', 'hurt', 'you', 'too',
'Apologize', 'to', 'her',
'Because', 'she', 'loves', 'you',
'And', 'you']

def lyrics_to_frequenies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] +=1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freq):
    values = freq.values()
    best = max(values)
    words = []
    for k in freq :
        if freq[k]==best:
            words.append(k)
    return (words, best)

def words_often(freq, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freq)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else:
            done= True
    return result

dic1 =  lyrics_to_frequenies(she_loves_you)
print(words_often(dic1,5))

#values = dic1.values()
#keys=dic1.keys()
#print (max(values))
#print(values)
#print(keys)
print(dic1)  

"""

# Fibonacci with a dictionary
def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans= fib_efficient(n-1,d) + fib_efficient(n-2,d)
        d[n]= ans
        return ans
    
d = {1:1,2:2}
print(fib_efficient(700,d))




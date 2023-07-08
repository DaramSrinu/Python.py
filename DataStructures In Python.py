#DATA STRUCTURES IN PYTHON
    #REPL = READ, EXPRESSION, PRINT, LOOP
# week1 Strings
n="srinu"
print(len(n))
#looping string
name="SrinivasaReddy"
for i in name:
    print(i)
print("\n")

print()

name1="Srinivasareddy"
for i in range(0,len(name1)):
    print(name1[i])

name2="Srinivasareddy"
count=0
for i in name2:
    if i =="a":
        count=count+1
print(count)

print()

#string slicing
s="HelloWorld"
print(s[:2])
print(s[2:5])
print(s[-1])
print(s[2:8:2])
print(s[::-1])
print(s[::2])

print()

#string library functions
fruit="banana"
print("a" in fruit)
print("m" in fruit)
if "a" in fruit:
    print("Found It")

s1="HelloWorld"
print(s.isupper())
print(s.islower())
print(s.upper())
print(s.lower())

print()

#Stripping Whitespace
greet="   HelloWorld   "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

print()

#Parsing And Extracting
data='From srinivasareddydaram25@gmail.com wed Oct 27 21'
d1=data.find("d")
print(d1)
d2=data.find("@")
print(d2)
d3=data.find(' ',d1)
print(d3)
d4=data[d1:d2]
print(d4)
d5=data[d3+1:d2]
print(d5)

print()

#Assignment
str="Perfect-Plan-b:0.7541"
n=str.find(":")
n1=str[n+1:]
float=float(n1)
print(float)

#week2  Files

#Opening Files:open(),(-> r=Read,a=Append,w=Write,x=Create)
x=open("Main.py","r")
for i in x:
    print(i)

#Counting  lines of files

y=open("Main.py","r")
count=0
for i in y:
    count=count+1
print("The Count of code is:",count)

#Read Whole File
#we can read thewhole file(newlines and all) into asingle string

x=open("Main.py")
input=x.read()
print(len(input))
print(input[:50])
for i in x:
    print(i)

#Searching Through a File
x=open("Main.py")
for i in x:
    i=i.rstrip()
    if(i.startswith("print")):
        print(i)

#Using Continue for Skipping
x=open("Main.py")
for i in x:
    i=i.rstrip()
    if(not i.startswith("Hello")):
        continue
    print(i)

#The below code execute by gap thus why we using rstrip in up code
#x=open("Main.py")
#for i in x:
#       print(i)

#Taking File Name From User
x=input("Enter the file name")
y=open(x)
count=0
for i in x:
    if(i.startswith("Hello")):
        count=count+1
print("There Were",count,"print lines in",x)

#Bad File Names
x=input("Enter the file name")
try:
    y=open(x)
except:
    print("File Cannot be Opened:",x)
    quit()
count=0
for i in x:
    if(i.startswith("Hello")):
        count=count+1
print("There Were",count,"print lines in",x)

#File Assignment
x=open("Main.py")
for i in x:
    y=i.rstrip()
    print(y.upper())

#Week 3 Lists
#Mutable,ordered
list=["Banana","Graphes","Mango"]
list[0]="Apple"
print(list)

#LENGTH RANGE(len() function)
x="PerfectPlanB"
print(len(x))
y=[1,2,3,4]
print(len(y))
print(len(range(5)))

students=['Srinu','vasu','vamsi']
for i in students:
    print("Hello ",i)
print()

#Secound way
for i in range(len(students)):
    print("Hello",students[i])

#Lists Continued

#List Slicing:similar to strings
t=[9,23,2,5,78,90,76]
print(t[1:3])
print(t[:3])
print(t[::-1])

#Buliding a list
x=list()
x.append("Srinu")
x.append("22")
print(x)
if "22"  in x:
    print("Yes")


#Using "IN for Searching
score=[1,2,3,4,5]
print(1 in score)
print(23 in score)

#Lists  are in order
l=["Srinu","Mahi","Chinna"]
l.sort()
print(l)
print(l[2])

#Sum Average Using Lists
total=0                          #numlist=list()
count=0
while True:
    inp=input("Enter a number")
    if inp =="done":break
    value=float(inp)
    total=total+value            #numlist.append(value)
    count=count+1             #average=sum(numlist)/len(sumlist)
average=total/count
print("Average",average)

#Split Function

#split() function:String to list
str="With three friends"
x=str.split()
print(x)
print(len(x))
for i in x:
    print(i)

string = "With;three;friends"
y=string.split()
print(y)
print(len(y))

string1="With;three;friends"
z=string1.split(";")
print(z)
print(len(z))

#Double Split Pattern
line="My name is srinivasa@reddy and I am from Ongole"
words=line.split()
email=words[3]
print(email)

pieces=email.split("@")
print(pieces)
print(pieces[1])

x=list(range(3))
print(x)

#Lists Assignment
x=open("file.txt")

for line in x:
    line=line.rstrip()
    y=line.split()
    if len(y)<3 or y[0]!="From":
        continue
    print(y[2])

#week 4 Dictionaries (key:values)

purse=dict()
purse['money']=12
purse['candy']=3
purse['tissues']=75
print(purse)
print(purse['candy'])
purse['candy']=purse['candy']+5
print(purse)

#Get Function Count Example
counts=dict()
names=['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

#Counting Example:Taking Input from user

counts=dict()
lines=input("Enter line of text")
words=lines.split()
print("Words:",words)

print("counting")
for word in words:
    counts[word]=counts.get(name,0)+1
print(counts)

#Loops and Dictionaries
counts={"chuck":1,"fred":42,"jan":100}
for t in counts:
    print(t,counts[t])

print(list(counts))
print(counts.keys())
print(counts.values())
print(counts.items())

for n,N in counts.items():
    print((n,N))

ppb=dict()
print(ppb.get('can',-1))

#Dictionaries Assignment
x=input("Enter File")
if len(x)<1:x="file.txt"
hand=open(x)

di=dict()
for line in hand:
    line=line.rstrip()
    words=line.split()
    for w in words:
        di[w]=di.get(w,0)+1

largest=-1
word=None
for k,v in di.items():
    print(k,v)
    if v>largest:
        largest=v
        word=k

print("Done",word,largest)

#week 5 Tuples
#Tuples are like Lists
#Tuples are Not Mutable
x=(1,2,3)
print(x)
print(max(x))

#Tuples and Dictionaries
x,y=(2,3)
print(x)

d=dict()
d['srinu']=2
d['vasu']=4
for (k,v) in d.items():
    print(k,v)

tups=d.items()
print(tups)

#Tuples are comparable
print((1,2,3)<(4,5,6))

#sorting Tuples
d={'a':10,'b':1,'c':22}
print(d.items())
print(sorted(d.items()))
for (k,v) in sorted(d.items()):
    print(k,v)
#
temp=list()
for k,v in d.items():
    temp.append((v,k))
print(temp)

temp=sorted(temp,reverse=True)

#shorter version
print(sorted([(v,k) for k,v in d.items()]))

#Tuple Assignment
name=input("Enter the file")
if len(name)<1:name='file.nxt'
hand =open(name)

d=dict()
for lin in hand:
    lin=lin.strip()
    words=lin.strip()
    for w in words:
        d[w]=d.get(w,0)+1

temp=list()
for k,v in d.items():
    newtxt=(v,k)
    temp.append(newtxt)

tmp=sorted(temp,reverse=True)
for v,k in temp[:5]:
    print(k,v)

#Week 6 Sets
#mutable,unorderd,not allowed duplicates
set={'python','machine learning','data structure'}
print(set)

#Empty set or Dictionary
#my_set= set()
#print(type(my_set))

#Sets Adding Updating
set_courses={'python','DS','ML'}
print(set_courses)
set_courses.add('Oops')
set_courses.update('c1','c2','c3')
print(set_courses)

#Removing Deleting Elements Of Sets
set_courses.discard('python')
print(set_courses)
x=set_courses.pop()
print(x)
set_courses.clear()
print(set_courses)
#del set_courses

#Sets Operations
A={1,2,3}
B={3,4,5}
x=A.union(B)
print(x)
y=A.intersection(B) #&
print(y)
z=A.difference(B)
print(z)
a={'a','b','c'}
b={1,2,4,5}
X=a.symmetric_difference(b)
print(X)

#Sets Functions
set_example={'python','DS','ML'}
print('python' in set_example)
print('python' not in set_example)

x='perfect plan B'
for letter in x:
    print(letter)
print(len(x))

#Python Frozensets
#Tuples=immutable sets
#Frozen sets=Immutable sets

m=frozenset([1,2,3,4])
print(m)

#Sets Assignment
l1=[1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,1,5,6,2]
set1,set2=set(),set()
for room in l1:
    if room not in set1:
        set1.add(room)
    else:
        set2.add(room)
        set1.difference_update(set2)
    print(set1.pop())
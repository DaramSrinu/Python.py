#1.Write a program to print sum of numbers from 1 to n
def sumofnumbers():
    n=int(input("Enter the Number:"))
    sum=0
    for i in range(1,n):
        sum=sum+i
    print("Total sum from 1 to {} is {}".format(n,sum))
sumofnumbers()

#2.Write a program to reverse a string
n=input("Enter the Name:")
 #print(n[::-1]) Direct Method
reverse= ""
for i in n:
     reverse = i + reverse
print('Entered value is {} is {}'.format(n,reverse))

#3.Write a program to check whether a string is palindrome or not ? # Reverse the string and compare
n=input("Enter a String:")
print("Original String:",n)
reversedValue = n[::-1]
print('Reversed string:',reversedValue)

if(n==reversedValue):
    print('It is palindrome ')
else:
    print('It is not a palindrome')

#4.write a program to find factorial of a number
n=int(input("Enter a number:"))

if(n<0):
    print('invalid number')
elif (n==0):
    print('factorial of 0 is 1')
else:
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    print('factorial of {} is {}'.format(n,fact))

#5.Write a program to check whether a number is Armstrong ?

n=int(input("Enter a number:"))
toString = str(n)
sum=0
for i in toString:
    #sum=sum + int(i)*int(i)*int(i)
    #sum = sum + pow(int(i),3)
    sum = sum + (int(i)**3)
if(n==sum):
    print('It is armstrong')
else:
    print('It is not armstrong')
#print('digits cube sum',sum)

#Write a program to check whether a number is Armstrong ?

n=int(input("Enter a number:"))
Originalvalue = n
cube = 0
while (n>0):
    num = n%10
    cube = cube + pow(num,3)
    n = n//10
    print(n)
print(cube)

if(Originalvalue==cube):
    print("It is armstrong")
else:
    print("It is not armstring")

#6.Write a program to print prime numbers from 1 to 100 ?
        # A number that is divisible only by itself and 1
n=100
primeNumbers = []
for i in range(2,101):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        primeNumbers.append(i)
print('Number of prime numbers from 1 to 100 is ',len(primeNumbers),primeNumbers)
'''for i in range(1,10):
       print(i)
       if(i==5):
            break
   else:
       print('Else Statement')     '''

#7.Write a program to swap two numbers without using temporary(third) variable ?
n=int(input('Enter the number:'))
m=int(input('Enter the number:'))
'''temp=n
   n=m
   m=temp'''
#n,m=m,n
n=n+m
m=n-m
n=n-m
print("n ={}, m ={}".format(n,m))

#8.Write a program to reverse a number
n =int(input('Enter a number:'))
originalvalue = n
reverse = 0
while(n>0):
    num = n%10
    reverse = reverse*10 +num
    n = n//10
print('Reverse of number {} is {}'.format(originalvalue,reverse))

#9.Write a program to determine the factors of a number
n=int(input("Enter the number:"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)

#10.Write a program to get the matching characters in a string
name = 'srinivasareddy'
print(name.count('0'))
matchingCharacters = set()
for i in name:
    if (name.count(i) > 1):
        matchingCharacters.add(i)
print(matchingCharacters)

#11.Write a program to print Fibonacci sequence
n=int(input("Enter n value:"))
n1=0
n2=1
count = 0
if(n<=0):
    print('Enter a vaild number')
elif(n==1):
    print('Fibonacci series of 1 is 0')
else:
    while(count<n):
        print(n1)
        nextElement = n1+n2
        n1 = n2
        n2 = nextElement
        count = count +1

#12. Calculate the number of vowels and consonants in a string
n=input("Enter a name:")
vowelsList=['a','e','i','o','u']
vowelsCount = 0
consonantCount = 0

for i in n:
    if(i in vowelsList):
        vowelsCount = vowelsCount + 1
    else:
        consonantCount = consonantCount + 1
print('Number of vowels: {},Number of consonants: {}'.format(vowelsCount,consonantCount))

#13.Check if two strings are anagrams ?
n1=input("Enter the n1:")
n2=input("Enter the n2:")

if(len(n1)==len(n2)):
    if(sorted(n1)==sorted(n2)):
        print('These are anagrams')
    else:
        print("These are not anagrams")
else:
    print('These are not anagrams')

#14. Find the count for the occurence of a particular character in a string

name=input('Enter a name')
character = input('Enter a character')
#print(name.count(character))
count = 0
for i in name:
    if(character==i):
        count = count +1
print('count of {} is {}'.format(character,count))

#15. How to calculate the number of numerial digits in a string ?
name=input("Enter a name")
'''for i in name:
    if(i.isdigit()):
        print(i)'''
numbers =['0','1','2','3','4','5','6','7','8','9']
count =0
for i in name:
    if(i in numbers):
        count = count +1
        print(i)

print('number of digits in {] is {]'.format(name,count))

#16. Find the first character of a string that  is not repeated?
n=input("Enter the string:")
'''for i in n:
    if(n.count(i)==1):
        print('First Non Repeated Character is:',i)
        break'''
foundNonRepeated = False
while n!='':
    originalNamelen=len(n)
    char = n[0]
    n = n.replace(char,'')
    afterReplaceLen = len(n)
    if(originalNamelen-1==afterReplaceLen):
        print('First Non Repeated Character is:',char)
        foundNonRepeated = True
        break

if(foundNonRepeated==False):
    print('No Non Repeated Characters Found')

#17.Finding missing number in a list of integers
numbers = [1,2,3,4,6,7,8,9,10]
n = len(numbers)+1

totalSum=n*(n+1)//2
print('total sum is',totalSum)
sum = 0
for i in numbers:
    sum = sum+i
print('missing number is:',totalSum-sum)

#18.Delete the repeated elements in an integer array?
list=[1,2,3,3,4,5,5,6,7,7,8,9,9]
#n=set(list)
#print(n)

newNumbers=[]

for i in list:
    if(i not in newNumbers):
        newNumbers.append(i)

print('After removing duplicates',newNumbers)

#19.Determine the largest and the smallest element of an array which is not sorted
list=[2,34,64,78,99,45,9]
    #print('smallest number:',min(list))
    #print('largest number:',max(list))

  #list.sort()
  #print(list[0],list[-1])

small = list[0]
large = list[0]
length=len(list)
for i in range(1,length):
    if(small>list[i]):
        small=list[i]
    if(large<list[i]):
        large=list[i]

print(small,large)

#20.Determine the second largest element of an array?
list=[23,54,76,28,16,5]
  #list.sort()
  #print(list[-2],list)

firstMax = max(list[0],list[1])
secondMax = min(list[0],list[1])
length = len(list)
for i in range(2,length):
    if(list[i]>firstMax):
        secondMax=firstMax
        firstMax = list[i]
    elif(list[i]>secondMax):
        secondMax = list[i]

print('second largest number is',secondMax)
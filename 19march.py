#1 program to check prime number
 
n=int(input("Enter a number"))
c=0
for i in range(1,n,1) :
    if n%i==0
       c=c+1

if c>2 :
   print("Not prime")
else :
   print("Prime")

#2 Program to check entered year is leap year or not

n=int(input("Enter a year"))
 if n%4==0:
    print("Leap year")
 else :
    print("Not a leap year")


#3 Program to find out the factorial of any number

n=int(input("Enter a number"))
for i in range(1,n+1,1) :
 if n%i==0:
   print(i)

#4 Program to check armstrong no.

n=int(input("Enter a number"))
sum=0
temp=n

while temp>0 :
  digit=temp%10
  sum+=digit**3
  temp//=10
if n==sum:
  print("Armstrong number")
else:
  print("Not an armstrong number")

#5 Program to find number vowels ,consonents,digits and special character present in given string

s=input("ENTER A STRING")
vowels =0
consonents =0
digits =0
spe =0

for i in range (0,len(s)):
 ch=s[i]
 if ch>='a' and ch<='z' :
     if ch>='A' and ch<='Z':
         ch = ch.lower() 
  
         if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
                            vowels += 1
         else :
                consonents+=1
 if ch>='0' and ch<='9' :
                digits+=1
 else:
                spe+=1
print("vowels =",vowels) 
print("consonents =",consonents) 
print("digits =",digits)
print("special characters =",spe) 




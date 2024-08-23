


'''
#1
s=input('enter string')
print(len(s))
#1.1
s=input('enter string')
c=0
for i in s:
    c+=1
print(c)

#1
1.Take a string from user as kavitha.
2.use len function to print the how many elements are present in given string.
#1.1
1.Take a string from user as kavi.
2.create a variable with 0 as values because we are assuming that given string might be empty.
3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
Iteration1:extract k and add 1 to c so c becomes 1.
Iteration1:extract a and add 1 to c so c becomes 2.
Iteration1:extract v and add 1 to c so c becomes 3.
Iteration1:extract i and add 1 to c so c becomes 4.
5.At last If there is no element left to iterate it will returns and moved to print(variable).
to print the how many elements are present in given string(count of elements).
NOTE:IF PRINT IS GIVEN IN THE ITERATION IT WILL GIVE OUTPUT AS LIST OF ELEMENTS PRESENT IN STRING LIKE 1,2,3...
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#2
s=input('enter a string')
sub=input('enter a string')
print(s.count(sub)) 
#2.2
s=input('enter string')
sub=input('enter string')
c=0
for i in s:
        if i==sub:
            c+=1
print(c)
#2
1.Take a string from user as kavitha.
2.Take another for substring from user as a.
3.use count function to print the how many times given substring is present in string.

#2.2
#2
1.Take a string from user as kavitha.
2.Take another for substring from user as a.
3.use count function to print the how many times given substring is present in string.

#2.2
1.Take a string from user as kavita.
2.Take another for substring from user as a.
3.create a variable with 0 as values because we are assuming that given string might not be present in given string.
4.To extract each and every element from given string we need to perform iteretion.
5.Iterations:
Iteration1:extract k and check if given element is equals to substring or not if it is false then c remains 0 and moved to next element.
Iteration2:extract a and check the given element is equals to substring or not if it is true then c becomes 1 by counting 0+1=1.
Iteration3:extract v and check if given element is equals to substring or not if it is false then c remains 1 and moved to next element.
Iteration4:extract i and check if given element is equals to substring or not if it is false then c remains 1 and moved to next element.
Iteration5:extract t and check if given element is equals to substring or not if it is false then c remains 1 and moved to next element.
Iteration6:extract a and check if given element is equals to substring or not if it is false then c becomes 1 by counting 1+1=2.
6.At last If there is no element left to iterate it will returns and moved to print(variable).
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
#3 vowels
s=input('enter string')
vowels='aeiouAEIOU'
c=0
for i in s:
    if i in vowels:
        c+=1
print(c)

1.Take a string from user as Kavi.
2.Take another for vowels from user. 
3.create a variable with 0 as values because we are assuming that given string might not be present in given string.
4.To extract each and every element from given string we need to perform iteretion.
5.Iterations:
Iteration1:extract K and check if given element is present in given collection or not if it is false c remains 0 and moved to next element.
Iteration2:extract a and check if given element is equals to substring or not if it is true then c becomes 1 by counting 0+1=1.
Iteration3:extract v and check if given element is equals to substring or not if it is false then c remains 1 and moved to next element.
Iteration4:extract i and check if given element is equals to substring or not if it is true then c becomes 1 by counting 1+1=2.
6.At last If there is no element left to iterate it will returns and moved to print(variable).
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#4 consonants
s=input('enter string')
vowels='aeiouAEIOU'
c=0
for i in s:
    if i.isalpha() and i not in vowels:
        c+=1
print(c)

1.Take a string from user as aeik.
2.Take another for vowels from user. 
3.create a variable with 0 as values because we are assuming that given string might not be present in given string.
4.To extract each and every element from given string we need to perform iteretion.
5.Iterations:
Iteration1:extract a and check if given element is alpha or not and whether it is not present in given collection or not if it is false c remains 0 and moved to next element.
Iteration2:extract e and check if given element is alpha or not and whether it is not present in given collection or not if it is true then c becomes 1 by counting 0+1=1.
Iteration3:extract i and check if given element is alpha or not and whether it is not present in given collection or not if it is false then c remains 1 and moved to next element.
Iteration4:extract k and check if given element is alpha or not and whether it is true then c becomes 1 by counting 1+1=2.
6.At last If there is no element left to iterate it will moved to print(variable).
==========================================================================================================================================================================================
#5 vowels and consonants
s=input('enter element')
vowels='aeiouAEIOU'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in vowels:
           vc+=1
        else:
           cc+=1
print(vc)
print(cc)

1.Take a string from user as kavita.
2.Take another for vowels from user. 
3.create a variable with 0 as values because we are assuming that given string might not be present in given string.
4.To extract each and every element from given string we need to perform iteretion.
5.Iterations:   
Iteration1:extract k and check if given element is alpha or not and whether it is present in given collection or not if it is false it moves to else cc becomes 0+1=1.
Iteration2:extract a and check if given element is alpha or not and whether it is present in given collection or not if it is true then vc becomes 1 by counting 0+1=1.
Iteration3:extract v and check if given element is alpha or not and whether it is present in given collection or not if it is false it moves to else cc becomes 1+1=2.
Iteration4:extract i and check if given element is alpha or not and whether it is present in given collection or not if it is true then vc becomes 1 by counting 1+1=2.
6.At last If there is no element left to iterate it will moved to print(vc) and print(cc).

-------------------------------------------------------------------------------------------------------------------------------------------------------------
#6
s=input('enter string')
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)
        
1.Take a string from user as k143.
2.create a variable with 0 as values because we are assuming that given string might not be present in given string.
3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
Iteration1:extract k and check if it is a digit or not if it is false then c remains 0 and moved to next element.
Iteration2:extract 1 and check if it is a digit or not if it is true then c becomes 0+1=1.
Iteration3:extract 2 and check if it is a digit or not if it is true then c becomes 1+1=2.
Iteration4:extract 3 and check if it is a digit or not if it is true then c becomes 2+1=3.
6.At last If there is no element left to iterate it will moved to print(variable)

.......................................................................................................................................................................
#7
s=input('enter string')
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        c+=k
print(c)

1.Take a string from user as k143.
2.create a variable with 0 as values because we are assuming that given string might not be present in given string.
3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
Iteration1:extract k and check if it is a digit or not and if it is false then c remains 0 and moved to next element.
Iteration2:extract 1 and check if it is a digit or not and type cast that into int and if it is true then c becomes 0+1=1.
Iteration3:extract 2 and check if it is a digit or not and type cast that into int and if it is true then c becomes 1+1=2.
Iteration4:extract 3 and check if it is a digit or not and type cast that into int and if it is true then c becomes 2+1=3.
6.At last If there is no element left to iterate it will moved to print(variable)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#8
s=input('enter string')
c=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            c+=k
print(c)


1.Take a string from user as k143.
2.create a variable with 0 as values because we are assuming that given string might not be present in given string.
3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
Iteration1:extract k and check if it is a  even digit or not and if it is false then c remains 0 and moved to next element.
Iteration2:extract 1 and check if it is a even digit or not and type cast that into int and if it is false then c remains 0.
Iteration3:extract 4 and check if it is a even digit or not and type cast that into int and if it is true then c becomes 0+4=4.
Iteration4:extract 3 and check if it is a even digit or not and type cast that into int and if it is true then c remains 4.
6.At last If there is no element left to iterate it will moved to print(variable)

::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

#9
s=input('enter string')
es=0
os=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            es+=k
        else:
            os+=k
if (es>os):
    print(es-os)
else:
    print(os-es)
    
1.Take a string from user as k143.
2.create a variable1 with 0 as values because we are assuming that given string might not be present in given string.
3.create a variable2 with 0 as values because we are assuming that given string might not be present in given string.
4.To extract each and every element from given string we need to perform iteretion.
5.Iterations:
Iteration1:extract k and check if it is a  even digit or odd and type cast that into int and if it is false then c remains 0.
Iteration2:extract 1 and check if it is a even digit or odd and type cast that into int and if it is false then os will goes to else os becomes 0+1=1.
Iteration3:extract 4 and check if it is a even digit or odd and type cast that into int and if it is true then es becomes 0+4=4.
Iteration4:extract 3 and check if it is a even digit or odd and type cast that into int and if it is false then os becomes 1+3=4.
6.At last If there is no element left to iterate it will moved to if statement and check es>os or not if it is true then it will print es-os or else os-es.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#10
s=input('enter string')
c=0
for i in s:
    if not i.isalnum():
        c+=1
print(c)

1.Take a string from user as ,l,@,.
2.create a variable with 0 as values because we are assuming that  given string might be empty.
3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
iteration1:extract , and check whether it is not a alnum then it returns true and increment the value into 0+1=1.
iteration2:extract l and check whether it is not a alnum then it returns false and moved to next element.
iteration3:extract , and check whether it is not a alnum then it returns true and increment the value into 1+1=2.
iteration4:extract @ and check whether it is not a alnum then it returns true and increment the value into 2+1=3.
iteration5:extract , and check whether it is not a alnum then it returns true and increment the value into 3+1=4.
6.At last If there is no element left to iterate it will moved to print(variable)

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#11
l=eval(input())
summ=0
for i in l:
    summ+=i
print(summ)
    
#11.1 list of collections
l=[100,200,[1,2],'hai',(23,'hai'),34,56]
summ=0
for i in l:
    if isinstance(i,int):
        summ+=i
print(summ)

#11
1.Take a list from user10,20,30.
2.2.create a variable with 0 as values because we are assuming that  given list might be empty.
3.3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
iteration1:extract 10 and add with summ as 0+10=10.
iteration2:extract 20 and add with summ as 10+20=30.
iteration3extract 10 and add with summ as 30+30=60.
5.at last If there is no element left to iterate it will moved to print(variable).

#11.1
1.Take a list from user [10,'hai,30].
2.2.create a variable with 0 as values because we are assuming that  given list might be empty.
3.3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
iteration1:extract 10 and check if it is instance(data,datatype) if it is true add with summ as 0+10=10.
iteration2:extract 'hai' and check if it is instance(data,datatype) if it is false summ remains same and moved to next line.
iteration3extract 30 and check if it is instance(data,datatype) if it is true add with summ as 10+30=40.
5.at last If there is no element left to iterate it will moved to print(variable).

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#12
l=eval(input())
mx=0
for i in l:
    if i>mx:
        mx=i
print(mx)

#12.1
l=eval(input())
l.sort()
print(l[-1])

#12.2
l=eval(input())
print(max(l))

1.Take a list from user [10,20,30].
2.create a variable with 0 as values because we are assuming that  given list might be empty.
3.To extract each and every element from given string we need to perform iteretion.
4.Iterations:
iteration1:extract 10 and check if it is  if it is greater than given variable then mx=i or else it moves to next.
iteration2:extract 'hai' and check if it is greater than given variable then mx=i or else it moves to next.
iteration3extract 30 and check if it is greater than given variable then mx=i or else it moves to next.
5.at last If there is no element left to iterate it will moved to print(variable).

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#13
l=eval(input())
es=0
os=0
for i in l:
    if i%2==0:
        es+=i
    else:
        os+=i
print(es)
print(os)
print(abs(es-os))

1.Take a list from user [10,20,30].
2.create a 2variables with 0 as values because we are assuming that  given list might be empty.
3.To extract each and every element from given list we need to perform iteretion.
4.Iterations:
iteration1:extract 10 and check if it is  if it is even or not if it is even es will incremented with that value or else os.
iteration2:extract 20 and check if it is even or not if it is even es will incremented with that value or else os.
iteration3extract 30 and check if it is even or not if it is even es will incremented with that value or else os.
5.at last If there is no element left to iterate it will moved to print(variable).

{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{

#14
range
n=int(input())
summ=0
for i in range(1,n+1):
    summ+=i
print(summ)


1.Take a input from user int of 3.
2.2.create a variable with 0 as values because we are assuming that given int might be 0.
3.To extract each and every element from given range we need to perform iteretion.
4.Iterations:
iteration1:extract 1 and add that into 0+1=1.
iteration2:extract 2 and add that into 1+2=3.
iteration3:extract 3 and add that into 3+3=6.
5.at last If there is no element left to iterate it will moved to print(variable).

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#15
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

1.Take a input from user int of 3.
2.2.create a variable with 0 as values because we are assuming that given int might be 0.
3.To extract each and every element from given range we need to perform iteretion.
4.Iterations:
iteration1:extract 1 and multipy that into 1*1=1.
iteration2:extract 2 and multipy that into 1*2=2.
iteration3:extract 3 and multipy that into 2*3=6.
5.at last If there is no element left to iterate it will moved to print(variable).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`

#16 perfect num
n=int(input())
ds=0
for i in range(1,n//2+1):
    if n%i==0:
        ds+=i
if n==ds:
    print('n is perfect num')
else:
    print('n is  not perfect num')

1.Take a input from user int of 6.
2.2.create a variable with 0 as values because we are assuming that given int might be 0.
3.To extract each and every element from given range we need to perform iteretion.
4.Iterations:
iteration1:extract 1 and check if the n value is divided and equals to 0 then ds+=i or else moved to next line.
iteration2:extract 2 and check if the n value is divided and equals to 0 then ds+=i or else moved to next line.
iteration3:extract 3 and check if the n value is divided and equals to 0 then ds+=i or else moved to next line.
5.it checks whether the given number is equal to ds or not if it is true then print('n is perfect num')or else print('n is not perfect num').
6.at last If there is no element left to iterate it will moved to print(variable).

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#17
#even numbers
m=int(input())
n=int(input())
for i in range(m,n+1):
    if i%2==0:
        print(i)

1.Take a input1 from  user.
2.Take a input2 from  user.
3.To extract each and every element from given range we need to perform iteretion.
4.Iterations:
iteration:extract elements according to the range and check if it is equal to 2 or not if it is true print even number
or else moved to print(variable) directly.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#18
m=int(input())
n=int(input())
l=[]
for i in range(m,n+1):
    if i%2==0:
        l.append(i)
        print(l[::2])


1.Take a input1 from  user.
2.Take a input2 from  user.
3.create a empty list to fetch the even numbers into it.
4.To extract each and every element from given range we need to perform iteretion.
5.Iterations:
iteration:extract elements according to the range and check if it is equal to 2 or not if it is true append the even numbers into the empty list
or else moved to print(variable) directly.

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#19
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if i%2==0:
       c+=1
       if c%2==0:
           print(c,i)

1.Take a input1 from  user.
2.Take a input2 from  user.
3.create a variable with 0 as we assuming that given input are might be zero.
4.To extract each and every element from given range we need to perform iteretion.
5.Iterations:
iteration:extract elements according to the range and check if it is equal to 2 or not if it is true then c become 0+1=1
or else moved to next element to iterate and check whether the count is divided by 2 or not if it is true moved to next line.
5.print the variables.

......................................................................................
#20
s=input()
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] in v:
        print(ip)
1.take a input string.
2.take a variable with vowels.
3.To perform iterations based on range and collection to find the index positions we use for
loop with range and collection.
iterations:
It extract each and every element based on the len(s) and check the below condition is true or not
if its true it prints the index position of the vowels.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#21
s=input()
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip].isalpha:
       if s[ip] not in v:
           print(ip,s[ip])
1.take a input string.
2.take a variable with vowels.
3.To perform iterations based on range and collection to find the index positions we use for
loop with range and collection.
iterations:
It extract each and every element based on the len(s) and check the below condition is true or not
if its true it will check another condition whether it is alpha or not.
4.if above condition is true it returns and print the output.
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#22
s=input()
summ=0
for i in s:
    if i.isdigit():
        summ+=int(i)
print(summ)
1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and check the below condition is not true it go back to the loop.
2.It extract 2nd element and check the below condition is true then it incements summ+=1.
3.It extract 3rd element and check the below condition is not true it go back to the loop.
4.It extract 4th element and check the below condition is true then it incements summ+=2.
5.it prints the output of summ value.

#23
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        summ+=ip
print(summ)

1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and check the below condition is not true it go back to the loop.
2.It extract 2nd element and check the below condition is true then it incements summ+=ip.
3.It extract 3rd element and check the below condition is not true it go back to the loop.
4.It extract 4th element and check the below condition is true then it incements summ+=ip.
5.it prints the output of summ value.


#24
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip])%2==0:
            if ip%2!=0:
                summ+=int(s[ip])
print(summ)

1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and if it is a digit check the below condition is not true it go back to the loop.
2.It extract 2nd element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
3.It extract 3rd element and if it is a digit check the below condition is not true it go back to the loop.
4.It extract 4th element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
5.it prints the output of summ value.

#25
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip])%2==0:
            if ip%2==0:
                summ+=ip
print(summ)

1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and if it is a digit check the below condition is not true it go back to the loop.
2.It extract 2nd element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
3.It extract 3rd element and if it is a digit check the below condition is not true it go back to the loop.
4.It extract 4th element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
5.it prints the output of summ value.


#26
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip])%2!=0:
            if ip%2==0:
                summ+=ip
print(summ)

1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and if it is a digit check the below condition is not true it go back to the loop.
2.It extract 2nd element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
3.It extract 3rd element and if it is a digit check the below condition is not true it go back to the loop.
4.It extract 4th element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
5.it prints the output of summ value.

#27
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip])%2==0:
            if ip%2==0:
                summ+=ip
print(summ)

1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and if it is a digit check the below condition is not true it go back to the loop.
2.It extract 2nd element and if it is a digit check the below condition is true then it incements summ+=ip.
3.It extract 3rd element and if it is a digit check the below condition is not true it go back to the loop.
4.It extract 4th element and if it is a digit check the below condition is true then it incements summ+=ip.
5.it prints the output of summ value.

#28
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip])%2!=0:
            if ip%2==0:
                summ+=int(s[ip])
print(summ)

1.take a input string.#k1v1
2.take a variable with 0 as assuming that given value might not be consists of digits.
3.To perform iterations based on collection we use for loop with collection.
iterations:
1.It extract 1st element and if it is a digit check the below condition is not true it go back to the loop.
2.It extract 2nd element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
3.It extract 3rd element and if it is a digit check the below condition is not true it go back to the loop.
4.It extract 4th element and if it is a digit check the below condition is true then it incements summ+=int(s[ip]).
5.it prints the output of summ value.


#29
s=input()
sub=input()
c=0
for ip in range(len(s)):#here we are using this bcoz the given substring consists of multiple elements.
    if s[ip:ip+len(s):]==sub:
        c+=1
print(c)

1.take a input string.
2.take a substring.
3.take a variable with 0 as assuming that given value might not be consists in given string.
4.As we are dealing with multiple elements based on the ip we need to use for loop with range and collection.
5.iteration:
1.it extract 1st element and check the condition based on slicing is equal to sub if it is true it add the count+=1.
2.it extract 2nd element and check the condition based on slicing is equal to sub if it is false it returns to for loop.
3.it extract 3rd element and check the condition based on slicing is equal to sub if it is true it add the count+=2
4.it extract 4th element and check the condition based on slicing is equal to sub if it is true it add the count+=3
5.it prints the count.


#30
s=input()
sub=input()
c=0
for ip in range(len(s)):#here we are using this bcoz the given substring consists of multiple elements.
    if s[ip:ip+len(s):]==sub:
        c+=ip
print(c)

1.take a input string.
2.take a substring.
3.take a variable with 0 as assuming that given value might not be consists in given string.
4.As we are dealing with multiple elements based on the ip we need to use for loop with range and collection.
5.iteration:
1.it extract 1st element and check the condition based on slicing is equal to sub if it is true it add the count+=ip.
2.it extract 2nd element and check the condition based on slicing is equal to sub if it is false it returns to for loop.
3.it extract 3rd element and check the condition based on slicing is equal to sub if it is true it add the count+=ip
4.it extract 4th element and check the condition based on slicing is equal to sub if it is true it add the count+=ip
5.it prints the count.


#31
l=[10,20,34]
l1=[]
for ip in range(len(l)):
    if l[ip]%2==0:
        l1.append('even')
    else:
        l2.append('odd')
print(l1)

l=[10,20,34]
for ip in range(len(l)):
    if l[ip]%2==0:
        l[ip]='even'
    else:
        l[ip]='odd'
print(l)

1.take a input from user.
2.take an empty list.
3.as we are dealing with ip we need to use for loop with range and collection.
iteration:
1.it extract 1st value and check the condition is true it append the even.
2.it extract 2nd value and check the condition is true it append the even.
3.it extract 3rd value and check the condition is true it append the even.
4.it prints the output l1.


#32
n=int(input())
i=0
while i<=n:
    print(i)
    i+=1
1.take a input number.
2.take a variable to initiliaze the 0 to it.
3.take a while to iterate the number.
4.print the i value from 1 to <=n.
5.here we need to give the increment or decrement otherwise it will iterate infinite times.


#33
n=int(input())
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)

1.1.take a input number.
2.take a factorial number.
3.take a variable to initiliaze the 0 to it.
3.take a while to iterate the number.
4.the values will be multiplied with factorial value.
5.here we need to give the increment or decrement otherwise it will iterate infinite times.
6.print the multiplied values of factorial.


#34
n=int(input())
ds=0
i=1
while i<=n//2:
    if n%i==0:
        ds+=i
    i+=1
if n==ds:
    print('perfect')
else:
    print('not perfect')


1.Take a input from user int of 6.
2.create a variable with 0 as values because we are assuming that given int might be 0.
3.To extract each and every element from while we need to perform iteretion.
4.Iterations:
iteration1:extract 1 and check if the n value is divided and equals to 0 then ds+=i or else moved to next line.
iteration2:extract 2 and check if the n value is divided and equals to 0 then ds+=i or else moved to next line.
iteration3:extract 3 and check if the n value is divided and equals to 0 then ds+=i or else moved to next line.
5.it checks whether the given number is equal to ds or not if it is true then print('n is perfect num')or else print('n is not perfect num').
6.here we need to give the increment or decrement otherwise it will iterate infinite times.
7.at last If there is no element left to iterate it will moved to print(variable).


#35
l=[11,22,33,44,55,66]
for ip in range(0,len(l),2):
    l[ip],l[ip+1]=l[ip+1],l[ip]
print(l)

1.take a list from user.
2.here we need to perform for loop wit range and collection because we are dealing with range and collection.
3.it will swap the values based on the given swaped variables.
4.print the l.

#36
s=input()
ch=' '
for i in s:
    ch=i+ch
print(ch)    

1.take a input string.
2.take an empty string.
3.to extract elements use for loop with cdt.
iterations:
it extract elements and add those as per the given condition.
4.print the output


s=input()
s1=' '
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip] in v:
        s1+=str(ip)
    else:
        s1+=s[ip]
print(s)


#37
n=int(input)
dummy=n
summ=0
while dummy>0:
     rem=dummy%10
     dummy=dummy//10
     sum+=rem
print(summ)

1.taking a input int.
2.taking a variable as dummy store actual number.
3.creating a variable with 0 as value because we are assuming that given number might be 0:
4.taking a while loop to iterate the given number until the d values is > 0 once its getting the while condition false.
5.to extract the last element of the given number we need to perform modulus operation and store that element into variable called rem.
6.to reduce the given number we need to use floor division and storing that element into the dummy variable.
7.adding the rem with summ and storing that into the summ variable.
8.printing the output of summ outside of the loop.

#38
n=int(input)
dummy=n
rev=0
while dummy>0:
     rem=dummy%10
     dummy=dummy//10
     rev=rem*10+rem
print(rev)


1.taking a input int.
2.taking a variable as dummy store actual number.
3.creating a variable with 0 as value because we are assuming that given number might be 0:
4.taking a while loop to iterate the given number until the d values is > 0 once its getting the while condition false.
5.to extract the last element of the given number we need to perform modulus operation and store that element into variable called rem.
6.to reduce the given number we need to use floor division and storing that element into the dummy variable.
7.storing the rem*10+rem into the rev variable.
8.printing the output of rev outside of the loop.


#39
n=int(input)
dummy=n
rev=0
while dummy>0:
     rem=dummy%10
     dummy=dummy//10
     rev=rem*10+rem
if rev==n:
print('n is palindrome')
else:
print('n is not a palindrome')

1.taking a input int.
2.taking a variable as dummy store actual number.
3.creating a variable with 0 as value because we are assuming that given number might be 0:
4.taking a while loop to iterate the given number until the d values is > 0 once its getting the while condition false.
5.to extract the last element of the given number we need to perform modulus operation and store that element into variable called rem.
6.to reduce the given number we need to use floor division and storing that element into the dummy variable.
7.storing the rem*10+rem into the rev variable.
8.checking the condition if the rev value is equal to the n value.
9.if it is true it prints n is palindrome.
10.if it is false it prints n is palindrome.
11.printing the output of rev outside of the loop.



#40
n=int(input())
summ=0
d=n
l=len(str(d))
while d>0:
     rem=d%10
     d=d//10
     summ+=rem**l
if n==sum:
     print('armstrong')
else:
     print('not a armstrong')


1.taking a input int.
2.taking a variable as dummy store actual number.
3.creating a variable with 0 as value because we are assuming that given number might be 0.
3.1.taking a l variable to store length of the given variable.
4.taking a while loop to iterate the given number until the given number until the d values is > 0 once its getting the while condition false.
5.to extract the last element of the given number we need to perform modulus operation and store that element into variable called rem.
6.to reduce the given number we need to use floor division and storing that element into the dummy variable.
7.addding the rem with summ**lstoring that element into the summ variable.
8.this process will repeated until the d values is > 0 once its getting the while condition false.
9.8.check the condition is true or not if it is true it print('armstrong') or else print('not a armstrong').

#41
n=int(input())
d=n
rev=' '
while d>0:
     rem=d%10
     d//=10
     rev+=str(rem)
print(rev)

#41.1

n=int(input())
d=n
summ=0
l=len(str(d))
while d>0:
     rem=d%10
     d//=10
     summ+=rem**l
     l-=1
if n==sum:
     print('disorium')
else:
     print('not a disorium')



1.taking a input int.
2.taking a variable as dummy store actual number.
3.creating a variable with empty string to store the string of elements init.
3.1.taking a l variable to store length of the given variable.
4.taking a while loop to iterate the given number until the given number until the d values is > 0 once its getting the while condition false.
5.to extract the last element of the given number we need to perform modulus operation and store that element into variable called rem.
6.to reduce the given number we need to use floor division and storing that element into the dummy variable.
7.addding the rem with summ**l storing that element into the summ variable.
7.1.subtracting the len of value with 1 to raised to power of the positions.
8.this process will repeated until the d values is > 0 once its getting the while condition false.
9.8.check the condition is true or not if it is true it print('disorium') or else print('not a disorium').

#42
n=int(input())
d=n
summ=0
l=len(str(d))
while d>0:
     rem=d%10
     d//=10
     summ+=rem
if n%summ==0:
     print('harshad')
else:
     print('not a harshad')

1.taking a input int.
2.taking a variable as dummy store actual number.
3.creating a variable with empty string to store the string of elements init.
3.1.taking a l variable to store length of the given variable.
4.taking a while loop to iterate the given number until the given number until the d values is > 0 once its getting the while condition false.
5.to extract the last element of the given number we need to perform modulus operation and store that element into variable called rem.
6.to reduce the given number we need to use floor division and storing that element into the dummy variable.
7.7.adding the rem with summ and storing that into the summ variable.
8.check the condition is true or not if it is true it print('harshad') or else print('not a harshad').

#43
#prime or not
n=int(input())
if n>1:
    for i in range(1,n//2+1):
        if n%i==0:
           print('n is a not prime')
           break
    else:
        print('n is a prime')
else:
    print('n is a not a prime')

1.take the input as int.
2.if the number is lesser than equal to 1 that would not be a prime so we directly  give if condition if the given
number is lesser than the 1.if it is true then it will move to the for loop.
3.we create for loop with range to iterate the loop for execition.
iterations:
1.extact each value and check the condition if it is true then it will move to if block and print the output then break the execution.
2.if the condition is not true then it will move the else block and print the output.
4.if the value is not entered into the loop it will move to the ifelse block and print the output.


#44
#fibbinoocci series
a=int(input())
b=int(input())
n=int(input())
if n==1:
      print(a)
elif n==2:
    print(a,b)
else:
    print(a,b,end=' ')
    for i in range(n-2):
        c=a+b
        print(c,end=' ')
        a,b=b,c
    

#45
m=int(input())
n=int(input())
for i in range(m,n+1):
    d=i
    l=len(str(i))
    summ=0
    while d>0:
        rem=d%10
        d//=10
        summ+=rem**l
    if summ==n:
     print(n)

#46
#pattern approches
n=int(input())
stars=1
spaces=0
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces+=1
exe:
1.taking input from user.
2.taking a variable with 1 as star starting from single star.
3.taking a variable with 0.
4.

#47
n=int(input())
stars=1
spaces=n-1
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1


#48
n=int(input())
stars=n
spaces=0
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1
    spaces+=1

#49
n=int(input())
stars=1
spaces=n-1
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    spaces-=1
    stars+=1

#50
n=int(input())
stars=1
for i in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=1


#51
n=int(input())
stars=n
for i in range(1,n+1):
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=1


#52
n=int(input())
stars=1
spaces=n-1
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars+=2
    spaces-=1
    

'''
#53
n=int(input())
stars=n*2-1
spaces=0
for i in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print('*',end=' ')
    print()
    stars-=2
    spaces+=1



)


s='hello123hhfd67uhjb88hbj9'
summ=0
n=''
l=[]
for i in s:
    if i.isdigit():
        n+=i
    else:
        if n:
            l.append(n)
            n=''
if n:
    l.append(n)
for j in l:
    if int(j)%2!=0:
        summ+=int(j)
print(summ)
    
l = [1,2,8,2,0,1]
new = []
for i in range(len(l)):
    suml = 0
    sumr = 0
    if i > 0:
        for le in range(i-1,-1,-1):
            suml += l[le]
    for re in range(i+1,len(l)):
        sumr += l[re]
    if suml == sumr:
        new.append(l[i])
if new:
    for i in new:
        print(i)
else:
    print(-1)




























# -*- coding: cp1252 -*-
import math;

class Stack:
     #from: http://interactivepython.org/runestone/static/pythonds/BasicDS/stacks.html
    
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def Euler1(m):
    #If we list all the natural numbers below 10 that are multiples of 3 or 5,
    # we get 3, 5, 6 and 9. The sum of these multiples is 23.
    #Find the sum of all the multiples of 3 or 5 below 1000.
    sumTotal = 0;
    counter = 0;
    while (counter < m):
        if (counter%3 ==0 or counter%5 == 0):
            sumTotal += counter;

        counter+=1;

    print sumTotal;


def Euler2(m):
    #Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    #By starting with 1 and 2, the first 10 terms will be:
    #1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    #By considering the terms in the Fibonacci sequence whose values do not exceed
    #four million, find the sum of the even-valued terms.
    #Personal challenge: Solve using material learned during Data Structures (CS102)

    fibStack = Stack()
    evenFibStack = Stack()
    fibStack.push(1);
    fibStack.push(2);
    evenFibSum = 0;
    while(fibStack.peek() < m):
        larger = fibStack.pop();
        if (larger%2 ==0):
            evenFibStack.push(larger);
        smaller = fibStack.pop();
        fibStack.push(larger);
        fibStack.push(larger+smaller);

    while(evenFibStack.size() > 0):
        temp = evenFibStack.pop();
        if temp%2 ==0:
            evenFibSum+=temp;
            print temp," ";
            
    print "Answer: ",evenFibSum;
    

    
def Euler3(m):
     #The prime factors of 13195 are 5, 7, 13 and 29.
     #What is the largest prime factor of the number 600851475143 ?
     primes = [];
     index = 0;
    
     count = 2;
     while (count<=m):
          if (m%count ==0):
               m/=count;
               if (primes.count(count) ==0):
                    primes.append(count)
          else:
               count+=1;

     i = 0;
     for i in range (0,len(primes)):
          max = primes[0];
          if (primes[i]>max):
               max = primes[i];

     return max;


#TODO
def Euler4(numDigits):
     #A palindromic number reads the same both ways.
     #The largest palindrome made from the product of two 2-digit numbers is 9009=91�99.
     #Find the largest palindrome made from the product of two 3-digit numbers.
     found = False;
     max = int(math.pow(10,numDigits)-1)
     number1 = max;
     number2 = max
     result = 0;
     palindromes = [];
     
     def findPalindromes(n ,a):
          count = int(math.pow(10,numDigits))*int(math.pow(10,numDigits))-1;
          while (count>0):
               if ((str(count)==reverse(str(count)))):
                   a.append(count);
               count-=1;
     
     def reverse(n):
          result="";
          i=len(n)-1;
          #print "In Number: ", n;
          while(i>-1):
               result+=n[i];
               i-=1;
         # print "Result: ", result;
          return result;

     findPalindromes(numDigits, palindromes);
     print palindromes

     while(found == False):
          # do stuff
          counter1 = 0;
          counter2 = 0;
          if (palindromes[counter1]%number1 ==0):
               while(number2!=0):
                    if ((palindromes[counter1]%number1)%number2 == 0):
                         found = True;
                    else:
                         number2-=1;
          else:
               number1-=1;
          if (number1==0):
               number2 = max;
               number1 = max;
               counter1 +=1;

     print "Numbers are: ", number1, " and ", number2


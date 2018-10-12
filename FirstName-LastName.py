#!/usr/bin/env python3

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():

'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"
def reverse(string):
     str=""
     for ch in string:
             str= ch+str
     return str
2. 
Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
    phrase = phrase.replace("-", " ")
    phraseList = phrase.split()
    print (phraseList)
    returnString = ""
    for i in phraseList:
        substring = i[0:1]
        returnString += substring
    returnString = return String.upper()
    print(returnString)
    return returnString			# You happy, Tom. :)

3.
def whatTriangle(side1,side2,side3):
       equalSides = 0
       if side1 == side2:
               equalSides += 1
       if side2 == side3:
               equalSides += 1
       if side1 == side3:
               equalSides += 1
       if equalSides == 3:
               return "Equilateral"
       elif equalSides == 1 or equalSides == 2:
               return "Isoceles"
       else:
               return "Scalene"



4.
def scrabble(word):
       point1 = "AEIOULNRST"
       point2 = "DG"
       point3 = "BCMP"
       point4 = "FHVWY"
       point5 = "K"
       point8 = "JX"
       point10 = "QZ"
       score = 0
       word = word.upper()
       for i in word:
               if i in point1:
                       score += 1
               elif i in point2:
                       score += 2
               elif i in point3:
                       score += 3
               elif i in point4:
                       score += 4
               elif i in point5:
                       score += 5
               elif i in point8:
                       score += 8
               elif i in point10:
                       score += 10
       print(score)
       return (score)

5.
def armstrong(number):
		#convert number to string
        #get number of digits by finding length of 
		#the string
        digits = len(str(number))
        sum = 0
		
		#iterate through string
        for n in str(number):
                sum += int(n) ** digits
        return sum == number


6.
def main():
        print(getPrimeFactors(910))
def getPrimeFactors(number):
        primeFactors = []
        for n in range(2,number):
                if number % n == 0:                     #filters for factors of the input
                        prime = True
                        for fact in range(2, n):        #filters those factors for which ones are prime
                                if n % fact == 0:
                                        prime = False
                        if prime:
                                primeFactors.append(n)  #check out list.append(entry) !
        return primeFactors
if __name__ == '__main__':
        main()

7.
def pangram(sentence):
       found = False
       sentence = sentence.lower()
       for n in range(ord('a'), ord('z') + 1):
               for m in sentence:
                       if ord(m) == n:
                               found = True
               if found:
                       found = False
               else:
                       return False
       return True

8.
def sort(vals):
        result = []
        while len(vals) > 0:
                curmax = max(vals)
                maxindex = vals.index(curmax)
                result = [curmax]+result
                del vals[maxindex]
        return result



9.
#!/usr/bin/env python3

def main():
       print(rot(5, 'hello'))
       print(rot(26, 'hello'))

def rot(shift, string):
       returnStringN = ''
       alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
       for n in range(0, len(string)):
               if alpha.index(string[n]) + shift > 25:
                       shift -= 26
               returnStringN += alpha[alpha.index(string[n]) + shift]
       return returnStringN
if __name__ == "__main__":
       main()


10.
def evenAndOdds():
       increase = 0
       while( increase  < 10) :
               innum = input("Insert a number: ")
               if increase != 0:
                       numbers.insert(increase,int(innum))
                       increase += 1
               else:
                       numbers = [int(innum)]
                       increase += 1
       outfile1 = open("Even.txt",'a')
       outfile2 = open("Odd.txt",'a')
       for num in numbers:
               if num%2 == 0:
                       outfile1.write(str(num)+"\n")
               else:
                       outfile2.write(str(num)+"\n")
       outfile1.close()
       outfile2.close()



if __name__ == "__main__"
    main()

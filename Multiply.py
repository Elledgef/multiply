#Author: Faith Elledge
#Grithub_ username: Elledgef
#Date: 4/27
#Description: Multiplies two numbers and outputs product

def multiply(n1, n2): 
   if n2 == 0:
       return 0
   else:
       return n1 + multiply(n1, n2 - 1)
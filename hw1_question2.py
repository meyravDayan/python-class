def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition.

   Note: It should print out the first number (with a palindrome in its last 4 digits),
   not all 4 "versions" of it.
   """
   positive_list = []
   def is_palindrom(num):
       if num == num[::-1]:
           return True
       else:
           return False
   for number in range(100000,1000000):
       if is_palindrom(str(number)[2:]):
           list_number = number
           number += 1
           if is_palindrom(str(number)[1:]):
               number += 1
               if is_palindrom(str(number)[1:5]):
                   number += 1
                   if is_palindrom(str(number)):
                       positive_list.append(list_number)
   return(positive_list)
   
   
print(check_palindrome())
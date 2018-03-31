#Python 3.6.4


try:
    number_to_squrare = int(input("Enter Number :"))   
except ValueError:
     print("Invalid Number Provided")
print(number_to_squrare * number_to_squrare)

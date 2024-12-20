#!/usr/bin/env python
# coding: utf-8

# In[11]:


number = 137 # Change this number to test other values

# Prime numbers must be integers and greater than 1
if number <= 1 or not float(number).is_integer():
    print(f"{number} is not a prime number.")
else:
    number = int(number)  # Ensure it's treated as an integer
    is_prime = True  # Assume the number is prime

    # Check divisors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:  # If divisible, it's not prime
            is_prime = False
            break

    # Output results
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


# In[ ]:





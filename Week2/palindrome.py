
user_input = input('Enter something: ')

# had to google this one, reverse the user_input
# StackOverlow: How do I reverse a string in Python? https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
reverse = user_input[::-1]

# IBID
# filter out non-alpha numeric characters and change to lowercase
# e.g. with A man, a plan, a canal, Panama!
# we don't consider the commas, punctuation or spaces in palindromes
reverse = ''.join(char for char in reverse if char.isalnum()).lower()

# do the same to user_input so that we can compare 
clean_input = ''.join(char for char in user_input if char.isalnum()).lower()

if clean_input == reverse:
    print(user_input, 'is a palindrome!')
else:
    print (user_input, 'is NOT a palindrome :(')


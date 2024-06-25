#PALINDROME CHECKER

user = input("Enter a word to check: ")
user = user.lower().replace(" ", "")

ispalindrome = ""
for i in user:
    ispalindrome = i + ispalindrome

if ispalindrome == user:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
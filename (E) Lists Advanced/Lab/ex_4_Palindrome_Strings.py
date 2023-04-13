# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome. First, you should print a list containing all the found
# palindromes in the sequence. Then, you should print the number of occurrences of the given palindrome in
# the format: "Found palindrome {number} times".
# Example
# Input
# wow father mom wow shirt stats
# wow
# Output
# ['wow', 'mom', 'wow', 'stats']
# Found palindrome 2 times
# Input
# hey how you doin? lol
# mom
# Output
# ['lol']
# Found palindrome 0 times
def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(' ')
palindrome = input()


palindromes = [word for word in words if palindrome_filtered(word)]

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")
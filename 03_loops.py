# a. Write a for loop that prints out "banana" one letter at a time, one letter per line
'''for symbol in "Banana":
    print(symbol)'''
 # b. Write a for loop that prints out "banana" backwards  one letter at a time, one letter per line
'''for symbol in 'Banana'[::-1]:
    print(symbol)'''
# c. Copy your code that creates the seven dwarves list, write a for loop
#    that prints out each of the dwarves names
'''dwarves = ['Grumpy','Happy','Sleepy','Sneezy','Dopey','Bashful','and Doc']
for i in dwarves:
    print(i)'''
# d. Write a for loop that prints each of the dwarf's names along with their
#    index in the list (0 - Sleepy, 1 - Happy...)
'''w = 0
dwarves = ['Grumpy','Happy','Sleepy','Sneezy','Dopey','Bashful','and Doc']
for i in dwarves:
    print(str(w) + (" - ")+i)
    w = w+1'''
# e. Write a while loop that prints each of the dwarf's names along with their
#    index in the list (this should have the same output as the part c)
w = 0

# f. Using a while loop, repeatedly prompt the user to enter a positive number.
#    If the user enters a non-positive number, print an error and ask again.

# g. Using a while loop, implement a simple guessing game: pick a secret
#    number 1 to 100 and keep asking the user to guess until they get
#    it right; then print how many guesses it took.

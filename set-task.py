#Task 1
#Create a new Set containing the numbers 1, 2, 3
#Create a new Set containing the letters A, B, C
#Combine the first and second Sets in three different ways and print each method on a line

nums = {1, 2, 3}
letters = {"A", "B", "C"}

new_set_1 = nums | letters
print(new_set_1)  # {1, 2, 3, 'A', 'B', 'C'}

new_set_2 = nums.union(letters)
print(new_set_2)  # {1, 2, 3, 'A', 'B', 'C'}

nums.update(letters)
print(nums)  # {1, 2, 3, 'A', 'B', 'C'}


# Task 2
#Create a Set containing the elements 1, 2, 3
#In the first line, print the content of the Set
#Empty the entire content of the Set with only one line 
#and then print the content in the second line to make sure that it is completely empty
#Add two elements “A”, “B” to this Set and then print its content on the third line
#Try to remove the element “C” Of course the element does not exist
# Make sure that you will not get an error when you try to remove the element that does not exist

my_set = {1, 2, 3}
letters = {"A", "B", "C"}
print(my_set)  # {1, 2, 3}
my_set.clear()  # Empty The Set
print(my_set)  # set()
my_set.update("A", "B")
print(my_set)  # {'A', 'B'}
# my_set.remove("C") # Error Will Appear
my_set.discard("C")  # No Error Will Appear

# Task 3

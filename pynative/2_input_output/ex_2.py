"""
Exercise Question 2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function
Expected Output:

Use print() statement formatting to display the ** separator between each word.

For example: print('My', 'Name', 'Is', 'James') will display MyNameIsJames

So use one of the formatting argument of print() to turn the output into My**Name**Is**James
"""


print("My", "Name", "Is", "James", sep="**")
print("**".join("My Name Is James".split()))

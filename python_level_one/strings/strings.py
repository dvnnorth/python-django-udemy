# STRINGS

# Basics
print("=== Basics ===")
# Strings can be single or double quote. Each escapes the other.
# Can also escape with /
tom = "Tom"
harry = "Harry"
jake_the_snake = "Jake 'The Snake' Roberts"
hulk_hogan = '"Hollywood" Hulk Hogan'
triple_h = "\"HHH\" aka \"Hunter Hearst Helmsley\", real name Paul Levesque"

print(tom)
print(harry)
print(jake_the_snake)
print(hulk_hogan)
print(triple_h)

# Indexing
print("=== Indexing ===")
print(tom[2])
print(triple_h[10])
# Strings are immutable, so no individual index can be reassigned
# the entire string must be changed
# tom[1] = 'X' will not work
print(id(tom))
tom = tom[0:1] + 'X' + tom[2:]
print(tom)
print(id(tom))
# Notice the ID changes; the variable has been redefined

# Slicing
print("=== Slicing ===")
# Slicing is done with square bracket notation with a : separating the start and ending indices
# First index is inclusive, second is exclusive
hulkster = hulk_hogan[12:21]
# Will only print Hulk Hoga because the 21st index is not included
print(hulkster)

# Having no start index indicates slice everthing from the start to the end index
triple_h_stage_name = triple_h[:34]
print(triple_h_stage_name)
# Having no end index indicates slice everything to the last character
triple_h_real_name = triple_h[46:]
print(triple_h[46:])
# Needless to say, just a : will give the whole string
print(triple_h[:])
# Indices can be variables as well
x = 2
y = 31
print(triple_h[x:y])

# You can also step through and grab every other or every third or every nth char with [::n]
print(triple_h[::2])
print(triple_h[::3])

# Basic Methods
print("=== Basic Methods ===")
# upper() returns string as upper case
print(triple_h.upper())
# lower() returns the string as lower case
print(triple_h.lower())
# capitalize() returns the string with first character capitalized
print("hello".capitalize())
# split() splits a string into an array of strings on a certain separator (default is whitespace)
print(triple_h.split())
print(triple_h.split('H'))


# Print Formatting
print("=== Formatting ===")
# You can use single curly braces with the .format() function to insert variables
string = "First arg: {}, Second arg: {}"
print(string.format("dog", "cat"))
string_two = "First arg: {x}, Second arg: {y}".format(x = "foo", y = "bar")
print(string_two)
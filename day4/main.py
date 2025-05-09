# Day 4: Error Handling & Debugging
# •	- Error Handling Basics (try/except)
# •	- Scope of Variables (Local vs Global)
# •	- Doc Strings vs Comments
# •	- Debugging Techniques


# try:
#     a = [1,2,5,5,4,6]
#     print(a[6])
# except Exception as e:
#     print(e)

# scope

# Local scope


def add(a, b):
    """This function adds two number."""
    global c
    c = a+b


# int a=4;
# int add(int d, int b){
#     int c = a+b;
#     return c;
# }


# a = int(input("Enter 1st number:"))
# b = int(input("Enter 2nd number:"))

add(4,9)
print(c)
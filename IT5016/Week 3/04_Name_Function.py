def function2 (name1, name2):
    len1 = len(name1)
    len2 = len(name2)
    shorter_length = min(len1,len2)
    return shorter_length

name1 = input("Enter Name1: ")
name2 = input("Enter Name2: ")
print(function2(name1,name2))

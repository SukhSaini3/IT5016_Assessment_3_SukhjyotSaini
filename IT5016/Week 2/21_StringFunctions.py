"Program for string functions find(), rfind(), count(), strip(), lstrip(),rstrip(), split()"

txt = "find me if you can"
txt2 = "   python   "
txt3 = "...rtgf.....pyhton...rtgf..."
r = txt3.strip(' .rtgf')
txt4 = "Hello how are you"

print(txt.find('i')) #will find the position of 'i' 
print(txt.rfind('i')) #will find the position of 'i' starting from the right side
print("Frequency of i: ", txt.count('i')) #will count the occurance of 'i' 


print(len(txt2))
result = txt2.strip()
print(result)
print("Length of trim version: ", len(result))

print(r) #will print the output with '.rtgf' trimmed

print(txt4.split())



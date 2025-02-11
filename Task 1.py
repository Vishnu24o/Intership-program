# normal print 
print('my name is vishnu')

#use of variables
a=10
print(a)

_var = 'India is a great nation'
print(_var)

# casesensitive
A='python'
print(A)

# overwrite variable
b=20
b='Nobita'
print(b)

# multiple variables
c,d,e=10,20,30
print(str(c)+str(d)+str(e)) #concatation of strings using + operator and str
print(c+d+e) #addition of numbers

#strings
str1 = 'Rohit'
str2 = 'Virat'
str3 = 'Sachin'
str4 = '(45)'
jno1 = 45
jno2 = 18
jno3 = 10
print(str(str1) + '(' + str(jno1) + ')' ) #concatenation of string & jno
print(f"{str1} ( {jno1} )") #concatenation of string & jno using (f"string")
print(str(str1) + str(str4)) #concatenation of string & jno using only strings

#slicing
string = "Python"
print(string)
print(string[0]) #indexing of string
print(string[:4])
print(string[3:])
print(string[0:4]) 
print(string[0:3:2]) #slicing with step
print(string[-1]) #negative indexing
print(string[-4:]) #negative slicing
print(string[-6:-2])  #negative slicing in range

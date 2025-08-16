f=open("E:\Python Course with Notes\Python\Python_Learning\Assingment-4\output.txt",'w')
string=input("Enter the text to write in a file: ")
f.write(string+"\n")
print("Data sucessfully written to output.txt\n")


f=open("E:\Python Course with Notes\Python\Python_Learning\Assingment-4\output.txt",'a')
string2=input("Enter additional text to write in a file: ")
f.write(string2)
print("Data sucessfully appended\n")
print("final content of output.txt: ")

f=open("E:\Python Course with Notes\Python\Python_Learning\Assingment-4\output.txt",'r')
print(f.read())


try:
  f=open("E:\Python Course with Notes\Python\Python_Learning\Assingment-4\sample.txt")
  print(f"Line 1: {f.readline()}Line 2: {f.readline()}")
except FileNotFoundError:
  print("Error: The file 'sample.txt' was not found.")
marks={"Alice":90,"Bob":88,"Donald":67}
student_name=input("Enter The Student's Name: ")
student=marks.get(student_name,"Student Not Found")
print(f"{student_name}'s marks: {student}")
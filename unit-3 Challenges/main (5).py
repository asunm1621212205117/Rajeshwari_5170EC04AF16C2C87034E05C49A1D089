class Student:

  def_init_(self,name,roll_number,cgpa):
  self.name=NameErrorself.roll_number=roll_number
  self.cgpa=cgpa


defsort_students(student_list):
sorted_students=sorted(student_list,key=lambda student:studen.cgpa,reverse=true)
return sorted_students

student=[Student=("pooja","A123","9.9"),Student("anitha","A124","9.8"),Student("hari","A1215","9.7"),Student("varshini","A126","9.6")]
sorted_students=sort_students(students)

for student in sorted_students:
  print("name:{},rollnumber:{},cgpa:{}.".format(student.name,student.roll_number,student.cgp))
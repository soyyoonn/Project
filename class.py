# def create_student(name, korean, math, english, science):
#     return{
#         "name": name,
#         "korean": korean,
#         "math": math,
#         "english": english,
#         "science": science
#     }
#
# def student_get_sum(student):
#     return student["korean"] + student["math"] + student["english"] + student["science"]
#
# def student_get_average(student):
#     return student_get_sum(student) / 4
#
# def student_to_string(student):
#     return "{}\t{}\t{}".format(
#         student["name"],
#         student_get_sum(student),
#         student_get_average(student))
#
# students = [
#     create_student("윤인성", 87, 98, 88, 95),
#     create_student("연하진", 92, 98, 96, 98),
#     create_student("구지연", 76, 96, 94, 90),
#     create_student("나선주", 98, 92, 96, 92),
#     create_student("윤아린", 95, 98, 98, 98),
#     create_student("윤명원", 64, 88, 92, 92),
# ]
#
# print("이름", "총점", "평균", sep = "\t")
# for student in students:
#     print(student_to_string(student))

#클래스 선언
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

#학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 88, 95),
    Student("윤명월", 87, 98, 88, 95)
]

#student 인스턴스의 속성에 접근하는 방법
students[0].name
students[0].korean
students[0].math
students[0].english
students[0].science

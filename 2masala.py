class User:
    def __init__(self, student, teacher):
        self.student  = student
        self.teacher = teacher


class Exam (User):
    def __init__(self, score, teacher ,student ):
        super().__init__(teacher,student)
        self.__score = score
        self.teacher = teacher

    def baho_olish(self,admin, baho):
        if admin.teacher == "Teacher":
            self.__score =baho
            return baho
        else:
            return baho

user2 = User("Talaba" , "Teacher")
obj = Exam(5,user2,"alijon")
print(obj.baho_olish(user2,3), )




































# class User:
#     def __init__(self, name, roli,):
#         self.name=name
#         self.roli=roli
#
# class Exam:
#     def __init__(self,owner,baholar):
#         self.owner=owner
#         self.__baholar=baholar
#
#     def baholar1(self,admin,natija):
#         if admin.roli == "o'qituvchi":
#             self.__baholar=natija
#             return natija
#
# user1=User("Alijon","Talaba")
# user2=User("Muhammadali","o'qituvchi")
# baho=Exam(user1,4)
# print(baho.baholar1(user1, 5))
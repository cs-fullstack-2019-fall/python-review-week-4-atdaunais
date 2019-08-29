# # Python review
# class SchoologyUser:
#     def __init__(self, studentName, schoolName, GPA, classes):
#         self.student = studentName
#         self.school = schoolName
#         self.GPA = GPA
#         self.classes = classes
#
#     def __str__(self):
#         full_info_str = f"studentName = {self.student}\n" \
#                         f"schoolName = {self.school}\n" \
#                         f"GPA = {self.GPA}\n" \
#                         f"classes = {self.classes}\n"
#         return full_info_str
#
#
# newUser = SchoologyUser("Andrew", "CHS", "3.5", "These classes")
# print(newUser)
#
#
# class CodeSchoolInstructor:
#     def __init__(self, teacherName, previousEmployer, knownLanguages):
#         self.teacherName = teacherName
#         self.previousEmployer = previousEmployer
#         self.knownlanguages = knownLanguages
#
#     def __str__(self):
#         show_teacher = f"teacherName = {self.teacherName}\n" \
#                        f"previousEmployer = {self.previousEmployer}\n" \
#                        f"knownLanguages = {self.knownlanguages}\n"
#         return show_teacher
#
#     def add_del_lang(self):
#         userInput = input("Would you like to add or remove a language from known languages?")
#         if userInput == "add":
#             newLang = input("What language would you like to add? ")
#             self.knownlanguages.append(newLang)
#         elif userInput == "remove":
#             del_lang = input("Which language would you like to delete? ")
#             while del_lang in self.knownlanguages: # loops through array to check for the string
#                 grab_lang = self.knownlanguages.index(del_lang) # grabs the index value and puts it into variable
#                 del self.knownlanguages[grab_lang] # deletes the element in the array with that index value
#
#
# newTeacher = CodeSchoolInstructor("Kevin Yancy", "I don't know", ["English", "Russian", "Portuguese"])
# print(newTeacher)
# newTeacher.add_del_lang()
# print(newTeacher)
# newTeacher.add_del_lang()
# print(newTeacher)
# newTeacher.add_del_lang()
# print(newTeacher)


# data = ['GOOD_DATA', 'DECENT_DATA', 'BAD_DATA', 'DECENT_DATA', 'GOOD_DATA', 'BAD_DATA', 'GOOD_DATA', 'DECENT_DATA',
#         'BAD_DATA', 'GOOD_DATA']
#
# print(len(data))
#
# while "BAD_DATA" in data:
#     take_data = data.index("BAD_DATA")
#     del data[take_data]
#
# print(len(data))

# def someFunc():
#     result1 = "yo yo yo"
#     result2 = "heya"
#     result3 = "never"
#     return result1, result2, result3
#
#
# hold_result1, hold_result2, hold_result3 = someFunc()
# print(hold_result1)
# print(hold_result2)
# print(hold_result3)

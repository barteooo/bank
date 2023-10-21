# class NoLoginInSystem(Exception):
#     pass
#
# class Options:
#     def enter_login(users):
#         while True:
#             try:
#                 login = input("Podaj login: ")
#                 if any(u for u in users if u.login != login):
#                     raise NoLoginInSystem("Nie ma użytkownika o podanym loginie")
#                 else:
#                     return
#             except NoLoginInSystem as error:
#                 print(error)


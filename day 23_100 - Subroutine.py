def replitLogin():
  while True:
    userName=input("What is your username: ")
    userPass=input("What is your password: ")
    if userName=="Hamza" and userPass=="123":
      break
    else:
      print("Wrong username or password!!!")
      print()
      continue
print("REPLIT LOGIN SYSTEM")
replitLogin()
print("Welcome to REPLIT")
input()
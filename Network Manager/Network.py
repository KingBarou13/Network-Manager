print("Website Create Account Page")
name = input("\nEnter your name: ")
age = int(input("\nEnter you age (You must be 16 and over to use this website): "))

if age < 16:
  print("\nYou must be 16 and over to use this website")
  exit()

else:
  username = input("\nCreate a username: ")
  
  print ("\nYour new username is", username)
  
  password = input("\nCreate a password (Between 6 and 12 characters): ")

  weak = 'weak'
  med = 'medium'
  strong = 'strong'

  if len(password) >12:
      print ('\nExcessive password length. It must be between 6 and 12 characters')
      exit()

  elif len(password) <6:
      print ('\nInsufficient password length. It must be between 6 and 12 characters')
      exit()


  elif len(password)    >=6 and len(password) <= 12:
      print ('\nSufficient Password Length')

      if password.lower()== password or password.upper()==password or password.isalnum()==password:
          print ('\nYour chosen password is', weak)
          exit()

      elif password.lower()== password and password.upper()==password or password.isalnum()==password:
          print ('\nYour chosen password is', med)

      else:
          password.lower()== password and password.upper()==password and password.isalnum()==password
          print ('\nYour chosen password is', strong)
          
  file = open("Login.txt","a")
  file.write (username)
  file.write (",")
  file.write (password)
  file.write("\n")
  file.close()
  
  print ("\nYour login details have been saved, Welcome to the website! ")


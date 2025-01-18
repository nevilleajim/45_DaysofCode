import re

def is_valid_email(email):
      email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # the ^ symbol indicates the start of the string and the $ sign indicates the end of the string

      if re.match(email_regex, email):
            return True
      
      else:
            return False
      
def main():
      email = input("Enter a valid email address: ")

      if is_valid_email(email):
            print("The email is valid.")
      else:
            print("THe email is invalid.")

if __name__ == "__main__":
      main()
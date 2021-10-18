import re
def email():
    str = "This is Ebbie Aden, you can reach me at ebbieaden@gmail.com for assistance"
    pattern = r"([\w\.-]+)@([\w\.-]+)(\w\.]+)"
    match = re.search(pattern, str)
email()

shii = email()

if shii:
    print(match.group())
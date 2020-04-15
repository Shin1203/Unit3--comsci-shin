# this program will ask the user for first name last name and a number, then generate email addresses.
firstname = input("Enter first name")
lastname = input("Enter last name")
number = int(input("Enter a number under 100"))
emails = []
placeholder = ""
for num in range(1,number+1):
    placeholder = ("{}.{}{}@uwcisak.jp".format(firstname,lastname,num))
    emails.append(placeholder)
print(emails)
f= open("emails.txt","w+")
for m in range(len(emails)):
    f.write("{}, ".format(emails[m]))

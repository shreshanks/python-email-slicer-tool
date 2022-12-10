emails_count = int (input("Enter The Number Of Emails : "))
emails = []
for i in range(emails_count):
    email = input("Enter Email %i : "%(i)).split("@")
    ext = email[1]
    emails.append(list(email))
for i in emails:
    username = i [0]
    domain = i[1]
    upper_domain = domain.upper()
print("username : %s and domain : %s"%(username,upper_domain) )

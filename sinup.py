users = []

# Add users
for i in range(3):
    users.append([input("Enter Email for signup : "), input("Enter Password for signup : "), input("Enter name for signup : ")])

def displayUser(user):
    print("*" * 20)
    print("Email : ", user[0])
    print("Password : ", user[1])
    print("Name : ", user [2])


for i in range(3):
    displayUser(users[i])
    print("Wellcome")
    print("xyz")

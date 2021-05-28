print("\t\tLets make you'r account")

user = {
    'name': input("please enter your name: "),
    'email': input("please enter your email id: "),
    'courses': []
}

if "@" not in user['email']:
    print("Please include a @ ")
    user['email'] = input("please enter your email id: ")

all_courses = ['Python', 'Java', 'Machine Learning', 'Big data', 'C programming', 'Oracle SQL', 'Power Bi''Go lang',
               'C++ Graphics', 'React JS', 'Ruby Rails', 'Flask', 'HTML & CSS', 'Salesforce', 'Javascript', 'Django']

b = 0

print("\t\tChoose your courses")

for i in all_courses:
    print("press {} for {}".format(b, i))
    b += 1
courses = int(input("Type here: "))

for i in range(len(all_courses)):
    if i == courses:
        user['courses'].append(all_courses[i])
        all_courses.remove(all_courses[i])
menu = ["All courses", "My courses", "Show profile"]
option = []
b = 0
print("\t\tMenu")

while True:

    for i in menu:
        print(f"press {b} for {i}")
        b += 1
        if b > len(menu)-1:
            b = 0

    chop = int(input("Type here: "))

    for i in range(len(menu)):
        if i == chop:
            if i not in option:
                option = []
                option.append(menu[i])
            break

    for i in option:
        if i == menu[0]:
            print(all_courses)
            print(
                "Do you want to enroll new course if yes then press 'y' otherwise press 'n'")
            yn = input()
            if yn == 'y':
                print(all_courses)
                courses = int(input("Type here: "))
                for i in range(len(all_courses)):
                    if i == courses:
                        user['courses'].append(all_courses[i])
                        all_courses.remove(all_courses[i])
            elif yn == 'n':
                continue
        elif i == menu[1]:
            for i in user['courses']:
                print(i)
            print("do you want to remove any course then press 'y' otherwise press 'n'")
            ron=input()
            if ron=='y':
                for i in user['courses']:
                    print(f"Press {b} for {i}")
                a = int(input())
                for i in range(len(user['courses'])):
                    if i==a:
                        for i in user['courses']:
                            user['courses'].remove(i)
            else:
                continue
        elif i == menu[2]:
            print(user)
        else:
            print("Invalid input")

    print("Do you want to quit or not if yes then press 'y' otherwise press 'n'")
    yn = input()
    if yn == 'y':
        break
    else:
        continue

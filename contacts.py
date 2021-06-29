contacts = {
    "number":4,
    "students":[
        {"Name":"Sara Holderness", "email":"sarah@example.com"},
        {"name":"harry potter", "email":"harry@example.com"},
        {"name":"hermione granger", "email":"hermione@example.com"},
        {"name":"ron weasley", "email":"ron@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])

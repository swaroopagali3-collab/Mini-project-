def create_resume():
    print("\n" + "=" * 50)
    print("        ONLINE RESUME BUILDER")
    print("=" * 50)
    name = input("Enter Full Name:G.susmitha ")
    email = input("Enter Email:sushmithagaradappagari42@gmail.com ")
    phone = input("Enter Phone Number:1234567890 ")
    address = input("Enter Address:annamacharya institute of technology and science ")
    objective = input("Enter Career Objective:engeering")
    education = input("Enter Education Details:B.TECH 4th year ,annamacharya institute of technology and science")
    skills = input("Enter Skills (comma separated):python
java
sql ")
    experience = input("Enter Experience Details:no experience ")

    resume = f"""
====================================================
                    RESUME
====================================================

PERSONAL DETAILS
----------------------------------------------------
Name       : {G.susmitha}
Email      : {sushmithagaradappagari42@gmail.com }
Phone      : {1234567890}
Address    : {annamacharya institute of technology and science}

CAREER OBJECTIVE
----------------------------------------------------
{engeering}

EDUCATION
----------------------------------------------------
{B.TECH 4th year ,annamacharya institute of technology and science}

SKILLS
----------------------------------------------------
{python
java
sql }

EXPERIENCE
----------------------------------------------------
{ No experience}

====================================================
"""

    print("\nResume Generated Successfully!\n")
    print(resume)
    filename = name.replace(" ", "_") + "_Resume.txt"

    with open(filename, "w") as file:
        file.write(resume)

    print(f"Resume saved as: {filename}")
while True:
    print("\n===== MENU =====")
    print("1. Create Resume")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_resume()

    elif choice == "2":
        print("Thank you for using Online Resume Builder!")
        break

    else:
        print("Invalid Choice! Please try again.")
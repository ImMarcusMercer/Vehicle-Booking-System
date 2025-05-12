from Student import StudentLinkedList
from Details import Details

def main():
    student_list = StudentLinkedList()
    details = Details()

    while True:
        x = """
            Enrollment System

    1.) Add Student
    2.) List of Student
    3.) View Certificate of Enrollment (COR)
    4.) Exit
        """
        print(x)
        choice = input("Enter your choice: ")

        if choice == '1':
            sid = input("School ID: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            age = int(input("Age: "))
            sex = input("Sex (M/F): ")
            year = input("Year Level: ")
            email = input("Email: ")
            section = input("Section Code: ")

            student_list.insert_node(sid, {
                "first_name": fname,
                "last_name": lname,
                "age": age,
                "sex": sex,
                "year_level": year,
                "email": email,
                "section": section
            })

            print("Student added and sorted by last name.")

        elif choice == '2':
            print("\n--- All Students (Sorted by Last Name) ---")
            student_list.display_students()

        elif choice == '3':
            sid = input("Enter School ID: ")
            student = student_list.get_student_info(sid)
            if student:
                print(f"\nName: {student['first_name']} {student['last_name']}")
                print(f"Section: {student['section']}")
                subjects = details.get_subjects_for_section(student['section'])
                if subjects:
                    print("\nSubjects:")
                    for sub in subjects:
                        print(f"{sub['code']} - {sub['description']} ({sub['schedule']})")
                else:
                    print("No subjects found for this section.")
            else:
                print("Student not found.")

        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
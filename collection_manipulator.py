red="\033[1;31m"
green="\033[1;32m"
gray="\033[1;30m"
yellow="\033[1;33m"
blue="\033[1;34m"
cyan="\033[1;36m"
magenta="\033[1;35m"
reset="\033[0m"
students=[]
print("\n-------------------------------------------------------------------------------------------------------------------------------------------")
print(green+"Welcome to Collection Manipulator. Progarmmed by Chirag Kori. This program is designed to \
manipulate collections of data in various ways..." + reset)
print("-------------------------------------------------------------------------------------------------------------------------------------------\n")

print("-------------------------------------------------------------------------------------------------------------------------------------------")
print(cyan+"LET'S BEGIN THE MANIPULATION OF COLLECTIONS...💥" + reset)
print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
while True:
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    print(magenta+"Press 1 to Add Student Details: ")
    print("Press 2 to View Student Details: ")
    print("Press 3 to Search Student Details: ")
    print("Press 4 to Update Student Details: ")
    print("Press 5 to Delete Student Details: ")
    print("Press 6 to Delete all the Student Details: ")
    print("Press 0 to Exit the Program."+reset)
    print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
    
    print("-------------------------------------------------------------------------------------------------------------------------------------------")
    choice = int(input(yellow+"Enter your choice: "+reset))
    
    match choice:
        case 1:
            grid =int(input(cyan+"\nEnter the GR ID of the Student: "+reset))
            name =input(cyan+"Enter the Name of the Student: "+reset)
            age =int(input(cyan+"Enter the Age of the Student:"+reset))
            dob =int(input(cyan+"Enter the Date of Birth of the Student (DD/MM/YYYY): "+reset))
            course=input(cyan+"Enter the Course of the Student: "+reset)
            student = {'GR ID':grid, 'Name':name, 'Age':age, 'Date of Birth':dob, 'Course':course}
            students.append(student)
            print("\n")
            print(green+"Student Details Added Successfully! ✅"+reset)
            print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
    
        case 2:
            if len(students)==0:
                print(red+"\nStudent Not Found! ❌"+reset)
            for stu in students:
                print(f"\n{cyan}GR ID:{reset} {stu['GR ID']} | {cyan}Name: {reset}{stu['Name']} |{cyan} Age:{reset} {stu['Age']} |{cyan} D.O.B:{reset} {stu['Date of Birth']} |{cyan} Course: {reset}{stu['Course']} {reset}")
                print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
    
        case 3:
            grid=int(input("\nEnter the GR ID of the Student to Search: "))
            found = False
            for stu in students:
                if stu['GR ID']==grid:
                    print(f"\n{cyan}GR ID:{reset} {stu['GR ID']} | {cyan}Name: {reset}{stu['Name']} |{cyan} Age:{reset} {stu['Age']} |{cyan} D.O.B:{reset} {stu['Date of Birth']} |{cyan} Course: {reset}{stu['Course']} {reset}")
                    found = True
            if not found:
                print(red+"\nStudent Not Found! ❌"+reset)
        case 4:
            grid=int(input("\nEnter the GR ID of the Student to Update: "))
            found = False
            for stu in students:
                if stu['GR ID']==grid:
                    found = True
                    print("\nPress 1 to Update Name")
                    print("Press 2 to Update Age")
                    print("Press 3 to Update Date of Birth")
                    print("Press 4 to Update Course")
                    update_choice = int(input("\nEnter your choice: "))
                    match update_choice:
                        case 1:
                            new_name=input("\nEnter the New Name of the Student: ")
                            stu['Name']=new_name
                            print(green+"\nStudent Name Updated Successfully! ✅"+reset)
                        case 2:
                            new_age=int(input("Enter the New age of the Student: "))
                            stu['Age']=new_age
                            print(green+"\nStudent Age Updated Successfully! ✅"+reset)
                        case 3:
                            new_dob=int(input("Enter the New Date of Birth of the Student : "))
                            stu['Date of Birth']=new_dob
                            print(green+"\nStudent Date of Birth Updated Successfully! ✅"+reset)   
                        case 4:
                            new_course=input("Enter the New Course of the Student: ")
                            stu['Course']=new_course
                            print(green+"\nStudent Course Updated Successfully! ✅"+reset)
            if not found:
                print(red+"\nStudent Not Found! ❌"+reset)      
        case 5:
            grid=int(input("\nEnter the GR ID of the Student to Delete: "))
            found = False
            for stu in students:
                if stu['GR ID']==grid:
                    students.remove(stu)
                    found=True
                    print(green+"\nStudent Details Deleted Successfully! ✅"+reset)
        case 6:
            password=input("\nEnter the Password to Delete all the Student Details: ")
            if password=="admin":
                students.clear()
                print(green+"\nAll Student Details Deleted Successfully! ✅"+reset)
            else:
                print(red+"\nIncorrect Password! ❌"+reset)
        case 0:
            print("---------------------------------------------------------------------------------------------------------------------------------------------")
            print(magenta+"Exiting the Program...👋"+reset)
            print(magenta+"Thank you for using Collection Manipulator. Have a great day! 🌞"+reset)
            print("-------------------------------------------------------------------------------------------------------------------------------------------\n")
            exit()
    
    
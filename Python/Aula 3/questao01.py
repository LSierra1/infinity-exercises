nameAge = {}
while True:
    options = int(input("Type an option:\n"
                        "0 for close the program\n"
                        "1 for add a person\n"
                        "2 to search for a person\n"
                        "3 to show the current list\n"
                        "Option: ")
                    )

    match options:
        case 0:
            print(nameAge)
            exit()
        case 1:
            name = input("Enter the name of the person: ")
            surname = input("Enter the surname of the person: ")
            age = int(input("Enter the age of the person: "))
            fullName = name.capitalize() + " " + surname.capitalize()
            confirm = input(f"{fullName}, {age} years old. Is that correct?\n"
                            "Type 'yes' to confirm, 'no' to abort: \n")
            while True:
                if confirm[0].upper() == "Y":
                    nameAge[fullName] = age
                    print(f"{fullName}, {age} years added to the database.")
                    break
                elif confirm[0].upper() == "N":
                    print("Okay, let's try again.")
                    name = input("Enter the name of the person: ").capitalize()
                    surname = input("Enter the surname of the person: ").capitalize()
                    age = int(input("Enter the age of the person: "))
                    fullName = name + " " + surname
                    confirm = input(f"{fullName}, {age} years old. Is that correct?\n"
                                    "Type 'yes' to confirm, 'no' to abort: \n")
                elif confirm[0].upper() not in "YN":
                    print("Sorry, I didn't understand what you said.")
                    confirm = input(f"{fullName}, {age} years old. Is that correct?\n"
                                    "Type 'yes' to confirm, 'no' to abort: \n")
                else:
                    print("Error.")
                    print(nameAge)
        case 2:
            while True:
                searchName = input("Search for the name of the specified person: ").capitalize()
                searchSurname = input("Search for the surname of the specified person: ").capitalize()
                fullNameSearch = searchName + " " + searchSurname
                found = False
# O segredo desse bloco funcionar de maneira logicamente correta é o found = false (flag). Sem ele, as condições vão se repetir o tempo todo.
                for name, age in nameAge.items():
                    if fullNameSearch == name:
                        print(f"{fullNameSearch} found in the database.")
                        found = True
                        break

                if not found:
                    print(f"{fullNameSearch} not found in the database.")

                        
                        # while True:
                        #     if confirmSearch[0].upper() == "Y":
                        #         continue
                        #     elif confirmSearch[0].upper() == "N":
                        #         break
                        #     elif confirmSearch[0].upper() not in "YN":
                        #         print("Sorry, I didn't understand what you said.")
                        #         confirmSearch = input("Do you still want to search?\n"
                        #                             "Type 'yes' to continue, 'no' to abort:\n")
                        #     else:
                        #         print("Error.")
                        #         print(nameAge)
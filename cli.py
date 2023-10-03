from cli_functions import(
    exit_cli,
    show_all_groups,
    show_group_by_id,
    show_group_by_name,
    show_groups_by_continent,
    show_groups_by_city,
    make_group,
    update_group,
    delete_group,
    show_all_adventurers,
    show_adventurer_by_id,
    show_adventurer_by_name,
    show_adventurers_by_alignment,
    show_adventurers_by_job,
    make_adventurer,
    update_adventurer,
    delete_adventurer,
    show_adventurers_by_group
)

def main():
    while True:
        menu()
        choice = input("-> ")
        if choice == "0":
            exit_cli()
        elif choice == "1":
            show_all_groups()
        elif choice == "2":
            show_group_by_id()
        elif choice == "3":
            show_group_by_name()
        elif choice == "4":
            show_groups_by_continent()
        elif choice == "5":
            show_groups_by_city()
        elif choice == "6":
            make_group()
        elif choice == "7":
            update_group()
        elif choice == "8":
            delete_group()
        elif choice == "9":
            show_all_adventurers()
        elif choice == "10":
            show_adventurer_by_id()
        elif choice == "11":
            show_adventurer_by_name()
        elif choice == "12":
            show_adventurers_by_alignment()
        elif choice == "13":
            show_adventurers_by_job()
        elif choice == "14":
            make_adventurer()
        elif choice == "15":
            update_adventurer()
        elif choice == "16":
            delete_adventurer()
        elif choice == "17":
            show_adventurers_by_group()
        else:
            print("Error: Not an option.")

def menu():
    print("=" * len("Make your choice:"))
    print("Make your choice:")
    print("0: Close the Program")
    print("1: Show all Groups")
    print("2: Show a Group by ID#")
    print("3: Show a Group by name")
    print("4: Show Groups by continent")
    print("5: Show Groups by city")
    print("6: Create a new Group")
    print("7: Update an existing Group")
    print("8: Delete an existing Group")
    print("9: Show all Adventurers")
    print("10: Show an Adventurer by ID#")
    print("11: Show an Adventurer by name")
    print("12: Show Adventurers by Alignment")
    print("13: Show Adventurers by Job")
    print("14: Create a new Advetnurer")
    print("15: Update an existing Adventurer")
    print("16: Delete an existing Adventurer")
    print("17: Show all Adventurers of a Group")

if __name__ == "__main__":
    main()

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
    print("=" * len("|Adventurer's Unite!|"))
    print("|Adventurer's Unite!|")
    while True:
        menu()
        choice = input("=}==> ")
        if choice == "0":
            exit_cli()
        elif choice == "1":
            group_submenu()
            gs_choice = input("=}===> ")
            if gs_choice == "0":
                print("Returning to main menu...")
            elif gs_choice == "1":
                show_all_groups()
            elif gs_choice == "2":
                show_group_by_id()
            elif gs_choice == "3":
                show_group_by_name()
            elif gs_choice == "4":
                show_groups_by_continent()
            elif gs_choice == "5":
                show_groups_by_city()
            elif gs_choice == "6":
                make_group()
            elif gs_choice == "7":
                update_group()
            elif gs_choice == "8":
                delete_group()
            elif gs_choice == "9":
                show_adventurers_by_group()
            else:
                print("Error: Not an option")
        elif choice == "2":
            adventurer_submenu()
            as_choice = input("=}===> ")
            if as_choice == "0":
                print("Returning to main menu...")
            elif as_choice == "1":
                show_all_adventurers()
            elif as_choice == "2":
                show_adventurer_by_id()
            elif as_choice == "3":
                show_adventurer_by_name()
            elif as_choice == "4":
                show_adventurers_by_alignment()
            elif as_choice == "5":
                show_adventurers_by_job()
            elif as_choice == "6":
                make_adventurer()
            elif as_choice == "7":
                update_adventurer()
            elif as_choice == "8":
                delete_adventurer()
            else:
                print("Error: Not an option")
        else:
            print("Error: Not an option.")

def menu():
    print("=" * len("|Adventurer's Unite!|"))
    print("Main Menu:")
    print("0: Close the Program")
    print("1: Group Options")
    print("2: Adventurer Options")

def group_submenu():
    print("0: Go back")
    print("1: Show all Groups")
    print("2: Show a Group by ID#")
    print("3: Show a Group by name")
    print("4: Show Groups by continent")
    print("5: Show Groups by city")
    print("6: Create a new Group")
    print("7: Update an existing Group")
    print("8: Delete an existing Group")
    print("9: Show all Adventurers of a Group")

def adventurer_submenu():
    print("0: Go back")
    print("1: Show all Adventurers")
    print("2: Show an Adventurer by ID#")
    print("3: Show an Adventurer by name")
    print("4: Show Adventurers by Alignment")
    print("5: Show Adventurers by Job")
    print("6: Create a new Advetnurer")
    print("7: Update an existing Adventurer")
    print("8: Delete an existing Adventurer")


if __name__ == "__main__":
    main()

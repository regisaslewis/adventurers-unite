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
    delete_adventurer
)

def main():
    while True:
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



if __name__ == "__main__":
    main()
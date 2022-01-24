import SQL_Connector
import queries


def main():
    menu()

    while True:
        try:
            answer = input("\nPlease enter a number: ")

        except:
            print("Please enter a number between 0-5")

        if answer == '0':
            SQL_Connector.close_conn()
            return False

        elif answer == '1':
            menu()

        elif answer == '2':
            queries.total_usa()

        elif answer == '3':
            queries.total_state()

        elif answer == '4':
            queries.vax_vs_nonvax()

        elif answer == '5':
            csv = input("\nPlease enter file path")
            table_name = input("\n Please enter the table name")
            SQL_Connector.into_table(csv, table_name)


def menu():
    print("This program displays up to date covid 19 numbers")
    print("\n What would you like to see?")

    print("\n 1: Redisplay menu")
    print("\n 2: Current US cases and deaths country wide")
    print("\n 3: Current US cases and deaths by state")
    print("\n 4: Vaxinated cases and deaths vs Unvaxinated")
    print("\n 5: Add a New Table")
    print("\n 0: Quit")


main()

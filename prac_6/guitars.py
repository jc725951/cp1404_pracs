from guitar import Guitar


def main():
    """Tests for Guitar class."""
    guitar_list = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":

        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_added = Guitar(name, year, cost)
        guitar_list.append(guitar_added)
        print(guitar_added,  "added.")
        name = input("Name: ")

    guitar_list.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitar_list.append(Guitar("Line 6 JTV-59", 2010, 1512.90))

    if guitar_list:

        print("These are my guitars:")
        for i, guitar in enumerate(guitar_list):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))

    else:
        print("Go and buy one guitar")


main()
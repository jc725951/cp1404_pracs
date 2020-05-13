from guitar import Guitar


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922

    guitar = Guitar(name, year)

    another = Guitar("Another Guitar", 2012)

    print("{} get_age()- Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))

    print("{} get_age()- Expected {}. Got {}".format(another.name, 7, another.get_age()))

    print("{} is_vintage()- Expected {}. Got {}".format(name, True,
                                                        guitar.is_vintage()))

    print("{} is_vintage()- Expected {}. Got {}".format(another.name, False,
                                                        another.is_vintage()))


if __name__ == '__main__':
    run_tests()
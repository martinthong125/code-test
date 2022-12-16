import scriptStructure


def func3():
    print("This is from func3")


def func4():
    print("This is from func4")


def main():
    scriptStructure.func1()
    scriptStructure.func2()
    func3()
    func4()


if __name__ == "__main__":
    main()

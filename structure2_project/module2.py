def welcome_module2():
    print("welcome from module2 - welcome_module2 function")

def main():
    print("-----------this is module 2---------------")
    welcome_module2()

    print(__name__)

    print("-------------This is the end of module2 ---------------")

if __name__ == '__main__':
    main()

def entryexit_log(func):
    def wrapper():
        print("******** "+ str(func).split(" ")[1])
        func()
        print("********" + str(func).split(" ")[1])
    return wrapper

@entryexit_log
def login_user():
    print("valid user")

def greet_user():
    print("greet user")


def enter_user():
    print("enter user")



login_user()
greet_user()
enter_user()


def greet():
    print("GOOD MORNING")

def callmymethod(func):
    func()


callmymethod(greet)


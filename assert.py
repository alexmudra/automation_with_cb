def get_name(name):
    assert type(name) is str, "user name must be string"
    print("searching...")



get_name(1) #AssertionError: user name must be string
get_name("sasha") #searching...

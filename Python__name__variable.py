# Python example about the usage of __name__ variable
# __name__ variable prints the program it is executing i.e main()
# In simple words, modules are nothing but programs that can be reused without having to rewrite the functionality
# That's why we are able to use libraries and packages provided by Python which are modules that are packaged and distributed widely to utilize code reusability
def func1():
    print(__name__)


# Still need to call the function like normal even though this module is being imported in another module
# func1()

# This means ONLY execute or call the func1() when the __name__ variable results to __main__, which will be true when ONLY this module is executed
# If this module is imported to other module, then this func1() will not be executed in other module because the value of __name__ will be Python__name__variable when other module is executed
if __name__ == "__main__":
    func1()

print("This is module1/file1")

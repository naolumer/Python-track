class User:
    def __init__(self, name):
        self.name= name
        self.is_logged_in= False
def decoratorr(functionn):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in== True:
            functionn(args[0])
    return wrapper
@decoratorr
def create_blogpost(user):
    print (f"Here is the blog of {user.name}")
new_user= User("Naol")
new_user.is_logged_in = True
create_blogpost(new_user)




        
    






# from flask import Flask
# app=Flask(__name__)


# def make_bold(functionn):
#     def wrapper():
#         text=functionn()
#         return f"<b>{text}</b>"
#     return wrapper

# def make_underlined(functionn):
#     def wrapper():
#         text=functionn()
#         return f"<u> {text}</u>"
#     return wrapper

# def make_emphasis(functionn):
#     def wrapper():
#         text=functionn()
#         return f"<em> {text}</em>"
#     return wrapper
    

# @app.route("/")
# # rendering html elements with flask

# def hello_world():
#     return '<h1 style="text-align: center"> hello world!</h1><p> This is a paragraph.</p><img src= "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmJzNGZsZWkxdnVzdnJrcThyOW9kbnJzZ2RjdzIxb2V3ZjdmdHF3eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12ELmx0C4EFKcE/giphy.webp"></img> '
# @app.route("/username/<name>")
# def greet(name):
#     return f"Hello there {name +12}!"

# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return "Bye!"

# if __name__=="__main__":
#     app.run(debug=True)


# Decorator exercise
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




        
    






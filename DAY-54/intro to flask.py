from flask import Flask
app=Flask(__name__)

@app.route("/")

def hello_world():
    return 'hello world!'

if __name__=="__main__":
    app.run()
    

# python decorator
import time
def decorator(functionn):
    def wrapper_function():
        functionn()
        time.sleep(2)
        functionn()
        time.sleep(3)
    return wrapper_function

@decorator
def delay():
    print('Hello World!')
delay()
    
# functions as first class variables
# functions passed in as an argument
def add(n1,n2):
    return n1+n2


def calculator(calculate, n1, n2):
    return calculate(n1,n2)

result= calculator(add,3,5)
print(result)

# python nested functions

def outer():
    x= "peanut"
    print(x)
    
    def inner():
        y="hamsters"
        print(y)
    inner()
outer()





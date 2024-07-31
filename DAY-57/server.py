from flask import Flask,render_template
import requests



app= Flask(__name__)

@app.route("/guess/<some_name>")
def home(some_name):
    
    urlg="https://api.genderize.io"
    urla="https://api.agify.io"
    parameterg= {"name": some_name}
    parametera={"name":some_name}
    
    responseg= requests.get(url=urlg, params=parameterg)
    responsea= requests.get(url=urla, params=parametera)
    responsea.raise_for_status()
    responseg.raise_for_status()
    
    datag= responseg.json() 
    dataa= responsea.json()
    
    agge= dataa["age"]
    gen= datag["gender"]
    return render_template("index.html", age=agge, gender=gen, name= some_name)




if __name__=="__main__":
    app.run(debug=True)
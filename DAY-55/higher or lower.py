from flask import Flask
import random

app= Flask(__name__)

@app.route("/")
def guess_the_number():
    return "<h1> Guess a number between '0' and '9'</h1> <img src='https://media2.giphy.com/media/l0Ex9pftnvPgw0nPa/200.webp?cid=790b76116vlndnz88wt6k2jtcll2jpku78g4qitiyqe46tae&ep=v1_gifs_search&rid=200.webp&ct=g'</img>"


random_num= random.randint(0,9)

@app.route("/<int:guess>")
def higher_or_lower(guess):
    if guess> random_num:
        return f"<h1 style= 'color: purple'> Too high, try again!</h1><img src='https://media4.giphy.com/media/gzBwhbjfjdZzIaO9En/giphy.webp?cid=790b7611quhhyahis886jak6dok5siij5kzj6pyqxl58ujuh&ep=v1_gifs_search&rid=giphy.webp&ct=g'</img>"
    
    elif guess< random_num:
        return f"<h1 style='color: red'> Too low, Try again!</h1> <img src='https://media2.giphy.com/media/VRKheDy4DkBMrQm66p/giphy.webp?cid=790b76117jdvitur75so0jnjp7ienalncns2csb5ynkd8cug&ep=v1_gifs_search&rid=giphy.webp&ct=g'</img>"
    
    else:
        return f"<h1 style='color:green'> You won, Congrats!</h1> <img src='https://media3.giphy.com/media/lyXFtyWkLiiA4ovywf/200.webp?cid=ecf05e474cqe6zwm6rs3lxca2lzmbpllbd7ttq9k15gxdylo&ep=v1_gifs_related&rid=200.webp&ct=g'</img>"
    
        

if __name__=="__main__":
    app.run(debug=True)
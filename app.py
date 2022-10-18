
from flask import Flask,render_template

calendario=Flask(__name__)

#Creamos el index de la app, utilizando templates, en html desde la carpteta templates
@calendario.route("/", methods=["POST","GET"])
def index():
    print("estoy en la app")
    return render_template("index.html")



if __name__=="__main__":
    calendario.run(debug=True)




    



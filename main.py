from flask import Flask, render_template

# Criação do site
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

# Site no ar
if __name__ == "__main__":
    app.run(debug=True)

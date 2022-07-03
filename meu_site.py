from flask import Flask, render_template

app = Flask(__name__)
# route -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/localizacao")
def contatos():
    return render_template("localizacao.html")

@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

    # servidor do heroku


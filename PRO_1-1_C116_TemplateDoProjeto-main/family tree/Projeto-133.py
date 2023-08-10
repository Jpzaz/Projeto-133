# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "João Paulo Zampier Zanon"
    idade = "13" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/")
def home():

    nome = "Maria Victória Zampier Zanon"
    idade = "04" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página da mãe
@app.route("/")
def home():

    nome = "Vitor Coutinho Zanon"
    idade = "38" 

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do amigo
@app.route("/")
def home():

    nome = "Cintia Andrade Zampier Zanon"
    idade = "37" 

    return render_template('index.html' , nome = nome , idade = idade)

# adicione outras rotas, se você quiser
@app.route("/")
def home():

    nome = "Agostinha Zampier"
    idade = "61" 

    return render_template('index.html' , nome = nome , idade = idade)

@app.route("/")
def home():

    nome = "Walter Zampier"
    idade = "67" 

    return render_template('index.html' , nome = nome , idade = idade)

# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)

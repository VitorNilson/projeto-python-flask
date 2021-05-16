from flask import Flask, render_template, request, redirect, flash, session\
    , url_for

app = Flask(__name__)
app.secret_key = "VitorNilson"

#Atributos não foram privados para agilizar o desenvolvimento
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#Atributos não foram privados para agilizar o desenvolvimento
class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha


usuario1 = Usuario("vitor", "Vitor Nilson", "1234")
usuario2 = Usuario("roberto", "Roberto Carlos", "emocoes")

lista_usuarios = {usuario1.id: usuario1, usuario2.id: usuario2}


jogo1 = Jogo('Super Mario', 'Ação', 'Nes 64')
jogo2 = Jogo('Crash Bandicoot', 'Aventura', 'Playstation 1')
jogo3 = Jogo('Need For Speed Underground 2', 'Corrida', 'Playstation 2')
jogo4 = Jogo('Call Of Duty Modern Warfare', 'Guerra', 'Playstation 3')

lista = [jogo1, jogo2, jogo3, jogo4]

@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima='novo'))
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=['POST',])
def criar():
    jogo = Jogo(request.form['nome'], request.form['categoria'], request.form['console'])

    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():

    if request.form['usuario'] in lista_usuarios:
        if lista_usuarios[request.form['usuario']].senha == request.form['senha']:
            session['usuario_logado'] = request.form['usuario']
            flash(lista_usuarios[request.form['usuario']].nome + ', logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Dados incorretos, tente novamente!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))

app.run(debug=True)
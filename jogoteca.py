from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = "VitorNilson"
class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

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
        return redirect('/login')
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=['POST',])
def criar():
    jogo = Jogo(request.form['nome'], request.form['categoria'], request.form['console'])

    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'teste' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ', logado com sucesso!')
        return redirect('/')
    else:
        flash('Dados incorretos, tente novamente!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')

app.run(debug=True)
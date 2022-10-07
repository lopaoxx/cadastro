import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'acimpacta'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravar', methods=['POST','GET'])
def gravar():
  nome = request.form['nome']
  sobrenome = request.form['sobrenome']
  email = request.form['email']
  senha = request.form['senha']
  endereco = request.form['endereco']
  numero = request.form['numero']
  complemento = request.form['complemento']
  estado = request.form['estado']
  cidade = request.form['cidade']
  if nome and sobrenome and email and senha and endereco and numero and complemento and estado and cidade:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into login (nome, sobrenome, email, senha, endereco, numero, complemento, estado, cidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (nome, sobrenome, email, senha, endereco, numero, complemento, estado, cidade))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome, sobrenome, email, senha, endereco, numero, complemento, estado, cidade')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
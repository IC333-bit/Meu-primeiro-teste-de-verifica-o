from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def pagina_login():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    texto = request.form['nome']
    print("Recebi do front end:", texto)
    if texto.lower() =='henrique' or texto.lower() == 'henrique':
        return f'Ola admin'
    else:
        return f"Errado"

if __name__ == '__main__':
    app.run(debug=True)

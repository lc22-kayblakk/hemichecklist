from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

checklists = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    mecanico = request.form.get('mecanico')
    obs = request.form.get('obs')
    categorias = {}

    for key, value in request.form.items():
        if key not in ['mecanico', 'obs']:
            categorias[key] = value

    checklist = {
        "mecanico": mecanico,
        "obs": obs,
        "categorias": categorias
    }
    checklists.append(checklist)
    return redirect(url_for('logistica'))

@app.route('/logistica')
def logistica():
    return render_template('logistica.html', checklists=checklists)

if __name__ == "__main__":
    app.run(debug=True)

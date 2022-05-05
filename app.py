from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/products')
def products():
    return render_template('our_prod.html')

if __name__ == "__main__":
    app.run(debug=True)

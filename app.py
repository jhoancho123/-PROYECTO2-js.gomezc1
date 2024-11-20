from flask import Flask
from models import db, Ingrediente, Producto
from heladeria import Heladeria

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1019069665aA*@localhost/tablas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def cargar_datos():
    heladeria = Heladeria()
    heladeria.cargar_datos()

if __name__ == '__main__':
    app.run(debug=True)

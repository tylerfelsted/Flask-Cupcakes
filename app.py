"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from forms import NewCupcakeForm
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secretkey"

connect_db(app)

@app.route('/')
def home_page():
    form = NewCupcakeForm()
    return render_template("index.html", form=form)

@app.route('/api/cupcakes')
def get_cupcakes():
    """returns a list of all cupcakes"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """returns a single cupcake specified by id"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """creates a new cupcake"""
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    if not image:
        image = "https://tinyurl.com/demo-cupcake"

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """updates an existing cupcake by id"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image", cupcake.image)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Deletes a cupcake by id"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
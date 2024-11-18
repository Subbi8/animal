from flask import Blueprint, render_template, request
from app.models import Animal, db

bp = Blueprint('animals', __name__, url_prefix='/animals')

@bp.route('/')
def list_animals():
    animals = Animal.query.all()
    return render_template('animals.html', animals=animals)

@bp.route('/add', methods=['POST'])
def add_animal():
    data = request.form
    animal = Animal(
        name=data['name'],
        species=data['species'],
        breed=data.get('breed'),
        age=data.get('age'),
        health_status=data.get('health_status')
    )
    db.session.add(animal)
    db.session.commit()
    return "Animal added successfully!"

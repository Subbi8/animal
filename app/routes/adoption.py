from flask import Blueprint, render_template, request
from app.models import Animal, Adopter, Adoption, db

bp = Blueprint('adoption', __name__, url_prefix='/adoption')

@bp.route('/')
def view_adoptions():
    adoptions = Adoption.query.all()
    return render_template('adoption.html', adoptions=adoptions)

@bp.route('/apply', methods=['POST'])
def apply_for_adoption():
    data = request.form
    adopter = Adopter(name=data['name'], contact_info=data['contact_info'])
    db.session.add(adopter)
    db.session.commit()

    adoption = Adoption(
        animal_id=data['animal_id'],
        adopter_id=adopter.id
    )
    db.session.add(adoption)
    db.session.commit()

    # Mark animal as adopted
    animal = Animal.query.get(data['animal_id'])
    animal.is_adopted = True
    db.session.commit()

    return "Adoption applied successfully!"

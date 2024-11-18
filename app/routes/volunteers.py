from flask import Blueprint, render_template, request
from app.models import Volunteer, db

bp = Blueprint('volunteers', __name__, url_prefix='/volunteers')

@bp.route('/')
def list_volunteers():
    volunteers = Volunteer.query.all()
    return render_template('volunteers.html', volunteers=volunteers)

@bp.route('/add', methods=['POST'])
def add_volunteer():
    data = request.form
    volunteer = Volunteer(
        name=data['name'],
        skills=data.get('skills'),
        availability=data.get('availability')
    )
    db.session.add(volunteer)
    db.session.commit()
    return "Volunteer added successfully!"

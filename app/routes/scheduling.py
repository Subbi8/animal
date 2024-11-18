from flask import Blueprint, render_template, request
from app.models import Schedule, db

bp = Blueprint('scheduling', __name__, url_prefix='/schedule')

@bp.route('/')
def view_schedule():
    schedule = Schedule.query.all()
    return render_template('schedule.html', schedule=schedule)

@bp.route('/assign', methods=['POST'])
def assign_schedule():
    data = request.form
    schedule = Schedule(
        volunteer_id=data['volunteer_id'],
        task=data['task'],
        date=data['date']
    )
    db.session.add(schedule)
    db.session.commit()
    return "Schedule assigned successfully!"

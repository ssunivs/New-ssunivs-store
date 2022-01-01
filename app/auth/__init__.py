from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError

from app import db
from app.models.user import User
from app.utils.auth import generate_token

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/register", methods=["POST"])
def register():
    incoming = request.get_json()

    user = User(
        email=incoming["email"],
        password=incoming["password"]
    )
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409

    new_user = User.query.filter_by(email=incoming["email"]).first()

    return jsonify(
        id=user.id,
        token=generate_token(new_user)
    )


@bp.route("/login", methods=["POST"])
def login():
    pass


@bp.route("/check", methods=["GET"])
def check():
    pass


@bp.route("/logout", methods=["POST"])
def logout():
    pass

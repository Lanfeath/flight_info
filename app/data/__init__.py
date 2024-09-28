from flask import Blueprint # type: ignore

bp = Blueprint('data', __name__)


from app.data import routes
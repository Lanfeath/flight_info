from flask import Blueprint # type: ignore

bp = Blueprint('search', __name__)


from app.search import routes
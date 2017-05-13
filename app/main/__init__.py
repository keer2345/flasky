from flask import Blueprint

from app.models import Permission

main = Blueprint('main', __name__)

from . import views, errors


def inject_permissions():
    return dict(Permission=Permission)

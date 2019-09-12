from flask import Blueprint

bp = Blueprint("bp",__name__)


@bp.before_request
@bp.after_request
@bp.errorhandler(404)


from flask import Blueprint, request, jsonify
from proj.model import *
from datetime import date

bp_proposal = Blueprint('bp_proposal', __name__)


@bp_proposal.route('/index')
def index():
    print("OK")
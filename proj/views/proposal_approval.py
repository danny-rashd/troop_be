from flask import Blueprint, request, jsonify
from proj.model import *
from datetime import date

bp_proposal_approval = Blueprint('bp_proposal_approval', __name__)


@bp_proposal_approval.route('/index')
def index():
    print("OK")
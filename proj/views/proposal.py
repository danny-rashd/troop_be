from flask import Blueprint, request, jsonify
from .functional import *
from proj.model import *
from datetime import date

bp_proposal = Blueprint('bp_proposal', __name__)


@bp_proposal.route('/index')
def index():
    print("OK")


@bp_proposal.route('/get_requestor_details/<pers_no>')
def get_requestor_details(pers_no):
    response = dict()
    response["status"] = "OK"
    response["data"] = list()
    response["error"] = "-"

    try:
        sp = StaffProfile.query.filter(StaffProfile.pers_no==pers_no).first()
        if sp:
            response['data'].append({
                "staff_name": sp.staff_name,
                "staff_id": sp.staff_no,
                "cost_center": sp.cost_centre if sp.cost_centre else "-",
                "division": sp.division_name,
                "lob": sp.lob_name,
            })

    except Exception as e:
        msg = error_log()
        response["status"] = "FAILED"
        response["error"] = msg

    finally:
        return jsonify(response)


@bp_proposal.route('/get_project_manager_details')
def get_project_manager_details():
    response = dict()
    response["status"] = "OK"
    response["data"] = list()
    response["error"] = "-"

    try:
        sp = StaffProfile.query.filter(StaffProfile.lob_name == "GITD").all()
        if sp:
            response['data'].append({
                "staff_name": sp.staff_name,
                "staff_id": sp.staff_no,
                "cost_center": sp.cost_centre if sp.cost_centre else "-",
                "division": sp.division_name,
                "lob": sp.lob_name,
            })

    except Exception as e:
        msg = error_log()
        response["status"] = "FAILED"
        response["error"] = msg

    finally:
        return jsonify(response)


@bp_proposal.route('/template')
def template():
    response = dict()
    response["status"] = "OK"
    response["data"] = list()
    response["error"] = "-"

    try:
        pass

    except Exception as e:
        msg = error_log()
        response["status"] = "FAILED"
        response["error"] = msg

    finally:
        return jsonify(response)
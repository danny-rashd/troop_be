from proj.views.proposal_approval.business_rule import *
from proj.views.proposal_approval.business_process import *


def get_budget_holder_approval(proposalID):
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        status = check_finance_approval_exist(proposalID)
        if status['status'] == "OK" and len(status['data']) > 0:

            status_view = lob_finance_approval_details(status['data'])
            if status_view['status'] == "OK" and len(status_view['data']) > 0:
                response['data'] = status_view['data']

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response


def get_business_case_approval(proposalID):
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        status = check_business_case_exist(proposalID)
        if status['status'] == "OK" and len(status['data']) > 0:

            status_view = business_case_details(status['data'])
            if status_view['status'] == "OK" and len(status_view['data']) > 0:
                response['data'] = status_view['data']

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response
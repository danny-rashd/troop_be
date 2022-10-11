from proj.views.proposal_approval.business_rule import *


def lob_finance_approval_details(listID):
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        ## check if data finance approval exist
        status = lob_finance_details(listID)
        if status['status'] == "OK":
            response['data'] = status['data']
        else:
            raise Exception

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response

def business_case_details(listID):
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        ## check if data finance approval exist
        status = lob_finance_details(listID)
        if status['status'] == "OK":
            response['data'] = status['data']
        else:
            raise Exception

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response
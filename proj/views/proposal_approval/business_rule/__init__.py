def check_finance_approval_exist(proposalID):
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        ## check if data finance approval exist
        response['data'] = ["dataID","dataID"]
        pass

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response


def lob_finance_details(listID):
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        for i in listID:
            pass
            ## connect database
        response['data'] = [{}]

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response

def check_business_case_exist():
    response = dict()
    response['status'] = "OK"
    response['data'] = []
    response['error'] = "-"

    try:
        ## check database
        response['data'] = ["dataID"]

    except Exception as e:
        response['error'] = str(e)
        response['status'] = "FAILED"
    finally:
        return response

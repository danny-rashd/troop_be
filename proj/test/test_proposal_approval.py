from proj.views.proposal_approval import *


def test_get_budget_holder_approval():
    # functional test
    response = get_budget_holder_approval("ID")
    assert response["status"] == "OK"

    # post-condition test
    ## connect to model


def test_get_business_case_approval():
    # functional test
    response = get_business_case_approval("ID")
    assert response["status"] == "OK"

    # post-condition test
    ## connect to model


def test_lob_finance_approval_details():
    # functional test
    response = lob_finance_approval_details("ID")
    assert response["status"] == "OK"

    # post-condition test
    ## connect to model


def test_business_case_details():
    # functional test
    response = business_case_details("ID")
    assert response["status"] == "OK"

    # post-condition test
    ## connect to model


def test_check_finance_approval_exist():
    # functional test
    response = check_finance_approval_exist("ID")
    assert response["status"] == "OK"

    # post-condition test
    ## connect to model


def test_lob_finance_details():
    # functional test
    response = lob_finance_details("ID")
    assert response["status"] == "OK"

    # post-condition test
    ## connect to model

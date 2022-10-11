import sys, os, json


def error_log():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    msg = exc_obj, fname, "Line number : ", exc_tb.tb_lineno
    print(msg)
    return str(msg)
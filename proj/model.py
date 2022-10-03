import uuid
from datetime import datetime

import pytz
from flask import json
from sqlalchemy import event

from proj import db


# class JsonEncodedDict(db.TypeDecorator):
#     """Enables JSON storage by encoding and decoding on the fly."""
#     impl = db.Text
#
#     def process_bind_param(self, value, dialect):
#         if value is None:
#             return '[]'
#         else:
#             return json.dumps(value)
#
#     def process_result_value(self, value, dialect):
#         if value is None:
#             return []
#         else:
#             return json.loads(value)

class StaffProfile(db.Model):
    pers_no = db.Column(db.String(16), primary_key=True)
    staff_no = db.Column(db.String(255))
    staff_name = db.Column(db.String(255))
    designation = db.Column(db.String(16))
    band = db.Column(db.String(16))
    cost_centre = db.Column(db.String(16))
    section_unit = db.Column(db.String(255))
    division_name = db.Column(db.String(255))
    lob_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_no = db.Column(db.String(16))
    record_status = db.Column(db.Boolean)
    last_update_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    staff_profile_hr_data_mart = db.relationship("StaffProfileHRDataMart", backref="staffprofile", lazy=True, cascade="all,delete")
    system_user = db.relationship("SystemUser", backref="StaffProfile", lazy=True, cascade="all,delete")

    def __init__(self, pers_no, staff_no, staff_name, designation, band, cost_centre, section_unit, division_name, lob_name,
                 email, phone_no, record_status, last_update_date):
        self.pers_no = pers_no
        self.staff_no = staff_no
        self.staff_name = staff_name
        self.designation = designation
        self.band = band
        self.cost_centre = cost_centre
        self.section_unit = section_unit
        self.division_name = division_name
        self.lob_name = lob_name
        self.email = email
        self.phone_no = phone_no
        self.record_status = record_status
        self.last_update_date = last_update_date

        IST = pytz.timezone('Asia/Kuala_Lumpur')
        raw_TS = datetime.now(IST)
        self.date_created = raw_TS

class SystemUser(db.Model):
    system_user_no = db.Column(db.String(16), primary_key=True)
    system_user_role = db.Column(db.String(32))
    bcpra_approval = db.Column(db.String(32))
    is_administrator = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    registered_date = db.Column(db.DateTime)
    last_update_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    system_log = db.relationship("SystemLog", backref="systemuser", lazy=True, cascade="all,delete")
    staffprofile_pers_no = db.Column(db.String(32), db.ForeignKey('StaffProfile.pers_no', ondelete='CASCADE', onupdate="CASCADE"),
                               nullable=False)

    def __init__(self, system_user_no, system_user_role, bcpra_approval, is_administrator, is_active, registered_date):
        self.system_user_no = system_user_no
        self.system_user_role = system_user_role
        self.bcpra_approval = bcpra_approval
        self.is_administrator = is_administrator
        self.is_active = is_active
        self.registered_date = registered_date

        IST = pytz.timezone('Asia/Kuala_Lumpur')
        raw_TS = datetime.now(IST)
        self.date_created = raw_TS

class SystemLog(db.Model):
    log_id = db.Column(db.String(16), primary_key=True)
    transaction_date = db.Column(db.DateTime)
    module = db.Column(db.String(255))
    description = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    system_user_no = db.Column(db.String(32), db.ForeignKey('systemuser.system_user_no', ondelete='CASCADE', onupdate="CASCADE"),
                               nullable=False)

    def __init__(self, log_id, transaction_date, module, description):
        self.log_id = log_id
        self.transaction_date = transaction_date
        self.module = module
        self.description = description

        IST = pytz.timezone('Asia/Kuala_Lumpur')
        raw_TS = datetime.now(IST)
        self.date_created = raw_TS

class HRDataMart(db.Model):
    pers_no = db.Column(db.String(16), primary_key=True)
    staff_no = db.Column(db.String(255))
    staff_name = db.Column(db.String(255))
    designation = db.Column(db.String(16))
    band = db.Column(db.String(16))
    cost_centre = db.Column(db.String(16))
    section_unit = db.Column(db.String(255))
    division_name = db.Column(db.String(255))
    lob_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone_no = db.Column(db.String(16))
    last_update_date = db.Column(db.DateTime)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    staff_profile_hr_data_mart = db.relationship("StaffProfileHRDataMart", backref="hrdatamart", lazy=True,
                                              cascade="all,delete")

    def __init__(self, pers_no, staff_no, staff_name, designation, band, cost_centre, section_unit, division_name,
                 lob_name, email, phone_no, last_update_date):
        self.pers_no = pers_no
        self.staff_no = staff_no
        self.staff_name = staff_name
        self.designation = designation
        self.band = band
        self.cost_centre = cost_centre
        self.section_unit = section_unit
        self.division_name = division_name
        self.lob_name = lob_name
        self.email = email
        self.phone_no = phone_no
        self.last_update_date = last_update_date

        IST = pytz.timezone('Asia/Kuala_Lumpur')
        raw_TS = datetime.now(IST)
        self.date_created = raw_TS

class StaffProfileHRDataMart(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    hrdatamart_pers_no = db.Column(db.String(32), db.ForeignKey('hrdatamart.pers_no', ondelete='CASCADE', onupdate="CASCADE"),
                               nullable=False)
    staffprofile_pers_no = db.Column(db.String(32), db.ForeignKey('staffprofile.pers_no', ondelete='CASCADE', onupdate="CASCADE"),
                               nullable=False)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self):
        self.id = uuid.uuid4().hex

        IST = pytz.timezone('Asia/Kuala_Lumpur')
        raw_TS = datetime.now(IST)
        self.date_created = raw_TS
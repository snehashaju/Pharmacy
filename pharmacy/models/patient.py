from odoo import models, fields,api
from datetime import datetime, date


class PatientInfo(models.Model):
    _name = "patient.patient"

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string="Name", help="Enter the name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date_of_Birth")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
    branch_ids = fields.Many2one('branch.branch', string='Branch')
    location = fields.Char(related='branch_ids.location', string='Location')
    medicine_ids = fields.Many2many('medicine.medicine', string='Medicine')

    @api.onchange('first_name','last_name')
    def onchange_get_name(self):
        if self.first_name and self.last_name:
            self.name = "%s %s" %(self.first_name, self.last_name)

    @api.onchange('date_of_birth')
    def _onchange_dob(self):
        current_date = date.today()
        current_year = current_date.year
        date_of_birth_year = self.date_of_birth.year
        # if self.date_of_birth:
        self.age = current_year - date_of_birth_year

from odoo import models, fields


class PatientInfo(models.Model):
    _name = "patient.patient"

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
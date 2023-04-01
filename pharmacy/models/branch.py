from odoo import models, fields


class BranchInfo(models.Model):
    _name = "branch.branch"

    name = fields.Char(string="Pharmacy Name", help="Enter the name")
    image = fields.Image(string="Image")
    location = fields.Char(string='Location')
    available_staff = fields.Boolean(string='Available Staff')
    staff_ids = fields.Many2one('pharmacy.pharmacy', string='Staff', domain="[('branch_ids', '=', name)]")
    staff_id = fields.One2many('branch.staff', 'branch_id', string='staff')
    color = fields.Integer(string='Color')
    medicine = fields.Many2many('medicine.medicine',string='Medicine')


class BranchStaff(models.Model):
    _name = "branch.staff"

    staff_ids = fields.Many2one('pharmacy.pharmacy', string='Staff', domain="[('branch_ids', '=', branch_id)]")
    branch_id = fields.Many2one('branch.branch', string='Branch')
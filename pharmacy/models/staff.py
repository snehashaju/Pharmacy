from odoo import models, fields, api


class StaffInfo(models.Model):
    _name = "pharmacy.pharmacy"

    name = fields.Char(string="Name", help="Enter the name")
    age = fields.Integer(string="Age")
    date_of_birth = fields.Date(string="Date_of_Birth")
    year = fields.Date(string="Current Date")
    image = fields.Image(string="Image")
    gender = fields.Selection([('female', 'Female'), ('male', 'Male')], 'Gender')
    education = fields.Selection([('dpharm', 'D Pharm'), ('b_pharm', 'B Pharm')],
                                'Education')
    status = fields.Selection([('temporary', 'Temporary'),
                               ('permanent', 'Permanent')],
                              'Status', default='temporary')
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
    branch_ids = fields.Many2one('branch.branch', string='Branch')
    location = fields.Char(related='branch_ids.location', string='Location')
    color = fields.Integer(string='color')

    #
    # @api.onchange('date_of_birth', 'year')
    # def get_age(self):
    #     if self.year and self.date_of_birth:
    #         self.age = self.year - self.date_of_birth




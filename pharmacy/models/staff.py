from odoo import models, fields,api


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
    staff_category = fields.Selection([('temporary', 'Temporary'),
                               ('permanent', 'Permanent')],
                              'staff_category')
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
    branch_ids = fields.Many2one('branch.branch', string='Branch')
    location = fields.Char(related='branch_ids.location', string='Location')
    color = fields.Integer(string='color')

    def set_employee_status(self, vals):
        if vals.get('staff_category') == 'temporary':
            vals['status'] = 'temporary'
        elif vals.get('staff_category') == 'permanent':
            vals['status'] = 'permanent'
        return vals

    def write(self, vals):
        vals = self.set_employee_status(vals)
        res = super(StaffInfo, self).write(vals)
        return res

    @api.model
    def create(self, vals):
        vals['gender'] = 'female'
        return super(StaffInfo, self).create(vals)








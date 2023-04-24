from odoo import models, fields,api
from datetime import datetime, date


class StaffInfo(models.Model):
    _name = "pharmacy.pharmacy"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.onchange('date_of_birth')
    def _onchange_dob(self):
        if self.date_of_birth:
            current_date = date.today()
            current_year = current_date.year
            date_of_birth_year = self.date_of_birth.year
            # if self.date_of_birth:
            self.age = current_year - date_of_birth_year

    @api.depends('number_of_days', 'per_day')
    def compute_amount_total(self):
        for rec in self:
            rec.total_amount = 0
            if rec.number_of_days:
                rec.total_amount = rec.number_of_days * rec.per_day

    @api.model
    def _get_default_user(self):
        return self.env.user.id

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
                              'Status', default='temporary', tracking=True)
    staff_category = fields.Selection([('temporary', 'Temporary'),
                               ('permanent', 'Permanent')],
                              'staff_category')
    phone = fields.Char(string="Phone")
    note = fields.Text(string='Note')
    branch_ids = fields.Many2one('branch.branch', string='Branch')
    location = fields.Char(related='branch_ids.location', string='Location')
    color = fields.Integer(string='color')
    user_id = fields.Many2one('res.users', string="User", default=_get_default_user)
    number_of_days = fields.Integer(string='Number Of Days')
    per_day = fields.Integer(string='Per Day Amount')
    total_amount = fields.Integer(string='Total Amount', compute='compute_amount_total')


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
        vals['note'] = 'New Join'
        vals['per_day'] = 200
        return super(StaffInfo, self).create(vals)











from odoo import models, fields, api


class BranchInfo(models.Model):
    _name = "branch.branch"

    @api.model
    def _get_default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    @api.model
    def _get_default_user_email(self):
        return self.env.user.email

    # @api.model
    # def _get_default_user_language(self):
    #     return self.env.user.Language

    name = fields.Char(string="Pharmacy Name", help="Enter the name")
    image = fields.Image(string="Image")
    location = fields.Char(string='Location')
    available_staff = fields.Boolean(string='Available Staff')
    staff_ids = fields.Many2one('pharmacy.pharmacy', string='Staff', domain="[('branch_ids', '=', name)]")
    staff_id = fields.One2many('branch.staff', 'branch_id', string='staff')
    color = fields.Integer(string='Color')
    medicine = fields.Many2many('medicine.medicine', string='Medicine')
    patient_ids = fields.One2many('patient.details', 'branch_id', string='Patient')
    user_id = fields.Many2one('res.users', string="User", default=_get_default_user)
    user_email = fields.Char('Email', default=_get_default_user_email)
    # user_language = fields.Selection('Language', default=_get_default_user_language)
    total = fields.Float('Total', compute='compute_fees_total')

    @api.depends('patient_ids.payment')
    def compute_fees_total(self):
        fees_total = 0
        for rec in self:
            for patient in rec.patient_ids:
                fees_total += patient.payment
            rec.total = fees_total

    def action_pharmacy_pharmacy(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Staff',
            'view_mode': 'list,form',
            'res_model': 'pharmacy.pharmacy',
            'context': "{}",
            'target': "current"
        }


class BranchStaff(models.Model):
    _name = "branch.staff"

    staff_ids = fields.Many2one('pharmacy.pharmacy', string='Staff', domain="[('branch_ids', '=', branch_id)]")
    branch_id = fields.Many2one('branch.branch', string='Branch')


class PatientDetails(models.Model):
    _name = "patient.details"

    patient_ids = fields.Many2one('patient.patient', string='Patient', domain="[('branch_ids', '=', branch_id)]")
    branch_id = fields.Many2one('branch.branch', string='Branch')
    payment = fields.Integer(string='Payment')


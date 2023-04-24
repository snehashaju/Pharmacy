from odoo import fields, models
from odoo.exceptions import ValidationError


class MedicineWizard(models.Model):
    _name = 'medicine.wizard'

    starting_date = fields.Date(string="Start Date")
    exp_date = fields.Date(string="EXP Date")
    # branch_ids = fields.Many2many('branch.branch', string='Branch')
    branch_ids = fields.One2many('medicine.exp','branch_id',string='Branch')


    def create_medicine(self):
        medicine_id = self.env.context.get('active_id')
        print('workiderrrrrrrrrrrrrr', medicine_id)
        update_medicine = self.env['medicine.medicine'].browse(medicine_id)
        vals = {
            'starting_date': self.starting_date,
            'exp_date': self.exp_date
        }
        update_medicine.write(vals)
        # payment = self.env['medicine.medicine'].create({
        #     'starting_date': self.starting_date,
        #     'exp_date': self.exp_date,
        # })


class MedicineBranch(models.Model):
    _name = 'medicine.exp'

    branch_id = fields.Many2one('branch.branch', string='Branch')
    medicine_id = fields.Many2one('medicine.medicine', string='Medicine')







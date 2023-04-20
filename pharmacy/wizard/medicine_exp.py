from odoo import fields, models


class MedicineWizard(models.Model):
    _name = 'medicine.wizard'

    starting_date = fields.Date(string="Start Date")
    exp_date = fields.Date(string="EXP Date")

    def create_medicine(self):
        medicine_id = self.env.context.get('active_id')
        print('workiderrrrrrrrrrrrrr', medicine_id)
        pass

from odoo import models, fields


class BranchInfo(models.Model):
    _name = "medicine.medicine"

    name = fields.Char(string="Medicine Name", help="Enter the name")
    image = fields.Image(string="Image")
    delivery_date = fields.Datetime(string="Delivery Date")




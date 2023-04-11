from odoo import fields, models


class Purchase(models.Model):
    _inherit = 'purchase.order'


    branch_id = fields.Many2one('branch.branch', string='Branch')


class PurchaseLine(models.Model):
    _inherit = 'purchase.order.line'

    line_number = fields.Integer(string='Line Number')
    branch_id = fields.Many2one('branch.branch', string='Branch')

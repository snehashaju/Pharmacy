from odoo import fields, models, api


class Purchase(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.price_total', 'payment')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                line._compute_amount()
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            currency = order.currency_id or order.partner_id.property_purchase_currency_id or self.env.company.currency_id
            order.update({
                'amount_untaxed': currency.round(amount_untaxed),
                'amount_tax': currency.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
                'total_amount': amount_untaxed + amount_tax + order.payment
            })


    branch_id = fields.Many2one('branch.branch', string='Branch')
    payment = fields.Integer(string='Payment')
    total_amount = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all')


class PurchaseLine(models.Model):
    _inherit = 'purchase.order.line'

    line_number = fields.Integer(string='Line Number')
    branch_id = fields.Many2one('branch.branch', string='Branch')



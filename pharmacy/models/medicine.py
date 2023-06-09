from odoo import models, fields, api


class BranchInfo(models.Model):
    _name = "medicine.medicine"

    @api.model
    def _get_default_user(self):
        return self.env.context.get('user_id', self.env.user.id)

    def action_test(self):
        return{
            'effect': {
                'fadeout': 'slow',
                'message': 'Click Successfull',
                'type': 'rainbow_man'
            }
        }
    def action_website(self):
        return{
                'target': 'new',
                'url': 'https://www.odoo.com/app/point-of-sale-shop',
                'type': 'ir.actions.act_url'
        }

    def action_done(self):
        for rec in self:
            rec.status = 'available'

    name = fields.Char(string="Medicine Name", help="Enter the name")
    image = fields.Image(string="Image")
    delivery_date = fields.Datetime(string="Delivery Date")
    status = fields.Selection([
        ('available', 'Available'),
        ('unavailable', 'Unavailable')],
        'Status', default='available')
    user_id = fields.Many2one('res.users', string="User", default=_get_default_user)
    starting_date = fields.Date(string="Start Date")
    exp_date = fields.Date(string="EXP Date")











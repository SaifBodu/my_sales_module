from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_subtotal = fields.Float(string='Custom Subtotal', compute='_compute_custom_subtotal', store=True)

    @api.depends('order_line.quantity', 'order_line.price_unit')
    def _compute_custom_subtotal(self):
        for order in self:
            order.custom_subtotal = sum(line.quantity * line.price_unit for line in order.order_line)

# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Quotation(models.Model):
    _name = 'vn.quotation'
    _description = 'Vendor Quotation'
    _inherit = ['mail.thread']

    name = fields.Char(string='Quotation Reference', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    rfq_id = fields.Many2one('vn.rfq', string='RFQ', required=True, ondelete='cascade')
    vendor_id = fields.Many2one('vn.vendor', string='Vendor', required=True)
    unit_price = fields.Float(string='Unit Price', required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    delivery_days = fields.Integer(string='Delivery Days')
    notes = fields.Text(string='Notes')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total', store=True)
    validity_date = fields.Date(string='Valid Until')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('selected', 'Selected'),
        ('rejected', 'Not Selected'),
    ], default='draft', tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('vn.quotation') or _('New')
        return super().create(vals_list)

    @api.depends('unit_price', 'quantity')
    def _compute_total(self):
        for rec in self:
            rec.total_amount = rec.unit_price * rec.quantity

    def action_submit(self):
        self.state = 'submitted'
        self.rfq_id.state = 'received'

    def action_select(self):
        self.state = 'selected'
        # reject all other quotations for same RFQ
        others = self.rfq_id.quotation_ids.filtered(lambda q: q.id != self.id)
        others.write({'state': 'rejected'})
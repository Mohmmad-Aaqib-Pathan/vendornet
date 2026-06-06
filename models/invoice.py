# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Invoice(models.Model):
    _name = 'vn.invoice'
    _description = 'Procurement Invoice'
    _inherit = ['mail.thread']

    name = fields.Char(string='Invoice Reference', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    po_id = fields.Many2one('vn.purchase.order', string='Purchase Order')
    vendor_id = fields.Many2one('vn.vendor', string='Vendor', required=True)
    invoice_date = fields.Date(string='Invoice Date', default=fields.Date.today)
    due_date = fields.Date(string='Due Date')
    amount_total = fields.Float(string='Total Amount', required=True)
    tax_amount = fields.Float(string='Tax Amount')
    grand_total = fields.Float(string='Grand Total', compute='_compute_grand_total', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True)
    notes = fields.Text(string='Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('vn.invoice') or _('New')
        return super().create(vals_list)

    @api.depends('amount_total', 'tax_amount')
    def _compute_grand_total(self):
        for rec in self:
            rec.grand_total = rec.amount_total + rec.tax_amount

    def action_confirm(self):
        self.state = 'confirmed'

    def action_paid(self):
        self.state = 'paid'

    def action_cancel(self):
        self.state = 'cancelled'
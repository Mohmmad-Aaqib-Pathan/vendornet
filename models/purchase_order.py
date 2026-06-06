# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _name = 'vn.purchase.order'
    _description = 'Purchase Order'
    _inherit = ['mail.thread']

    name = fields.Char(string='PO Reference', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    rfq_id = fields.Many2one('vn.rfq', string='RFQ')
    quotation_id = fields.Many2one('vn.quotation', string='Quotation')
    vendor_id = fields.Many2one('vn.vendor', string='Vendor', required=True)
    order_date = fields.Date(string='Order Date', default=fields.Date.today)
    delivery_date = fields.Date(string='Expected Delivery')
    amount_total = fields.Float(string='Total Amount', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], default='draft', tracking=True)
    notes = fields.Text(string='Notes')
    invoice_ids = fields.One2many('vn.invoice', 'po_id', string='Invoices')
    invoice_count = fields.Integer(compute='_compute_invoice_count')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('vn.po') or _('New')
        return super().create(vals_list)

    def _compute_invoice_count(self):
        for rec in self:
            rec.invoice_count = len(rec.invoice_ids)

    def action_confirm(self):
        self.state = 'confirmed'
        self.rfq_id.state = 'po_created'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancelled'

    def action_create_invoice(self):
        invoice = self.env['vn.invoice'].create({
            'po_id': self.id,
            'vendor_id': self.vendor_id.id,
            'amount_total': self.amount_total,
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'vn.invoice',
            'res_id': invoice.id,
            'view_mode': 'form',
        }
    
    def action_view_invoices(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Invoices',
        'res_model': 'vn.invoice',
        'view_mode': 'list,form',
        'domain': [('po_id', '=', self.id)],
        }
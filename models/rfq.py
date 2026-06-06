# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class RFQ(models.Model):
    _name = 'vn.rfq'
    _description = 'Request for Quotation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='RFQ Reference', required=True, copy=False,
                       readonly=True, default=lambda self: _('New'))
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline', required=True)
    vendor_id = fields.Many2one('vn.vendor', string='Vendor', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('received', 'Quotation Received'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('po_created', 'PO Created'),
    ], default='draft', tracking=True, string='Status')
    quotation_ids = fields.One2many('vn.quotation', 'rfq_id', string='Quotations')
    quotation_count = fields.Integer(compute='_compute_quotation_count')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('vn.rfq') or _('New')
        return super().create(vals_list)

    def _compute_quotation_count(self):
        for rec in self:
            rec.quotation_count = len(rec.quotation_ids)

    def action_send(self):
        self.state = 'sent'

    def action_approve(self):
        self.state = 'approved'

    def action_reject(self):
        self.state = 'rejected'

    def action_reset(self):
        self.state = 'draft'
    
    def action_view_quotations(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Quotations',
        'res_model': 'vn.quotation',
        'view_mode': 'list,form',
        'domain': [('rfq_id', '=', self.id)],
        }
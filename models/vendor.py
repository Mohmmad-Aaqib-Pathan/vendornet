# -*- coding: utf-8 -*-
from odoo import fields, models

class Vendor(models.Model):
    _name = 'vn.vendor'
    _description = 'Vendor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Vendor Name', required=True, tracking=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    gst_number = fields.Char(string='GST Number')
    address = fields.Text(string='Address')
    category = fields.Selection([
        ('goods', 'Goods Supplier'),
        ('services', 'Service Provider'),
        ('both', 'Goods & Services'),
    ], string='Category', default='goods')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('blacklisted', 'Blacklisted'),
    ], string='Status', default='active', tracking=True)
    rating = fields.Float(string='Rating', digits=(2, 1))
    rfq_ids = fields.One2many('vn.rfq', 'vendor_id', string='RFQs')
    rfq_count = fields.Integer(compute='_compute_rfq_count', string='RFQ Count')

    def _compute_rfq_count(self):
        for rec in self:
            rec.rfq_count = len(rec.rfq_ids)
    
    def action_view_rfqs(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'RFQs',
        'res_model': 'vn.rfq',
        'view_mode': 'list,form',
        'domain': [('vendor_id', '=', self.id)],
        }
# -*- coding: utf-8 -*-
{
    'name': 'VendorNet',
    'version': '17.0.1.0.0',
    'summary': 'Procurement and Vendor Management ERP',
    'author': 'Aaqib Pathan',
    'category': 'Purchases',
    'depends': ['base', 'mail', 'purchase', 'account'],
    'data': [
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/vendor_views.xml',
        'views/rfq_views.xml',
        'views/quotation_views.xml',
        'views/purchase_order_views.xml',
        'views/invoice_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
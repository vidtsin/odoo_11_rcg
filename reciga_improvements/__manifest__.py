###############################################################################
# Copyright(c): 2019 Asigal, S.L. (<https://libreinnova.com/>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
# All Rights Reserved
###############################################################################
{
    'name': 'Reciga improvements',
    'version': '1.0',
    'summary': 'Different improvements for Reciga odoo ERP',
    'description': '',
    'category': 'Accounting',
    'author': 'Asigal, S.L.',
    'website': 'https://libreinnova.com/',
    'images': [
        'static/description/icon.png'
    ],
    'depends': [
        'product_barcode',
        'stock'
    ],
    'data': [
        'data/paperformat.xml',
        'views/barcode.xml',
        'views/external_layout.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

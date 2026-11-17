# -*- coding: utf-8 -*-
{
    'name': "Barcode Extension",

    'summary': "Display the last seven barcode characters in the product variant list",

    'description': """
Display a stored, computed short barcode in the product variant tree view
without changing the original product barcode.
    """,

    'author': "KIO",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '17.0.1.1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'product',
        'stock',
        'kio_inventory_product_extension',
    ],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'installable': True,
    'license': 'LGPL-3',
}


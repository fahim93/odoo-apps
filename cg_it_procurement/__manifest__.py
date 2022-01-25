# -*- coding: utf-8 -*-
{
    'name': "IT Procurement",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fahimul Islam",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase', 'stock', 'web_digital_sign'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/purchase_security.xml',
        'views/purchase_order_view.xml',
        'report/purchase_order_report_template.xml',
        'report/purchase_reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}

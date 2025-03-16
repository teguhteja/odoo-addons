# -*- coding: utf-8 -*-
{
    'name': "Open Academy Website",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "IB Teguh TM",
    'website': "https://www.teguhteja.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/class_templates.xml',
        'views/website_pages.xml',
        'views/website_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
}


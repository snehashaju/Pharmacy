# -*- coding: utf-8 -*-
{
    'name': "Pharmacy",
    'author': "Sneha",
    'version': '0.1',
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/branch_view.xml',
        'views/staff_views.xml',
        'views/patient_view.xml',
        'views/medicine_view.xml',
        'views/purchase_views.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
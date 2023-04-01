# -*- coding: utf-8 -*-
{
    'name': "Pharmacy",
    'author': "Sneha",
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/branch_view.xml',
        'views/staff_views.xml',
        'views/patient_view.xml',
        'views/medicine_view.xml'

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
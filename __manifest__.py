{
    'name': 'My Sales Module',
    'version': '1.0',
    'author': 'Saif',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'views/sale_order_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

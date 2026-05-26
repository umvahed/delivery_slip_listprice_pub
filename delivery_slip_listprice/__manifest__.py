# -*- coding: utf-8 -*-
{
    'name': 'Delivery Slip List Price',
    'version': '18.0.1.0.0',
    'summary': 'Adds a List Price column and Grand Total to the Delivery Slip report',
    'description': """
Extends the standard Odoo 18 Delivery Slip (stock transfer report) to display the
product **list price** (public selling price) and a **Grand Total** row.

Covers all three table variants that appear on a delivery slip:

- **Aggregated moves** — products without serial/lot tracking
- **Serial-tracked moves** — products tracked by serial number
- **Done moves** — validated transfer quantities + grand total footer

No Python code — pure QWeb template inheritance. Zero performance impact.
Compatible with Odoo 18 Community and Enterprise.

Related module: **Delivery Slip Unit Cost** (shows cost price instead).
    """,
    'author': 'Bitquanta',
    'website': 'https://sebenz.co.za',
    'support': 'support@sebenz.co.za',
    'category': 'Inventory/Reporting',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'report/report_deliveryslip_listprice.xml',
    ],
    'images': ['static/description/banner.png'],
    'price': 0,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}

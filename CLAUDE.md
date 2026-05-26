# delivery_slip_listprice

Odoo 18 module that extends the standard Delivery Slip report to show the **list price** (public selling price, `product.list_price`) and a **Grand Total** across all three table variants on a delivery slip.

## Publisher
- Author: Bitquanta
- Website: https://sebenz.co.za
- Support: support@sebenz.co.za
- License: LGPL-3

## Structure

```
delivery_slip_listprice_pub/
├── README.md                              # Repo-level docs (GitHub)
└── delivery_slip_listprice/
    ├── __manifest__.py
    ├── __init__.py
    ├── LICENSE
    ├── report/
    │   └── report_deliveryslip_listprice.xml  # Four XPath overrides (priority=300)
    ├── doc/
    │   └── index.rst                      # Odoo store documentation
    └── static/description/
        ├── index.html                     # Store listing page
        ├── icon.png                       # MISSING — needs to be added (128×128 PNG)
        └── banner.png                     # MISSING — needs to be added
```

## Key Design Decisions

- Pure QWeb — zero Python, no model changes.
- Four templates with `priority="300"` cover: aggregated moves, serial-tracked moves, done moves, and grand total.
- Uses `product.list_price` (pricelist-independent public price), not sale order price.
- Companion module: `delivery_slip` (shows cost price instead).

## Dependencies
- `stock`

## Status
- [x] Manifest placeholders filled in
- [x] README.md + doc/index.rst written
- [ ] icon.png needed at `static/description/icon.png`
- [ ] banner.png needed at `static/description/banner.png`
- [ ] Screenshots needed (add to `static/description/` and list in manifest `images`)

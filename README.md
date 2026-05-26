# Delivery Slip – List Price & Totals

Odoo 18 module — extends the standard Delivery Slip report to show the **list price** (public selling price) of each product and a **Grand Total** row, across all three table variants that can appear on a delivery slip.

## Features

- **List Price column** — shows `product.list_price` (the pricelist-independent public price) next to each move line
- **Grand Total** — sums `list_price × qty_done` across all lines
- Covers all three delivery slip table types:
  - Aggregated moves (products without serial/lot tracking)
  - Serial-tracked moves (products tracked by serial number)
  - Done moves with grand total footer
- Zero Python — four XPath overrides with `priority="300"`
- Compatible with Odoo 18 Community and Enterprise

## Requirements

| Dependency | Notes |
|---|---|
| `stock` | Odoo Inventory module (standard) |
| Odoo version | 18.0 |

## Installation

1. Copy the `delivery_slip_listprice` folder into your Odoo addons path.
2. Restart the Odoo server.
3. Go to **Apps → Update Apps List**.
4. Search for **Delivery Slip – List Price & Totals** and click **Install**.

## Usage

No configuration required. Once installed, every printed Delivery Slip will automatically include a **Unit Price** column and a **Grand Total** row.

To print a delivery slip: open a stock transfer and click **Print → Delivery Slip**.

## Related module

Looking for **cost price** instead of selling price? See the companion module **Delivery Slip – Unit Cost & Totals** (`delivery_slip`).

## License

LGPL-3 — see [delivery_slip_listprice/LICENSE](delivery_slip_listprice/LICENSE).

## Support

support@sebenz.co.za

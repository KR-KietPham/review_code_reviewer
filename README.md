# Order Review Lab

A small Python project for testing read-only PR reviews. All data in this repository is synthetic.

- **Totals:** Sum integer unit prices in cents times integer quantities. A price of zero is valid. Negative prices, nonpositive quantities, and non-integer inputs are rejected for the whole order. Empty orders return zero.
- **Customer summary:** Return only `order_id` and `total_cents`. Internal test annotations are reserved for back-office records.
- **Product aggregation:** Return total quantity by SKU. Traverse the input rows once with dictionary updates. A batch may contain 10,000 distinct SKUs and repeated rows.

Run the baseline tests with `python -m unittest discover -s tests -v` from the repository root.

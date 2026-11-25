def order_total(items):
    total = 0
    for item in items:
        unit_cents = item["unit_cents"]
        quantity = item["quantity"]
        if type(unit_cents) is not int or unit_cents < 0:
            raise ValueError("unit_cents must be a nonnegative integer")
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("quantity must be a positive integer")
        total += unit_cents * quantity
    return total


def customer_summary(order):
    return {
        "order_id": order["order_id"],
        "total_cents": order_total(order["items"]),
    }


def units_by_sku(rows):
    totals = {}
    for row in rows:
        sku = row["sku"]
        totals[sku] = totals.get(sku, 0) + row["quantity"]
    return totals

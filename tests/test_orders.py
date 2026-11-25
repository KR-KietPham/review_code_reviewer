import unittest

from orders import customer_summary, order_total, units_by_sku


class OrderTotalTests(unittest.TestCase):
    def test_empty_and_gift_orders(self):
        self.assertEqual(order_total([]), 0)
        self.assertEqual(order_total([{"unit_cents": 0, "quantity": 2}]), 0)

    def test_sums_multiple_items(self):
        self.assertEqual(
            order_total([
                {"unit_cents": 150, "quantity": 2},
                {"unit_cents": 80, "quantity": 1},
            ]),
            380,
        )

    def test_rejects_invalid_item_even_after_a_valid_item(self):
        for price, quantity in [(-100, 2), (150, 0), (150, -1), (150, 1.5)]:
            with self.subTest(price=price, quantity=quantity):
                with self.assertRaises(ValueError):
                    order_total([
                        {"unit_cents": 150, "quantity": 2},
                        {"unit_cents": price, "quantity": quantity},
                    ])


class CustomerSummaryTests(unittest.TestCase):
    def test_output_has_only_customer_fields(self):
        order = {
            "order_id": "demo-order",
            "items": [{"unit_cents": 150, "quantity": 2}],
            "internal_note": "SYNTHETIC TEST ANNOTATION",
        }
        self.assertEqual(
            customer_summary(order),
            {"order_id": "demo-order", "total_cents": 300},
        )


class ProductAggregationTests(unittest.TestCase):
    def test_aggregates_repeated_skus(self):
        self.assertEqual(
            units_by_sku([
                {"sku": "demo-A", "quantity": 2},
                {"sku": "demo-B", "quantity": 1},
                {"sku": "demo-A", "quantity": 3},
            ]),
            {"demo-A": 5, "demo-B": 1},
        )

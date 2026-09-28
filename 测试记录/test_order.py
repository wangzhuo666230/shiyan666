# -*- coding: utf-8 -*-
"""订单模块单元测试。运行：python -m unittest 测试记录/test_order.py"""

import unittest

import sys
sys.path.insert(0, "源代码")

from order import Order


class OrderTest(unittest.TestCase):

    def test_total_quantity(self):
        o = Order("A001", {"咖啡": 2, "牛奶": 1})
        self.assertEqual(o.total_quantity(), 3)

    def test_total_price(self):
        o = Order("A001", {"咖啡": 2, "牛奶": 1})
        self.assertEqual(o.total_price({"咖啡": 18, "牛奶": 6}), 42)

    def test_empty_items(self):
        o = Order("A000", {})
        self.assertEqual(o.total_quantity(), 0)


if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
"""订单模块：Order 数据模型与基础操作。"""


class Order:
    """订单对象，包含订单编号和商品条目。"""

    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items  # 形如 {"商品名": 数量}

    def total_quantity(self):
        """返回商品总数量。"""
        return sum(self.items.values())

    def total_price(self, price_map):
        """根据单价表计算订单总价。

        price_map: {"商品名": 单价}
        """
        return sum(qty * price_map.get(name, 0) for name, qty in self.items.items())


if __name__ == "__main__":
    o = Order("A001", {"咖啡": 2, "牛奶": 1})
    print("总数量:", o.total_quantity())
    print("总价:", o.total_price({"咖啡": 18, "牛奶": 6}))

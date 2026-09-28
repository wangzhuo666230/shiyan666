# -*- coding: utf-8 -*-
"""报修工单模块单元测试。运行：python -m unittest 测试记录/test_order.py"""

import unittest

import sys
sys.path.insert(0, "源代码")

from order import RepairTicket


class RepairTicketTest(unittest.TestCase):

    def test_priority_default(self):
        t = RepairTicket("T001", "投影仪", "画面闪烁", "张老师")
        self.assertEqual(t.priority, "中")

    def test_escalate(self):
        t = RepairTicket("T001", "投影仪", "画面闪烁", "张老师")
        t.escalate()
        self.assertEqual(t.priority, "高")

    def test_invalid_priority(self):
        t = RepairTicket("T001", "投影仪", "画面闪烁", "张老师")
        t.set_priority("极高")
        self.assertEqual(t.priority, "中")

    def test_close(self):
        t = RepairTicket("T001", "投影仪", "画面闪烁", "张老师")
        t.close()
        self.assertEqual(t.status, "已完成")


if __name__ == "__main__":
    unittest.main()

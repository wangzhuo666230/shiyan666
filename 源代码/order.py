# -*- coding: utf-8 -*-
"""报修工单模块：设备故障报修工单的数据模型与基础操作。"""


class RepairTicket:
    """设备报修工单对象。"""

    PRIORITIES = {"低": 1, "中": 2, "高": 3, "紧急": 4}
    _ORDER = ["低", "中", "高", "紧急"]

    def __init__(self, ticket_id, device, fault_desc, reporter):
        self.ticket_id = ticket_id      # 工单编号
        self.device = device            # 设备名称
        self.fault_desc = fault_desc    # 故障描述
        self.reporter = reporter        # 报修人
        self.priority = "中"            # 紧急程度（默认中）
        self.status = "待派单"          # 状态：待派单/维修中/已完成

    def set_priority(self, level):
        """设置紧急程度，仅接受合法级别。"""
        if level in self.PRIORITIES:
            self.priority = level

    def escalate(self):
        """紧急程度自动升一级。"""
        if self.priority != "紧急":
            self.set_priority(self._ORDER[self._ORDER.index(self.priority) + 1])

    def close(self):
        """标记工单完成。"""
        self.status = "已完成"


if __name__ == "__main__":
    t = RepairTicket("T001", "投影仪", "画面闪烁无法正常显示", "张老师")
    t.escalate()
    print("工单:", t.ticket_id, t.device, "| 优先级:", t.priority, "| 状态:", t.status)

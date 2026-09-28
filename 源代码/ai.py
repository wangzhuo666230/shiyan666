# -*- coding: utf-8 -*-
"""AI 智能工单模块：基于故障描述自动分级并给出维修建议。"""


KEYWORDS = {
    "紧急": ["火灾", "断电", "漏电", "冒烟", "爆炸"],
    "高": ["无法开机", "无法使用", "完全不能", "蓝屏", "损坏", "无法正常"],
    "中": ["故障", "异常", "卡顿", "报错", "失灵", "闪烁", "不清晰"],
}


def classify(fault_desc):
    """根据故障描述中的关键词自动判断紧急程度。"""
    for level, words in KEYWORDS.items():
        for w in words:
            if w in fault_desc:
                return level
    return "低"


def suggest(fault_desc):
    """根据故障描述给出初步维修建议。"""
    if any(w in fault_desc for w in ["投影", "屏幕", "显示"]):
        return "检查信号线与显示接口，尝试重启设备"
    if any(w in fault_desc for w in ["网络", "无法联网", "断网"]):
        return "重启路由器，检查网线/无线连接"
    return "联系设备管理员上门检修"


if __name__ == "__main__":
    desc = "投影仪画面闪烁，无法正常显示"
    print("紧急程度分级:", classify(desc))
    print("维修建议:", suggest(desc))

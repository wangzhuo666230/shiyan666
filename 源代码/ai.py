# -*- coding: utf-8 -*-
"""AI 推荐模块：基于历史订单做简单的商品推荐。"""

from collections import Counter


def recommend(items, top_n=3):
    """根据商品出现次数推荐热门商品，返回前 top_n 个。

    items: 所有历史订单中的商品名列表。
    """
    counter = Counter(items)
    return [name for name, _ in counter.most_common(top_n)]


def personalize(user_items, all_items, top_n=3):
    """给单个用户推荐：优先该用户没买过的热门商品。"""
    hot = recommend(all_items, top_n=10)
    bought = set(user_items)
    return [name for name in hot if name not in bought][:top_n]


if __name__ == "__main__":
    history = ["咖啡", "牛奶", "咖啡", "面包", "牛奶", "咖啡"]
    print("热门推荐:", recommend(history))
    print("个性化:", personalize(["咖啡"], history))

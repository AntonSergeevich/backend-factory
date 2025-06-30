# core/utils.py
from collections import deque
from .models import Factory, Unit, Equipment

def get_all_parents(obj):
    parents = []
    queue = deque([obj])
    while queue:
        cur = queue.popleft()
        if isinstance(cur, Equipment):
            for u in cur.units.all():
                parents.append(u)
                queue.append(u)
        elif isinstance(cur, Unit):
            f = cur.factory
            if f:
                parents.append(f)
                queue.append(f)
        # Factory — нет родителя
    return parents

def get_all_children(obj):
    children = []
    queue = deque([obj])
    while queue:
        cur = queue.popleft()
        if isinstance(cur, Factory):
            for u in cur.units.all():
                children.append(u)
                queue.append(u)
        elif isinstance(cur, Unit):
            for e in cur.equipment.all():
                children.append(e)
                queue.append(e)
        # Equipment — нет детей
    return children

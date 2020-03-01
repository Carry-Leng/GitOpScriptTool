# -*- coding: UTF-8 -*-

"""
Authors: Carry·Leng

Date: 2020/03/01 18:13:00
"""

def isEmpty(text):
    if text is None:
        return True
    if isinstance(text, str):
        if text.strip():
            return False
        else:
            return True
    return False

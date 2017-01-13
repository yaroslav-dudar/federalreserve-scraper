# -*- coding: utf-8 -*-


def base_serialzier(value):
    if value:
        return value[0].strip().encode('utf-8')
    return ''

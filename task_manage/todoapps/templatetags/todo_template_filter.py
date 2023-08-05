"""
Djangoのカスタムテンプレートフィルターです。
以下のケースで使用します。

- "to_date"：日時オブジェクトを文字列に変換します。
- "to_string"：任意のデータを文字列に変換します。

"""

from django import template
from datetime import datetime

register = template.Library()

@register.filter
def to_date(value):
    """日付オブジェクトを文字列に変換します。"""
    if isinstance(value, datetime):
        return f"{value:%Y-%m-%d}"
    return value

@register.filter
def to_string(value):
    """任意の値を文字列に変換します。"""
    return str(value)
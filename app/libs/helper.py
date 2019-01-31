"""
Created by Oort on 2018/12/6 2:49 PM.
"""

__author__ = 'Oort'


def is_isbn_or_key(word):
    """
    判断字符串是isbn还是查询关键字
    """
    isbn_or_key = 'key'
    # .isdigit()返回字符串是否为纯数字
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/26 11:18
# @Author  : haoxu
# @File    : data_process.py
# @Software: PyCharm
import ast
import os


def shift_json_to_text(file_path: str):
    json_data = [
        ast.literal_eval(row).text + "\t" + str(0) if ast.literal_eval(row).label == "other" else ast.literal_eval(
            row).text + "\t" + str(1) for row in
        open(file_path, "r")]

    os.path.splitext()


if __name__ == '__main__':
    print(os.path.dirname("/haoxuge/haoge.text"))
    print(os.path.splitext("/haoxuge/haoge.text"))

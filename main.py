#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    main.py 'a experiment script for KS research'
    Copyright (C) 2021, Wei Zi-qian

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.



    If you find it useful in your research, please consider citing.

    @misc{weiziqian1996,
        author = {Wei, Z.},
        title = {KS_tasks},
        year = 2021,
        version = {1.0},
        publisher = {Github},
        url = {https://github.com/weiziqian1996/KS_task}
    }
"""

from settings import *
from components import *
from functions import *
from cmap_task import *
from writing_task import *
from reading_task import *
from instruction_page import *

for i in [1, 2, 4, 'r', 5, 6, 7, 'c', 10]:
    if type(i) == int:
        run_instruction_page(i)
    elif i == 'r':
        run_reading_task()
    elif i == 'c':
        run_cmap_task()
    elif i == 'w':
        run_writing_task()
    show_interval(wait_secs=0.5)

win.close()
print('不要管上面那些WARNING，如果你看到这行文字，说明程序已经顺利运行并结束了')

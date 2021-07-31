#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    writing_task.py 'a experiment script for KS research'
    Copyright (C) 2020, Wei Zi-qian

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
        year = 2020,
        version = {1.0},
        publisher = {Github},
        url = {https://github.com/weiziqian1996/KS_task}
    }
"""
import win32con
from psychopy import visual, event
from psychopy.hardware import keyboard
import re
import win32api

keyterms = ['蜜蜂', '养蜂人', '蜂蜜', '科学家', '采蜜', '冬天', '疫情', '农药',
            '花田', '太阳', '8字形', '震动', '腹部', '果树', '全球气候变暖', '授粉']
window_size = [1000, 800]
linefeed = 29
text_color = 'white'
click_color = [0, 0, 0]

# Setup the Window
win = visual.Window(
    size=window_size, fullscr=False, screen=0,
    winType='pyglet', allowGUI=True, allowStencil=False, color=[-1, -1, -1], colorSpace='rgb',
    units='pix')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
textbox = visual.TextBox2(
    win, text='蜜蜂帮助果树授粉，给养蜂人带来蜂蜜，是人类的好朋友', font='Microsoft YaHei',
    pos=(0, -50), letterHeight=20.0,
    size=(600, 400), borderWidth=2.0,
    color=text_color, colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor='black', borderColor='white',
    flipHoriz=False, flipVert=False,
    editable=True,
    name='textbox',
    autoLog=True
)

button = visual.ButtonStim(
    win=win,
    text='点击继续', font='Microsoft YaHei',
    size=[150, 50], borderWidth=2,
    fillColor='black', borderColor=text_color,
    color=text_color, colorSpace='rgb',
    opacity=1,
    bold=True,
    padding=None,
    anchor='center',
    name='button')
button.pos = [window_size[0]/2-button.size[0]/2,
              -window_size[1]/2+button.size[1]/2]
button.setAutoDraw(True)

title = visual.TextStim(
    win=win,
    text='关键词列表（灰色为已经使用的关键词）',
    font='Microsoft YaHei',
    color=text_color,
    pos=[0, window_size[1]/2-50])
text_list = []

text_pos = [-300, window_size[1]/2-100]
for i in range(0, len(keyterms)):

    text_list.append(visual.TextStim(
        win=win,
        text=keyterms[i],
        opacity=1,
        font='Microsoft YaHei',
        pos=text_pos)
    )
    if i in [3, 7, 11]:
        text_pos[1] -= 25
        text_pos[0] = -300
    else:
        text_pos[0] += 200

punctuation = '!,;:?"\'、，；.。：’”'


def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip()


count = visual.TextStim(
        win=win,
        text='字数统计：0',
        opacity=1,
        font='Microsoft YaHei',
        color=text_color,
        pos=[0, -window_size[1]/2+100])

textlength = len(textbox.text)

continueRoutine = True
# -------Run Routine "trial"-------
while continueRoutine:

    title.draw()
    button.draw()

    textbox.setAutoDraw(True)  # textbox updates

    for term in keyterms:
        if term in textbox.text:
            text_list[keyterms.index(term)].color = [0, 0, 0]
        else:
            text_list[keyterms.index(term)].color = text_color

    # auto linefeed function
    if textlength != len(textbox.text):
        for i in range(0, len(textbox.text)):
            if i != 0 and i % linefeed == 0 and textbox.text[i] != '\n':
                textbox.text = textbox.text[0:i] + '\n' + textbox.text[i:]

                # press key 'End' twice to relocate the input position
                win32api.keybd_event(35, 0, 0, 0)
                win32api.keybd_event(35, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(35, 0, 0, 0)
                win32api.keybd_event(35, 0, win32con.KEYEVENTF_KEYUP, 0)

    for text in text_list:
        text.draw()

    print(type(textbox.text))
    words = removePunctuation(textbox.text)
    print(words)
    print(len(words))
    count.text = '字数统计：{}'.format(len(words))
    count.draw()

    win.flip()

    key = event.getKeys()
    if len(key) != 0:
        if key[0] == 'escape':
            win.close()

    # click to continue when all key-terms were used
    if button.isClicked:
        complete = 0
        for term in keyterms:
            if term in textbox.text:
                complete += 1
        if complete == len(keyterms):
            win.color = 'green'
            win.flip()


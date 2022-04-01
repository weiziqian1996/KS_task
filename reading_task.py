#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    reading_task.py 'a experiment script for KS research'
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

from psychopy.visual import Window, TextBox2, ButtonStim
from psychopy.event import Mouse, getKeys
from psychopy.core import getTime
from psychopy.gui import DlgFromDict, Dlg
from settings import *
from components import *
from functions import *


def run_reading_task():

    action_reading = []
    timestamp_reading = []

    reading = True
    textbox.text = '点击按钮呈现文章'  # the initial introduction on the textbox
    current_text = None
    current_paraph = 1

    title.text = '阅读任务'
    title.setAutoDraw(True)
    timer.setAutoDraw(True)
    prompt_title.setAutoDraw(True)

    prompt.text = mask_text([prompt_text_reading], 0)
    prompt.setAutoDraw(True)

    button_continue.setAutoDraw(True)

    for button in button_switch:
        button.text = button_switch_text_reading[button_switch.index(button)]
        button.setAutoDraw(True)

    textbox.setAutoDraw(True)

    prompt_x = (290, 690)
    prompt_y = (-300, 300)

    for i in range(0, len(aoi)):
        aoi[i].setAutoDraw(True)

    # prompt, p1, p2, p3, p4, p5
    read_prompt = False
    last_switch = None  # last switch action using mouse

    t0 = getTime()
    action_reading.append('beginning task')
    timestamp_reading.append(t0)

    while reading:

        if current_text is not None:
            for i in range(0, len(aoi)):
                aoi[i].height = aoi_height[current_text][i]
                aoi[i].pos = aoi_pos[current_text][i]

        # show the prompt only when mouse is pressed in the prompt button
        if mouse.getPos()[0] in range(prompt_x[0], prompt_x[1]) and mouse.getPos()[1] in range(prompt_y[0], prompt_y[1]):
            prompt.text = prompt_text_reading
            if not read_prompt:
                # data record
                if last_switch is None:
                    # print('switch to read prompt', getTime())
                    action_reading.append('switch to prompt')
                    timestamp_reading.append(getTime())
                    last_switch = 'prompt'
                elif last_switch is not None and last_switch != 'prompt':
                    # print('switch to read prompt', getTime())
                    action_reading.append('switch to prompt')
                    timestamp_reading.append(getTime())
                    last_switch = 'prompt'

                if current_text is not None:
                    content = [texts[current_text][0]]
                    for ii in range(1, len(texts[current_text])):
                        content.append(mask_text([texts[current_text][ii]], 0))
                    textbox.text = ''.join(content)
        else:
            prompt.text = mask_text([prompt_text_reading], 0)
            read_prompt = False

        # switch different texts
        for i in range(0, len(button_switch)):

            if button_switch[i].isClicked and current_text != i:
                # print(f'switch t{i}', getTime())
                action_reading.append(f'switch to t{i}')
                timestamp_reading.append(getTime())

                # mask the text
                textbox.text = mask_text(texts[i].copy(), 1)

                for jj in range(0, len(button_switch)):
                    if jj != i:
                        button_switch[jj].fillColor = buttoncolor
                        button_switch[jj].color = 'black'
                    else:
                        button_switch[jj].fillColor = clickcolor
                        button_switch[jj].color = 'white'

                current_text = i
                # print('current text', i)

        # switch different paraphrases in a text
        if current_text is not None:
            for i in range(0, len(aoi)):
                rect_x = (int(aoi[i].pos[0] - aoi[i].width/2), int(aoi[i].pos[0] + aoi[i].width/2))
                rect_y = (int(aoi[i].pos[1] - aoi[i].height/2), int(aoi[i].pos[1] + aoi[i].height/2))
                if mouse.getPos()[0] in range(rect_x[0], rect_x[1]) and mouse.getPos()[1] in range(rect_y[0], rect_y[1]):

                    # data record
                    if last_switch is None:
                        # print(f'switch to p{i}', getTime())
                        action_reading.append(f'switch to p{i}')
                        timestamp_reading.append(getTime())
                        last_switch = f'p{i}'
                    elif last_switch is not None and last_switch != f'p{i}':
                        # print(f'switch to p{i}', getTime())
                        action_reading.append(f'switch to p{i}')
                        timestamp_reading.append(getTime())
                        last_switch = f'p{i}'

                    content = [texts[current_text][0]]
                    for ii in range(1, len(texts[current_text])):
                        if ii - 1 != i:
                            content.append(mask_text([texts[current_text][ii]], 0))
                        else:
                            content.append(texts[current_text][ii])
                    textbox.text = ''.join(content)

        timer.text = f'{timer_text}{str(int((getTime() - t0) / 60))}分钟'

        if button_continue.isClicked:

            action_reading.append('finish task')
            timestamp_reading.append(getTime())

            date = (time.strftime("%Y_%b_%d_%H%M%S"))  # date of experiment

            # save data
            c = open('data/reading_online_{}_{}.csv'.format(sub_info['id'], date),
                     'w', encoding='utf-8-sig', newline='')  # create a csv file
            csv_writer = csv.writer(c)  # a csv obeject
            csv_writer.writerow(['id', 'gender', 'age', 'handedness',
                                'action', 'timestamp', 'duration', 'total duration'])  # head
            for i in range(0, len(action_reading)):  # write data into csv
                if i != len(action_reading) - 1:
                    duration = timestamp_reading[i + 1] - timestamp_reading[i]
                else:
                    duration = 0
                csv_writer.writerow([sub_info['id'],
                                     sub_info['gender'],
                                     sub_info['age'],
                                     sub_info['handedness'],
                                     action_reading[i],
                                     timestamp_reading[i],
                                     duration,
                                     timestamp_reading[-1] - timestamp_reading[0]
                                     ])

            button_continue.fillColor = clickcolor
            button_continue.color = 'white'
            win.flip()
            button_continue.fillColor = buttoncolor
            button_continue.color = 'black'

            title.setAutoDraw(False)
            timer.setAutoDraw(False)
            prompt_title.setAutoDraw(False)

            prompt.text = prompt_text_cmap
            prompt.setAutoDraw(False)

            button_continue.setAutoDraw(False)

            for button in button_switch:
                button.text = button_switch_text_reading[
                    button_switch.index(button)]
                button.setAutoDraw(False)

            textbox.setAutoDraw(False)

            button_continue.setAutoDraw(False)

            reading = False

        win.flip()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Cmap_task.py 'a experiment script for KS research'
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
        title = {{KS_task}},
        year = 2020,
        version = {1.0},
        publisher = {Github},
        url = {https://github.com/weiziqian1996/KS_task}
    }
"""

import csv
import time
from random import uniform
from psychopy import core, event, visual

# some parameters
window_size = [1000, 800]
keyterms = ['蜜蜂', '养蜂人', '蜂蜜', '科学家', '采蜜', '冬天', '疫情', '农药',
            '花田', '太阳', '8字形', '震动', '腹部', '果树', '全球气候变暖', '授粉']
stim_num = len(keyterms)
cmap_instruction_text = '【操作说明】\n' \
                        '拖曳：鼠标左键拖曳关键词\n' \
                        '连线：鼠标右键词A，再右键词B，即可建立词A和词B的连线，重复操作即可删除连线\n' \
                        '完成概念图后，按Enter键继续'

# open a window
win = visual.Window(
    size=window_size, fullscr=False, screen=0,
    winType='pyglet', allowGUI=True, allowStencil=False, color=[0, 0, 0], colorSpace='rgb',
    units='pix')
mouse = event.Mouse(win=win)

# stimulus
stimulus = []
box_list = []
line_list = []
line_start = []
line_end = []
for i in range(0, stim_num):
    stimulus.append(
        visual.TextStim(  # text stimulus (i.e., key-terms)
            win=win,
            text=keyterms[i],
            color='black',
            font='Microsoft YaHei',
            pos=(uniform(-window_size[0] / 2 + 100, window_size[0] / 2 - 100),  # random position
                 uniform(-window_size[1] / 2 + 100, window_size[1] / 2 - 100))
        )
    )
    box_list.append(
        visual.Rect(
            win=win,
            units='pix',
            width=stimulus[i].boundingBox[0],
            height=stimulus[i].boundingBox[1],
            fillColor=win.color,
            lineColor=win.color
        )
    )
    box_list[i].setAutoDraw(True)
    stimulus[i].setAutoDraw(True)  # auto-draw whenever win.flip()
# button = visual.ButtonStim(
#     win=win,
#     text='继续', font='Microsoft YaHei',
#     pos=(0, 0),
#     size=[200, 100], borderWidth=2,
#     fillColor='darkgrey', borderColor='black',
#     color='black', colorSpace='rgb',
#     opacity=None,
#     bold=True, italic=False,
#     padding=None,
#     anchor='center',
#     name='button')
cmap_instruction = visual.TextStim(
            win=win,
            text=cmap_instruction_text,
            color='black',
            font='Microsoft YaHei',
            alignText='left'
        )
cmap_instruction.pos = [-window_size[0]/2+cmap_instruction.boundingBox[0]/2,
                        window_size[1]/2-cmap_instruction.boundingBox[1]/2]
cmap_instruction.setAutoDraw(True)


def update():
    for i, line in enumerate(line_list):
        line.start = stimulus[line_start[i]].pos
        line.end = stimulus[line_end[i]].pos
        line.draw()
    for i in range(0, stim_num):
        box_list[i].pos = stimulus[i].pos


# stimulus presentation
update()
win.flip()

# loop
# continueRoutine = True
cmap = True
t0 = core.getTime()  # timing: record duration time of concept map task
while cmap:

    if event.getKeys() == ['return']:

        # save screenshot as a image file
        # so that we can have a view inspection on participant's concept map
        win.getMovieFrame()
        win.saveMovieFrames('Screenshot.png')

        # save data
        sub_info = {'subNum': 1001,
                    'gender': 'male',
                    'age': 25,
                    'handedness': 'right'}
        date = (time.strftime("%Y_%b_%d_%H%M%S"))  # date of experiment
        c = open('data/BeeExp_{}_{}.csv'.format(sub_info['subNum'], date),
                 'w', encoding='utf-8', newline='')  # create a csv file
        csv_writer = csv.writer(c)  # a csv obeject
        for i in range(0, len(line_start)):  # write data into csv
            csv_writer.writerow([sub_info['subNum'],
                                 sub_info['gender'],
                                 sub_info['age'],
                                 sub_info['handedness'],
                                 core.getTime() - t0, line_start[i], line_end[i]])
        c.close()  # close csv file
        win.close()  # close the window (script would keep running)

    # drag function
    for stimuli in stimulus:  # for each stimuli
        if mouse.isPressedIn(stimuli, buttons=[0]):  # if the stimuli is clicked by the left button
            stimuli.pos = mouse.getPos()  # set stimuli position to mouse position - drag and drop
            update()
            win.flip()  # and every stimuli is auto-drew
            break  # exit the loop, so only one moves

        # link function
        # select node1
        if mouse.isPressedIn(stimuli, buttons=[2]):  # if the stimuli is clicked by the right button
            stimuli.color = 'red'
            update()
            win.flip()

            # select node2
            to_link = True
            while to_link:
                for another_stimuli in stimulus:
                    if another_stimuli != stimuli:
                        if mouse.isPressedIn(another_stimuli, buttons=[0]):
                            another_stimuli.color = 'red'
                            update()
                            win.flip()

                            # add line
                            linked = None
                            for index in range(0, len(line_start)):
                                if line_start[index] == stimulus.index(stimuli) and \
                                        line_end[index] == stimulus.index(another_stimuli):
                                    linked = index
                                elif line_start[index] == stimulus.index(another_stimuli) and \
                                        line_end[index] == stimulus.index(stimuli):
                                    linked = index

                            if linked is None:
                                line_list.append(
                                    visual.Line(
                                        win=win,
                                        lineWidth=2,
                                        start=stimuli.pos,  # link stimuli ...
                                        end=another_stimuli.pos,  # ... to another stimuli
                                        lineColor='black'))
                                line_start.append(stimulus.index(stimuli))
                                line_end.append(stimulus.index(another_stimuli))
                            else:
                                del line_list[linked]
                                del line_start[linked]
                                del line_end[linked]

                            stimuli.color = 'black'
                            another_stimuli.color = 'black'
                            update()
                            win.flip()
                            to_link = False

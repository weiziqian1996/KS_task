#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    cmap_task.py 'a experiment script for KS research'
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

import csv
import time
from psychopy import core, event, visual
from psychopy.gui import DlgFromDict
from settings import *
from components import *
from functions import *


def run_cmap_task():
    # record data
    action_cmap = []
    timestamp_cmap = []
    used = []

    # set components as visible
    title.text = '概念图任务'
    title.setAutoDraw(True)
    term_counter.setAutoDraw(True)
    timer.setAutoDraw(True)
    prompt_title.setAutoDraw(True)

    panel_task.setAutoDraw(True)
    panel_terms.setAutoDraw(True)

    prompt.text = prompt_text_cmap
    prompt.setAutoDraw(True)

    button_continue.setAutoDraw(True)

    for button in button_switch:
        # print(button_switch_text[button_switch.index(button)])
        button.text = button_switch_text[button_switch.index(button)]
        button.setAutoDraw(True)

    stimuli[-1].setAutoDraw(True)

    # loop
    # continueRoutine = True
    cur_terms = None  # current terms
    terms_range = [[0, 13], [13, 26], [26, 38]]
    range_x, range_y = cmap_panel_range(panel_task)

    prompt_x = (290, 690)
    prompt_y = (-300, 300)
    read_prompt = False

    link_num = 0

    t0 = core.getTime()
    action_cmap.append('beginning task')
    timestamp_cmap.append(t0)

    cmap = True
    while cmap:

        # show the prompt only when mouse is pressed in the prompt button
        if mouse.getPos()[0] in range(prompt_x[0], prompt_x[1]) and \
                mouse.getPos()[1] in range(prompt_y[0], prompt_y[1]):
            prompt.text = prompt_text_cmap
            if not read_prompt:
                # data record
                # print('switch to read prompt', core.getTime())
                action_cmap.append('switch to prompt')
                timestamp_cmap.append(core.getTime())
                read_prompt = True
        else:
            prompt.text = mask_text([prompt_text_cmap], 0)
            if read_prompt:
                # print('switch out of prompt', core.getTime())
                action_cmap.append('switch out of prompt')
                timestamp_cmap.append(core.getTime())
                read_prompt = False

        # check whether each key-term have at less one edge with other(s)
        selected = set()
        check_linked = set()
        for line in line_list:  # write data into csv
            selected.add(stimuli[eval(line.name)[0]].text + '\n')
            selected.add(stimuli[eval(line.name)[1]].text + '\n')
        for i in range(0, len(used)):
            for j in range(0, len(selected)):
                if used[i] in list(selected)[j]:
                    check_linked.add(i)
        # print('check linked', len(check_linked))

        if button_continue.isClicked and term_counter.text == '关键词数量 13' and len(check_linked) == len(used):

            action_cmap.append('finish task')
            timestamp_cmap.append(core.getTime())

            date = (time.strftime("%Y_%b_%d_%H%M%S"))  # date of experiment

            # save screenshot as a image file
            # so that we can have a view inspection on participant's concept map
            win.getMovieFrame()
            win.saveMovieFrames(
                f"data/cmap_screenshot_{sub_info['id']}_{date}.png")

            # save on-line measurement data
            c = open('data/cmap_online_{}_{}.csv'.format(sub_info['id'], date),
                     'w', encoding='utf-8', newline='')  # create a csv file
            csv_writer = csv.writer(c)  # a csv obeject
            csv_writer.writerow(['id', 'gender', 'age', 'handedness',
                                 'action', 'timestamp', 'total_duration'])  # head
            for i in range(0, len(action_cmap)):  # write data into csv
                csv_writer.writerow([sub_info['id'],
                                     sub_info['gender'],
                                     sub_info['age'],
                                     sub_info['handedness'],
                                     action_cmap[i],
                                     timestamp_cmap[i],
                                     timestamp_cmap[-1] - timestamp_cmap[0]])

            # save ks data of cmap
            c = open('data/cmap_ks_{}_{}.csv'.format(sub_info['id'], date),
                     'w', encoding='utf-8-sig', newline='')  # create a csv file
            csv_writer = csv.writer(c)  # a csv obeject
            csv_writer.writerow(['id', 'gender', 'age', 'handedness', 'start',
                                 'end', 'start index', 'end index'])  # head
            # saving index of start & end, in case Chinese characters cannot
            # presented correctly in the csv file.
            selected = set()
            for line in line_list:  # write data into csv
                csv_writer.writerow([sub_info['id'],
                                     sub_info['gender'],
                                     sub_info['age'],
                                     sub_info['handedness'],
                                     stimuli[eval(line.name)[0]].text,
                                     stimuli[eval(line.name)[1]].text,
                                     eval(line.name)[0],
                                     eval(line.name)[1]]
                                    )
                selected.add(stimuli[eval(line.name)[0]].text + '\n')
                selected.add(stimuli[eval(line.name)[1]].text + '\n')

            # save selected key-terms
            f = open('data/keyterms.txt', 'w', encoding='utf-8')
            for term in selected:
                f.write(term)
            f.close()

            cmap = False  # exit the cmap task

        # key-terms switch button
        for i in range(0, len(button_switch)):
            if button_switch[i].isClicked and cur_terms != i:
                # print(f'action: switch to {i}', core.getTime())
                action_cmap.append(f'action: switch to {i}')
                timestamp_cmap.append(core.getTime())
                cur_terms = i
                for jj in range(0, len(button_switch)):
                    if jj != i:
                        button_switch[jj].fillColor = buttoncolor
                        button_switch[jj].color = 'black'
                    else:
                        button_switch[jj].fillColor = clickcolor
                        button_switch[jj].color = 'white'

        # drag function
        for i in range(0, len(stimuli)):  # for each stimulus
            # if a stimulus is clicked by the left button
            if mouse.isPressedIn(stimuli[i], buttons=[0]):
                if stimuli[i].text == '阿尔茨海默症':
                    while mouse.getPressed()[0] == 1:
                        drag_it(stimuli[i], cur_terms, line_list, line_start,
                                line_end)
                elif i in range(terms_range[cur_terms][0],
                                terms_range[cur_terms][1]) or stimuli[i].pos[
                    0] in range(range_x[0], range_x[1]) and \
                        stimuli[i].pos[1] in range(range_y[0], range_y[1]):
                    while mouse.getPressed()[0] == 1:
                        # print(stimuli.index(stimuli[i]))
                        # print(terms_range[cur_terms])
                        drag_it(stimuli[i], cur_terms, line_list, line_start,
                                line_end)
                    break  # exit the loop, so only one moves

            # link function
            # select node1
            if mouse.isPressedIn(stimuli[i], buttons=[
                2]):  # if a stimulus is clicked by the right button
                stimuli[i].color = clickcolor
                update(cur_terms, line_list, line_start, line_end)
                win.flip()

                # select node2
                to_link = True
                while to_link:
                    for another_stimuli in stimuli:
                        if another_stimuli != stimuli[i]:
                            if mouse.isPressedIn(another_stimuli, buttons=[0]):
                                another_stimuli.color = clickcolor
                                update(cur_terms, line_list, line_start,
                                       line_end)
                                win.flip()

                                # add line
                                linked = None
                                for index in range(0, len(line_list)):

                                    start_end = eval(line_list[index].name)
                                    if start_end[0] == i and start_end[
                                        1] == stimuli.index(another_stimuli):
                                        linked = index
                                    elif start_end[1] == i and start_end[
                                        0] == stimuli.index(another_stimuli):
                                        linked = index

                                if linked is None:
                                    line_list.append(
                                        visual.Line(
                                            win=win,
                                            lineWidth=2,
                                            start=stimuli[i].pos,
                                            end=another_stimuli.pos,
                                            lineColor='black',
                                            name=str([i, stimuli.index(
                                                another_stimuli)])
                                        )
                                    )
                                    line_list[-1].setAutoDraw(True)

                                    # print('action: add link', core.getTime())
                                    # action_cmap.append(f'action: add link')
                                    # timestamp_cmap.append(core.getTime())
                                else:
                                    line_list[linked].setAutoDraw(False)
                                    del line_list[linked]

                                    # print('action: del link', core.getTime())
                                    # action_cmap.append(f'action: del link')
                                    # timestamp_cmap.append(core.getTime())

                                stimuli[i].color = forecolor
                                another_stimuli.color = forecolor

                                # print(len(line_list))

                                to_link = False

        timer.text = f'{timer_text}{str(int((core.getTime() - t0) / 60))}分钟'

        # refresh term_counter and key-terms in canvas
        old_used = used
        used = []  # a list, contained string variable of selected key-terms
        for stimulus in stimuli:
            if stimulus.pos[0] in range(range_x[0], range_x[1]) and \
                    stimulus.pos[1] in range(range_y[0], range_y[1]):
                stimulus.setAutoDraw(True)  # set concepts in canvas as visible
                used.append(stimulus.text)  # count the number of key-terms

        if len(used) == 13:
            term_counter.color = 'green'
        else:
            term_counter.color = forecolor
        term_counter.text = f'{term_counter_text}{len(used)}'

        # data record -- node
        if len(used) > len(old_used):  # which means an "add" action
            # print('action: add key-term', core.getTime())
            action_cmap.append(f'action: add key-term')
            timestamp_cmap.append(core.getTime())
        elif len(used) < len(old_used):  # which means a "del" action
            # print('action: del key-term', core.getTime())
            action_cmap.append(f'action: del key-term')
            timestamp_cmap.append(core.getTime())
        update(cur_terms, line_list, line_start, line_end)

        # data record -- edge
        ks_file = []  # edges
        for i in range(0, len(line_list)):
            ks_file.append([stimuli[eval(line_list[i].name)[0]].text,
                           stimuli[eval(line_list[i].name)[1]].text])

        old_link_num = link_num
        # print(list(ks_cmap.edges))
        link_num = len(ks_file)
        # print(ks_file)
        if link_num > old_link_num:  # which means an "add" action
            # print('action: add link', core.getTime())
            action_cmap.append('action: add link')
            timestamp_cmap.append(core.getTime())
        elif link_num < old_link_num:  # which means a "del" action
            for i in range(0, old_link_num - link_num):
                print('action: del link', core.getTime())
                action_cmap.append('action: del link')
                timestamp_cmap.append(core.getTime())

        if not cmap:
            # set as invisible
            title.setAutoDraw(False)
            term_counter.setAutoDraw(False)
            timer.setAutoDraw(False)
            prompt_title.setAutoDraw(False)

            panel_task.setAutoDraw(False)
            panel_terms.setAutoDraw(False)

            prompt.setAutoDraw(False)

            for button in button_switch:
                # print(button_switch_text[button_switch.index(button)])
                button.setAutoDraw(False)

            for line in line_list:
                line.setAutoDraw(False)

            for stimulus in stimuli:
                stimulus.setAutoDraw(False)

            button_continue.setAutoDraw(False)

        win.flip()

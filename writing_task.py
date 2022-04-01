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

from psychopy import visual, event, core
from psychopy.gui import DlgFromDict
from psychopy.hardware import keyboard
import re
from text2graph import *
from settings import *
from components import *
from functions import *


def run_writing_task(selected=None):
    # record data
    action_writing = []
    timestamp_writing = []
    used = []
    link_num = 0

    title.text = '写作任务'
    title.setAutoDraw(True)
    term_counter.setAutoDraw(True)
    timer.setAutoDraw(True)
    counter.setAutoDraw(True)
    prompt_title.setAutoDraw(True)

    panel_task.setAutoDraw(True)
    panel_terms.setAutoDraw(True)

    prompt.text = prompt_text_writing
    prompt.setAutoDraw(True)

    button_continue.setAutoDraw(True)

    textbox.editable = False

    for button in button_switch:
        button.text = button_switch_text[button_switch.index(button)]
        button.setAutoDraw(True)

    textbox.editable = True
    textbox.text = '阿尔茨海默症'
    textbox.setAutoDraw(True)

    cur_terms = None
    # line_end = None

    prompt_x = (290, 690)
    prompt_y = (-300, 300)
    read_prompt = False

    t0 = core.getTime()
    action_writing.append('beginning task')
    timestamp_writing.append(t0)

    writing = True
    while writing:

        # show the prompt only when mouse is pressed in the prompt button
        if mouse.getPos()[0] in range(prompt_x[0], prompt_x[1]) and \
                mouse.getPos()[1] in range(prompt_y[0], prompt_y[1]):
            prompt.text = prompt_text_writing
            if not read_prompt:
                # data record
                # print('switch to read prompt', core.getTime())
                action_writing.append('switch to prompt')
                timestamp_writing.append(core.getTime())
                read_prompt = True
                textbox.color = 'white'
        else:
            prompt.text = mask_text([prompt_text_cmap], 0)
            if read_prompt:
                # print('switch out of prompt', core.getTime())
                action_writing.append('switch out of prompt')
                timestamp_writing.append(core.getTime())
                read_prompt = False
                textbox.color = forecolor

        # switch to key-terms
        for i in range(0, len(button_switch)):
            if button_switch[i].isClicked and cur_terms != i:

                # print(f'action: switch to {i}', core.getTime())
                action_writing.append(f'switch to {i}')
                timestamp_writing.append(core.getTime())
                cur_terms = i

                if i == 0:
                    for j in range(0, 13):
                        stimuli[j].setAutoDraw(True)
                    for jj in range(13, 38):
                        stimuli[jj].setAutoDraw(False)
                    cur_terms = i
                elif i == 1:
                    for j in range(13, 26):
                        stimuli[j].setAutoDraw(True)
                    for jj in range(0, 13):
                        stimuli[jj].setAutoDraw(False)
                    for jjj in range(26, 38):
                        stimuli[jjj].setAutoDraw(False)
                    cur_terms = i
                elif i == 2:
                    for j in range(26, 38):
                        stimuli[j].setAutoDraw(True)
                    for jj in range(0, 26):
                        stimuli[jj].setAutoDraw(False)
                    cur_terms = i

                # # set concepts in canvas as visible
                # for stimulus in stimuli:
                #     if stimulus.pos[0] in range(-495, 145) and \
                #             stimulus.pos[1] in range(-250, 250):
                #         stimulus.setAutoDraw(True)

                for jj in range(0, len(button_switch)):
                    if jj != i:
                        button_switch[jj].fillColor = buttoncolor
                        button_switch[jj].color = 'black'
                    else:
                        button_switch[jj].fillColor = clickcolor
                        button_switch[jj].color = 'white'

        words = removePunctuation(textbox.text)
        words = words.replace('\n', '')
        counter.text = f'{counter_text} {str(len(words))}字'
        timer.text = f'{timer_text}{str(int((core.getTime() - t0) / 60))}分钟'

        # count the key-terms
        old_used = used
        used = []
        if '阿尔茨海默症' in words:
            used.append('阿尔茨海默症')
        for i in total_keyterm:
            if i in words and i != '染色体':
                used.append(i)
                stimuli[total_keyterm.index(i)].color = 'grey'
            elif i in words and i == '染色体':
                if '二十一号染色体' not in words and '十九号染色体' not in words:
                    used.append(i)
                    stimuli[total_keyterm.index(i)].color = 'grey'
                elif '二十一号染色体' in words or '十九号染色体' in words:
                    check_words = words  # del two terms mentioned above
                    if '二十一号染色体' in check_words:
                        check_words = check_words.replace('二十一号染色体', '')
                    if '十九号染色体' in check_words:
                        check_words = check_words.replace('十九号染色体', '')
                    if '染色体' in check_words:  # if the term is still being used
                        used.append(i)
                        stimuli[total_keyterm.index(i)].color = 'grey'
                    else:
                        stimuli[total_keyterm.index(i)].color = forecolor
            else:
                stimuli[total_keyterm.index(i)].color = forecolor

        # put "chromosome" in the end
        if '染色体' in used:
            del used[used.index('染色体')]
            used.append('染色体')

        if selected:
            for i in range(0, len(stimuli)):
                if stimuli[i].text not in selected:
                    stimuli[i].color = 'white'

            used = set(used) & set(selected)
        #     for i in selected:
        #         if stimuli[all_keyterms.index(i)] not in words:
        #             stimuli[all_keyterms.index(i)].color = 'green'
        #         else:
        #             stimuli[all_keyterms.index(i)].color = '#6eaa5e'

        # if selected:  # do not count selected terms
        #     do_not_count = []
        #     for i in range(0, len(selected)):
        #         if selected[i] not in used:
        #             do_not_count.append(selected[i])
        #     for term in do_not_count:
        #         if term
        #         used.remove(term)
        if len(used) == 13:
            term_counter.color = 'green'
        else:
            term_counter.color = forecolor
        term_counter.text = f'{term_counter_text}{len(used)}'

        # data record
        if len(used) > len(old_used):  # which means an "add" action
            # print('action: add key-term', core.getTime())
            action_writing.append('action: add key-term')
            timestamp_writing.append(core.getTime())
        elif len(used) < len(old_used):  # which means a "del" action
            # print('action: del key-term', core.getTime())
            action_writing.append('action: del key-term')
            timestamp_writing.append(core.getTime())

        # links counter
        old_link_num = link_num
        # use different key-terms to construct KS, so that we can calculate how
        # many links in participant's writing correctly.
        if not selected:
            ks_terms = all_keyterms
        else:
            ks_terms = selected
        # put "chromosome" in the end
        ks_terms = list(ks_terms)
        if '染色体' in ks_terms:  # put "chromosome" in the end
            del ks_terms[ks_terms.index('染色体')]
            ks_terms.append('染色体')
        edges = text2graph_get_edges(text=words, keyterms=ks_terms,
                                     read_from_file=False, as_lower=False)
        # print(ks_data.edges)
        # edges = list(ks_data.edges)
        link_num = len(edges)

        if link_num > old_link_num:  # which means an "add" action
            # print('action: add link', core.getTime())
            action_writing.append('action: add link')
            timestamp_writing.append(core.getTime())
        elif link_num < old_link_num:  # which means a "del" action
            # print('action: del link', core.getTime())
            action_writing.append('action: del link')
            timestamp_writing.append(core.getTime())

        key = event.getKeys()
        if len(key) != 0:
            if key[0] == 'escape':
                win.close()

        # click to continue when all key-terms were used
        if button_continue.isClicked and term_counter.text == '关键词数量 13':

            action_writing.append('finish task')
            timestamp_writing.append(core.getTime())

            date = (time.strftime("%Y_%b_%d_%H%M%S"))  # date of experiment

            if selected:
                d3 = 'd3'
            else:
                d3 = ''

            # save screenshot as a image file
            # so that we can have a view inspection on participant's concept map
            win.getMovieFrame()
            win.saveMovieFrames(
                f"data/{d3}writing_screenshot_{sub_info['id']}_{date}.png")

            # save origin text in the writing task
            f = open(f"data/{d3}writing_content_{sub_info['id']}_{date}.txt",
                     'w', encoding='utf-8')
            f.write(textbox.text)
            f.close()

            # save online data
            c = open(f"data/{d3}writing_online_{sub_info['id']}_{date}.csv",
                     'w', encoding='utf-8', newline='')  # create a csv file
            csv_writer = csv.writer(c)  # a csv obeject
            csv_writer.writerow(['id', 'gender', 'age', 'handedness',
                                 'action', 'timestamp',
                                 'total_duration'])  # head
            for i in range(0, len(action_writing)):  # write data into csv
                csv_writer.writerow([sub_info['id'],
                                     sub_info['gender'],
                                     sub_info['age'],
                                     sub_info['handedness'],
                                     action_writing[i],
                                     timestamp_writing[i],
                                     timestamp_writing[-1] - timestamp_writing[
                                         0]])

            # save ks data of cmap
            c = open(f"data/{d3}writing_ks_{sub_info['id']}_{date}.csv",
                     'w', encoding='utf-8-sig', newline='')  # create a csv file
            csv_writer = csv.writer(c)  # a csv obeject
            csv_writer.writerow(['id', 'gender', 'age', 'handedness', 'start',
                                 'end', 'start index', 'end index'])  # head
            # saving index of start & end, in case Chinese characters cannot
            # presented correctly in the csv file.

            selected = set()
            for edge in edges:  # write data into csv
                csv_writer.writerow([sub_info['id'],
                                     sub_info['gender'],
                                     sub_info['age'],
                                     sub_info['handedness'],
                                     edge[0],
                                     edge[1],
                                     all_keyterms.index(edge[0]),
                                     all_keyterms.index(edge[1])]
                                    )
                selected.add(edge[0] + '\n')
                selected.add(edge[1] + '\n')

            # save selected key-terms
            selected = list(selected)
            if '染色体' in selected:  # put "chromosome" in the end
                del selected[selected.index('染色体')]
                selected.append('染色体')
            f = open('data/keyterms.txt', 'w', encoding='utf-8')
            for term in selected:
                f.write(term)
            f.close()

            button_continue.fillColor = clickcolor
            button_continue.color = 'white'
            win.flip()
            button_continue.fillColor = buttoncolor
            button_continue.color = 'black'

            title.setAutoDraw(False)
            term_counter.setAutoDraw(False)
            timer.setAutoDraw(False)
            counter.setAutoDraw(False)
            prompt_title.setAutoDraw(False)

            panel_task.setAutoDraw(False)
            panel_terms.setAutoDraw(False)

            prompt.text = prompt_text_cmap
            prompt.setAutoDraw(False)

            for button in button_switch:
                button.text = button_switch_text[button_switch.index(button)]
                button.setAutoDraw(False)

            for stimulus in stimuli:
                stimulus.setAutoDraw(False)

            textbox.setAutoDraw(False)

            button_continue.setAutoDraw(False)

            writing = False

        # if selected:
        #     for i in range(0, len(stimuli)):
        #         if stimuli[i].text not in selected:
        #             stimuli[i].setAutoDraw(False)

        win.flip()

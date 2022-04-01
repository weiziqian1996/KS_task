#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import *
from components import *
import re


def mask_text(text_list, start_index):
    # mask the prompt
    content = text_list
    for ii in range(start_index, len(content)):
        mask = ''
        for char in content[
            ii]:  # cntent[ii]: a single paragraph
            if char != '\n':  # char: each character in a paragraph
                mask += '口'
            else:
                mask += '\n'
        content[ii] = mask
    text = ''.join(content)
    return text


def update(cur_terms, line_list, line_start, line_end, seltect=None):
    # updata the position of each line
    for ii, line in enumerate(line_list):
        if line.setAutoDraw:
            line.start = stimuli[eval(line.name)[0]].pos
            line.end = stimuli[eval(line.name)[1]].pos

    # refresh the key-terms panel
    if cur_terms == 0:
        for j in range(0, 13):
            stimuli[j].setAutoDraw(True)
        for jj in range(13, 38):
            stimuli[jj].setAutoDraw(False)
    elif cur_terms == 1:
        for j in range(13, 26):
            stimuli[j].setAutoDraw(True)
        for jj in range(0, 13):
            stimuli[jj].setAutoDraw(False)
        for jjj in range(26, 38):
            stimuli[jjj].setAutoDraw(False)
    elif cur_terms == 2:
        for j in range(26, 38):
            stimuli[j].setAutoDraw(True)
        for jj in range(0, 26):
            stimuli[jj].setAutoDraw(False)
    stimuli[-1].setAutoDraw(True)

    # set concepts in cmap panel as visible
    for i in range(0, len(stimuli)):
        # 只基于横坐标来判断
        range_x, range_y = cmap_panel_range(panel_task)
        if stimuli[i].pos[0] in range(range_x[0], range_x[1]) and \
                stimuli[i].pos[1] in range(range_y[0], range_y[1]):
            stimuli[i].setAutoDraw(False)
            stimuli[i].setAutoDraw(True)
        else:  # if a concept is in the key-terms panel

            # set the concept to its initial position
            if stimuli[i].text == '阿尔茨海默症':
                stimuli[i].pos = ad_pos
            else:
                for length in total_keyterms_list:
                    if stimuli[i].text in length:
                        stimuli[i].pos = (initial_pos[0],
                                          initial_pos[1] - length.index(
                                              stimuli[i].text) * 25)

                    # and delete related lines
                    for line in line_list:
                        if i in eval(line.name):
                            line.setAutoDraw(False)
                            del line_list[line_list.index(line)]

    # this function is used to present selected key-terms
    if seltect:
        for i in range(0, len(stimuli)):
            if stimuli[i].text not in select:
                stimuli[i].setAutoDraw(False)


def drag_it(stimulus, cur_terms, line_list, line_start, line_end):
    stimulus.pos = mouse.getPos()  # set stimulus position to mouse position - drag and drop
    update(cur_terms, line_list, line_start, line_end)
    win.flip()  # and every stimulus is auto-drew


def cmap_panel_range(cmap_rect):
    range_x = [int(cmap_rect.pos[0] - cmap_rect.width / 2),
               int(cmap_rect.pos[0] + cmap_rect.width / 2)]
    range_y = [int(cmap_rect.pos[1] - cmap_rect.height / 2),
               int(cmap_rect.pos[1] + cmap_rect.height / 2)]
    return range_x, range_y


def removePunctuation(text):
    punctuation = '!,;:?"\'、，；.。：’”'
    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip()


def selected_terms(file):
    f = open(file, 'r', encoding='utf-8')
    content = f.readlines()
    f.close()
    selected = []
    for i in range(0, len(content)):
        selected.append(content[i].replace('\n', ''))
    # print(selected)
    if '染色体' in selected:  # put "chromosome" in the end
        del selected[selected.index('染色体')]
        selected.append('染色体')
    return selected

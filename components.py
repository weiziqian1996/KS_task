#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import *

# prompt on the right side
# note: add text before draw
prompt = visual.TextBox2(
    win=win,
    text='',
    font=exp_font,
    pos=(690, 0), letterHeight=exp_fontsize,
    size=(400, 600), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='right_center',
    fillColor='white', borderColor='black',
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True
)

# cmap drawing or writing panel on the left side
panel_task = visual.Rect(
    win=win,
    width=720,
    height=600,
    units='pix',
    pos=(-330, 0),
    lineColor='grey',
    fillColor='white',
    lineWidth=2)

# key-terms selected panel on the center
panel_terms = visual.Rect(
    win=win,
    width=220,
    height=400,
    units='pix',
    pos=(140, -20),
    lineColor='grey',
    fillColor='white',
    lineWidth=2)

# buttons used to switch different texts or key-terms in texts
# note: add text before draw
button_switch = []
for i in range(0, len(button_switch_text)):
    button_switch.append(visual.ButtonStim(
        win=win,
        text='',
        font=exp_font,
        letterHeight=exp_fontsize,
        size=[180, 30],
        borderWidth=2,
        fillColor=buttoncolor,
        borderColor='grey',
        color='black', colorSpace='rgb',
        opacity=None,
        bold=False,
        padding=None,
        anchor='center',
        pos=button_switch_pos[i]))

button_prompt = visual.ButtonStim(
    win=win,
    text='查看任务说明',
    font=exp_font,
    letterHeight=exp_fontsize,
    size=[180, 30],
    borderWidth=2,
    fillColor=buttoncolor,
    borderColor='grey',
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False,
    padding=None,
    anchor='center',
    pos=(160, 205 - 40))

# button used to continue
button_continue = visual.ButtonStim(
    win=win,
    text=button_continue_text,
    font=exp_font,
    letterHeight=exp_fontsize,
    size=[180, 30],
    borderWidth=2,
    fillColor=buttoncolor,
    borderColor='grey',
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False,
    padding=None,
    anchor='center',
    name='button',
    pos=(490, -325))

prompt_title = visual.TextBox2(
    win=win,
    text='任务说明',
    font=exp_font,
    pos=(490, 325), letterHeight=exp_fontsize,
    size=(110, 30), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor=backcolor, borderColor=forecolor,
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)

title = visual.TextBox2(
    win=win,
    text='概念图任务',
    font=exp_font,
    pos=(-320, 325), letterHeight=exp_fontsize,
    size=(110, 30), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor=backcolor, borderColor=forecolor,
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)

timer = visual.TextBox2(
    win=win,
    text=timer_text,
    font=exp_font,
    pos=(-320, -325), letterHeight=exp_fontsize,
    size=(160, 30), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor=backcolor, borderColor='black',
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)

term_counter = visual.TextBox2(
    win=win,
    text=term_counter_text,
    font=exp_font,
    pos=(-690 + 150 / 2, -325), letterHeight=exp_fontsize,
    size=(150, 30), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor=backcolor, borderColor='black',
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True
)

# stimuli
stimuli = []
line_list = []
line_start = []
line_end = []

initial_pos = (160, 130)
total_keyterm = keyterm_s + keyterm_g + keyterm_d
for i in range(0, len(total_keyterm)):
    stimuli.append(
        visual.ButtonStim(win=win,
                          text=total_keyterm[i],
                          font=exp_font,
                          letterHeight=exp_fontsize,
                          size=(100, 100),
                          borderWidth=0,
                          fillColor='white',
                          borderColor=None,
                          color=forecolor,
                          colorSpace='rgb',
                          opacity=1,
                          bold=False,
                          padding=0,
                          anchor='center'
                          )
    )

    # we can set the size based on the letter height
    stimuli[i].size = (
        len(total_keyterm[i]) * stimuli[i].letterHeight,
        stimuli[i].letterHeight)

ad_pos = (-320, 0)
stimuli.append(
    visual.ButtonStim(
        win=win,
        text='阿尔茨海默症',
        font=exp_font,
        letterHeight=exp_fontsize,
        size=(100, 100),
        borderWidth=0,
        fillColor='white',
        borderColor=None,
        color=forecolor,
        colorSpace='rgb',
        opacity=1,
        bold=False,
        padding=0,
        anchor='center',
        pos=ad_pos
    )
)
stimuli[-1].size = (
    len(stimuli[-1].text) * stimuli[-1].letterHeight, stimuli[-1].letterHeight)

# initial position
index = 0
for length in total_keyterms_list:
    for i in range(0, len(length)):
        stimuli[index].pos = (initial_pos[0], initial_pos[1] - i * 25)
        index += 1

textbox = visual.TextBox2(
    win=win,
    text='',
    font=exp_font,
    pos=(-690, 0), letterHeight=exp_fontsize,
    size=(720, 600), borderWidth=0,
    color=forecolor, colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='left_center',
    fillColor='white', borderColor=forecolor,
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)

counter = visual.TextBox2(
    win=win,
    text=counter_text,
    font=exp_font,
    pos=(-30, -325), letterHeight=exp_fontsize,
    size=(150, 30), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor=backcolor, borderColor='black',
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)

# area of interest
aoi = []
for i in range(0, 5):
    aoi.append(visual.Rect(
        win=win,
        width=textbox.size[0],
        height=0,
        units='pix',
        pos=(-330, 0),
        lineColor=None,
        fillColor=None,
        lineWidth=2)
    )
aoi_height = [[exp_fontsize * 3,  # text0
               exp_fontsize * 7,
               exp_fontsize * 6,
               exp_fontsize * 6,
               exp_fontsize * 6],
              [exp_fontsize * 5,  # text1
               exp_fontsize * 3,
               exp_fontsize * 6,
               exp_fontsize * 5,
               exp_fontsize * 5],
              [exp_fontsize * 3,  # text2
               exp_fontsize * 6,
               exp_fontsize * 6,
               exp_fontsize * 4,
               exp_fontsize * 8],
              ]
aoi_pos = [[(-330, 300 - exp_fontsize * 4),  # text0
            (-330, 300 - exp_fontsize * 9),
            (-330, 300 - exp_fontsize * 15.5),
            (-330, 300 - exp_fontsize * 21.5),
            (-330, 300 - exp_fontsize * 27.5)],
           [(-330, 300 - exp_fontsize * 4.5),  # text1
            (-330, 300 - exp_fontsize * 8.5),
            (-330, 300 - exp_fontsize * 13),
            (-330, 300 - exp_fontsize * 18.5),
            (-330, 300 - exp_fontsize * 23.5)],
           [(-330, 300 - exp_fontsize * 4),  # text2
            (-330, 300 - exp_fontsize * 8.5),
            (-330, 300 - exp_fontsize * 14.5),
            (-330, 300 - exp_fontsize * 19.5),
            (-330, 300 - exp_fontsize * 25.5)]
           ]

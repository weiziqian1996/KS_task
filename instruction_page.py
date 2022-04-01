#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import *
from components import *

interval = visual.ImageStim(win, image='pic/000.jpg')
instruction1 = visual.ImageStim(win, image='pic/001.jpg')
instruction2 = visual.ImageStim(win, image='pic/002.jpg')
instruction3 = visual.ImageStim(win, image='pic/003.jpg')
instruction4 = visual.ImageStim(win, image='pic/004.jpg')
instruction5 = visual.ImageStim(win, image='pic/005.jpg')
instruction6 = visual.ImageStim(win, image='pic/006.jpg')
instruction7 = visual.ImageStim(win, image='pic/007.jpg')
instruction8 = visual.ImageStim(win, image='pic/008.jpg')
instruction9 = visual.ImageStim(win, image='pic/009.jpg')
instruction10 = visual.ImageStim(win, image='pic/010.jpg')
instruction_list = [instruction1,
                    instruction2,
                    instruction3,
                    instruction4,
                    instruction5,
                    instruction6,
                    instruction7,
                    instruction8,
                    instruction9,
                    instruction10
                    ]


def show_interval(wait_secs):

    for button in button_switch:
        button.fillColor = buttoncolor
        button.color = forecolor
    interval.draw()
    win.flip()
    core.wait(wait_secs)


def run_instruction_page(instruc_num=None):

    if type(instruc_num) == int:
        instruction_list[instruc_num - 1].setAutoDraw(True)

    button_continue.text = '继续'
    button_continue.setAutoDraw(True)

    instruction = True

    while instruction:

        if button_continue.isClicked:

            button_continue.fillColor = clickcolor
            button_continue.color = 'white'

            win.flip()

            button_continue.fillColor = buttoncolor
            button_continue.color = 'black'

            instruction_list[instruc_num - 1].setAutoDraw(False)

            button_continue.setAutoDraw(False)

            instruction = False

        win.flip()

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

from psychopy import visual, event, core

window_size = [1280, 800]
keyterms = ['蜜蜂', '养蜂人', '蜂蜜', '科学家', '采蜜', '冬天', '疫情', '农药',
            '花田', '太阳', '8字形', '震动', '腹部', '果树', '全球气候变暖', '授粉']
stim_num = len(keyterms)

prompt_text = '【操作说明】\n'\
         '点击右侧的按钮来\n'\
         '查看各个文章。\n'\
         '\n'\
         '同一时间只能呈现\n'\
         '一个段落，你可以\n'\
         '通过按上下方向键\n'\
         '来查看段落。\n'\
         '\n'\
         '你可以反复查看每\n'\
         '个文章中的段落，\n'\
         '也可以反复查看不\n'\
         '同的文章，以便更\n'\
         '好地理解文章内容。'\
         '\n\n\n\n\n\n\n\n\n\n\n'\
         '【阅读用时】\n'\

text_s = ['《阿尔茨海默症的大脑变化、症状和诊断》\n\n',
         '阿尔茨海默症是一种不可逆转的、逐步发展的大脑疾病，能够缓慢地摧毁记忆和思维能\n'
         '力，并且目前无法被彻底治愈。\n\n',
         '关于阿尔茨海默症的发病以及发展的复杂的大脑变化正在被持续地揭示。大脑变化可能\n'
         '在记忆和其他思维问题出现之前就显现。在阿尔茨海默症的临床前阶段，虽然不存在症\n'
         '状，但有害的大脑变化已经出现。其中，大脑中的异常的蛋白沉积导致的淀粉样斑块和\n'
         '神经元纤维缠结是该症的主要特征，这些现象意味着大脑的损伤。损伤最初出现于对于\n'
         '形成记忆有重要作用的大脑区域，其将随着病情的发展而不断加重，范围也越来越大。\n\n',
         '记忆方面的问题是阿尔茨海默症相关症状的典型的第一信号。一些人具有轻度认知障碍，\n'
         '这意味着他们比同龄的正常人具有更多的记忆问题，且在老年期具有更高的罹患阿尔茨\n'
         '海默症的风险。但并非所有具有轻度认知障碍的人都会罹患阿尔茨海默症，一些人甚至\n'
         '会恢复到正常的状态。\n\n',
          '对大多数人而言，非记忆方面的思维问题，例如视觉、推理和判断方面的障碍，标志了\n'
         '疾病的早期阶段。生物标记物是脑成像、脑脊液和血液中的与疾病有关的生物信号。目\n'
         '前正被尝试用于检测可能罹患阿尔茨海默症的高风险人群的早期的大脑变化，但还未达\n'
         '到可以实际应用的程度。\n\n',
          '采用多种方式进行诊断是必要的，这将有助于确认症状是由于阿尔茨海默症导致的，还\n'
         '是其他原因导致的。例如，人们需要提供自己的病史，以排除其他疾病导致记忆问题的\n'
         '可能。早期诊断有助于在一定时间内保持日常功能、有助于未来的家庭计划，以及提供\n'
         '了更多参与临床试验的机会。']
text_g = ['《阿尔茨海默症的遗传因素》\n\n',
         '基因遗传自一个人的亲生父母，其携带的信息定义了像是眼睛颜色和身高这样的特质。\n'
         '基因的突然变化称为遗传突变，基因的某些差异则称为遗传变异。对基因相关的因素的\n'
         '识别有助于找到治疗或预防个体罹患阿尔茨海默症的有效方法。\n\n',
         '根据阿尔茨海默症发生的时间点，可以分为早发型和晚发型。两种类型都与遗传突变或\n'
         '遗传变异有关。\n\n',
         '大多数人罹患的阿尔茨海默症属于晚发型，该类型的发病时间是六十岁之后。与晚发型\n'
         '有关的是十九号染色体上的名为载脂蛋白E的基因。载脂蛋白E具有几种不同的遗传变异\n'
         '类型，大部分人具有的类型既不减少也不增加患病概率，但某种罕见的遗传变异则会增\n'
         '加个体罹患阿尔茨海默症的可能性，虽然这并不意味着一定会患病。\n\n',
         '早发型则较为罕见，其一般发病于六十岁之前。与早发型有关的是某些基因的遗传突变。\n'
         '例如，二十一号染色体中名为淀粉样前体蛋白的精确功能尚未得到了解，但这一基因的\n'
         '突变与异常的淀粉样蛋白斑块的产生有关，后者被视为阿尔茨海默症的一种标志。\n\n',
          '一个人所具有的基因可以通过血液测试进行鉴别。人们可以据此推断自己罹患阿尔茨海\n'
         '默症的可能性，但要注意，血液测试无法以百分之百的准确性预测个体的患病概率。因\n'
         '为除了基因之外，还有太多因素会影响疾病的发展和过程。']
text_d = ['《阿尔茨海默症与唐氏综合症患者，以及临床研究》\n\n',
         '唐氏综合征患者比以往活得更久了，但这也带来了新的健康挑战。评估表明，随着年龄\n'
         '增长，一半以上的唐氏综合征患者将会因为阿尔茨海默症而罹患痴呆。\n\n',
         '唐氏综合征患者天生具有一个额外的编号为二十一的染色体，该染色体携带的一种遗传\n'
         '信息与一种特殊的蛋白有关，该蛋白会导致淀粉形态的斑块在人脑中堆积。在三十岁之\n'
         '后，大多数唐氏综合征患者具有这些斑块，以及缠结的神经细胞纤维，从而导致罹患阿\n'
         '尔茨海默症的风险增高。\n\n',
         '大多数成年的唐氏综合征患者不会意识到自身的健忘问题的出现，且由于存在智力缺陷，\n'
         '对该能力变化的评估也变得困难。为此，在唐氏综合征患者三十岁之前建立一个关于思\n'
         '考和行为能力的基线数据文档是很有必要的，这将有助于了解其能力的变化，并进而判\n'
         '断痴呆的原因。\n\n',
         '阿尔茨海默症会持续数年甚至更久，随着时间而加重并最终导致死亡。科学家正在努力\n'
         '工作以揭开阿尔茨海默症的根源，以寻求可以停止、延缓乃至预防该症发展的方法。但\n'
         '是，如果没有志愿者参与临床研究，新的发现就不可能存在。\n\n',
         '在正式参与之前，志愿者应当考虑一个研究的风险和收益。同时，符合研究要求也是必\n'
         '要的。例如，志愿者可能需要处于一个特定的年龄阶段或具有特定的遗传特征，这将有\n'
         '助于科学家确认研究结果的有效性。对于参与临床研究的成年唐氏综合征患者，其家庭\n'
         '成员/监护人在其中扮演了重要的角色。他们可能会被要求陪伴该志愿者进行研究访问并\n'
         '回答问题。志愿者通常需要签署协议以声明他们理解研究中的风险和收益，对于唐氏综\n'
         '合征患者，这一步骤通常由其家庭成员/监护人来完成。']
texts = [text_s, text_g, text_d]

# open a window
win = visual.Window(
    size=window_size, fullscr=False, screen=0,
    winType='pyglet', allowGUI=True, allowStencil=False, color=[1, 1, 1], colorSpace='rgb',
    units='pix')
mouse = event.Mouse(win=win)

# prompt
prompt = visual.TextBox2(
    win=win,
    text='',
    font='Microsoft YaHei',
    pos=(-550, 350), letterHeight=20.0,
    size=(120, 500), borderWidth=0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center_top',
    fillColor='white', borderColor='black',
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)
prompt.setAutoDraw(True)

# text stimuli
document = visual.TextBox2(
    win=win,
    text='',
    font='Microsoft YaHei',
    pos=(0, 0), letterHeight=20.0,
    size=(800, 700), borderWidth=2.0,
    color='black', colorSpace='rgb',
    opacity=None,
    bold=False, italic=False,
    lineSpacing=1.0,
    padding=None,
    anchor='center',
    fillColor='white', borderColor='black',
    flipHoriz=False, flipVert=False,
    editable=False,
    name='textbox',
    autoLog=True,
)
document.setAutoDraw(True)

# text_buttons used to switch different texts
text_buttons = list()
button_name = ['文本1', '文本2', '文本3']
button_pos = [(500, 325), (500, 275), (500, 225)]
for i in range(0, len(button_name)):
    text_buttons.append(visual.ButtonStim(
        win=win,
        text=button_name[i],
        font='Microsoft YaHei',
        letterHeight=20,
        size=[100, 50],
        borderWidth=2,
        fillColor='white',
        borderColor='black',
        color='black', colorSpace='rgb',
        opacity=None,
        bold=False,
        padding=None,
        anchor='center',
        name=button_name[i],
        pos=button_pos[i]))
    text_buttons[i].setAutoDraw(True)

# continue button
continue_button = visual.ButtonStim(
        win=win,
        text='结束阅读',
        font='Microsoft YaHei',
        letterHeight=20,
        size=[100, 50],
        borderWidth=2,
        fillColor='white',
        borderColor='black',
        color='black', colorSpace='rgb',
        opacity=None,
        bold=False,
        padding=None,
        anchor='center',
        name='continue_button',
        pos=(500, -325))
continue_button.setAutoDraw(True)

reading = True
document.text = '请点击右侧的选项切换文本'  # the initial introduction on the textbox
current_text = None
current_paraph = 1

t0 = core.getTime()
print('beginning timestamp', core.getTime())

while reading:

    # switch different texts
    for i in range(0, len(text_buttons)):

        if text_buttons[i].isClicked and current_text != i:

            print('switch text timestamp', core.getTime())

            content = texts[i].copy()
            for ii in range(2, len(content)):
                mask = ''
                for char in content[ii]:  # cntent[ii]: a single paragraph
                    if char != '\n':  # char: each character in a paragraph
                        mask += '口'
                    else:
                        mask += '\n'
                content[ii] = mask
            document.text = ''.join(content)
            for jj in range(0, len(text_buttons)):
                if jj != i:
                    text_buttons[jj].fillColor = 'white'
                    text_buttons[jj].color = 'black'
                else:
                    text_buttons[jj].fillColor = 'black'
                    text_buttons[jj].color = 'white'

            current_text = i
            current_paraph = 1
            print('current text', i)

    # switch different paraphrases in a text
    key = event.getKeys()
    if len(key) != 0:
        if key[0] in ['down', 'up']:

            print('switch paraphrase timestamp', core.getTime())

            value = 99  # an initial value, can be detected as ERROR
            if key[0] == 'down':
                value = 1
            elif key[0] == 'up':
                value = -1

            content = texts[current_text].copy()
            if current_paraph + value not in [0, len(content)]:  # 99 not in this range
                for i in range(1, len(content)):
                    if i != current_paraph + value:

                        mask = ''
                        for char in content[i]:
                            if char != '\n':
                                mask += '口'
                            else:
                                mask += '\n'
                        content[i] = mask
                current_paraph += value
                document.text = ''.join(content)

    prompt.text = f'{prompt_text}{str(int((core.getTime() - t0)/60))}分钟'
    win.flip()

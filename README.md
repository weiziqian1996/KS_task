# ks_tasks
PsychoPy scripts for reading comprehension experiments.
- **reading_task.py** can be used to measure various indicators in multiple document comprehension, such as response time for each paragraph, manipulation actions (e.g., switch from the instruction to documents) and the total duration of the task.
- **cmap_task.py** can be used to measure learning products in the format of concept maps. It records concepts used in the concept map, links among concepts, the total duration of the task and so on.
- **writing_task.py** is similar to cmap_task.py, but measures learning products in the format of summary/argument/essay. It firstly converts the writing results into the network format by using the function *text2graph* in [*cookiemilk*](https://github.com/weiziqianpsych/cookiemilk), and then records various indicators mentioned above in the section of cmap_task.py.

![Fig 1](https://github.com/weiziqianpsych/ks_tasks/interfaces_screenshot.png)

Figure 1 Example of interfaces (from the top to the bottom: the reading task, the concept map task and the writing task)

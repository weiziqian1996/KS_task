# ks_tasks
PsychoPy scripts for reading comprehension experiments.
- **reading_task.py** can be used to measure various indicators in multiple documents reading, such as response time for each paragraph, manipulation actions (e.g., switch from the instruction to documents) and the total duration of the task.
- **cmap_task.py** can be used to measure learning products in the format of concept maps. It records concepts used in the concept map, links among concepts, the total duration of the task and so on.
- **writing_task.py** is similar to cmap_task.py, but measures learning products in the format of summary/arugment/essay. It firstly converts the writing results into the network format by using the function *text2graph* in [*AutoKS*](https://github.com/weiziqianpsych/AutoKS), and then records various indicators mentioned above in the section of cmap_task.py.

![alt text](https://github.com/weiziqianpsych/ks_tasks/blob/main/interfaces.png?raw=true)

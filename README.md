# ks_tasks
PsychoPy scripts for reading comprehension experiments.
- **reading_task.py** can be used to measure various indicators in multiple documents reading, such as response time for each paragraph, manipulation actions (e.g., switch from the instruction to documents) and total duration of the task.
- **cmap_task.py** can be used to measure learning products in the format of concept maps. It records concepts used in the concept map, links among concepts, total duration of the task and so on.
- **writing_task.py** is simialr to cmap_task.py, but measure learning products in the format of summary/aurgment/essay. It firstly converts the writing results into the network format by using the function *text2graph* in [*AutoKS*](https://github.com/weiziqianpsych/AutoKS), and then records indicators mentioned above in the section of cmap_task.py.

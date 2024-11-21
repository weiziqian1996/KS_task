# ks_tasks
PsychoPy scripts for reading comprehension experiments.
- **reading_task.py** is designed for measuring various on-line indicators when reading texts, such as response time for each paragraph, manipulation actions (e.g., switch from the instruction to documents), and the total task duration.
- **cmap_task.py** is designed for measuring after-reading learning products in the format of a concept map. It records concepts used in the map, links among the concepts, the total task duration, etc.
- **writing_task.py** is similar to cmap_task.py, but measures learning products in the format of a summary/argument essay. It firstly converts the writing results into the network format by using the function *text2graph* in [*cookiemilk*](https://github.com/weiziqianpsych/cookiemilk), and then records various indicators mentioned above in the section of cmap_task.py.

![Fig 1](interfaces_screenshot.png)

Figure 1 Example of interfaces (from the top to the bottom: the reading task, the concept map task and the writing task)

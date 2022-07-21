Blendyn is one of MBDyn post-processor which is built as an addons of 
Blender. Blendyn's structure and most of its function implemented in 2017. 
However, some of its function is out of date and their is some new ideas 
for improvement. In 2022 GSoC, we planed to update and implement some 
Blendyn features as follow:

1. Adding two new plotting engines `matplotlib` and `bokeh` into plotting.
2. Finding an optimal way to visualize some missing element such as `beam slider`, 
`modal`.
3. Visualise internal forces and stress/strain fields of deformable 
components `beam2`, `beam3`, `shell4`, `membrance`  during animation.
4. Improving UI interface

My code could be seen on `devel2` branch of [Blendyn 
Github](https://github.com/zanoni-mbdyn/blendyn)

### **GSoC Bonding Time**

Before coding, I spent time to install and learn how to use necessary 
library such as `matplotlib`, `bokeh`, `pygal`. Then, I tested some 
Blendyn feature with [Blendyn 
Tutorial](https://github.com/zanoni-mbdyn/blendyn/wiki/Tutorials)  
and reading throught the code structure to get to know how 
Blendyn work in general.

### **First Week: June 13th - June 19th**

In this week, I read carefully plotting code in `plot.py`. Then, I start 
to create `matplotlib.py` python file and implement `matplotlib`.

1. Adding `matplotlib` library information into dependency list in 
`dependencies.py`
2. Create the following operator:
	`BLENDYN_OT_mplot_var_scene`
	`BLENDYN_OT_mplot_var_object`
	`BLENDYN_OT_mplot_variables_list`
	`BLENDYN_OT_mplot_var_sxx_scene`
	`BLNEDYN_OT_mplot_var_sxx_object`
	`BLENDYN_OT_mplot_trajectory_scene`
	`BLENDYN_OT_mplot_trajectory_object`
3. Create `plot engine` choosing function into plotting panels and 
add `Trajectory` option into `plot type`.
4. Moving `Pygal plotting function` into new python file name `pygallib,py`

### **Second Week: June 20th - June 26th**
This week, I continue to implementing `bokeh` plotting engine into Blendyn:
1. Adding `bokeh` library information into dependency list in `dependencies.py`
2. Create the following operator:
	`BLENDYN_OT_bplot_var_scene`
        `BLENDYN_OT_bplot_var_object`
        `BLENDYN_OT_bplot_variables_list`
        `BLENDYN_OT_bplot_var_sxx_scene`
        `BLNEDYN_OT_bplot_var_sxx_object`
        `BLENDYN_OT_bplot_trajectory_scene`
        `BLENDYN_OT_bplot_trajectory_object`
3. Adding `Bokeh` into plotting engine in plotting panel.

### **Third Week: June 27th - July 3rd**###
This week, I test my code by plotting different MBDyn output variables with new 
`operator` function. Then, I fixed some bugs.

1. Register new `operator` function `__init__.py`
2. Create two options `show in localhost` and `save as png` when plotting with `bokeh` engine

### **Four Week: July 4th - July 10th** ###
This week, I fucus on reading material and exsiting code about two elements `beam slider` and `modal`. Then, I 
thought about how to design and visualize them in blender.

### **Fifth Week: July 11th - July 17th** ###
This week, I start to implement `automatic import` functions of `beam slider`
1. Create a new Python file name `beamsliderlib.py`
2. Implementing `automatic import` functions as follow:
	`BLENDYN_OT_import_beam_slider`
	`parse_beam_slider`
	`beam_slider_info_draw`
	`spawn_beam_slider_element`
3. Adding `parse_beam_slider` into `joint_type` list in 
`elementlib.py`
4. Drawing `beam slider` symbol in `joints.blend` (it looks 
like a hollow cylinder) 

### **Sixth Week: July 18th - July 24th** ###
This week, I focused on visualize and automatic import 
`modal` joint as a Blendyn Component.
1. Create a new Python file name `modallib.py`
2. Implementing `automatic import` functions as follow:
        `BLENDYN_OT_import_modal`
        `parse_modal`
        `modal_info_draw`
        `spawn_modal_element`
3. Adding `parse_modal` into `joint_type` list in
`elementlib.py`
4. Drawing `modal` symbol in `joints.blend` (it looks
like a spherical surface)
5. Adding `add_comp_armature_bones_modal` into 
`add_mesh_component` to enable visualize `modal`
as a Blendyn Component
6. Implementing some functions in `component.py` as follow
	`BLENDYN_OT_element_add_node`
        `BLENDYN_OT_element_add_all_selected_nodes`
        `BLENDYN_OT_element_remove_node`
        `BLENDYN_OT_element_remove_all_nodes`
        `BLENDYN_OT_element_add_new_connect`
        `BLENDYN_OT_element_remove_connect`
        `BLENDYN_OT_element_remove_all_connects`
7. Modifying `BLENDYN_PT_components` to create suitable UI 
for import `modal`
  
  


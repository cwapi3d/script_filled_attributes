import cadwork
import element_controller as ec
import attribute_controller as ac
import geometry_controller as gc

element_ids = cadwork.get_auto_attribute_elements()

for element_id in element_ids:
    height = round(gc.get_height(element_id),3)
    width = round(gc.get_width(element_id),3)
    if height % 20 == 0 and width % 20 == 0:
        cadwork.set_auto_attribute([element_id], 'Standard cross-section')
    else:
        cadwork.set_auto_attribute([element_id], 'Special cross-section')
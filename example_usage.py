import cadwork
import attribute_controller
import geometry_controller

#gets the specified elements
elements = cadwork.get_auto_attribute_elements()

for element in elements:
    length = geometry_controller.get_length(element)
    group = attribute_controller.get_group(element)
    result = ' Group:' + group + 'Length:' + str(length)
    #sets the attribute
    cadwork.set_auto_attribute([element], result)

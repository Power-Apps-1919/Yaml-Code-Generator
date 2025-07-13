import cpa_yaml_builder
from cpa_yaml_builder.control_factory import *
auto_import_controls() 
print("Control factory module imported successfully.")  
print("Control factory functions available:", dir(cpa_yaml_builder.control_factory))
print(list_registered_controls())
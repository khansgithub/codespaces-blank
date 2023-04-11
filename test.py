import os
import importlib.util

workflow_modules = {}
module_root = "mod"
directory_path = f"./{module_root}/"

# Loop over all files in the directory
for module in os.listdir(directory_path):
    # import ipdb;ipdb.set_trace()
    if not os.path.isdir(os.path.join(directory_path, module)):
        print("skip")
        continue
    
    if module[0] == ".":
        continue

    # Import the module
    module_name = f"{module_root}.{module}"
    spec = importlib.util.find_spec(module_name)
    improted_module = importlib.import_module(module_name)
    workflow_modules[module] = improted_module

import ipdb; ipdb.set_trace()
# 
    # Do something with the imported module
    # print(f"Imported module: {module}")
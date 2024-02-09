import os
import importlib
from domlogger import Domlogger as DomLogger

## Dynamically load modules

class DomsManager:
    def __init__(self, doms_directory : str) -> None:
        self.log = DomLogger()
        if (not os.path.isdir(doms_directory)):
            raise ValueError(f"Path needs to be defined")
        self.doms_directory = doms_directory
        
        self.plugins = {} # {"plugin.name" : { "function_name" : }}
        self.dom_loader()

    def import_module(self, name):
        # implement a safer method, by safer I mean one that allows specific directories

        try:
            module = importlib.import_module(f"modules.{name}")
            return module
        except Exception as e:
            self.log.LogError(f"Cannot import {module}\n {e}")


    def dom_loader(self): # mass load plugins

        dom_files = [f for f in os.listdir(self.doms_directory) if f.endswith(".py")]
        dom_entries = [d[:-3] for d in dom_files] # list any python scripts in the requested directory and remove the ".py" extension

        for dom_entry in dom_entries:
            
            # module = importlib.import_module(f"modules.{dom_entry}") # import module
            module = self.import_module(f"{dom_entry}") # import module
            
            try: # if file has class Dom() defined
                self.log.LogInfo(f"{module.__name__} found")
                doms_class = getattr(module, "Dom") 
            except:
                continue
                       
            classes = {} 
            for attrName in dir(module): # get all attributes of the imported module
                attr = getattr(module, attrName) 
                if callable(attr):
                    classes[attrName] = attr # if an attribute can be called, add to classes list
                    
            self.plugins[f"{dom_entry}"] = classes
                    
    # def dom_runner(self, dom : str , function : str):
    #     dom_class = None # initialize variable
    #     if dom in self.plugins:
    #         dom_module = importlib.import_module(f"modules.{dom}")
    #         dom_class = getattr(dom_module, "Dom", None) # get class 
    #     else:
    #         self.log.LogWarn(f"Could not access module [\"{dom}\"] or its class")
            
    #     if dom_class:
    #         dom_instance = dom_class()
            
    #         dom_method = getattr(dom_instance, function, None) # search for the requested function, fallback is None
            
    #         if callable(dom_method): # if function is callable
    #             self.log.LogInfo(f"Found [\"{dom}.{dom_method.__name__}\"]")
    #             return dom_method() # return to run
    #         else:
    #             self.log.LogWarn(f"Could not find function [\"{dom}.{function}\"]")
                
    def dom_runner(self, dom: str, function: str, *args, **kwargs):
        dom_class = None  # Initialize variable
        if dom in self.plugins:
            dom_module = importlib.import_module(f"modules.{dom}")
            dom_class = getattr(dom_module, "Dom", None)  # Get class
        else:
            self.log.LogWarn(f"Could not access module [\"{dom}\"] or its class")

        if dom_class:
            dom_instance = dom_class()

            dom_method = getattr(dom_instance, function, None)  # Search for the requested function, fallback is None

            if callable(dom_method):  # If function is callable
                self.log.LogInfo(f"Found [\"{dom}.{dom_method.__name__}\"]")
                try:
                    return dom_method(*args, **kwargs)  # Pass dynamic arguments and return the result
                except Exception as e: # function won't completely fuck up if e.g too many arguments were passed
                    self.log.LogError(f"Could not run function{dom_method.__name__}\n {e}") 
            else:
                self.log.LogWarn(f"Could not find function [\"{dom}.{function}\"]")

    def cache_functions():
        pass

if __name__ == "__main__":
    print(f"Running as {__file__}")
    c = DomsManager("modules/")

    c.dom_loader()
    
    c.log.LogInfo(f"listed plugins: [\"{c.plugins}\"]")
    
    print(c.dom_runner("dom_math", "math_add", first_number=123, second_number=345,asdd="2"))
    
    c.import_module("MyModule")

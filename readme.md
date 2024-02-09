# Learning project

I am learning how to make and use a plugin system in python.



## Structure

A plugin is defined as a "dom"

Plugger.py is the main file
it looks for .py files in `modules/`, imports those if they contain a `Dom()` function

DomsManager() requires a path to be defined in doms_directory, planned to use this for custom plugin directories

import_module() imports a file and returns it

dom_loader() iterates over all the .py files in the specified directory

old dom_runner() has been commented out, for reference

dom_runner() runs a function, if it exists inside the requested module


domlogger.py just prints text with colour indication for information, warn and errors, this is not the focus at the moment


from ctypes import *

import template

class GoString(Structure):
    _fields_ = [("p", c_char_p), ("n", c_longlong)]

def get_go_string(val):
    return GoString(val.encode('utf-8'), len(val))

def get_go_path(file):
    if not os.path.isabs(file) and file:
        file = os.path.join(os.getcwd(),file)
    return get_go_string(file)

def render_template(template, value_file, output):
    template = get_go_path(template)
    value_file = get_go_path(value_file)
    output = get_go_path(output)

    template.RenderTemplate.argtypes = [GoString, GoString, GoString]
    template.RenderTemplate(template, value_file, output)

# render_template('tests/sample.tmpl', 'tests/values.yml','')

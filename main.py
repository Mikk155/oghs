"""
The MIT License (MIT)

Copyright (c) 2024 Mikk155

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

#========================================
# Python libraries
#========================================

import importlib.util
import os;
import sys;
import importlib;
import subprocess;

#========================================
# End
#========================================

#========================================
# Project libraries
#========================================

from python.utils.jsonc import jsonc;
from python.utils.DynDict import dyndict;

global config;

config = dyndict(                       \
    jsonc.load(                          \
        os.path.join(                     \
            os.path.dirname(__file__), \
            "svencoop_addon/scripts/plugins/config.json"
        )
    )
);

from python.utils.printf import printf;

#========================================
# End
#========================================

#========================================
# Load the correct module
#========================================

module = '';

module_file = '';

mode: int = config[ "SERVER" ][ "mode" ];

if mode == 1:

    module = "bot.py";

else:

    module = "loop.py";

module_file = os.path.join( os.path.dirname(__file__), "python/module" );
module_file = os.path.join( module_file, module );

#========================================
# End
#========================================

#========================================
# Install requirements for the module we'll use
#========================================

requirements = module_file.replace( '.py', '_requirements.txt' );

subprocess.check_call( [ sys.executable, "-m", "pip", "install", "-r", requirements ] );

r = '';

f = open( requirements, 'r' ).readlines();

for l in f:

    r=f'{r}\n{l}';

#========================================
# End
#========================================

#========================================
# Import the module we'll use
#========================================

spec = importlib.util.spec_from_file_location( module, module_file );

obj = importlib.util.module_from_spec( spec );

spec.loader.exec_module( obj );

plugin_data = obj.on_initialization();

#========================================
# End
#========================================

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

global config;
from __main__ import config;
config: dict;

def __language__() -> str:

    import locale;

    __syslang__ = locale.getlocale();

    __lang__ = __syslang__[ 0 ];

    if __lang__.find( '_' ) != -1:

        __lang__ = __lang__[ 0 : __lang__.find( '_' ) ];

    return str( __lang__.lower() );

def printf( data: str, arguments: list[str] = [], dont_print: bool = False, dont_color: bool = False ) -> str:

    '''
    Prints a message with a formatted string

    Returns the formatted string

    ``data`` label from **__main__**'s ``config[ "sentences" ]`` dict

    ``arguments`` list of arguments to replace brackets from the string

    ``dont_print`` **True** won't print to console

    ``dont_color`` **True** won't use color formatting
    '''

    from colorama import Fore, Back;

    __data__ = config[ "sentences" ][data];

    __string__ = __data__.get( __language__(), __data__.get( 'english', '' ) );

    for __arg__ in arguments:

        __string__ = __string__.replace( "{}", str( __arg__ ), 1 );

    __printf__ = f'{Back.WHITE}{Fore.BLACK}{__string__}{Back.RESET}{Fore.RESET}\n' if not dont_color else f'{__string__}\n';

    __result__ = None;

    if not dont_print:

        print(__printf__);

    return __printf__;

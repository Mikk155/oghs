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

class cache:

    '''
    %AppData% Cache
    '''

    class path_e:
        cache = 0;
        svencoop = 1;
        appdata = 2;

    @staticmethod
    def path() -> list[str]:

        import os;

        __appdata_path__ = os.getenv( "APPDATA" );

        __app_folder__ = os.path.join( __appdata_path__, "svencoop" );

        __config_path__ = os.path.join( __app_folder__, "config.json" );

        __dirs__ = [ __config_path__, __app_folder__, __appdata_path__ ];

        return __dirs__;

    @staticmethod
    def set( cfg: dict ) -> None:

        import os;

        import json;

        __path__ = cache.path();

        os.makedirs( __path__[cache.path_e.svencoop], exist_ok=True );

        with open( __path__[cache.path_e.cache], 'w' ) as __config__:

            json.dump( cfg, __config__, indent=4 );

    def get() -> dict:

        import os;

        import json;

        __path__ = cache.path();

        __data__ = {};

        if os.path.exists( __path__[cache.path_e.cache] ):

            with open( __path__[cache.path_e.cache], 'r' ) as __config__:

                __data__ = json.load( __config__ );

                __config__.close();

        return __data__;

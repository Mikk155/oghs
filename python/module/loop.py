import os
import time
import psutil
import subprocess

from __main__ import __file__ as abs;

global config;
from __main__ import config;
config: dict;

def on_initialization() -> None:

    GameDS = 'SvenDS.exe';

    def running() -> bool:

        for process in psutil.process_iter( [ 'name' ] ):

            if process.info[ 'name' ] == GameDS:

                return True;

        return False;

    exe = f"\"{os.path.join( os.path.dirname(abs), GameDS )}\"";

    for arg in config[ "SERVER" ][ "arguments" ]:

        exe = f'{exe} {arg}';

    sleep = config[ "SERVER" ][ "mode == 0" ][ "check delay" ];

    while True:

        try:

            if not running():

                subprocess.Popen( exe, shell=True );

        except Exception as exception:

            print( "A problem ocurred while ejecuting \"{}\"\n{}".format( GameDS, exception ) );

        time.sleep( sleep );

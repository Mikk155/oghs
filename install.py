import os
import shutil

global destination;
destination = '';

while not os.path.exists( destination ):

    destination = input( "Write the full path to your \"Sven Co-op\" folder." );

    if not os.path.exists( os.path.join( destination, 'svencoop' ) ):

        print( "Couldn't find \"svencoop\" folder in {}".format( destination ) );

        destination = '';

source = os.path.abspath( os.path.dirname(__file__) );

for item in os.listdir( source ):

    source_item = os.path.join( source, item );

    dest_item = os.path.join( destination, item );

    if os.path.isdir( source_item ):

        if os.path.exists( dest_item ):

            shutil.rmtree( dest_item, True );

        shutil.copytree( source_item, dest_item, dirs_exist_ok=True );

    else:

        shutil.copy2( source_item, dest_item );

print( "All Done!" );

input( "You can delete this folder now." );

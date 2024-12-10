/*
    ChatSounds
*/

ChatSound@ g_cs = ChatSound(); //Esto

final class ChatSound : initializer::Initializer
{
    // const string GetName() { return "ChatSounds" }; // Ya no seria necesario esto pq ya en el iniciaicer

    CLogger@ m_Logger;

    json@ data;

    void PluginInit()
    {
        UpdateJson();
        
        this.name = "ChatSounds";
        @m_Logger = CLogger( GetName() );
        // @m_Logger = CLogger( this.name = "ChatSounds" ); //Creo que funciona
        
        if( IsEnabled() )
        {
            m_Logger.info( "Loaded." );
        }
    }

    void UpdateJson()
    {
        @data = cast<json@>( gpData[ GetName() ] );

        enable = data[ "active", false ];
    }

    private uint m_DynLastIndex;;
    private string m_DynMapName;
    private array<string> m_DynArray = {};
    private array<string> m_StaticArray = {};

    private dictionary m_soundlist;

    private void push_back( const string& in szSound )
    {
        string folder = cast<string>( this.data[ "folder" ] );
        m_StaticArray.insertLast( folder + szSound );
    }

    void ReadFile()
    {
        UpdateJson();

        dictionary m_soundlist = cast<json@>( this.data[ "sounds"] ).data;

        array<string> szSounds = m_soundlist.getKeys();

        for( uint ui = 0; ui < szSounds.length(); ui++ )
        {
            this.push_back( szSounds[ui] );
        }
    }

    void MapInit()
    {
    }
}

/*
    Logger
*/

class CLogger
{
    private const string m_Member;

    CLogger( const string &in csMember )
    {
        m_Member = csMember;
    }

    private void __printf__( const string &in csSuffix, const string &in csMessage, array<string> asArguments )
    {
        string str;
        snprintf( str, "%s [%s] %s\n", m_Member, csSuffix, csMessage );

        for( uint ui = 0; ui < asArguments.length(); ui++ )
        {
            uint index = str.Find( "{}", 0 );

            if( index != String::INVALID_INDEX ) {
                str = str.SubString( 0, index ) + asArguments[ui] + str.SubString( index + 2 );
            }
        }

        g_EngineFuncs.ServerPrint( str );
    }

    void warn( const string &in csMessage, array<string> asArguments = {} ) {
        this.__printf__( "WARNING", csMessage, asArguments );
    }

    void debug( const string &in csMessage, array<string> asArguments = {} ) {
        this.__printf__( "DEBUG", csMessage, asArguments );
    }

    void info( const string &in csMessage, array<string> asArguments = {} ) {
        this.__printf__( "INFO", csMessage, asArguments );
    }

    void critical( const string &in csMessage, array<string> asArguments = {} ) {
        this.__printf__( "CRITICAL", csMessage, asArguments );
    }

    void error( const string &in csMessage, array<string> asArguments = {} ) {
        this.__printf__( "ERROR", csMessage, asArguments );
    }
}
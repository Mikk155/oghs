namespace initializer
{
    json@ jsonData;
    array<Initializer@> arrPluginInit;
    array<Initializer@> arrPluginExit;
    array<Initializer@> arrMapInit;
    array<Initializer@> arrMapActivate;
    array<Initializer@> arrMapStart;
    array<Initializer@> arrThink;
    array<Initializer@> arrReadFile;

    void PluginInit()
    {
        initializer::ReadFile();

        for(uint ui = 0; ui < arrPluginInit.length(); ui++)
        {
            Initializer@ pInit = arrPluginInit[ui];

            if(!pInit.IsEnabled())
                continue;

            pInit.PluginInit();

            if( !pInit.IsActive() )
            {
                arrPluginInit.removeAt(ui);
                ui--;
            }
        }
    }

    void PluginExit()
    {
        for(uint ui = 0; ui < arrPluginExit.length(); ui++)
        {
            Initializer@ pInit = arrPluginExit[ui];

            if(!pInit.IsEnabled())
                continue;

            pInit.PluginExit();

            if( !pInit.IsActive() )
            {
                arrPluginExit.removeAt(ui);
                ui--;
            }
        }
    }

    void MapInit()
    {
        for(uint ui = 0; ui < arrMapInit.length(); ui++)
        {
            Initializer@ pInit = arrMapInit[ui];
    
            if(!pInit.IsEnabled())
                continue;

            pInit.MapInit();

            if( !pInit.IsActive() )
            {
                arrMapInit.removeAt(ui);
                ui--;
            }
        }
    }

    void MapActivate()
    {
        for(uint ui = 0; ui < arrMapActivate.length(); ui++)
        {
            Initializer@ pInit = arrMapActivate[ui];

            if(!pInit.IsEnabled())
                continue;

            pInit.MapActivate();

            if( !pInit.IsActive() )
            {
                arrMapActivate.removeAt(ui);
                ui--;
            }
        }

        initializer::ResetScheduler();
    }

    void MapStart()
    {
        for(uint ui = 0; ui < arrMapStart.length(); ui++)
        {
            Initializer@ pInit = arrMapStart[ui];

            if(!pInit.IsEnabled())
                continue;

            pInit.MapStart();

            if( !pInit.IsActive() )
            {
                arrMapStart.removeAt(ui);
                ui--;
            }
        }
    }

    void Think()
    {
        for(uint ui = 0; ui < arrThink.length(); ui++)
        {
            Initializer@ pInit = arrThink[ui];

            if(!pInit.IsEnabled())
                continue;

            if( pInit.IsValidNextThink() )
            {
                pInit.Think();

                if( !pInit.IsActive() )
                {
                    arrThink.removeAt(ui);
                    ui--;
                }
            }
        }
    }

    void ReadFile()
    {
        for(uint ui = 0; ui < arrReadFile.length(); ui++)
        {
            Initializer@ pInit = arrReadFile[ui];

            if(!pInit.IsEnabled())
                continue;

            pInit.ReadFile();

            if( !pInit.IsActive() )
            {
                arrReadFile.removeAt(ui);
                ui--;
            }
        }
    }
}

class Initializer
{
    string name = "NONE";
    bool enable = true;
    bool active = true;
    float nextthink = 0.0;

    Initializer()
    {
        initializer::arrPluginInit.insertLast(this);
        initializer::arrPluginExit.insertLast(this);
        initializer::arrMapInit.insertLast(this);
        initializer::arrMapActivate.insertLast(this);
        initializer::arrMapStart.insertLast(this);
        initializer::arrThink.insertLast(this);
        initializer::arrReadFile.insertLast(this);
    }

/*
!@Gaftherman
Añade estas funciones:
    void MapInit() {}
    void MapStart() {}
    void MapActivate() {}
    void PluginInit() {}
    void PluginExit() {}
    void Think() {} < 0.1? o menos, idk luego vemos en q lo usamos
    void PlayerSay( args ) {}
    void PlayerKilled() {}
    void PlayerObserver() < paso enum si salio o entro
    void PlayerSpawn()
    void PlayerConnect() < ClientPutInServer
    void PlayerAttack() < Enum de los tres
*/
    void PluginInit()
    {
        active = false;
    }

    void PluginExit()
    {
        active = false;
    }

    void MapInit()
    {
        active = false;
    }

    void MapActivate()
    {
        active = false;
    }

    void MapStart()
    {
        active = false;
    }

    void Think()
    {
        active = false;
    }

    void ReadFile()
    {
        active = false;
    }

    bool IsActive()
    {
        bool result = active;
        active = true;
        return result;
    }

    bool IsEnabled()
    {
        return enable;
    }

    string GetName()
    {
        return name;
    }

    bool IsValidNextThink()
    {
        if(nextthink != 0.0 && nextthink < g_Engine.time)
        {
            nextthink = 0.0;
            return true;
        }

        return false;
    }
}
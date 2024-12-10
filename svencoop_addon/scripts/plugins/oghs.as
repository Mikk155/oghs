/*
    Main
*/

// Utilities
#include "oghs/json"
#include "oghs/Logger"

#include "oghs/chatsounds"

#include "initializer"

json@ gpData;

void PluginInit()
{
    g_Module.ScriptInfo.SetAuthor( "Mikk | Gaftherman" );
    g_Module.ScriptInfo.SetContactInfo( "github.com/Mikk155 | github.com/Gaftherman" );
    gpData.load( "scripts/plugins/oghs.json", false );
    initializer::PluginInit();
}

void PluginExit() {
    initializer::PluginExit();
}

void MapInit() {
    gpData.reload( "scripts/plugins/oghs.json", false );
    initializer::MapInit();
}

void MapActivate() {
    initializer::MapActivate();
}

void MapStart() {
    initializer::MapStart();
}

void Think() {
    initializer::Think();
}

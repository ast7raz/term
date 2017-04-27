def get_rc(id):
    src="""
    -- Standard awesome library
    local awful = require("awful")
    awful.rules = require("awful.rules")
    local gears = require("gears")
    require("awful.autofocus")
    
    
    for s = 1, screen.count() do
        gears.wallpaper.centered("/usr/share/rub90/config/awesome/logo.png", s)
        end
        
        modkey = "Mod4"
        
        local layouts = {
            awful.layout.suit.max.fullscreen,
                awful.layout.suit.tile
                }
                
                
                globalkeys = awful.util.table.join(
                    awful.key({ modkey,           }, "Return",
                        function ()
                                awful.util.spawn("x-terminal-emulator")
                                    end),
                                        awful.key({ modkey,           }, "Tab",
                                            function ()
                                                    awful.client.focus.byidx(1)
                                                            if client.focus then
                                                                        client.focus:raise()
                                                                                end
                                                                                    end),
                                                                                    
                                                                                        awful.key({ modkey,           }, "space", function () awful.layout.inc(layouts,  1) end),
                                                                                        
                                                                                            awful.key({ modkey, "Shift"    }, "r",
                                                                                                function()
                                                                                                        awful.util.spawn_with_shell("wget -t 1 -O- --post-data='' http://localhost/shutdown/reboot")
                                                                                                            end),
                                                                                                                awful.key({ modkey, "Shift"    }, "s",
                                                                                                                    function()
                                                                                                                            awful.util.spawn_with_shell("wget -t 1 -O- --post-data='' http://localhost/shutdown/soft")
                                                                                                                                end),
                                                                                                                                    awful.key({ modkey, "Shift"    }, "p",
                                                                                                                                        function()
                                                                                                                                                awful.util.spawn_with_shell("wget -t 1 -O- --post-data='' http://localhost/set_server/prod")
                                                                                                                                                    end),
                                                                                                                                                        awful.key({ modkey, "Shift"    }, "t",
                                                                                                                                                            function()
                                                                                                                                                                    awful.util.spawn_with_shell("wget -t 1 -O- --post-data='' http://localhost/set_server/test")
                                                                                                                                                                        end),
                                                                                                                                                                            awful.key({ modkey, "Shift"    }, "d",
                                                                                                                                                                                function()
                                                                                                                                                                                        awful.util.spawn_with_shell("wget -t 1 -O- --post-data='' http://localhost/set_server/dev")
                                                                                                                                                                                            end),
                                                                                                                                                                                                awful.key({ modkey, "Shift"    }, "k",
                                                                                                                                                                                                    function()
                                                                                                                                                                                                            awful.util.spawn_with_shell("wget -t 1 -O- --post-data='' http://localhost/toggle_kiosk")
                                                                                                                                                                                                                end),
                                                                                                                                                                                                                
                                                                                                                                                                                                                    awful.key({        }, "Print", function () awful.util.spawn("scrot -e 'curl --upload-file $f https://transfer.sh/ >> /tmp/screenshots && rm $f'") end),
                                                                                                                                                                                                                        awful.key({ "Mod1" }, "Print", function () awful.util.spawn("scrot -u -e 'curl --upload-file $f https://transfer.sh/ >> /tmp/screenshots && rm $f'") end)
                                                                                                                                                                                                                        )
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        root.keys(globalkeys)
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        spawn_apps = {
                                                                                                                                                                                                                            "xset s off -dpms",
                                                                                                                                                                                                                        	"bash /usr/share/rub90/config/awesome/kiosk.sh http://support.firstgaming.com/first/%s/",
                                                                                                                                                                                                                        	    
                                                                                                                                                                                                                        	    }
                                                                                                                                                                                                                        	    
                                                                                                                                                                                                                        	    
                                                                                                                                                                                                                        	    tags = {}
                                                                                                                                                                                                                        	    
                                                                                                                                                                                                                        	    for s = 1, screen.count() do
                                                                                                                                                                                                                        	        tags[s] = awful.tag({ 1, }, s, awful.layout.suit.max.fullscreen)
                                                                                                                                                                                                                        	        end
                                                                                                                                                                                                                        	        
                                                                                                                                                                                                                        	        awful.rules.rules = {
                                                                                                                                                                                                                        	            {
                                                                                                                                                                                                                        	                    rule = {},
                                                                                                                                                                                                                        	                            properties = {
                                                                                                                                                                                                                        	                                        focus = awful.client.focus.filter,
                                                                                                                                                                                                                        	                                                    raise = true,
                                                                                                                                                                                                                        	                                                                size_hints_honor = false
                                                                                                                                                                                                                        	                                                                        }
                                                                                                                                                                                                                        	                                                                            },
                                                                                                                                                                                                                        	                                                                                {
                                                                                                                                                                                                                        	                                                                                        rule = { instance = "first" },
                                                                                                                                                                                                                        	                                                                                                properties = { tag = tags[1][1] },
                                                                                                                                                                                                                        	                                                                                                    }
                                                                                                                                                                                                                        	                                                                                                    }
                                                                                                                                                                                                                        	                                                                                                    if screen.count() == 2 then
                                                                                                                                                                                                                        	                                                                                                        table.insert(awful.rules.rules, {
                                                                                                                                                                                                                        	                                                                                                                rule = { instance = "second" },
                                                                                                                                                                                                                        	                                                                                                                        properties = { tag = tags[2][1] },
                                                                                                                                                                                                                        	                                                                                                                            })
                                                                                                                                                                                                                        	                                                                                                                                table.insert(spawn_apps, "bash /usr/share/rub90/config/awesome/kiosk.sh http://support.firstgaming.com/second")
                                                                                                                                                                                                                        	                                                                                                                                    table.insert(spawn_apps, "bash /usr/share/rub90/config/awesome/movecursor.sh")
                                                                                                                                                                                                                        	                                                                                                                                    end
                                                                                                                                                                                                                        	                                                                                                                                    
                                                                                                                                                                                                                        	                                                                                                                                    for key, value in ipairs(spawn_apps) do
                                                                                                                                                                                                                        	                                                                                                                                        awful.util.spawn(value)
                                                                                                                                                                                                                        	                                                                                                                                        end
                                                                                                                                                                                                                        	                                                                                                                                            
    
    
    
    
    
    
    
    

""" %id
    #print(src)
    return src
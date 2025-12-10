config.load_autoconfig()

c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'

config.bind(',ce', 'config-edit')

css = '~/proj/solarized-everything-css/css/gruvbox/gruvbox-all-sites.css'


#blank startpage
c.url.default_page = "about:blank"
c.url.start_pages = ["about:blank"]

#risky
c.tabs.show = 'always'         # keep tabs visible
c.tabs.favicons.show = "never"   # disable favicons
#end risky



# c.fonts.tabs = '8pt monospace'
# c.fonts.statusbar = '8pt monospace'

c.search.incremental = False
c.editor.command = ['code', '-nw', '{}']

#c.qt.args = ['ppapi-widevine-path=/usr/lib/qt/plugins/ppapi/libwidevinecdmadapter.so']

config.source('gruvbox.py')

c.tabs.padding = {'top': 2, 'bottom': 2, 'left': 5, 'right': 5}
c.tabs.indicator.width = 0 # no tab indicators
c.tabs.width = '7%'


#c.content.blocking.method = 'adblock' # uncomment this if you install python-adblock
#c.content.blocking.adblock.lists = [
#       "https://github.com/ublockorigin/uassets/raw/master/filters/legacy.txt",
#       "https://github.com/ublockorigin/uassets/raw/master/filters/filters.txt",
#       "https://github.com/ublockorigin/uassets/raw/master/filters/filters-2020.txt",
#       "https://github.com/ublockorigin/uassets/raw/master/filters/filters-2021.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/filters-2022.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/filters-2023.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/filters-2024.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/badware.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/privacy.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/badlists.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/annoyances.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/annoyances-cookies.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/annoyances-others.txt",
#       "https://github.com/ublockorigin/uassets/raw/master/filters/quick-fixes.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/resource-abuse.txt",
#        "https://github.com/ublockorigin/uassets/raw/master/filters/unbreak.txt"]

c.content.blocking.method = "adblock"

c.content.blocking.adblock.lists = [
    # Hagezi Pro (Adblock syntax)
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",

    # Core
    "https://easylist.to/easylist/easylist.txt",
    "https://easylist.to/easylist/easyprivacy.txt",
    
    # Regional (optional but useful)
    "https://easylist-downloads.adblockplus.org/easylistgermany.txt",

    # reddit
    "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/LegitimateURLShortener.txt",

    # uBlock-compatible public lists (ABP-syntax only)
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/badware.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/privacy.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
    "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/unbreak.txt",

    # Anti-annoyances
    "https://easylist.to/easylist/fanboy-annoyance.txt",

    # Anti-tracking (not ideal; hosts format may be ignored)
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
]


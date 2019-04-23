"""
descriptors module that describe vendors syslog formats by regexes
{
    'name': 'cisco', # name
    'sig': r'\s+%\S+\s?:\s', signature to determine if this a cisco's syslog
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'%(\S+)\s?:',
        '_msg': r'%\S+\s?:\s+(.*)'
    },

}
"""
default_desc = {
    'name': 'default',
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'%(\S+)',
        '_msg': r'>(.*)'
    }
}

cisco_desc = {
    'name': 'cisco',
    'sig': r'\s+%\S+\s?:\s',
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'%(\S+)\s?:',
        '_msg': r'%\S+\s?:\s+(.*)'
    },

}

arista_desc = cisco_desc
arista_desc.update({'name': 'arista'})

juniper_desc = {
    'name': 'juniper',
    'sig': '_\S+:\S+:',
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'([\w_]+):\S+:\s',
        '_msg': r'_\S+:\S+:\s(.*)'
    }
}

forinet_desc = {
    'name': 'fortinet',
    'sig': '.level=\w+',
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'type=([\w_]+)',
        '_msg': r'type=[\w_]+\.(.*)'
    }
}

f5_desc = {
    'name': 'f5',
    'sig': '\w+\[\w+\]:\s+\w+:\d+',
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'([\w_]+)\[\w+\]:',
        '_msg': r'\s+\S+:\S+:\s(.*)'
    }
}

huawei_desc = {
    'name': 'huawei',
    'sig': '%%',
    'fields': {
        '_pri': r'<(\d+)>',
        '_tag': r'%%\s?\d+(.+)\(',  # /4/REBOOT(l): or /4/REBOOT(l)[123]:
        '_msg': r'%%.+:\s?(.*)'
    }
}

all_descriptors = [cisco_desc, arista_desc, juniper_desc, forinet_desc, f5_desc, huawei_desc]

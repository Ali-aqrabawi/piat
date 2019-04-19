"""
descriptors modules that descript vendors syslog formats by regexes
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
    'sig': r'%\S+\s?:\s',
    'name': 'cisco',
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

all_descriptors = [cisco_desc, arista_desc, juniper_desc]

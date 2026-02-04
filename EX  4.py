def pluralize(noun):
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'
    else:
        return noun + 's'

print(pluralize("cat"))   # cats
print(pluralize("baby"))  # babies
print(pluralize("box"))   # boxes

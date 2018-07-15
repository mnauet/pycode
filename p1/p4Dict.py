super_villains = { 'key1' : 'key1Value' ,
                   'key2' : 'key2Value' ,
                   'key3': 'key3Value',
                   'key4': 'key4Value',
                   'key5': 'key5Value',
                   'key6': 'key6Value',
                   'key7': 'key7Value'}
print(super_villains['key1'])
print(super_villains.get('key2'))
print(len(super_villains))
del super_villains['key7']
print(super_villains)
print(super_villains.keys())
print(super_villains.values())
print((super_villains.items()))

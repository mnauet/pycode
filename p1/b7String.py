long_string ="I'll catch you if you fall- The floor"
print(long_string)
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])

print("%c is my %s letter and my number %d is %.5f"
      % ('x', 'favourite',1,.14))

print(long_string.capitalize())
print(long_string.find('floor'))
print(long_string.isalpha())
print(len(long_string))
print(long_string.replace('floor',  'ground'))
quote_list = long_string.split(' ')
print(quote_list)
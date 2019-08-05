from string import Template


name = "Nick"
errno = 50159747054


# 'old style' string formatting 
print('Hey %s, there is a 0x%x error!' % (name, errno))
print('Hey %(name)s, there is a 0x%(errno)x error!' % {'name': name, 'errno': errno})


# 'new style' string formatting
print('Hey {name}, there is a 0x{errno:x} error!'.format(name=name, errno=errno))


# Literal string interpolations with python 3.6+
print(f'Hey {name}, there is a {errno:#x} error!')


# Template strings for user input.
template_string = 'Hey $name, there is a $error error!'
out = Template(template_string).substitute(
                                           name=name,
                                           error=hex(errno))
print(out)


def tag(name, *content, class_=None, **attrs):
    if class_ is not None:
        attrs['class'] = class_
    attrs_pairs = (f'{attr}={value}' for attr, value in
                   sorted(attrs.items()))
    attr_str = ''.join(attrs_pairs)
    if content:
        elements = (f'<{name} {attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', class_='sidebar'))
print(tag('p', 'hello', 'world', 'img'))

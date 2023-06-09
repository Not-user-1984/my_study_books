import chardet

# определяем кодировку для строки my_bytes
my_bytes = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
result = chardet.detect(my_bytes)
print(result['encoding'])   # выведет 'utf-8
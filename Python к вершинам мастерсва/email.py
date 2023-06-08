import dns.resolver

domain = 'networkutopia.com.'

# Создаем объект-разрешитель DNS-запросов
resolver = dns.resolver.Resolver()

# Выполняем запрос A-записи для заданного домена
answers = resolver.query(domain)

# Печатаем ответы
for rdata in answers:
    print(rdata)

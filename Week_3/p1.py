import dns.resolver


result = dns.resolver.resolve('gmail.com', 'MX')
for mx_record in result:
    print('IP', mx_record)
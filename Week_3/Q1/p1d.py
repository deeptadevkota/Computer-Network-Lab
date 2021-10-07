import dns.resolver


host_name=input('Enter the host name: ')

result = dns.resolver.resolve('gmail.com', 'MX')


print(f'The priority followed by the mail server of {host_name} are as follows:\n')
for mx_record in result:
    print(mx_record)
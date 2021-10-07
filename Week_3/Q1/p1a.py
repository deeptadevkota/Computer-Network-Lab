import dns.resolver

domain = input("\nEnter domain: ")

try:

    records = dns.resolver.resolve(domain,'MX')

    print('\nMail exchange servers with their preferences are: \n')
    print(" ____________________________________________")
    print("| Prefence  |           MX Record            |")
    print("|-----------|--------------------------------|")
    for record in records:
        r = str(record)
        l = r.split(' ',1)
        print("| {:<8}  |  {:30}|".format(l[0],l[1]))
    
    print("|___________|________________________________|")

    print('\n')

except:
    print('\nError: Invalid Domain\n')
import dns.resolver

domain = input("\nEnter domain: ")

try:

    records = dns.resolver.resolve(domain,'MX')

    print('\nMail exchange servers with their preferences are: \n')
    print(" _______________________________________________")
    print("| Preferennce  |           MX Record            |")
    print("|--------------|--------------------------------|")
    for record in records:
        r = str(record)
        l = r.split(' ',1)
        print("| {:<11}  |  {:30}|".format(l[0],l[1]))
    
    print("|______________|________________________________|")

    print('\n')

except:
    print('\nError: Invalid Domain\n')
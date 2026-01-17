import dns.resolver

resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8']  # Google DNS

domain = input("Enter domain name: ")

record_types = ["A", "MX", "NS"]

for record in record_types:
    try:
        answers = resolver.resolve(domain, record)
        print(f"\n{record} Records:")
        for rdata in answers:
            print(rdata)
    except Exception as e:
        print(f"\nNo {record} record found")

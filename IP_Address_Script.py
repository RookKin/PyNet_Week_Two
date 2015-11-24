
ip_addr = raw_input("\n\nPlease enter an ip address: ")

octets = ip_addr.split(".")
octets = octets[:3]
octets.append('0')


ip_number = ".".join(octets)
print "\nYour IP's subnetwork number is: %s" % ip_number

first_octet_binary = bin(int (octets[0]))
first_octet_hex = hex(int(octets[0]))

print "\n%-20s %-20s %-20s" % ("Your IP", "Your IP in Binary", "Your IP in Hex")
print "%-20s %-20s %-20s" % (ip_number, first_octet_binary, first_octet_hex)
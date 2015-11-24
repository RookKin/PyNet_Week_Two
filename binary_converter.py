#Prompt the user to enter an ip address
network = raw_input("\n\nEnter an IP Address: ")


#Splits the ip address into four seperate ints
octets = network.split(".")


#Defines each seperate int into a list
first_octet = bin(int(octets[0]))
second_octet = bin(int(octets[1]))
third_octet = bin(int(octets[2]))
fourth_octet = bin(int(octets[3]))

#Converts the ip address into binary and displays the result in a table
#with the octets as headers
print "\n\n%15s %15s %15s %15s" % ("first Octet", "Second Octet", "Third Octet", "Fourth Octet")
print "%15s %15s %15s %15s\n\n" % (first_octet, second_octet, third_octet, fourth_octet)


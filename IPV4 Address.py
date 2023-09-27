
def is_valid_ipv4(ip):
    # Split the IP address into its octets
    octets = ip.split(".")

    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False

    try:
        # Check if each octet is a valid integer in the range [0, 255]
        for octet in octets:
            value = int(octet)
            if value < 0 or value > 255:
                return False
    except ValueError:
        # If conversion to int fails, it's not a valid IPv4 address
        return False
    
    return True

# Input the IP address you want to validate
ip_address = input("Enter an IPv4 address: ")

if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
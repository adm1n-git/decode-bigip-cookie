
import sys

def extract_ip_from_cookie(ip_dec):
    ip_hex = hex(int(ip_dec))[2:].upper()
    ip_hex_reverse = [ip_hex[index:index+2] for index in range(6,-1,-2)]
    return [int(ip_hex_reverse[index], 16) for index in range(0,4,1)]  

def extract_port_from_cookie(port_dec):
    port_hex = hex(int(port_dec))[2:].upper()
    port_hex_reverse = [port_hex[index:index+2] for index in range(2,-1,-2)]
    return int("".join(port_hex_reverse), 16)

def main(cookie):
    ip_dec, port_dec, other = cookie.split(".")
    ip = extract_ip_from_cookie(ip_dec)
    port = extract_port_from_cookie(port_dec)

    print(f"\n[+] The Cookie \"{cookie}\" has been successfully decoded.")
    print(f"[+] IP: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}")
    print(f"[+] Port: {port}\n")

if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        print(f"\n[+] Usage: {sys.argv[0]} cookie-string")
        sys.exit(1)
    else:
        if len(sys.argv[1].split(".")) != 3:
            print("\n[-] The Cookie is in an invalid format. Please provide the F5 cookie to decode.")
            sys.exit(1)
        else:
            main(sys.argv[1])

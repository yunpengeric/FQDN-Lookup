#!/usr/bin/python3
import subprocess,sys
def fqdnLookup(input,output):
    with open(input) as ipFile:
        try:
            ipAddresses = ipFile.readlines()
            fqdns = []
            for ipAddress in ipAddresses:
                fqdn = subprocess.check_output("host " +ipAddress, shell=True)
                fqdns.append(fqdn)
        finally:
            ipFile.close()
    with open(output, "x") as fqdnFile:
        try:
            fqdnFile.write(str(fqdns))
        finally:
            fqdnFile.close()
            
if __name__ == "__main__":
    input = str(sys.argv[1])
    output = "output.txt"
    fqdnLookup(input,output)

        
        

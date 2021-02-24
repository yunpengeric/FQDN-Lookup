#!/usr/bin/python3
import subprocess
import sys


def fqdnLookup(input, output):
    with open(input) as ipFile:
        try:
            ipAddresses = ipFile.read().splitlines()
            fqdns = []
            for ipAddress in ipAddresses:
                if ipAddress != "":
                    fqdn = subprocess.check_output("host -W 2 " + ipAddress, shell=True)
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
    fqdnLookup(input, output)

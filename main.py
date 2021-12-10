#!/usr/bin/python3.6
import os
import subprocess as sb
import time
from cfg import data
from pathlib import Path


def main():
    pwd = Path(__file__).resolve().parent
    os.chdir(pwd)
    while True:
        availability = True if os.system(f"ping -c 4 {data['mainIP']}") is 0 else False
        bind = True if data['mainInterface'] in \
                str(sb.check_output('./client.sh DescribeAddresses', shell = True)) else False
        if availability and not bind:
            os.system(f"./client.sh AssociateAddress PublicIp {data['publicIP']} \
                        NetworkInterfaceId {data['mainInterface']}")
        elif not availability and bind:
            os.system(f"./client.sh AssociateAddress PublicIp {data['publicIP']} \
                        NetworkInterfaceId {data['additionalInterface']}")
        time.sleep(data['freacuency'])


if __name__ == '__main__':
    main()


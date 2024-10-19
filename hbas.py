import os
import sys
import zipfile
import argparse
import requests
import time

# Main Command Line functions
parser = argparse.ArgumentParser(prog='HBAS-Downloader-CLI', description='Downloads Homebrew via CLI')
parser.add_argument('-p', '--platform', type=str, required=True, help="The console you use")
parser.add_argument('-d', '--download', type=str, required=True, help="Downloads the app (make sure to input it with .zip at the end)")

args = parser.parse_args()
# Download functions
def wii_u_download(url):
    directory = input("Enter a directory name (This includes drive letters as well)")
    wiiu_resp = requests.get(url)
    wiiu_file_path = 'wiiu_downloaded.zip'
    with open(wiiu_file_path, 'wb') as wiiu_file:
        wiiu_file.write(wiiu_resp.content)
        with zipfile.ZipFile(wiiu_file_path, 'r') as wiiu_ex:
            wiiu_ex.extractall(directory)
        print("Successfully downloaded your app!")

def nx_download(url):
    directory = input("Enter a directory name (This includes drive letters as well)")
    nx_resp = requests.get(url)
    nx_file_path ='nx_downloaded.zip'
    with open(nx_file_path, 'wb') as nx_file:
        nx_file.write(nx_resp.content)
        with zipfile.ZipFile(nx_file_path, 'r') as nx_ex:
            nx_ex.extractall(directory)
            print("Successfully downloaded your app!")
# App Downloading configuration
NX_valid = {"NX", "Nx", "Nintendo-Switch", "Nintendo-switch"}
if args.platform == "Wii-U" or args.platform == "Wii-u":
    print("Downloading your package for Wii U...")
    wii_u_download('https://wiiu.cdn.fortheusers.org/zips/' + (args.download))
elif args.platform == NX_valid:
    print("Downloading your package for Nintendo Switch...")
    nx_download('https://switch.cdn.fortheusers.org/zips/' + (args.download))
else:
    print("Argument invalid!  Aborting!")
    time.sleep(1)
    sys.exit()

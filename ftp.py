import shodan
import argparse
import pyfiglet

ascii_banner = pyfiglet.figlet_format("shadow Krd")
asci_banner = pyfiglet.figlet_format("ftp server")
print(ascii_banner)
print(asci_banner)

SHODAN_API_KEY = "EJV3A4Mka2wPs7P8VBCO6xcpRe27iNJu"

def search_ftp_default_credentials(query):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search(query)
        print(f"Total results found: {results['total']}")

        for result in results['matches']:
            ip = result['ip_str']
            print(f"\nIP: {ip}")
            try:
                ftp = result['ftp']
                if ftp['anonymous']:
                    print("Default credentials: anonymous:anonymous")
                else:
                    print(f"Default credentials: {ftp['user']}:{ftp['pass']}")
            except KeyError:
                print("FTP data not available.")
    except shodan.APIError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for FTP servers with default credentials using Shodan.")
    parser.add_argument("query", help="Shodan search query to find FTP servers.")
    args = parser.parse_args()

    search_ftp_default_credentials(args.query)

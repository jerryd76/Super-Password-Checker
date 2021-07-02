import requests
import hashlib

mypass = "poda0punda"


def response_api(sha1_pass):
    url = 'https://api.pwnedpasswords.com/range/' + sha1_pass[:5] # want only first 5 chracter due to security
    response = requests.get(url)
    return checker(sha1_pass,response)

def get_hash(password):
    sha1_pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  # hexdigest converts hashobject to hex digits
    return response_api(sha1_pass)

def checker(sha1_pass,response):
    hashes = (line.split(':') for line in response.text.splitlines())
    """ splitlines() converts string to list of lines
        Now hashes are tupel that has list as an object where 1st item of list is hash and 2nd item is count
    """
    for hash,count in hashes:
        if hash == sha1_pass[5:]:
            return count
    return 0


count = get_hash(mypass)
if count!=0:
    print(f"Your Password {mypass} has been hacked {count} times... ")
else:
    print("your password is safe ...keep it up")

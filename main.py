import requests
import webbrowser
from bs4 import BeautifulSoup

login_url = 'https://teaching.pupilfirst.org/users/sign_in'
get_magic_link_url = 'https://teaching.pupilfirst.org/get_magic_link'

def extract_authenticity_token(html):
    soup = BeautifulSoup(html, 'html.parser')
    meta_tag = soup.find('meta', attrs={'name': 'csrf-token'})
    return meta_tag['content'] if meta_tag else None

def login(email):
    session = requests.Session()

    # Extract token
    response = session.get(login_url)
    authenticity_token = extract_authenticity_token(response.text)

    data = {
        'email': email,
        'authenticity_token': authenticity_token
    }

    # Send POST to login
    response = session.post(get_magic_link_url, data=data)

    if response.status_code == 200:
        print(f"Magic Link sent: {email}. Status Code: {response.status_code}. AuthToken: {authenticity_token}")
    else:
        print(f"Failed: {email}. Status Code: {response.status_code} AuthToken: {authenticity_token}")

# List of email addresses to use for login attempts
email_addresses = [ ]

# Perform login attempts
for i in range(10):
    for email in email_addresses:
        login(email)

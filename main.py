import requests
from bs4 import BeautifulSoup
import os

def scrape_website(url):
    """Scrapes basic information from the given website URL."""

    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and extract elements - Customize based on your target website
    title = soup.find('title').text  
    all_paragraphs = [p.text for p in soup.find_all('p')]  
    links = [a['href'] for a in soup.find_all('a', href=True)] 

    print("Title:", title)
    print("Paragraphs:", all_paragraphs)
    print("Links:", links)

if __name__ == "__main__":
    username = input("Enter the username to scrape: ")
    scrape_website(f"https://instagram.com/{username}")
    os.system(f'mkdir {username}')

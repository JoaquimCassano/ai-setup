import openai
import requests
from bs4 import BeautifulSoup

def get_website_css(url:str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        html = BeautifulSoup(response.content, 'html.parser')
        styles = html.find_all('link', rel='stylesheet')
        css_content = ""
        for style in styles:
            css_url = style['href']
            if not css_url.startswith('http'):
                css_url = url + css_url
            css_response = requests.get(css_url)
            if css_response.status_code == 200:
                css_content += css_response.text + "\n"
        return css_content
    else:
        raise Exception(f"Failed to retrieve CSS from {url}")

if __name__ == "__main__":
    url = "https://motherduck.com/"
    css = get_website_css(url)
    print(css)
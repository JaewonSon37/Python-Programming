## Name: Jaewon Son
## Date: October 18 2023
## Honor Statement: I have not given or received any unauthorized assistance on this assignment.
## Link: https://youtu.be/YjGfYAnS0sE


from html.parser import HTMLParser
from collections import Counter
from urllib.parse import urljoin
import requests


class LinkParser(HTMLParser):

    """A HTMLParser to extract links from HTML content.
    """

    def __init__(self):

        """Initializes the parser and the inital link.
        """

        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):

        """Handle start tags in the HTML content and extract links if found.
        """

        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])


def extract_links(url):

    """Extrach links from a webpage.

    Returns:
        list: Returns a list of extracted links.
    """

    try:
        response = requests.get(url)
        parser = LinkParser()
        parser.feed(response.text)
        return parser.links
    
    except Exception as e:
        return []


class TextParser(HTMLParser):

    """A HTMLParser to extract text content from HTML content.
    """

    def __init__(self):

        """Initializes the parser.
        """

        super().__init__()
        self.in_text = False
        self.text = ""

    def handle_starttag(self, tag, attrs):

        """Handle start tags in the HTML content and identify text content.
        """

        if tag in ('p', 'a'):
            self.in_text = True

    def handle_data(self, data):

        """Handle text content data within HTML tags.
        """

        if self.in_text:
            self.text += data

    def handle_endtag(self, tag):

        """Handle end tags in the HTML content and stop text accumulation if necessary.
        """

        if tag in ('p', 'a'):
            self.in_text = False


def count_words_on_website(url, word_counter):

    """Count words on a webpage.
    """

    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

        if response.status_code == 200:   # When A request is successful
            parser = TextParser()
            parser.feed(response.text)   
            tokens = parser.text.split()   # Split a string to token
            word_counter.update(tokens)

    except Exception as e:
        return []


start_url = "http://cdm.depaul.edu"   # Start crawling from here
maximum_cap = 1000   # Maximum cap on the number of visited links
visited_urls = set([start_url])
to_crawl = [start_url]
word_counter = Counter()


while to_crawl and len(visited_urls) < maximum_cap:

    current_url = to_crawl.pop(0)   # Remove a old link and return a new link

    links_on_page = extract_links(current_url)   # A list of extracted links

    for link in links_on_page:
        if link is not None and not link.startswith("http://cdm"):
            link = urljoin(current_url, link)
        if link is not None and link not in visited_urls:
            visited_urls.add(link)
            to_crawl.append(link)


websites_to_visit = visited_urls

for website in websites_to_visit:
    count_words_on_website(website, word_counter)

common_words = word_counter.most_common(25)   # Find the 25 most common words and store into a list

for word, count in common_words:
    print(f"{word}: {count}")

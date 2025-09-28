import feedparser

# URL of the cryptocurrency news RSS feed
RSS_URL = 'https://cointelegraph.com/rss'  # Cointelegraph RSS feed as an example


def fetch_crypto_news(url):
    """Fetches the latest crypto news headlines from the given RSS feed URL.
    Returns a list of (title, link) tuples.
    """
    feed = feedparser.parse(url)
    headlines = []
    for entry in feed.entries[:10]:  # Limit to the first 10 headlines
        headlines.append((entry.title, entry.link))
    return headlines


if __name__ == '__main__':
          news = fetch_crypto_news(RSS_URL)
          print('Latest Crypto News Headlines:')
          for i, (title, link) in enumerate(news, 1):
        # Print the headline and link on separate lines with indentation
        print(f"{i}. {title}\n   {link}\n")

import logging
import sys
from berga_crawler import search_with_info

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

def test():
    print("Starting crawler for cartacapital.com.br...")
    feed = search_with_info("http://cartacapital.com.br")

    print("\n--- TEST RESULTS ---")
    print(f"Feeds found: {len(feed.feeds)}")
    for f in feed.feeds:
        print(f" - {f.url}")
    
    if feed.root_error:
        print(f"Root Error: {feed.root_error.message} (Type: {feed.root_error.error_type})")

    return feed

if __name__ == "__main__":
    test()

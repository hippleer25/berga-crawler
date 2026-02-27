import logging
import sys
from berga_crawler import search_with_info

# Setup logging to see what's happening
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

# Use a site that is likely to work
result = search_with_info("https://pypi.org")

print(f"\nFeeds found: {len(result.feeds)}")
for feed in result.feeds:
    print(f"Feed: {feed.url}, Score: {feed.score}")

if result.root_error:
    print(f"Root Error: {result.root_error.message}")
    print(f"Error Type: {result.root_error.error_type}")

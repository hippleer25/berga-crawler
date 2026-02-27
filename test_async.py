import asyncio
import logging
import sys
import time
from berga_crawler import search_async_with_info

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

async def main():
    url = "https://pypi.org"
    
    print(f"Starting async search for {url}...")
    start_time = time.perf_counter()
    
    # Run async search
    result = await search_async_with_info(url, include_stats=True)
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    
    print(f"\nAsync search finished in {duration:.2f} seconds")
    print(f"Feeds found: {len(result.feeds)}")
    for feed in result.feeds:
        print(f"Feed: {feed.url}, Score: {feed.score}")
        
    if result.stats:
        print(f"\nStats: Requests Queued: {result.stats.get('requests_queued')}")
        print(f"Stats: Successful: {result.stats.get('requests_successful')}")

if __name__ == "__main__":
    asyncio.run(main())

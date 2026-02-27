from berga_crawler import search_with_info
import logging
import sys

# Suppress noisy logs for this specific test
logging.getLogger("berga_crawler").setLevel(logging.WARNING)

def run_test():
    feed = search_with_info("http://cartacapital.com.br")

    print(feed)
    return feed

if __name__ == "__main__":
    run_test()

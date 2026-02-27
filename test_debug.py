import logging
import sys
from berga_crawler import search_with_info

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

def test():
    print("Testing cartacapital.com.br")
    result = search_with_info("http://cartacapital.com.br")
    print("Feeds found count:")
    print(len(result.feeds))
    if result.root_error:
        print("Error:")
        print(result.root_error.message)

if __name__ == "__main__":
    test()

from berga_crawler import search_with_info
import json

def run_test():
    result = search_with_info("http://cartacapital.com.br")
    print(json.dumps(result.serialize(), indent=2))

if __name__ == "__main__":
    run_test()

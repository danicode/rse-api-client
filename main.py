from rse_api_client import RSEAPIClient

def main():
    client = RSEAPIClient()
    response = client.make_request('get', 'jobs')
    print("Response: ", response)

if __name__ == "__main__":
    main()

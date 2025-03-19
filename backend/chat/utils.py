import json

import requests
from dotenv import load_dotenv
import os

load_dotenv()


def generate_serpapi_params(query, location):
    return {
        "q": query,
        "location": location or "egypt",
        "api_key": os.getenv("SERP_API_KEY")
    }



def get_product_link(serpapi_product_link):
    session = requests.Session()
    cookies = {"api_key": os.getenv("SERP_API_KEY") , "_SerpAPI_session" : "zFsA0OHbJqDVdVvASCvZe1KHYljATAX8mnPEWHJlWXgkE29%2F02TN4pfI9Pdx9gCrNNjMaPB8tWkA41%2FxoFnPDrJDBwzHe3AweaIHA%2BE4NgwLcd%2FPzXiRnAmlEOf0lCWrbXYnBcG%2BK%2BaY6PbYfDVtI3R3wJrlRWb67Vz67x6hLy1OsduwAzmIKd1kXA5U0FTEUxZOkvy79%2FHcpt%2B2T7znFL9I1%2FlARJkEOhqARePtNqW9u5ac%2FRuo0Y7YMjLbPxhLeehtCo7GaUKNkpHf3LA2T2Ws1JFH0Gt8wbXHNShu3hak4wT8lwyAMMtPOu7%2BxsN976UKPFIioS00g7np1Tgqihiwtb5xHHZkm0r8gIAb5AE2AjtjkoiOq3VRRKOk81LO0kZai0OZvvnSWGVPagWl7MmteJvzNFSB4V83p%2Bzawj8cAYOObk%2BvK1XUCa0%3D--DL6gU4vdZiyytGjw--MuzSQsxWkMOFh4puS3I3fQ%3D%3D"}

    response = requests.get(serpapi_product_link , cookies=cookies)

    direct_link = response.json()["sellers_results"]["online_sellers"][0]["direct_link"]
    print(direct_link)

    return direct_link
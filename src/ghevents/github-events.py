#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
    """Fetches GitHub events data"""
    result_text = requests.get(url).text
    events_data = json.loads(result_text)
    return events_data

def print_events(events, n=5):
    """Prints formatted event type and repo name for the first n events."""
    for x in events[:n]:
        event = x["type"] + " :: " + x["repo"]["name"]
        print(event)

def main():
    """Main function to print the values of GHUSER and url, and fetch and print the list of events"""
    print(GHUSER)
    print(url)
    list_events = retrieve_events(url)
    print_events(list_events)

if __name__ == "__main__":
    main()


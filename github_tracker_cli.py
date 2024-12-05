import sys
import requests

def handle_event(event):
    event_handlers = {
        "IssueCommentEvent": lambda e: f"- commented on issue {e['payload']['issue']['number']}",
        "PushEvent": lambda e: f"- pushed to {e['repo']['name']}",
        "IssuesEvent": lambda e: f"- created issue {e['payload']['issue']['number']}",
        "WatchEvent": lambda e: f"- starred {e['repo']['name']}",
        "PullRequestEvent": lambda e: f"- created pull request {e['payload']['pull_request']['number']}",
        "PullRequestReviewEvent": lambda e: f"- reviewed pull request {e['payload']['pull_request']['number']}",
        "PullRequestReviewCommentEvent": lambda e: f"- commented on pull request {e['payload']['pull_request']['number']}",
        "CreateEvent": lambda e: f"- created {e['payload']['ref_type']} {e['payload']['ref']}"
    }
    
    return event_handlers.get(event['type'], lambda e: f"- {e['type']}")(event)

def get_latest_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        events = response.json()
        print(f"Latest events for {username}:")
        for event in events:
            print(handle_event(event))
    else:
        print(f"Error fetching events for {username}: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_latest_events(sys.argv[1])
    else:
        print("You must enter a github username as a command line.")

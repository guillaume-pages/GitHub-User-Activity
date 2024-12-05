# GitHub-User-Activity

Link to the project : https://roadmap.sh/projects/github-user-activity

In this project, you will build a simple command line interface (CLI) to fetch the recent activity of a GitHub user and display it in the terminal. This project will help you practice your programming skills, including working with APIs, handling JSON data, and building a simple CLI application.

### Requirements

The application should run from the command line, accept the GitHub username as an argument, fetch the user’s recent activity using the GitHub API, and display it in the terminal. The user should be able to:

Provide the GitHub username as an argument when running the CLI :

```
github-activity <username>
```

Fetch the recent activity of the specified GitHub user using the GitHub API. You can use the following endpoint to fetch the user’s activity:

```
# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events
```

Display the fetched activity in the terminal.

```
Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- ...
```

You can learn more about the GitHub API here.
Handle errors gracefully, such as invalid usernames or API failures.
Use a programming language of your choice to build this project.
Do not use any external libraries or frameworks to fetch the GitHub activity.

## My Solution

### Installation

1. Clone the repository

```
git clone git@github.com:guillaume-pages/GitHub-User-Activity.git
```

Run the script with :

```
python3 github_tracker_cli.py <username>
```

Code :
```python
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
```

Output :

```
python3 github_tracker_cli.py guillaume-pages
Latest events for guillaume-pages:
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- pushed to guillaume-pages/task-tracker
- created branch master
- created repository None
- pushed to guillaume-pages/second-frontend-mentor
- created branch main
- created repository None
- created repository None
- pushed to guillaume-pages/first-frontend-mentor
- pushed to guillaume-pages/first-frontend-mentor
- created branch main
- created repository None
- starred unicodeveloper/awesome-nextjs
- starred Dokploy/dokploy
- PublicEvent
- pushed to guillaume-pages/guillaume-pages
- pushed to guillaume-pages/guillaume-pages
- ForkEvent
- ForkEvent
- starred stackblitz/bolt.new
- starred stackblitz/bolt.new
- starred Grace-Rasaily780/boringfinance
- starred kamranahmedse/developer-roadmap

```
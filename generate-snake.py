import requests
import os

USERNAME = 'karreemm'
TOKEN = os.getenv('GITHUB_TOKEN')

def fetch_commits(username, token):
    events = []
    page = 1
    while True:
        url = f'https://api.github.com/users/{username}/events?page={page}'
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            batch = response.json()
            if not batch:
                break
            events.extend(batch)
            page += 1
        else:
            print(f"Failed to fetch events: {response.status_code}")
            break
    return events

def generate_snake_animation(events):
    # Implement your logic to create the snake animation from events
    commit_events = [event for event in events if event['type'] == 'PushEvent']
    animation_data = f"Generated Snake Animation with {len(commit_events)} push events"
    os.makedirs('dist', exist_ok=True)
    with open('dist/snake.svg', 'w') as f:
        f.write(animation_data)

if __name__ == "__main__":
    commits = fetch_commits(USERNAME, TOKEN)
    generate_snake_animation(commits)

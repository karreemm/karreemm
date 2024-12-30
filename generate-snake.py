import requests
import os
from datetime import datetime, timedelta

USERNAME = 'karreemm'
TOKEN = os.getenv('GITHUB_TOKEN')

def fetch_commits(username, token):
    commits = []
    page = 1
    # Get the date one year ago from today
    since = (datetime.now() - timedelta(days=365)).isoformat()
    while True:
        url = f'https://api.github.com/repos/{username}/{username}.github.io/commits?since={since}&page={page}&per_page=100'
        headers = {'Authorization': f'token {token}'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            batch = response.json()
            if not batch:
                break
            commits.extend(batch)
            page += 1
        else:
            print(f"Failed to fetch commits: {response.status_code}")
            break
    return commits

def generate_snake_animation(commits):
    # Implement your logic to create the snake animation from commits
    animation_data = f"Generated Snake Animation with {len(commits)} commits"
    os.makedirs('dist', exist_ok=True)
    with open('dist/snake.svg', 'w') as f:
        f.write(animation_data)

if __name__ == "__main__":
    commits = fetch_commits(USERNAME, TOKEN)
    generate_snake_animation(commits)


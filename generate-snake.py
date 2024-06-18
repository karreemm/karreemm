# generate_snake.py
import requests
import datetime
import os

USERNAME = 'karreemm'
TOKEN = os.getenv('GITHUB_TOKEN')

def fetch_commits(username, token):
    url = f'https://api.github.com/users/{username}/events'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return []

def generate_snake_animation(commits):
    # Implement your logic to create the snake animation from commits
    # This is a placeholder for the actual snake animation generation logic
    animation_data = f"Generated Snake Animation with {len(commits)} commits"
    with open('dist/snake.svg', 'w') as f:
        f.write(animation_data)

if __name__ == "__main__":
    commits = fetch_commits(USERNAME, TOKEN)
    generate_snake_animation(commits)

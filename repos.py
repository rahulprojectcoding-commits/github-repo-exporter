import requests
import csv
def fetch_all_repos(username):
    all_repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException:
            print("Could not reach GitHub. Check your internet connection and try again.")
            return None
        if response.status_code != 200:
            print(f"Could not fetch repos for {username} (status {response.status_code})")
            return None
        data = response.json()
        if not data:
            break
        all_repos.extend(data)
        page += 1
    return all_repos

def clean_repos(repos):

    rows = []
    if repos is not None:
    
        for repo in repos:
            language = repo["language"]
            if language is None:
                language = "Unknown"
            rows.append({"name":repo["name"], "language":language, "stars":repo["stargazers_count"]})
        return rows

def save_csv(rows,filename):
    heads = ["name","language","stars"]
    with open(filename,"w",newline="") as f:
        writer =  csv.DictWriter(f,fieldnames =heads)
        writer.writeheader()
        writer.writerows(rows)

def ask_top_n():
    while True:
        text = input("How many top repos to show? ").strip()
        try:
            n = int(text)
            if n > 0:
                return n
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")
    
    

def top_repos(rows,n):
    top_rows = sorted(rows, key=lambda r: r["stars"], reverse=True)[:n]
    return top_rows
    

def main():
    
    username = input("GitHub username: ").strip()
    if not username:
        print("Please enter a username")
        return
    repos = fetch_all_repos(username)
    if repos is None:
        return
    rows =clean_repos(repos)
    filename = f"{username}.csv"
    save_csv(rows, filename)
    print(f"Saved {len(rows)} repos to {filename}")
    n = ask_top_n()
    top =top_repos(rows, n)
    shown = min(n, len(rows))
    print(f"Top {shown} repos by stars:")
    for repo in top:
        print(f"{repo['name']} {repo['language']} {repo['stars']}")

main()
    








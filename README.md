# GitHub Repo Exporter

A small command-line tool that takes a GitHub username, downloads all of that user's public repositories, saves them to a CSV file you can open in Excel, and shows the most-starred ones.

## What it does

- Asks for a GitHub username
- Fetches **every** public repo, including users with more than 100 (it reads all pages from the GitHub API)
- Cleans the data: repos with no detected language are labelled `Unknown`
- Saves `name`, `language` and `stars` to `<username>.csv`
- Asks how many top repos to show, and prints them sorted by stars
- Handles problems without crashing: empty input, unknown users, no internet connection

## Requirements

- Python 3.15 or newer
- The `requests` library

## How to run

```
pip install requests
python repos.py
```

Then enter a GitHub username (for example `octocat`) and a number of top repos to display.

## Example output

```
GitHub username: octocat
Saved 8 repos to octocat.csv
How many top repos to show? 3
Top 3 repos by stars:
Spoon-Knife HTML 14124
Hello-World Unknown 3858
octocat.github.io CSS 1186
```

Star counts are live data, so the numbers will differ when you run it.

## Output file

`<username>.csv` is created in the same folder, with the columns `name`, `language`, `stars`. Running the tool again for the same user overwrites the file.

## Limitations

- Uses GitHub's public API without a login, which allows about 60 requests per hour. Very large accounts, or many runs in a row, can hit that limit (you will see status 403).
- Only public repositories are included.
- No automated tests yet.
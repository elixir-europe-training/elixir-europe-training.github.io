import requests
import json

# get metadata from all repositories in the organization "elixir-europe-training" from the GitHub API
# this includes the repository name, the description, the website and the number of stars
# the metadata is written to a json file called "repos.json"

# get the list of repositories in the organization
url = "https://api.github.com/orgs/elixir-europe-training/repos"
response = requests.get(url)
repos = response.json()

# create a list of dicts that each as three items:
    # 1. an item called 'title' with the name of the repository
    # 2. an item called content with the description, homepage and stargazers in a list in markdown format
    # 3. an item called 'image' that uses the file in docs/images/elixir_image.png as the image

# order repo dict by stargazers_count
repos = sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)

# get metadata for each repository
metadata = []
for repo in repos:
    if repo["description"] is None:
        repo["description"] = ""
    metadata.append({
        "title": repo["name"],
        "url": repo["homepage"],
        "content": f"{repo['description']} :star: {repo['stargazers_count']}",
        "image": "assets/images/white-orange-logo.png"
    })

# write the metadata to a json file called docs/assets/cards/repos.json
with open("docs/assets/cards/repos.json", "w") as f:
    json.dump(metadata, f, indent=4)


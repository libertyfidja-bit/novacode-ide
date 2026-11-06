import base64
import urllib.request
import json

class GitRepoClient:
    """Loads and commits files to remote Git repositories via REST API."""
    BASE_URL = "https://api.github.com"

    def fetch_repo_tree(self, owner: str, repo: str, branch: str = "main"):
        url = f"{self.BASE_URL}/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json"
        })
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def encode_content(self, text: str) -> str:
        return base64.b64encode(text.encode("utf-8")).decode("ascii")
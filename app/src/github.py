import httpx

class GithubApi():
    def __init__(self) -> None:
        self.url = "https://api.github.com/repos/seo888/MirrorElf/releases/latest"
    
    def get_new_version(self):
        
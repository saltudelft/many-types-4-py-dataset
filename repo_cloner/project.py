class Project:
    def __init__(self, json_repo):

        #print(json_repo["private"])
        self.id = json_repo["id"] # pylint: disable=invalid-name
        self.full_name = json_repo["full_name"]
        self.name = json_repo["name"]
        self.description = json_repo["description"]
        self.html_url = json_repo["html_url"]
        self.clone_url = json_repo["clone_url"]
        self.language = json_repo["language"]
        self.stargazers_count = json_repo["stargazers_count"]
        self.size = json_repo["size"]
        self.fork = json_repo["fork"]
        self.fork_count = json_repo["forks_count"]
        self.watch_count = json_repo["watchers_count"]
        self.created_at = json_repo["created_at"]
        self.updated_at = json_repo["updated_at"]
        self.license = json_repo.get("license")
        # self.license = json_repo["license"]['name'] if json_repo["license"] is not None else "None"

    def __eq__(self, other):
        return self.full_name == other.full_name

    def __hash__(self):
        return hash(self.full_name)


# To encapsulate another JSON format
class GitProject:
    def __init__(self, json_repo):

        self.name = json_repo["repo"]
        self.author = json_repo["author"]
        self.full_name = self.author + "/" + self.name
        self.clone_url = json_repo["repoUrl"] + ".git"
        self.stargazers_count = json_repo["stars"]
        self.fork_count = json_repo["forks"]


def base_url():
    return "https://api.github.com"


def get_repos_url(username):
    return "https://api.github.com/users/" + username + "/repos"


def get_single_repo_url(username, repo_name):
    return "https://api.github.com/repos/" + username + "/" + repo_name

def post_repo_url():
    return "https://api.github.com/user/repos"


def patch_repo_url(username, repo_name):
    print("https://api.github.com/repos/" + username + "/" + repo_name)
    return "https://api.github.com/repos/" + username + "/" + repo_name


def delete_repo_url(username, repo_name):
    return "https://api.github.com/repos/" + username + "/" + repo_name

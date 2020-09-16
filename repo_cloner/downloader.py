import os.path as path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
from urllib.error import HTTPError
import subprocess
import logging
import json

from repo_cloner.project import Project, GitProject


def is_repo_accessible(url: str) -> bool:
    try:
        urlopen(url)
        return True
    except HTTPError:
        return False


def download_git_project(project, output_dir, full_fetch=False):
    command = ["git", "clone"]
    if not full_fetch:
        command += ["--depth", "1"]
    command += [project.clone_url, output_dir]
    subprocess.run(command)


def download_project(project: GitProject, output_base_dir, full_fetch=False):
    try:
        output_dir = path.join(output_base_dir, project.full_name)
        if path.isdir(output_dir):
            logging.info("%s already exists", project.full_name)
            return False
        if is_repo_accessible(project.clone_url):
            download_git_project(project, output_dir, full_fetch=full_fetch)
            return True
        else:
            print("The project %s doesn't exist or it's private." % project.clone_url)
            return False
    except Exception as e: # pylint: disable=broad-except
        logging.warning("could not download %s: %s", project.full_name, e)


def download_projects(projects, output_dir, full_fetch=False):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda p: download_project(p, output_dir, full_fetch=full_fetch), projects)


def load_projects_from_file(input_file):
    with open(input_file, "r") as f:
        return [Project(project) for project in json.load(f)]


def load_projects(input_file, num_projects):

    gh_projects = []
    with open(input_file, "r") as f:

        for i, p in enumerate(json.load(f)):

            # Stop loading projects after a certain number
            # if not i >= num_projects:

            gh_projects.append(GitProject(p))

            # else:
            #     break

    return gh_projects


def download_projects_command(args):
    #projects = load_projects_from_file(args.input_file)
    projects = load_projects(args.input_file, 500)

    download_projects(projects, args.output_dir)

from argparse import ArgumentParser
from repo_cloner.downloader import download_projects_command


def main():

    arg_parser = ArgumentParser(description="A tool for cloning GitHub repositories")
    arg_parser.add_argument("-i", "--input-file", required=True, help="JSON file containing projects' characteristics")
    arg_parser.add_argument("-o", "--output-dir", required=True, help="directory where to download projects")

    args = arg_parser.parse_args()
    download_projects_command(args)


if __name__ == '__main__':

    main()

from file.Blacklist import Blacklist
from file.GitRepositoriesFinder import GitRepositoriesFinder
from git_sync.GitRepoOperations import GitRepoOperations
import logging
import argparse


def main():
    logging.basicConfig(format='%(asctime)s [%(threadName)s] %(levelname)s %(filename)s:%(lineno)d [logtoken] %(message)s',
                        level=logging.INFO)
    logging.info('Started')
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseDir", required=True, dest="base_dir", help="base directory from which to start searching for git repositories")
    parser.add_argument("--blacklistPath", default="./blacklist.txt", dest="blacklist_path", help="path to a blacklist file (including file name) containing all repositories which should not be synced")
    parser.add_argument("--searchDepth", type=int, default=1, dest="search_depth", help="depth of search for git repositories from base directory")

    args = parser.parse_args()

    git_repos = GitRepositoriesFinder(args.base_dir, args.search_depth).get_repos()
    git_repos = Blacklist(args.blacklist_path).filter(git_repos)
    GitRepoOperations(git_repos).sync_repositories()

    logging.info('Finished')


if __name__ == '__main__':
    main()

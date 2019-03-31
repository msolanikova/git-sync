from git import Repo, GitCommandError

from file.Blacklist import Blacklist
import logging


class GitRepoOperations:

    def __init__(self, repo_folders):
        self.repo_folders = repo_folders

    def sync_repositories(self):
        """ Execute git pull on all local repository folders """

        for repo_folder in self.repo_folders:
            self.__sync_repository(repo_folder)

    def __sync_repository(self, repo_folder):
        """ Execute git pull on local repository folder """

        repo = Repo(repo_folder)
        logging.debug("Going to pull %s", repo)
        try:
            repo.remotes.origin.pull()
            logging.info("Repo %s synced successfully", repo)
        except GitCommandError as err:
            logging.error("Git error on repo %s: %s", repo, err)


import os
import logging

from utils.OsUtils import OsUtils


class GitRepositoriesFinder:
    """ Finds all git_sync repositories folders in work_dir directory """

    def __init__(self, base_dir, search_depth=2):
        if not os.path.exists(base_dir):
            raise ListRepoError('[%s] does not exist!' % base_dir)
        if not os.path.isdir(base_dir):
            raise ListRepoError('[%s] is not a directory!' % base_dir)
        self.base_dir = OsUtils.norm(base_dir)
        self.search_depth = search_depth
        self.__repos = []

    def get_repos(self):
        if not self.__repos:
            self.load_repos()

        return self.__repos

    def load_repos(self):
        if os.path.exists(os.path.join(self.base_dir, '.git')):
            self.__repos.append(OsUtils.norm(self.base_dir))
            logging.debug("Git repositories found: %s", self.__repos)
            return

        # way to iterate over all dirs to search_depth depth
        for root, dirs, files in os.walk(self.base_dir, topdown=True):
            depth = root[len(self.base_dir) + len(os.path.sep):].count(os.path.sep)

            # for each dir find out whether it is a git_sync repository
            for dir in dirs:
                git_folder_path = os.path.join(root, dir, '.git')
                if os.path.exists(git_folder_path):
                    self.__repos.append(OsUtils.norm(os.path.join(root, dir)))

            if depth == self.search_depth:
                # We're currently search_depth directories in, so all subdirs have depth search_depth+1
                dirs[:] = []  # Don't recurse any deeper

        logging.debug("Git repositories found: %s", self.__repos)
        if not self.__repos:
            logging.warning("No git repositories found under %s", self.base_dir)
        return


class ListRepoError(Exception):
    pass

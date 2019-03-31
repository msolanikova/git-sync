import os
import logging

from utils.OsUtils import OsUtils


class Blacklist:

    def __init__(self, file='./blacklist.txt'):
        self.file = file
        self.__blacklisted_repos = self.__load_blacklist()
        if self.__blacklisted_repos:
            logging.debug("Blacklisted repositories: %s", self.__blacklisted_repos)

    def __load_blacklist(self):
        if not os.path.exists(self.file):
            logging.info("Blacklist file [%s] was not found, no folder blacklisted", self.file)
            return

        with open(self.file) as f:
            content = f.readlines()

        return [self.__process_line(line) for line in content if line and not line.startswith("#")]

    def __process_line(self, line):
        return OsUtils.norm(line.replace(os.linesep, '').replace('\n', ''))

    def filter(self, repos_to_filter):
        """ Filter out all repositories that are blacklisted """
        repos_to_sync = []
        for repo in repos_to_filter:
            if repo in self.__blacklisted_repos:
                logging.info("Blacklisted: %s - will not be synced", repo)
            else:
                repos_to_sync.append(repo)

        return repos_to_sync

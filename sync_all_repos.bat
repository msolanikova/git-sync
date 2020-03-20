@echo off
set GIT_SYNC_RUNNER_PATH=c:\Development\GitRepos\private\git-sync\GitSyncRunner.py
set DIR_TO_SYNC=c:\Development\GitRepos\
set IGNORE_LIST_PATH=c:\Development\GitRepos\private\git-sync\blacklist.txt

python %GIT_SYNC_RUNNER_PATH% --baseDir %DIR_TO_SYNC% --blacklistPath %IGNORE_LIST_PATH%

set /p DUMMY=Hit ENTER to continue...

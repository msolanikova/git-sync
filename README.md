# README #

### What is this repository for? ###
Discovers all git repositories within given base folder and performs git pull on each of them. 


### Prerequisites ###
* python 3.6
* (pip install gitpython)
* (pip install logging)
* no password has to be required to access git repositories otherwise git pull will fail


### How to configure git repositories for no password? ###
* each repository should be cloned using ssh protocol instead of https. For existing repositories this can be updated e.g. in SourceTree. 
    * Example: `git@bitbucket.org:msolanikova/gitsync.git`
* new ssh keys have to be generated
    * use [puttygen.exe](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) 
    * or SourceTree (Tools -> Create or Import SSH keys)
* store private key on disk 
    * don't forget to protect it with a password - Key passphrase
* copy public key part and import it to stash / bitbucket
    * SSH keys are located in user profile / manage account section
* start [pageant.exe](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and load previously generated private key

[Note] windows users neeed to create new **user environment variable** called **GIT_SSH** where value needs to be path to [plink.exe](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)   

[Note] pageant.exe with loaded keys needs to be running when syncing git repositories


### How to use it ###

#### CMD arguments ####
* --baseDir - base directory from which to start searching for git repositories
    * in case baseDir is repo directory, no other git repos will be searched
* --blacklistPath - path to a blacklist file (including file name) containing all repositories which should not be synced
    * default value: ./blacklist.txt
    * comparison to blacklist is case insensitive
* --searchDepth - depth of search for git repositories from base directory
    * default value: 2
    * if searchDepth = 0 - all git repos listed directly in baseDir (e.g. baseDir\repoDir)
    * if searchDepth = 1 - all git repos listed in subdirectories of baseDir (e.g. baseDir\subdir\repoDir)
    * ...

Example:
```
python GitSyncRunner.py --baseDir c:\Development\GitRepos --blacklistPath c:\Development\GitRepos\blacklist.txt
```

#### Blacklist ####
There might be some repositories which given user does not own and doesn't have possibility to upload keys there. In that case such repository cannot be updated by this sync and git pull will fail. In order to avoid these failures it is possible to add given local repository to a blacklist file. 

By default, system will try to load blacklist.txt located at the same directory as GitSyncRunner.py. Each line represents a path to a repository to be blacklisted. Empty lines and lines starting with # will be excluded.

In following example, two repository folders will be blacklisted:
```
# list of all git repositories folders NOT to sync
c:\Development\GitRepos\repository1\
c:\Development\GitRepos\repository2

```  
## auto-repo

Creates a github repo from a local repo from the comfort of your shell.

## Setup

1. Clone this repo:
    `$ git clone https://github.com/daj0ker/auto-repo.git`
2. Change working directory
    `$ cd auto-repo`
3. Change permissions
    `$ chmod +x auto-repo.py`
4. Create symlink (optional)
  `$ sudo ln -s CURRENT_PATH /usr/local/bin/auto-repo`

$$ Usage

This script uses SSH based authentication. You need to add SSH keys to your github account.account

Follow [this](https://help.github.com/articles/generating-ssh-keys/) tutorial to add an SSH key to your github account. 

Assuming you're done with that,

Use 
    `$ auto-repo username reponame`
to run the script.
# Git

## Install

This is for windows:

- Download: https://git-scm.com/

> Note：https://git-scm.com/doc is good place to learn git.

- Run the setup, remenber to check `PATH` and `gitbash`

> Note: Customize gitbash: Right click on the topbar of gitbash ---> Options

# Config

```sh
git config --global user.email "youremail@email.com" user.name "yourname"
# bueatiful git lg
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

git config --global http.proxy 127.0.0.1:7890
```


# Github

This section, we will connect git and github.

Step 1: Generate `ssh key`:

Open gitbash , and goto `/c/user/<user-name>/.ssh`，Just type:

```sh
ssh-keygen -t rsa -C "<youremail@email.com>"
# If you come up with some options, just leave them blank
```

You will get the ssh key for github.

Step 2: Copy the content in `id_rsa.pub` to GitHub:

- [Github SSH Link Here](https://github.com/settings/ssh/new)
- Title: just type some note
- Key: content of `id_rsa.pub`

Step 3: Type `ssh -T git@github.com` to test your connection.

## Tips

If you have more than one github account, you can change your account like this:

 ```sh
git credential-manager delete https://github.com
 ```

See https://stackoverflow.com/questions/41689395/how-to-change-git-account-in-git-bash

# Usage

## Create

Option 1:  :1st_place_medal:

You can create a new project at https://github.com/new. Then clone it to your local folder:

```sh
git clone https://github.com/<name>/<project>.git
```

Option 2:

In the new folder, Type:

```sh
git init
```

## Track your file

Just type the following commands one by one:

```sh
git status
git add *
git commit -am "update something"
```

## Sync to GitHub:

Just type the following commands one by one:

```shell
git pull origin main
git push origin main
```

## branch

```sh
git branch <branchName>                 # create a branch
git branch -d <branchName>              # delete a branch -D:forces
git checkout <newBranchName>            # swith to new branch
git push -d <remote_name> <branch_name> # delete remote branch
```

## Misic


- Add remote repo

`git remote add <remote-name> <git@github.com:repo.git>`

- Pull special branch

`git pull <remote-name> <remote-brauch>:<local-branch>`

- Pull special branch

`git push <remote-name> <remote-brauch>:<local-branch>`



# 深入理解git

# Git object

https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

## blob 对象

往git数据库里添加文件记录。

```sh
$ echo 'test content' | git hash-object -w --stdin
d670460b4b4aece5915caf5c68d12f560a9fe3e4

$ echo 'version 1' > test.txt
$ git hash-object -w test.txt
83baae61804e65cc73a7201a7252750c76066a30
```

从git数据库里读取文件记录

```sh
$ git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4
test content
```

## tree对象

构造tree对象，往tree对象里写记录的方式有：

方式一：手动写一条记录：

```sh
git update-index --add --cacheinfo 100644 \
  83baae61804e65cc73a7201a7252750c76066a30 test.txt
```

方式二：用文件对象构造一条记录：

```sh
$ git update-index --add new.txt
```

方式三：用一个已存在的tree对象构造一条记录

```sh
$ git read-tree --prefix=name_for_this_tree d8329fc1cc938780ffdd9f94e0d364e0ea74f579

```

保存tree对象：

```sh
$ git write-tree
3c4e9cd789d88d8d89c1073707c3585e41b0e614
```

## commit 对象

```sh
$ echo 'First commit' | git commit-tree d8329f
fdf4fc3344e67ab068f836878b6c4951e3b15f3d

$ echo 'Second commit' | git commit-tree 0155eb -p fdf4fc3
cac0cab538b970a37ea1e769cbbde608743bc96d
```

## Git refs

```sh
$ echo 1a410efbd13591db07496601ebc7a059dd55cfe9 > .git/refs/heads/master
# or equival cmd
$ git update-ref refs/heads/master 1a410efbd13591db07496601ebc7a059dd55cfe9
# HEAD is current ref
$ cat .git/HEAD
ref: refs/heads/master
# or git equival cmd
$ git symbolic-ref HEAD
refs/heads/master
# You can also set the value of HEAD using the same command:
$ git symbolic-ref HEAD refs/heads/test
$ cat .git/HEAD
ref: refs/heads/test
```

Note:

If you run `git gc`, files like `refs/heads/master` may disappear.

## Git pack

```sh
 $ git verify-pack -v .git/objects/pack/pack-978e03944f5c581011e6998cd0e9e30000905586.idx
```



## Git diff

`git diff` is the diff between commits.

输出格式：

`@@ from-file-range to-file-range @@` = `@@-<start line>,<number of lines> +<start line>,<number of lines>@@`

- '+' -- A line was added here to the first file.
- '-' -- A line was removed here from the first file.

See https://stackoverflow.com/questions/2529441/how-to-read-the-output-from-git-diff



# 理解 Git 编程，python 语言实现

基于项目：https://github.com/dulwich/dulwich

[Click me for more details](https://github.com/dulwich/dulwich/blob/master/docs/tutorial/repo.txt)

Open a existing git repository :

```python
import os
from  dulwich.repo import(
  Repo
)

BASE_DIR = r'D:\tmp'

def open_repo():
  name = 'pygit2'
  repo_path = os.path.join(BASE_DIR, name, '.git')
  # repo_path = os.path.join(BASE_DIR, name)
  repo = Repo(repo_path)
  print(repo.head())
  c = repo[repo.head()]
  print(c.message)

def main():
  open_repo()
  
if __name__ == '__main__':
  main()
```

Init a repo:

```python
import os
from  dulwich.repo import(
  Repo
)

BASE_DIR = r'D:\tmp'

def init_repo():
  name = 'myrepo'
  repo_path = os.path.join(BASE_DIR, name)
  if os.path.exists(repo_path):
    print(f'{name} already exists!')
    return
  else:
    os.makedirs(repo_path)
    repo = Repo.init(repo_path)
    print(repo)

def main():
  # open_repo()
  init_repo()
  
if __name__ == '__main__':
  main()
```

Staging new files

```python
import os
import sys
from  dulwich.repo import(
  Repo
)

BASE_DIR = r'D:\tmp'

def stage_new_files():
  name = 'myrepo'
  repo_path = os.path.join(BASE_DIR, name)
	repo = Repo(repo_path)
  
  file_name = 'file0.md'
  file_content = 'hello, 中文'
  encoding = sys.getfilesystemencoding()
  file_path = os.path.join(repo_path, file_name)
  with open('file_path', 'wb') as f:
    f.write(bytes(file_content, encoding=encoding))
  repo.stage([bytes(file_name, encoding=encoding)])
  print(",".join([f.decode(encoding) for f in repo.open_index()]))

def main():
  # open_repo()
  # init_repo()
  stage_new_files()
  
if __name__ == '__main__':
  main()
```

Commiting new commits

```python
import os
import sys
from  dulwich.repo import(
  Repo
)

BASE_DIR = r'D:\tmp'

def commit_files():
  name = 'myrepo'
  repo_path = os.path.join(BASE_DIR, name)
	repo = Repo(repo_path)
  commit_message = 'my first commit'
  committer = 'Jelmer Vernooij <jelmer@samba.org>'
  encoding = sys.getfilesystemencoding()
  commit_id = repo.do_commit(bytes(commit_message, encoding=encoding), committer=bytes(committer, encoding=encoding))
  print(commit_id)
  c = repo[commit_id]
  print(c.message)
  
  
  
def main():
  # open_repo()
  # init_repo()
  # stage_new_files()
  commit_files()
  
if __name__ == '__main__':
  main()
```



List Items of a tree.

```python
import os
import sys
from io import StringIO
from  dulwich.repo import(
  Repo
)
from dulwich.porcelain import(
  ls_tree
)

BASE_DIR = r'D:\tmp'

def files():
  name = 'pygit2'
  repo_path = os.path.join(BASE_DIR, name)
  repo = Repo(repo_path)
  f = StringIO()
  ls_tree(repo=repo, outstream=f)
  print(f.getvalue())
  
  
  
def main():
  # open_repo()
  # init_repo()
  # stage_new_files()
  files()
  
if __name__ == '__main__':
  main()

'''
def ls_tree(repo, treeish=b"HEAD", outstream=sys.stdout, recursive=False,
            name_only=False):
    """List contents of a tree.
    Args:
      repo: Path to the repository
      tree_ish: Tree id to list
      outstream: Output stream (defaults to stdout)
      recursive: Whether to recursively list files
      name_only: Only print item name
    """
    def list_tree(store, treeid, base):
        for (name, mode, sha) in store[treeid].iteritems():
            if base:
                name = posixpath.join(base, name)
            if name_only:
                outstream.write(name + b"\n")
            else:
                outstream.write(pretty_format_tree_entry(name, mode, sha))
            if stat.S_ISDIR(mode) and recursive:
                list_tree(store, sha, name)
    with open_repo_closing(repo) as r:
        tree = parse_tree(r, treeish)
        list_tree(r.object_store, tree.id, "")       
'''
```

Get file content by sha:

```python
def get_file():
  name = 'pygit2'
  repo_path = os.path.join(BASE_DIR, name)
  repo = Repo(repo_path)
  store = repo.object_store
  _, content = store.get_raw(b'cd5264128765f10cd56498612cdee83098aa96d2')
  print('setup.py:\n',content)
```

Or

```python
def get_file():
  name = 'pygit2'
  repo_path = os.path.join(BASE_DIR, name)
  repo = Repo(repo_path)
  obj = repo[b'4426e70d752d00d2ec4da6b835830deb76a57a45']
  if obj.type_name == b'blob':
    return obj.data
  #store = repo.object_store
  #_, content = store.get_raw(b'cd5264128765f10cd56498612cdee83098aa96d2')
  #print('setup.py:\n',content)
```




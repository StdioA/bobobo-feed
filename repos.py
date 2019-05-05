import os
from git import Repo

blog_url = "https://github.com/liuyubobobo/my-blog.git"
blog_path = "my-blog"
atom_url = "https://github.com/liuyubobobo-blog/feed.git"
atom_path = "feed"


class GitRepo:
    def __init__(self, url, path, force=False):
        self.url = url
        self.path = path
        self.update(force=force)

    def update(self, force=False):
        if os.path.exists(self.path):
            self.repo = Repo(self.path)
            if force:
                self.repo.remote().pull()
        else:
            self.repo = Repo.clone_from(self.url, self.path)

    @property
    def last_committed_at(self):
        commit = next(self.repo.iter_commits())
        return commit.committed_datetime


blog_repo = GitRepo(blog_url, blog_path)
atom_repo = GitRepo(atom_url, atom_path)

import os
import datetime
from git import Repo


class GitRepo:
    def __init__(self, url, path, force=False, **extra):
        self.url = url
        self.path = path
        self.update(force=force)
        self.extra_conf = extra

    def update(self, force=False):
        if os.path.exists(self.path):
            self.repo = Repo(self.path)
            if force:
                self.repo.remote().pull()
        else:
            self.repo = Repo.clone_from(self.url, self.path)

    def commit_all(self):
        repo = self.repo
        repo.git.add(all=True)
        now = datetime.datetime.now()
        msg = "Feed update: {}".format(now.strftime("%Y-%m-%d %H:%M:%S"))
        repo.index.commit(msg)

    def push(self):
        remote_url = self.extra_conf.get("push_url", self.url)
        try:
            remote = self.repo.remote("push")
        except ValueError:
            remote = self.repo.create_remote("push", remote_url)
        remote.push()

    @property
    def last_committed_at(self):
        commit = next(self.repo.iter_commits())
        return commit.committed_datetime

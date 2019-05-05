import os


GIT_TOKEN = os.environ.get("GIT_TOKEN", "")
BLOG_CONF = {
    "path": "my-blog",
    "url": "https://github.com/liuyubobobo/my-blog.git"
}
ATOM_CONF = {
    "path": "feed",
    "url": "https://github.com/liuyubobobo-blog/feed.git",
    "push_url": "https://{}@github.com/liuyubobobo-blog/feed.git".format(
        GIT_TOKEN)
}

BLOG_URL_BASE = "https://github.com/liuyubobobo/my-blog/blob/master/"
BLOG_IMG_BASE = "https://github.com/liuyubobobo/my-blog/raw/master/"

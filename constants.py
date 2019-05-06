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

ATOM_METADATA = {
    "id": "https://github.com/liuyubobobo/my-blog",
    "author": {
        "name": "liuyubobobo",
        "email": "liuyubobobo@gmail.com"
    },
    "icon": "https://www.gravatar.com/avatar/c4c67099540a54bd845d8e404fe8cc41",
    "title": "是不是很酷",
    "subtitle": "坚持有质量的技术原创，用技术人的视角看世界",
    "language": "zh-CN",
    "generator": {
        "generator": "bobobo-feed",
        "version":  "0.0.1",
        "uri": "https://github.com/StdioA/bobobo-feed"
    }
}

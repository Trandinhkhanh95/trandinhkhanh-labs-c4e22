from youtube_dl import YoutubeDL
options = {
    "default_search": "ytsearch",
    "maxdownload":1,
}
d1 = YoutubeDL(options)
d1.download([""])
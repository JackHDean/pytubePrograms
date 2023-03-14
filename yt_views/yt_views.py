from pytube import YouTube

def get_views(link):
    youtubeObject = YouTube(link)
    youtubeViews = youtubeObject.views
    youtubeViews = f'{youtubeViews:,}'
    viewsStr = str(youtubeViews)
    youtubeObject = print("This video has " + viewsStr + " views!")

link = input("Enter URL here: ")
get_views(link)
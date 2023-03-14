from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject = YouTube(link)
    except:
         print("Error!")
    print("VIDEO DOWNLOADED!")

link = input("Please insert URL of your video here: ")
download(link)
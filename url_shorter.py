#pip install pyshorteners
import pyshorteners

def shorter_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

long_url = "https://www.geeksforgeeks.org/courses/dsa-to-development-coding-guide?itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=courses"
short_url = shorter_url(long_url)
print("Shortened URL:", short_url)

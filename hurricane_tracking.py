import feedparser

def main():
    data = feedparser.parse('https://www.nhc.noaa.gov/xml/TWOAT.xml')

    title = data.entries[0].title
    description = data.entries[0].description
    description = description.replace('<br />', '')
    print()
    print(title)
    print(description)
    print()
      

if __name__ == '__main__':
    main()

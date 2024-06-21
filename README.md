
# NOAA RSS Feed Parser

This project fetches and displays the latest tropical weather outlook from the National Hurricane Center's RSS feed.

## Description

This script uses the feedparser library to parse an RSS feed from the National Hurricane Center (NHC). It retrieves the title and description of the first entry in the feed, cleans the description by removing HTML line break tags, and prints the title and cleaned description.
## Prerequisites

Python 3.x
feedparser library

You can install the feedparser library using pip:

```pip install feedparser```

## Usage

1. Clone the repository or download the script.
2. Ensure you have the required feedparser library installed.
3. Run the script:

```python hurrican_tracking.py```


## Example

When you run the script, it will output the title and description of the latest tropical weather outlook from the NHC. The description will have HTML line breaks removed for better readability.
## Code Explanation

``` 
import feedparser  # Import the feedparser module for parsing RSS feeds

def main():
# Parse the RSS feed from the specified URL
data = feedparser.parse('https://www.nhc.noaa.gov/xml/TWOAT.xml')

# Extract the title of the first entry in the feed
title = data.entries[0].title
# Extract the description of the first entry in the feed
description = data.entries[0].description
# Replace the HTML line break tags with an empty string
description = description.replace('<br />', '')

# Print a blank line for formatting
print()
# Print the title of the first entry
print(title)
# Print the description of the first entry
print(description)
# Print a blank line for formatting
print()

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
	# Call the main function to execute the script
	main()
```
	
	- The script uses the feedparser library to parse the RSS feed from the given URL.
	- It retrieves the title and description of the first entry in the feed.
	- It removes HTML line break tags from the description for better readability.
	- It prints the title and cleaned description to the console.

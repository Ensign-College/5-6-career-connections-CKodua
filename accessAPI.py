import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
import requests
import json
from urllib.parse import quote

print("Welcome to the Book of Mormon Summary Tool!")
while True:
    book = input("Which book of the Book of Mormon would you like? ")
    chapter_str = input("Which chapter of %s are you interested in? " % book)
    
    try:
        chapter = int(chapter_str)
    except ValueError:
        print("Please enter a valid chapter number.")
        continue

    # Properly encode the book name
    encoded_book = quote(book)
    base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/%s/%s' % (encoded_book, chapter)
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data for {book} chapter {chapter}. Error: {e}")
        another = input("Would you like to try again (Y/N)? ")
        if another.lower() != 'y':
            print("Thank you for using the Book of Mormon Summary Tool!")
            break
        else:
            continue

    data = response.json()
    if 'chapter' in data and 'summary' in data['chapter']:
        print("Summary of %s chapter %s:" % (book, chapter))
        print(data['chapter']['summary'])
    else:
        print("Summary not found for %s chapter %s." % (book, chapter))

    print(" ")
    another = input("Would you like to view another (Y/N)? ")

    if another.lower() != 'y':
        print("Thank you for using the Book of Mormon Summary Tool!")
        break


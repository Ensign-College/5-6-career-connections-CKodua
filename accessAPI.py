import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'
import requests

# Define the base URL
base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

def get_chapter_summary(book, chapter):
    try:
        # Replace spaces with dashes for API URL and convert to lowercase
        book = book.replace(" ", "-").lower()
        # Construct the API URL
        url = f"{base_url}{book}/{chapter}"
        
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        # Check if 'summary' is in the response data
        if 'summary' in data:
            summary = data['summary']
        else:
            summary = 'No summary available'
        
        return summary
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve the summary. {e}"

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    
    while True:
        book = input("Which book of the Book of Mormon would you like? ")
        chapter = input(f"Which chapter of {book} are you interested in? ")
        
        summary = get_chapter_summary(book, chapter)
        print(f"Summary of {book} chapter {chapter}:")
        print(summary)
        
        another = input("Would you like to view another (Y/N)? ").strip().lower()
        if another != 'y':
            break
    
    print("Thank you for using the Book of Mormon Summary Tool!")

if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time
import os
from string_helper import format_manga_name
from settings import SAVE_PATH
import requests

# Set up Firefox options to run in headless mode
options = Options()
options.headless = True

# Initialize the WebDriver using Service
service = Service(executable_path="/Users/johnbrand/Downloads/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

def fetch_manga_page(manga_name, chapter_number):
    formatted_name = format_manga_name(manga_name)
    url = f"https://ww1.mangafreak.me/Read1_{formatted_name}_{chapter_number}"

    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load (adjust this depending on internet speed)

        # Debugging: Print the page title to ensure it's loading correctly
        print(f"Page loaded: {driver.title}")

        # Scrape the necessary data using the updated XPath for images
        images = driver.find_elements(By.XPATH, "//img[contains(@src, 'mangas')]")  # Updated XPath
        print(f"Found {len(images)} images.")  # Debugging: Check how many images are found

        manga_images = []
        for img in images:
            img_url = img.get_attribute('src')
            print(f"Found image URL: {img_url}")  # Debugging: Print the image URL
            manga_images.append(img_url)

        return manga_images

    except Exception as e:
        print(f"Error occurred: {e}")
        return []

def save_manga(manga_images, manga_name, chapter_number):
    # Create the main folder for the manga if it doesn't exist
    manga_folder = os.path.join(SAVE_PATH, manga_name)
    os.makedirs(manga_folder, exist_ok=True)

    # Now create the subfolder for the chapter inside the manga folder
    chapter_folder = os.path.join(manga_folder, f"Chapter_{chapter_number}")
    os.makedirs(chapter_folder, exist_ok=True)

    for index, img_url in enumerate(manga_images):
        try:
            img_data = requests.get(img_url).content
            with open(os.path.join(chapter_folder, f"page_{index + 1}.jpg"), 'wb') as f:
                f.write(img_data)
            print(f"Saved page {index + 1}")
        except Exception as e:
            print(f"Failed to save page {index + 1}: {e}")

def download_range_of_chapters(manga_name, start_chapter, end_chapter):
    for chapter_number in range(start_chapter, end_chapter + 1):
        print(f"Downloading Chapter {chapter_number}...")
        manga_images = fetch_manga_page(manga_name, chapter_number)

        if manga_images:
            save_manga(manga_images, manga_name, chapter_number)

def main():
    manga_name = input("Enter manga name: ").lower().replace(" ", "_")
    option = input("Do you want to download (1) a single chapter, (2) a range of chapters, or (3) all chapters? Enter 1, 2, or 3: ")

    if option == "1":
        chapter_number = int(input("Enter chapter number: "))
        manga_images = fetch_manga_page(manga_name, chapter_number)
        
        if manga_images:
            save_manga(manga_images, manga_name, chapter_number)

    elif option == "2":
        start_chapter = int(input("Enter the start chapter number: "))
        end_chapter = int(input("Enter the end chapter number: "))
        download_range_of_chapters(manga_name, start_chapter, end_chapter)

    elif option == "3":
        # To download all chapters, you could specify a reasonable range (e.g., last 50 chapters)
        start_chapter = 1
        end_chapter = 50  # Adjust this as needed
        download_range_of_chapters(manga_name, start_chapter, end_chapter)

if __name__ == "__main__":
    main()

# Close the driver at the end
driver.quit()

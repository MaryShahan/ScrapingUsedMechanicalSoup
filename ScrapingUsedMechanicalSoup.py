#Can you create a local database of cat and dog photos? automating the process of searching for images on Google, downloading them and saving them to a new local directory
#Navigate to Google image
import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com/imghp?hl=en"

browser.open(url)
print(browser.get_url())

#Type a search term and click "search"
#extractig total HTML from the webpage(get HTML)
browser.get_current_page()
print(browser.get_current_page())

# target the search input e.g. input element name="q"
browser.select_form()
browser.get_current_form().print_summary()

# search for a term
search_term = 'dogs'
browser["q"] = search_term

# submit/"click" search
browser.launch_browser()
response = browser.submit_selected()

print('new url:' , browser.get_url())
print('my response:\n' , response.text[:500])

#Navigate to the new page and target all the images
# open new url:
new_url = browser.get_url()
browser.open(new_url)

# get HTML
page = browser.get_current_page()
all_images = page.find_all('img')
print(all_images)

# target the source attribute
image_source = []
for image in all_images:
    image = image.get('src')
    image_source.append(image)
print(image_source)

#getting rid of all the bad links
image_source = [image for image in image_source if image.startswith('https')]
print(image_source)

#Create a new local directory on our computer
import os #to help us create new directory
import wget #to help us with saving

path = os.getcwd() #will return the current dir we are in
path = os.path.join(path , search_term + "s") #path = os.path.join(path , 'dogs')

# lets create this dir:
os.mkdir(path)

print(path)

# lets download images:
counter = 0
for image in image_source:
    save_as = os.path.join(path , search_term + str(counter) + '.jpg') # #save_as = os.path.join(path, 'dog1.jpg')
    wget.download(image, save_as)
    counter += 1



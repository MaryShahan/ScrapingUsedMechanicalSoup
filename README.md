# ScrapingUsedMechanicalSoup

Using Google colab for entire coding except "Create a new local directory on our computer" then switch to Pycharm to run all

#Create a new local directory on our computer
import os #to help us create new directory
import wget #to help us with saving

path = os.getcwd() #will return the current dir we are in
path = os.path.join(path , search_term + "s") #path = os.path.join(path , 'dogs')

#lets create this dir:
os.mkdir(path)

print(path)

#lets download images:
counter = 0
for image in image_source:
    save_as = os.path.join(path , search_term + str(counter) + '.jpg') # #save_as = os.path.join(path, 'dog1.jpg')
    wget.download(image, save_as)
    counter += 1

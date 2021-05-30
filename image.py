import json
import threading
import requests
import time
import datetime
# class Download():
# def image_into_python():



# class Image_(object):

    # def __init__(self,image1,image2,image3 ):
    #     self.image1 = image1
    #     self.image2 = image2
    #     self.image3 = image3

with open("image_json.json", "r") as image_file:
    print(image_file)
    data = json.load(image_file)
    print(F"data is \n{data}")

for img in data["images"]:
    print(img)
    x = list(img.values())
    print(x)

# def download_image():

responce = requests.get(x[0])
with open("photo1.png", "wb") as file:
    file.write(responce.content)
responce1 = requests.get(x[1])
with open("photo2.png", "wb") as file:
    file.write(responce1.content)
responce2 = requests.get(x[2])
with open("photo3.png", "wb") as file:
    file.write(responce2.content)



# thread_list = []
# # for i in x:
# y = threading.Thread(target=download_image)
# thread_list.append(y)
# y.start()
# for thrd in thread_list:
#     thrd.join()
if __name__ == '__main__':
    starting_time = datetime.datetime.today()
b = (datetime.datetime.today() - starting_time).seconds
print(f"it took {b} seconds")



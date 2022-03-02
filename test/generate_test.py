import os

image_files = []
os.chdir(os.path.join("/Users/kevin/Downloads/yolotinyv4_PI", "test"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("/content/yolotinyv4_PI/obj/" + filename)
os.chdir("..")
with open("test.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")

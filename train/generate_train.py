import os

image_files = []
os.chdir(os.path.join("/Users/kevin/Downloads/yolotinyv4_PI", "train"))
retval = os.getcwd()
#print "Directory changed successfully %s" % retval
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("/content/yolotinyv4_PI/obj/" + filename)
        #image_files.append("/Users/kevin/Downloads/xml2yolo-master/images" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")

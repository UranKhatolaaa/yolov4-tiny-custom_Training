import glob, os
import argparse

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

print(current_dir)

#path to one folder that has both images and labels
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--imgdir", type=str, required=True, help="File containing the image paths")
args = parser.parse_args()

current_dir = args.imgdir

# Percentage of images to be used for the test set
percentage_test = 20;

# Create and/or truncate train.txt and test.txt
file_train = open('data/train.txt', 'w')
file_test = open('data/valid.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1

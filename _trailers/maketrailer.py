import os

dir = '/home/jetroid/Downloads/derek/pics/'
for file in os.listdir(dir):
    print(file)
    filename = file.split(".")[0]
    with open(filename + ".md", 'w') as f:
        f.write("---\n")
        f.write("title: " + filename + "\n")
        f.write("date: 2022-05-17 12:11:55 +0100" + "\n")
        f.write("image: /assets/images/" + file + "\n")
        f.write("video_id: Qi74UagYgWk" + "\n")
        f.write("---" + "\n")
        f.write("Sample text if you want it.")


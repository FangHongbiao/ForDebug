import os


def walk_files(rootdir):
    file_list = []
    label_list = []

    file_list_5 = []
    label_list_5 = []
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            fullFilename = os.path.join(subdir, file)
            filenameNoSuffix =  os.path.splitext(fullFilename)[0]
            if file.endswith('.WAV'):
                arr = filenameNoSuffix.split('/')
                mark_name = arr[-3]+ '-' + arr[-2] + '-' + arr[-1]
                label = int((str(arr[-3])[-1]))
                file_list.append(mark_name + ' ' + fullFilename)
                label_list.append(mark_name + ' ' + str(label-1))
                if label != 1 and label != 6 and label !=8:
                    file_list_5.append(mark_name + ' ' + fullFilename)
                    label_list_5.append(mark_name + ' ' + str(label-1))
    print(len(file_list))
    print(len(label_list))
    print(len(file_list_5))
    print(len(label_list_5))
    file_list = map(lambda x:x.strip()+'\n',file_list)
    label_list = map(lambda x:x.strip()+'\n',label_list)
    file_list_5 = map(lambda x:x.strip()+'\n',file_list_5)
    label_list_5 = map(lambda x:x.strip()+'\n',label_list_5)
    with open('file_list.txt', 'w') as f:
        f.writelines(file_list)
    with open('label_list.txt', 'w') as f:
        f.writelines(label_list)
    with open('file_list_5.txt', 'w') as f:
        f.writelines(file_list_5)
    with open('label_list_5.txt', 'w') as f:
        f.writelines(label_list_5)

if __name__ == "__main__":
    rootdir = '/home/fanghb/Dataset/speech/TIMIT/train'
    walk_files(rootdir)
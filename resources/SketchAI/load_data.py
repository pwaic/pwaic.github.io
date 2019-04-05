import urllib.request


NUM_CLASSES = 150;


def download():
    base = 'https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/'
    for c in [str(x) for x in range(NUM_CLASSES)]:
        cls_url = c.replace('_', '%20')
        path = base+cls_url+'.npy'
        print(path)
        # urllib.request.urlretrieve(path, 'data/'+c+'.npy')


def main():
    download()


if __name__ == "__main__":
    main()
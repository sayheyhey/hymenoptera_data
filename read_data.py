from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):

    def __init__(self,root_dir, label_dir):
        # super(MyData, self).__int__()
        self.root_dir = root_dir       # 获取train
        self.label_dir = label_dir     # 获取ants
        self.path = os.path.join(self.root_dir, self.label_dir)     # 获取train\\ant
        self.img_path = os.listdir(self.path)    #  将图片放入集合中


    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir,self.label_dir,img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = "train"
label_dir = "ants"
ant_dataset = MyData(root_dir,label_dir)


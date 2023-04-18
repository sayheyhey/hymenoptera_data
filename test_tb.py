from  torch.utils.tensorboard import  SummaryWriter
import numpy as np
from PIL import  Image

writer = SummaryWriter("logs")

writer.add_image()
# y = x
for i in range(100):
    writer.add_scalar("y=2x",2*i,i) # 标题，y轴，x轴

writer.close()

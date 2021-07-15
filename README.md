一、需求规格

​	1.运行环境

​		(1) python (version>=3.7);

​		(2) 如果有含cuda单元的gpu，请根据gpu自身的型号安装相关的cuda组件;

​		(3) Microsoft Visual C++ 14.0;

​	 （4）lav解码器.

​	2.所需的库

​		tqdm ; typeguard ; visualdl>=2.1.0 ; opencv-python ; PyYAML ; shapely ; scipy ; terminaltables ; pycocotools ; setuptools>=42.0.0 ; paddlepaddle-gpu=2.1.1(有带cuda单元的gpu)/paddlepaddle=2.1.1(无带cuda单元的gpu) ; Pyqt5.

二、使用说明书（以windows为例）

​	1.打开exe文件

![image-20210714175304925](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714175304925.png)

2.点击VideoFile选择需要播放的文件

![image-20210714175502887](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714175502887.png)

3.在播放视频时可以任意拉动进度条 、点击Pause暂停、点击Play继续播放的操作

![QQ图片20210715113006](C:\Users\Andy Huang\Pictures\QQ图片20210715113006.png)

4.先在Threshold的方框中输入0-1的置信度，然后点击Detect，选择需要进行目标检测的文件。否则会有提示。

提示如下：

![image-20210714193134684](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714193134684.png)

![image-20210714193240518](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714193240518.png)

正常运行：

![image-20210714193400629](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714193400629.png)

5.等待运行完成之后，检测处理之后的视频会自动播放

![QQ图片20210715113314](C:\Users\Andy Huang\Pictures\QQ图片20210715113314.png)

三、实现场景与功能

​	1.场景：基于深度学习的行人跟踪，是安防场景的重要研究领域，该领域的研究对于重点人员跟踪，违法犯罪事件预警有着重要意义。例如火车站、小区的摄像头对范围人员追踪、夜晚监控小区或者主人不在家时家中是否有可疑人士都有重要的意义。随着技术经济的发展和城市化进程的加快，安防监控逐渐遍及小区、超市、校园以及其他很多公共场合。

​	2.功能：

​		(1)可以导入视频、输入相应的置信度并对其中的人物进行实时追踪;

​		(2)可以统计出任意时刻内检测到的人数;

​	    (3)交互逻辑友好的GUI界面;

​		(4)镶嵌在GUI内的多功能播放器(暂停、继续播放、拉动进度条跳动等功能);

​		(5)GUI会对一些不正确的操作给出相应的提示.

四、技术实现

​	1.前期准备

​		(1)下载MOT20数据集（单摄像头目标跟踪训练数据集为公开数据集MOT20：https://motchallenge.net/data/MOT20/）;

​		(2)也可使用aistudio上的已经处理好的coco或voc的MOT20训练集.

​	2.训练模型

​		(1)在aistudio上使用PaddleDetection，选用yolov3，darknet作为骨干网络;

​		(2)根据自身需求修改yolov3 darknet coco.yml的配置文件,改变训练模型的epoch、anchor、batch、learningrate等参数;

![image-20210715115419436](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210715115419436.png)

​		(3)对上述选择的训练集进行训练、测试;

​		(4)使用paddledetection自带的tool中的的infer.py对某一张图片进行检测，测试模型效果;

​		(5)使用tool中的export_model.py导出训练的模型

​	3.设计带GUI的可预测软件

​		(1)设计架构

![无标题1](C:\Users\Andy Huang\Pictures\无标题1.png)

​		(2)前端部分使用了Pyqt5的可视化工具Qt Designer来进行gui的设计，界面设计如下：

![image-20210714175304925](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714175304925.png)

​		(3)在播放视频时可以任意拉动进度条 、点击Pause暂停、点击Play继续播放的操作

![QQ图片20210715113006](C:\Users\Andy Huang\Pictures\QQ图片20210715113006.png)

​		(4)未输入置信度点击Detect不可开启检测功能，并给出相应的提示

![image-20210714193134684](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714193134684.png)

​		(5)成功开启检测功能而没有选择视频，也会停止运行检测功能的开启，并给出相应的提示的提示

![image-20210714193240518](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714193240518.png)

​		(6)正常运行检测功能

![image-20210714193400629](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210714193400629.png)

​		(7)检测期间也可正常使用GUI内的功能播放视频的实现过程

![image-20210715121216089](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210715121216089.png)

​		(8)检测功能运行时图像处理的过程

![image-20210715121331733](C:\Users\Andy Huang\AppData\Roaming\Typora\typora-user-images\image-20210715121331733.png)



​		(9)等待运行完成之后，检测处理之后的视频会自动播放

![QQ图片20210715113314](C:\Users\Andy Huang\Pictures\QQ图片20210715113314.png)

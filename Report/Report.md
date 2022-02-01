## Aim
To Use the idea of motion segmentation, from the papers below. To segment out the foreground, you may use the Sequential Labelling algorithm. Or K-Means, for that matter. Please generate two videos (in terms of the frames, and the video file as well) -
- the background, and
- one with the foreground objects

### Original Frame :
![22](https://user-images.githubusercontent.com/76518189/152031934-80527d51-7509-434f-b362-9ca41ea4f0ad.jpg)
### Foreground Frame:
 ![res900](https://user-images.githubusercontent.com/76518189/152031722-00db92b7-484f-420b-b64c-5884b5cb3d92.png)
 
## Assumptions
We have only experimented on the template video. The parameters which we have experimented upon is limited to this video only. [Link](https://github.com/Mainak1792/Backround_Subtraction/blob/main/assets/umcp.mpg)
The parameters are as follows:
- Learning Rate
- Threshold
- Variance
- Weight
## Learning Rate


| Learning RATE  	| 1  	| 0.1  	|  0.01 	| 0.001  	|
|:-: 	|:-:	|:-:	|:-:	|:-:	|

## Threshold
|Threshold   	|  1 	| 0.65  	| 0.75  	| 0.5  	|
|:-: 	|:-:	|:-:	|:-:	|:-:	|

##Variance
|Variance   	| 100  	| 75  	| 32  	|  6 	|
|:-: 	|:-:	|:-:	|:-:	|:-:	|

## Weight
|Weight   	| 1  	| 0.75  	| 0.5  	|  0.25 	|
|:-: 	|:-:	|:-:	|:-:	|:-:	|

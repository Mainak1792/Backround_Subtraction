## Aim
i) To Use the idea of motion segmentation, to segment out the foreground, using Sequential Labelling algorithm Or K-Means, for that matter. 
ii) Generate two videos (in terms of the frames, and the video file as well) -
- the background, and
- one with the foreground objects
- 

### Original Frame :
 <img width="252" alt="lr0 1" src="https://user-images.githubusercontent.com/76518189/152031934-80527d51-7509-434f-b362-9ca41ea4f0ad.jpg">

### Foreground Frame:
 ![res900](https://user-images.githubusercontent.com/76518189/152031722-00db92b7-484f-420b-b64c-5884b5cb3d92.png)

## Steps

### Initialisation
- Assign initial parameters.
- Learning Rate, mean(first pixel location) , large standard deviation , Weight(summation 1), Threshold

### Creating Model
- Background Subtraction using on-line K means
![Background Subtraction](https://user-images.githubusercontent.com/68754422/152684006-cce67572-3ec1-482b-9e35-386a11676654.png)


#### CASE 1: Atleast One Gaussian Match
- Matches whether the gaussian will generate the current observation Xt(pixel location)
- Matching Definition:
M(xt) = 1 ; (xt-ut)/sigma <=2.5
      = 0 ; otherwise

#### CASE 2: No Gaussian Match
- Create a new Gaussian for Xt
- low weight
- u=xt
- large sigma
- Remove the gaussian with least weight if they are already K gaussians

### Updating Model

### Subtraction Process
- sort all gaussian
## Assumptions
We have only experimented on the template video. The parameters which we have experimented upon is limited to this video only. [Link](https://github.com/Mainak1792/Backround_Subtraction/blob/main/assets/umcp.mpg)
The parameters are as follows:
- Learning Rate
- Threshold
- Variance
- Weight
## Learning Rate

### BackGround 
Our Experiments show optimum learning for a background is 0.01.
- Learning Rate 0.1
<img width="242" alt="blr0 1" src="https://user-images.githubusercontent.com/76518189/152182713-c32b0db8-16ea-43f0-92a1-eaebf3a77953.png">
- Learning Rate 0.01
	<img width="238" alt="blr0 01" src="https://user-images.githubusercontent.com/76518189/152182641-1e99a4b6-dda7-4b20-90b2-55942280e13c.png">
 - Learning Rate 0.001 
<img width="248" alt="blr0 001" src="https://user-images.githubusercontent.com/76518189/152182550-e469c32a-b298-4d05-a20d-f532fcbd84e4.png">

### Foreground
The optimum learning rate for a foreground is 0.1.
- Learning Rate 0.1
 <img width="252" alt="lr0 1" src="https://user-images.githubusercontent.com/76518189/152183425-aeb858ed-6ad3-47df-9b61-c62fad0b7f51.png">
- Learning Rate 0.01
<img width="245" alt="lr0 01" src="https://user-images.githubusercontent.com/76518189/152183556-6cded4c1-e7fb-499c-abbb-ff9e8f400dde.png">
- Learning Rate 0.001
<img width="242" alt="lr0 001" src="https://user-images.githubusercontent.com/76518189/152183593-893267fb-3ba4-4a0d-9107-b3c30f2bc4d9.png">


## Threshold

### Background
- Threshold 1
<img width="240" alt="bthr1" src="https://user-images.githubusercontent.com/76518189/152189378-ab2dc1b4-747f-49ee-ba6e-bf1b148618e4.png">


- Threshold 0.75
<img width="238" alt="bthr0 75" src="https://user-images.githubusercontent.com/76518189/152189462-7bfd2c9c-a196-4b80-ad52-60e1edc82e38.png">


- Threshold 0.5
<img width="251" alt="fthe0 5" src="https://user-images.githubusercontent.com/76518189/152189656-cefed7ba-78a5-4517-90a1-edcdfcf0ac27.png">

 
### Foreground

- Threshold 1
<img width="245" alt="image" src="https://user-images.githubusercontent.com/76518189/152190142-89e71d99-2ac0-4982-8806-74ce12248494.png">



- Threshold 0.75
<img width="245" alt="bthr0 7" src="https://user-images.githubusercontent.com/76518189/152189840-6d04db76-4713-45c3-9d5e-54a0d0171310.png">

- Threshold 0.5
<img width="247" alt="bth0 5" src="https://user-images.githubusercontent.com/76518189/152189787-8237660d-d07a-4cdc-b9fc-36d7d90acdc9.png">

## Variance

### Background
- Variance 100
<img width="252" alt="bvar100" src="https://user-images.githubusercontent.com/76518189/152184310-cbd71764-75c9-460c-8a07-fc5c40e05223.png">
- Variance 64
<img width="242" alt="bvar64" src="https://user-images.githubusercontent.com/76518189/152184401-197e58c8-bd6c-4e7f-bb60-3c5f7968c621.png">

- Variance 32
<img width="239" alt="bvar32" src="https://user-images.githubusercontent.com/76518189/152184427-19cd1af5-c1c7-4005-9024-64dd23a28237.png">

- Variance 6
<img width="247" alt="bvar5" src="https://user-images.githubusercontent.com/76518189/152184459-02ecfb2f-4e74-4408-a8e7-5087759871a6.png">

### Foreground
- Variance 100
<img width="248" alt="FVAR100" src="https://user-images.githubusercontent.com/76518189/152184498-8478be35-d3e5-4623-80a9-7c0328242ac5.png">

- Variance 64
<img width="252" alt="FVAR63" src="https://user-images.githubusercontent.com/76518189/152184521-cbb26e9e-a562-4276-b6f9-e200521dc913.png">

- Variance 32
<img width="244" alt="FVAR32" src="https://user-images.githubusercontent.com/76518189/152184555-fd7324a2-6bc9-484f-a5c0-42c73b9a9e1f.png">

- Variance 6
<img width="240" alt="FVAR6" src="https://user-images.githubusercontent.com/76518189/152184583-41971ee4-e0cc-4e83-9c69-1d5288e47171.png">




 ---

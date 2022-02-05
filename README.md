## Backround_Subtraction
This Project is a assingment of ELL784, an introductory machine learning course floated By [Prof. Sumantra Dutta Roy](https://www.cse.iitd.ac.in/~sumantra/).

## Problem Statement : 
- A robust video surveillance system does not depend only on the careful placements of cameras but is also robust to whatever is in its visual field or whatever lighting effects occur.
- It should be capable of dealing with movement through cluttered areas, objects overlapping in the visual field, shadows, lighting changes, effects of moving elements of the scene (e.g. swaying trees), slow-moving objects, and objects being introduced or removed from the scene.
- A standard method is effective in situations where objects move continuously and the background is visible a significant portion of the time, it is not robust to scenes with many moving objects particularly if they move slowly. It also cannot handle bimodal backgrounds, recovers slowly when the background is uncovered and has a single, predetermined threshold for the entire scene.
- For more details Please look into [Link](https://www.cse.iitd.ac.in/~sumantra/courses/ml/assignment_1.html)

## Approach:
- We model the values of a particular pixel as a mixture of Gaussians. 
- Based on the persistence and the variance of each of the Gaussians of the mixture, we determine which Gaussians may correspond to background colors. Pixel values that do not fit the background distributions are considered foreground until there is a Gaussian that includes them with sufficient, consistent evidence supporting it. 
- Our system adapts to deal robustly with lighting changes, repetitive motions of scene elements, tracking through cluttered regions, slow-moving objects, and introducing or removing objects from the scene.
- Background Subtraction: It is the process of separating out the foreground objects from the background in a sequence of the video frames.

## Model:
- The pixel process is a time series of pixel values, e.g. scalars for grayvalues or vectors for color images.
- The value of each pixel represents a measurement of the radiance in the direction of the sensor of the first object intersected by the pixels optical ray. With a static background and static lighting, that value would be relatively constant.

## Report
 - Please look into the [report](https://github.com/Mainak1792/Backround_Subtraction/blob/main/Report/Report.md) for the detailed explanation
 
## Output
 - Find the [Background]() and [Foreground]() video. 

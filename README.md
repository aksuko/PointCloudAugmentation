# PointCloudAugmentation


The script defines several functions for applying different types of point cloud augmentations which are jittering, scaling, shifting, rotating, RGB jittering and RGB light effect. It then loads point cloud data from the input folder and applies random combinations of these augmentations to the point clouds, generating augmented point clouds for each point cloud in the input folder. The augmented point clouds are saved to the output folder and an augmentation report is created that records the applied augmentations for each point cloud.


- __--input_folder:__ the path to the input folder
- __--output_folder:__ the path to the output folder
- __--jittering:__ the probability of jittering
- __--scaling:__ the probability of scaling
- __--shifting:__ the probability of shifting
- __--rotating:__ the probability of rotating
- __--rgb_jittering:__ the probability of RGB jittering
- __--rgb_light_effect:__ the probability of RGB light effect
- __--aug_num:__ number of the augmentation of each class

__Sample usage:__
* ```python pcd_aug.py --input_folder ./input --output_folder ./output --rotating 0.5 --shifting 0.1 --aug_num 25```

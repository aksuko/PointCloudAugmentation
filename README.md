# Point Cloud Augmentation

This script provides several functions to apply various types of point cloud augmentations, including jittering, scaling, shifting, rotating, RGB jittering, and RGB light effects. These augmentations can be randomly combined and applied to point clouds to generate augmented point clouds. Additionally, an augmentation report is created that records the specific augmentations applied to each point cloud.

- __--input_folder:__ the path to the input folder
- __--output_folder:__ the path to the output folder
- __--jittering:__ the probability of jittering (0-1)
- __--scaling:__ the probability of scaling (0-1)
- __--shifting:__ the probability of shifting (0-1)
- __--rotating:__ the probability of rotating (0-1)
- __--rgb_jittering:__ the probability of RGB jittering (0-1)
- __--rgb_light_effect:__ the probability of RGB light effect (0-1)
- __--aug_num:__ number of the augmentation of each class

 

## Input folder structure:
* pcd_data
  * class-a
    * class-a_#.txt
  * class-b
    * class-b_#.txt
  * class-c
    * class-c_#.txt
    
txt data: XYZRGB (single space delimiter)

## Sample usage:

```python pcd_aug.py --input_folder ./input --output_folder ./output --rotating 0.5 --shifting 0.1 --aug_num 25```


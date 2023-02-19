# PointCloudAugmentation


The script defines several functions for applying different types of point cloud augmentations which are jittering, scaling, shifting, rotating, RGB jittering and RGB light effect. It then loads point cloud data from the input folder and applies random combinations of these augmentations to the point clouds, generating augmented point clouds for each point cloud in the input folder. The augmented point clouds are saved to the output folder and an augmentation report is created that records the applied augmentations for each point cloud.


--input_folder: the path to the input folder \t
--output_folder: the path to the output folder
--jittering: the probability of performing jittering
--scaling: the probability of performing scaling
--shifting: the probability of performing shifting
--rotating: the probability of performing rotating
--rgb_jittering: the probability of performing RGB jittering
--rgb_light_effect: the probability of performing RGB light effect
--aug_num: number of the augmentation of each class

Sample Usage:
python pcd_aug.py --input_folder ./input --output_folder ./output --rotating 0.5 --shifting 0.1 --aug_num 25

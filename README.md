# PointCloudAugmentation


The script defines several functions for applying different types of point cloud augmentations which are jittering, scaling, shifting, rotating, RGB jittering, RGB light effect. It then loads point cloud data from the input folder and applies random combinations of these augmentations to the point clouds, generating augmented point clouds for each point cloud in the input folder. The augmented point clouds are saved to the output folder and an augmentation report is created that records the applied augmentations for each point cloud.

The script takes as input a folder containing subfolders for each class of point clouds. Each subfolder contains text files containing point cloud data. The augmented point clouds are saved to corresponding subfolders in the output folder.

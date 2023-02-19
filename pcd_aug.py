import os
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Perform data augmentation on a given dataset.')
parser.add_argument('--input_folder', type=str, help='the path to the input folder')
parser.add_argument('--output_folder', type=str, help='the path to the output folder')
parser.add_argument('--jittering', type=float, default=0.6, help='the probability of performing jittering (default: 0.6)')
parser.add_argument('--scaling', type=float, default=0.6, help='the probability of performing scaling (default: 0.6)')
parser.add_argument('--shifting', type=float, default=0.6, help='the probability of performing shifting (default: 0.6)')
parser.add_argument('--rotating', type=float, default=0, help='the probability of performing rotating (default: 0)')
parser.add_argument('--rgb_jittering', type=float, default=0.25, help='the probability of performing RGB jittering (default: 0.25)')
parser.add_argument('--rgb_light_effect', type=float, default=0.25, help='the probability of performing RGB light effect (default: 0.25)')
parser.add_argument('--aug_num', type=int, default=50, help='number of the augmentation of each class')
args = parser.parse_args()



# The augmentation functions
def jittering(data, prob):
    if np.random.uniform() < prob:
        data[:,:3] += np.random.normal(0, 0.01, size=data[:,:3].shape)
        return "jittering"
    return ""

def scaling(data, prob):
    if np.random.uniform() < prob:
        data[:,:3] *= np.random.uniform(0.9, 1.1)
        return "scaling"
    return ""

def shifting(data, prob):
    if np.random.uniform() < prob:
        data[:,:2] += np.random.normal(0, 0.01, size=data[:,:2].shape)
        return "shifting"
    return ""

def rotating(data, prob):
    if np.random.uniform() < prob:
        angle = np.random.uniform(0, 360)
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        data[:,:2] = data[:,:2].dot(rotation_matrix)
        return "rotating"
    return ""

def rgb_jittering(data, prob):
    if np.random.uniform() < prob:
        data[:,3:] += np.random.randint(-5,5,size=data[:,3:].shape)
        return "rgb_jittering"
    return ""

def rgb_light_effect(data, prob):
    if np.random.uniform() < prob:
        data[:,3:] += np.random.normal(0, 20, size=data[:,3:].shape)
        data[:,3:] = np.clip(data[:,3:], 0, 255)
        return "rgb_light_effect"
    return ""

os.makedirs(args.output_folder, exist_ok=True)
report_file = open(os.path.join(args.output_folder, "augmentation_report.txt"), "w")

# Process all subfolders in the input folder (class labels)
for class_folder in os.listdir(args.input_folder):
    class_folder_path = os.path.join(args.input_folder, class_folder)
    if os.path.isdir(class_folder_path):
        report_file.write("Class: {}\n".format(class_folder))
        # Create a corresponding subfolder in the output folder
        output_class_folder_path = os.path.join(args.output_folder, class_folder)
        if not os.path.exists(output_class_folder_path):
            os.makedirs(output_class_folder_path)
        

        pcd = os.listdir(class_folder_path)
        pcd_count = len(pcd)
        sample_count = 0
        while sample_count < args.aug_num:
            random_index = np.random.randint(0, pcd_count)
            pcd_path = os.path.join(class_folder_path, pcd[random_index])
            if pcd_path.endswith('.txt'):
                data = np.genfromtxt(pcd_path, delimiter=' ')
                applied_augmentations = []
                applied_augmentations.append(jittering(data, args.jittering))
                applied_augmentations.append(scaling(data, args.scaling))
                applied_augmentations.append(shifting(data, args.shifting))
                applied_augmentations.append(rotating(data, args.rotating))
                applied_augmentations.append(rgb_jittering(data, args.rgb_jittering))
                applied_augmentations.append(rgb_light_effect(data, args.rgb_light_effect))
                applied_augmentations = list(filter(None, applied_augmentations))

                output_file_path = os.path.join(output_class_folder_path, f"{class_folder}_{sample_count}.txt")
                np.savetxt(output_file_path, data, delimiter=' ', fmt='%.3f %.3f %.3f %.3f %.3f %.3f')

                print("Processed: ", pcd_path, "with augmentations: ", applied_augmentations)
                
                # Write the augmentation report
                report_file.write(f"{pcd_path}, {applied_augmentations}\n")
                sample_count += 1
report_file.close()

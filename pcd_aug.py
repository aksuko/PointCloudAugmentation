import os
import numpy as np

# Define the probability of performing each augmentation
probability = {
    "jittering": 0.6,
    "scaling": 0.6,
    "shifting": 0.6,
    "rotating": 0,
    "rgb_jittering": 0.25,
    "rgb_light_effect": 0.25
}

# Define the augmentation functions
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

# Define the input and output folder
input_folder = r"path_of_input_folder"
output_folder = r"path_of_output_folder"

# Create processed directory if not exists
os.makedirs(output_folder, exist_ok=True)

# Create an augmentation report file
report_file = open(os.path.join(output_folder, "augmentation_report.txt"), "w")

# Process all subfolders in the input folder (class labels)
for class_folder in os.listdir(input_folder):
    class_folder_path = os.path.join(input_folder, class_folder)
    if os.path.isdir(class_folder_path):
        report_file.write("Class: {}\n".format(class_folder))
        # Create a corresponding subfolder in the output folder
        output_class_folder_path = os.path.join(output_folder, class_folder)
        if not os.path.exists(output_class_folder_path):
            os.makedirs(output_class_folder_path)
        
        # Generate random indices of the examples 
        examples = os.listdir(class_folder_path)
        examples_count = len(examples)
        sample_count = 0
        while sample_count < 20:
            random_index = np.random.randint(0, examples_count)
            example_path = os.path.join(class_folder_path, examples[random_index])
            if example_path.endswith('.txt'):
                # Load the data into a numpy array
                data = np.genfromtxt(example_path, delimiter=' ')
                applied_augmentations = []
                # Apply the augmentation functions
                applied_augmentations.append(jittering(data, probability["jittering"]))
                applied_augmentations.append(scaling(data, probability["scaling"]))
                applied_augmentations.append(shifting(data, probability["shifting"]))
                applied_augmentations.append(rotating(data, probability["rotating"]))
                applied_augmentations.append(rgb_jittering(data, probability["rgb_jittering"]))
                applied_augmentations.append(rgb_light_effect(data, probability["rgb_light_effect"]))
                applied_augmentations = list(filter(None, applied_augmentations))
                # Save the augmented data to the output folder
                output_file_path = os.path.join(output_class_folder_path, f"{data}_{sample_count}.txt")
                np.savetxt(output_file_path, data, delimiter=' ', fmt='%.3f %.3f %.3f %d %d %d')
                # Print the name of processed file and applied augmentations
                print("Processed: ", example_path, "with augmentations: ", applied_augmentations)
                # Write the augmentation report
                report_file.write(f"{example_path}, {applied_augmentations}\n")
                sample_count += 1

# Close the augmentation report file
report_file.close()

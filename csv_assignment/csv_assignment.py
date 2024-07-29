#import necessary libraries
import os
import pandas as pd

#set the root directory of your image dataset
dataset_root = "C:\Users\James\Documents\MYAIProjects\csv_assignment\images"

# initialize an empty dataframe with columns for imapge_path and label
image_data = pd.DataFrame(columns=["image_path", "label"])

# traverse the dataset directory
for root, dirs, files in os.walk(dataset_root):
    # iterate over each file in the current directory
    for file in files:
        # combine the root directory and file name to get the complete image path
        image_path = os.path.join(root, file)

        # extract the label or class name from the directory name
        label = os.path.basename(root)

        # create a new dataframe with the image path and label as values
        row = pd.DataFrame({"image_path": [image_path], "label": [label]})

        # concatenate the new row with the existing image_data DataFrame
        image_data = pd.concat([image_data, row], ignore_index=True)

# Save the DataFrame as a csv file name "image_dataset.csv"
image_data.to_csv("image_dataset.csv", index=False)

file_path = "image_dataset.csv"
os.startfile(file_path)
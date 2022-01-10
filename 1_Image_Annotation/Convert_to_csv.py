import os
import argparse
import codecs
import pandas as pd

def get_parent_dir(n=1):
    """returns the n-th parent dicrectory of the current
    working directory"""
    current_path = os.path.dirname(os.path.abspath(__file__))
    for k in range(n):
        current_path = os.path.dirname(current_path)
    return current_path

def txt2csv(location):
    # Return list
    temp_res = []

    # Run through all the files
    for file in os.listdir(location):
        # Check the file name ends with txt
        #  and not class.txt
        if (not file.endswith(".txt")) | \
                (file == "classes.txt"):
            continue

        # Get the file name
        file_whole_name = f"{location}/{file}"

        # Read in txt as csv
        df_txt = pd.read_csv(file_whole_name, sep=" ", header=None)

        # Create data for each labels
        for index, row in df_txt.iterrows():
            # Temp array for csv, initialized by the training types
            file_name_txt = file_whole_name.split('/')[-1]
            file_name = file_name_txt.split('.')[0]
            file_name = file_name + '.JPG'
            temp_csv = [file_name]

            # Add the upper left coordinate

            xmin = min(max(0.0, row[1] - row[3] / 2), 1.0)
            ymin = min(max(0.0, row[2] - row[4] / 2), 1.0)
            temp_csv.extend([xmin, ymin])

            # Add the lower left coordinate (not necessary, left blank)
            #temp_csv.extend(["", ""])

            # Add the lower right coordinate
            xmax = min(max(0.0, row[1] + row[3] / 2), 1.0)
            ymax = min(max(0.0, row[2] + row[4] / 2), 1.0)
            temp_csv.extend([xmax, ymax])

            # Add the upper right coordinate (not necessary, left blank)
            #temp_csv.extend(["", ""])

            # Class label
            temp_csv.extend([class_labels[int(row[0])]])

            # Append to the res
            temp_res.append(temp_csv)

    return temp_res
if __name__ == "__main__":
    # Add the argument parse
    arg_p = argparse.ArgumentParser()
    arg_p.add_argument("-c", "--classes",
                       type=str,
                       default="C:/Users/joell/Desktop/TrainYourOwnYOLO/Data/Source_Images/Training_Images/classes.txt",
                       help="Label classes path")
    args = vars(arg_p.parse_args())

    Data_Folder = os.path.join(get_parent_dir(1), "Data")
    training_folder = os.path.join(
        Data_Folder, "Source_Images", "Training_Images")

# Class labels
    class_labels = []

# Load in the defined classes
    if os.path.exists(args["classes"]) is True:
        with codecs.open(args["classes"], 'r', 'utf8') as f:
            for line in f:
                line = line.strip()
                class_labels.append(line)
    else:  # Exit if errors occurred
        print(f"File: {['classes']} not exists")
        exit(1)

    res = []
    res.extend(txt2csv(training_folder))
    res_csv = pd.DataFrame(res,
                           columns=["image",
                                    "xmin", "ymin",
                                    "xmax", "ymax",
                                    "label"])

    res_csv.to_csv("training_data.csv", index=False, header=True)

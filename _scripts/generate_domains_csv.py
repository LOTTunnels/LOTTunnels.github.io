import os
import yaml
import csv

# Define the path to the cloned repository
repo_path = "../_lottunnels/Binaries"

# List to store collected domains and their corresponding file names
entries = []

# Walk through the repository to find YAML files
for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith(".md"):  # Check for .MD files
            print (f"Processing file: {file}")
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    # Read the file and strip YAML front matter
                    raw_content = f.read()
                    if raw_content.startswith("---") and raw_content.endswith("---"):
                        raw_content = raw_content.strip("---")
                    # Parse YAML content
                    yaml_items = yaml.safe_load_all(raw_content)
                    filtered_items = [item for item in yaml_items if item is not None]

                    for content in filtered_items:
                        # Check if "Detection" section exists and collect domains
                        if "Detection" in content:
                            lol_name = content["Name"]
                            detection_data = content["Detection"]
                            for d in detection_data:
                                if "Domain" in d:
                                    domain = d["Domain"]
                                    # print (domain)
                                    entries.append({"domain": domain, "name": lol_name})
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML file {file}: {e}")

# Write collected data to a CSV file
output_file = "domains.csv"
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["domain", "name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the CSV headers
    writer.writeheader()

    # Write the data entries
    writer.writerows(entries)

print(f"CSV file saved to {output_file}")

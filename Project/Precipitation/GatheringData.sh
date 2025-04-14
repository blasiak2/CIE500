#This is a Bash file to collect data from 
#https://console.cloud.google.com/storage/browser/gcp-public-data-nexrad-l3;tab=objects?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false&pli=1&inv=1&invt=Abslcg

#!/bin/bash

# Set variables
RADAR_SITE="KBUF"  # Change this to the radar site you want
START_YEAR=2023
START_MONTH=01
START_DAY=01
END_YEAR=2023
END_MONTH=01
END_DAY=05
OUTPUT_DIR="nexrad_data"

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Loop through the dates
current_date="$START_YEAR-$START_MONTH-$START_DAY"
end_date="$END_YEAR-$END_MONTH-$END_DAY"

while [[ "$current_date" <= "$end_date" ]]; do
  year=$(date -d "$current_date" +%Y)
  month=$(date -d "$current_date" +%m)
  day=$(date -d "$current_date" +%d)

  # Construct the GCS path
  gcs_path="gs://gcp-public-data-nexrad-l3/$year/$month/$day/$RADAR_SITE/"

  # Download the files
  echo "Downloading data from: $gcs_path"
  gsutil cp "$gcs_path*" "$OUTPUT_DIR/"

  # Increment the date
  current_date=$(date -d "$current_date + 1 day" +%Y-%m-%d)
done

echo "Download complete."


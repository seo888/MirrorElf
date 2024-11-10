#!/bin/bash

sudo apt install -y jq
sudo apt install -y unzip

# Fetch the latest release information from GitHub API
RELEASE_JSON=$(curl -s https://api.github.com/repos/seo888/MirrorElf/releases/latest)

# Extract the zipball URL from the JSON response
ZIP_URL=$(echo "$RELEASE_JSON" | jq -r .zipball_url)

# Check if the ZIP URL is empty
if [ -z "$ZIP_URL" ]; then
  echo "Failed to get the ZIP URL from the GitHub API"
  exit 1
fi

# Define the output ZIP file name based on the URL (we can extract the tag version)
ZIP_FILE="MirrorElf-$(echo "$RELEASE_JSON" | jq -r .tag_name).zip"

# Download the zipball using curl
echo "Downloading release from $ZIP_URL..."
curl -L -o "$ZIP_FILE" "$ZIP_URL"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "Download successful!"
else
  echo "Download failed!"
  exit 1
fi

# Extract the downloaded zip file
echo "Extracting $ZIP_FILE..."
unzip "$ZIP_FILE"

# Check if unzip was successful
if [ $? -eq 0 ]; then
  echo "Extraction successful!"
else
  echo "Extraction failed!"
  exit 1
fi

# Navigate into the extracted directory
EXTRACTED_DIR=$(unzip -Z1 "$ZIP_FILE" | head -n 1 | cut -d/ -f1)
cd "$EXTRACTED_DIR"

echo "Ready to use the extracted files in $EXTRACTED_DIR"

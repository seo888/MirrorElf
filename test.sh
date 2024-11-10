#!/bin/bash

# Install jq and tar if they are not already installed
sudo apt install -y jq tar

# Fetch the latest release information from GitHub API
RELEASE_JSON=$(curl -s https://api.github.com/repos/seo888/MirrorElf/releases/latest)

# Extract the tarball URL from the JSON response
TAR_URL=$(echo "$RELEASE_JSON" | jq -r .tarball_url)

# Check if the TAR URL is empty
if [ -z "$TAR_URL" ]; then
  echo "Failed to get the TAR URL from the GitHub API"
  exit 1
fi

# Define the output tar file name based on the tag version
TAR_FILE="MirrorElf-$(echo "$RELEASE_JSON" | jq -r .tag_name).tar.gz"

# Download the tarball using curl
echo "Downloading release from $TAR_URL..."
curl -L -o "$TAR_FILE" "$TAR_URL"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "Download successful!"
else
  echo "Download failed!"
  exit 1
fi

# Extract the downloaded tar file
echo "Extracting $TAR_FILE..."
tar -xzf "$TAR_FILE"

# Check if tar extraction was successful
if [ $? -eq 0 ]; then
  echo "Extraction successful!"
else
  echo "Extraction failed!"
  exit 1
fi

# Navigate into the extracted directory
EXTRACTED_DIR=$(tar -tzf "$TAR_FILE" | head -n 1 | cut -d/ -f1)
cd "$EXTRACTED_DIR"

echo "Ready to use the extracted files in $EXTRACTED_DIR"

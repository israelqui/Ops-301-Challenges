#!/bin/bash

# Directory for backups
backup_dir="/var/log/backups"

# Function to get timestamp
get_timestamp() {
    date +"%Y%m%d%H%M%S"
}

# Function to compress and backup log files
compress_and_backup() {
    log_files=("/var/log/syslog" "/var/log/wtmp")

    for file in "${log_files[@]}"; do
        # Get original file size
        original_size=$(du -h "$file" | awk '{print $1}')

        # Get timestamp
        timestamp=$(get_timestamp)

        # Compress file
        compressed_file="${backup_dir}/$(basename "$file")-${timestamp}.zip"
        gzip -c "$file" > "${compressed_file}"

        # Clear contents of log file
        > "$file"

        # Get compressed file size
        compressed_size=$(du -h "$compressed_file" | awk '{print $1}')

        # Display original and compressed file sizes
        echo "Original file size of $file: $original_size"
        echo "Compressed file size of ${compressed_file}: $compressed_size"

        # Compare sizes
        echo "Comparison of sizes:"
        echo "Original: $original_size"
        echo "Compressed: $compressed_size"
        echo "---------------"
    done
}

# Call the function to perform the tasks
compress_and_backup
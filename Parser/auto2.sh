#!/bin/bash

# Create a directory to store the results
mkdir -p resultsTWO

# Define the base directory where your code is
BASE_DIR=$(pwd)

# This loop is now more robust and can handle spaces in file/directory names.
find . -type f \( -name "*.c" -o -name "*.py" -o -name "*.php" -o -name "*.js" -o -name "*.java" -o -name "*.cs" \) -print0 | while IFS= read -r -d $'\0' filepath; do
    
    # Get the filename and extension
    filename=$(basename -- "$filepath")
    extension="${filename##*.}"
    nameonly="${filename%.*}"

    # Create a unique name for the output file, preserving the directory structure
    output_path="resultsTWO/$(dirname "${filepath#./}")/${nameonly}_output.txt"
    mkdir -p "$(dirname "$output_path")"
    
    echo "--- Processing $filepath ---"

    case $extension in
        c)
            docker run --rm -v "$(dirname "${BASE_DIR}/${filepath}")":/src gcc:latest \
            sh -c "gcc /src/\"$filename\" -o /src/a.out && /src/a.out" &> "$output_path"
            ;;
            
        py)
            docker run --rm -v "$(dirname "${BASE_DIR}/${filepath}")":/src python:3.9-slim \
            python3 /src/"$filename" &> "$output_path"
            ;;

        php)
            docker run --rm -v "$(dirname "${BASE_DIR}/${filepath}")":/src php:cli \
            php /src/"$filename" &> "$output_path"
            ;;

        js)
            docker run --rm -v "$(dirname "${BASE_DIR}/${filepath}")":/src node:18-alpine \
            node /src/"$filename" &> "$output_path"
            ;;

        java)
            docker run --rm -v "$(dirname "${BASE_DIR}/${filepath}")":/src openjdk:11-slim \
            sh -c "javac /src/\"$filename\" && java -cp /src \"$nameonly\"" &> "$output_path"
            ;;

        cs)
            echo "SKIPPED: This appears to be an ASP.NET Core file, which cannot be executed as a standalone console application." > "$output_path"
            ;;
            
        *)
            echo "Unsupported file type: $extension for file $filepath" > "$output_path"
            ;;
    esac

    echo "Output for $filename saved to $output_path"
    echo ""
done

echo "--- All files processed. ---"

#!/bin/bash

# Create a directory to store the results
mkdir -p results

# Define the base directory where your code is
BASE_DIR=$(pwd)

# Use 'find' to locate all relevant code files
# Added .java and .cs to the list
find . -type f \( -name "*.c" -o -name "*.py" -o -name "*.php" -o -name "*.js" -o -name "*.java" -o -name "*.cs" \) | while read filepath; do
    
    # Get the filename and extension
    filename=$(basename -- "$filepath")
    extension="${filename##*.}"
    nameonly="${filename%.*}"

    # Create a unique name for the output file, preserving the directory structure
    output_path="results/$(dirname ${filepath#./})/${nameonly}_output.txt"
    mkdir -p "$(dirname "$output_path")"
    
    echo "--- Processing $filepath ---"

    case $extension in
        c)
            # For C: compile with gcc, then run the output
            docker run --rm -v "$(dirname ${BASE_DIR}/${filepath})":/src gcc:latest \
            sh -c "gcc /src/$filename -o /src/a.out && /src/a.out" &> "$output_path"
            ;;
            
        py)
            # For Python: run with the python interpreter
            docker run --rm -v "$(dirname ${BASE_DIR}/${filepath})":/src python:3.9-slim \
            python3 /src/$filename &> "$output_path"
            ;;

        php)
            # For PHP: run with the php command-line interpreter
            docker run --rm -v "$(dirname ${BASE_DIR}/${filepath})":/src php:cli \
            php /src/$filename &> "$output_path"
            ;;

        js)
            # For JavaScript: run with node
            docker run --rm -v "$(dirname ${BASE_DIR}/${filepath})":/src node:18-alpine \
            node /src/$filename &> "$output_path"
            ;;

        java)
            # NEW: For Java: compile with javac, then run the class file
            # This assumes the main class name matches the filename
            docker run --rm -v "$(dirname ${BASE_DIR}/${filepath})":/src openjdk:11-slim \
            sh -c "javac /src/$filename && java -cp /src $nameonly" &> "$output_path"
            ;;

        cs)
            # NEW: For C#: compile and run using the .NET SDK
            # This is a basic attempt that may not work for complex files
            docker run --rm -v "$(dirname ${BASE_DIR}/${filepath})":/src mcr.microsoft.com/dotnet/sdk:6.0 \
            sh -c "cd /src && dotnet new console --force > /dev/null 2>&1 && mv /src/$filename /src/Program.cs && dotnet run" &> "$output_path"
            ;;
            
        *)
            echo "Unsupported file type: $extension for file $filepath" > "$output_path"
            ;;
    esac

    echo "Output for $filename saved to $output_path"
    echo ""
done

echo "--- All files processed. ---"

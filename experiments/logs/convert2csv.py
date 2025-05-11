import csv
import os

def convert_to_csv(input_file_path):
    """
    Reads a file with space-separated or comma-separated values on each line,
    and saves it as a CSV file with a header.

    Args:
        input_file_path (str): The path to the input file.
    """
    if not os.path.exists(input_file_path):
        print(f"Error: Input file not found at {input_file_path}")
        return

    directory, filename = os.path.split(input_file_path)
    base_filename, _ = os.path.splitext(filename)
    output_file_path = os.path.join(directory, f"{base_filename}.csv")

    header = ['xyz_magnitude', 'xyz_cosine_similarity', 'rot_magnitude', 'rot_cosine_similarity']

    try:
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(header)

            for line_number, line in enumerate(infile, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                # Attempt to split by comma first, then by space if comma fails or gives wrong number of fields
                values = [v.strip() for v in line.split(',')]
                if len(values) != 4: # If comma splitting didn't yield 4 values, try splitting by space
                    values = [v.strip() for v in line.split()]


                if len(values) == 4:
                    try:
                        # Attempt to convert to float to ensure data integrity, though not strictly necessary for just writing
                        float_values = [float(v) for v in values]
                        csv_writer.writerow(float_values)
                    except ValueError:
                        print(f"Warning: Could not convert values to float on line {line_number}: {line}. Writing as is.")
                        csv_writer.writerow(values) # Write original string values if conversion fails
                else:
                    print(f"Warning: Line {line_number} does not contain 4 values: {line}. Skipping.")

        print(f"Successfully converted '{input_file_path}' to '{output_file_path}'")

    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main execution ---
# Replace this with the actual path to your file
input_file = '/data/home/qyjh/openvla/experiments/logs/motion_trace.out'
convert_to_csv(input_file)
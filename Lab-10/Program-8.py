def process_file_basic(input_filename, output_filename):
    infile = open(input_filename, 'r')
    outfile = open(output_filename, 'w')
    words_to_delete = ['a', 'an', 'the']

    for line in infile:
        output_line = ''
        for word in line.lower().split():
            if word not in words_to_delete:
                output_line += word + ' '
        outfile.write(output_line.strip() + '\n')

    infile.close()
    outfile.close()
    print(f"Processed to '{output_filename}'")

in_file = input("Input file: ")
out_file = input("Output file: ")
process_file_basic(in_file, out_file)











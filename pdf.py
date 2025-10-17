from pypdf import PdfWriter

merger = PdfWriter()

num_files = int(input("How many PDF files do you want to merge? "))

pdf_files = []

for i in range(num_files):
    filename = input(f"Enter path for PDF file {i+1}: ")
    pdf_files.append(filename)

for pdf in pdf_files:
    merger.append(pdf)

output_name = input("Enter name for the merged PDF (e.g., merged.pdf): ")
merger.write(output_name)
merger.close()

print(f"Successfully merged {num_files} files into '{output_name}'")
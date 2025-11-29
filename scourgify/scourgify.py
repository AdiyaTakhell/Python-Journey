import csv
import sys
def main():
    if len(sys.argv)==3:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
        try:
            check(input_filename,output_filename)
        except FileNotFoundError:
            sys.exit(f"Could not read {input_filename}")
    elif len(sys.argv)<=2:
        sys.exit("Too few  command line arguments")
    else:
        sys.exit("Two many  command line arguments")
def check(input_file,output_file):
    students=[]
    with open(input_file,newline='')as file:
        reader=csv.DictReader(file)
        for row in reader:
            last,first=row["name"].split(", ")
            students.append({"first":first,"last":last,"house":row["house"]})

    with open(output_file,"w",newline='')as file_output:
        writer=csv.DictWriter(file_output,fieldnames=["first","last","house"])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == '__main__':
    main()







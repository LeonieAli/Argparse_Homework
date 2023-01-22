import argparse

parser = argparse.ArgumentParser(description='argparse homework')
parser.add_argument("input_file", default=None, help=("Input text file to read")) 
parser.add_argument('-r', '--replace', help='number that will replace letter', required=True, type=int)
#parser.add_argument("--indent", action="store_true", help=("name will be indented by 4 spaces")) --> not needed for this operation
parser.add_argument("output_file", default=None, help=("Output file to be generated"))

args = parser.parse_args()

def change(replace):

    with open('homew11.txt', encoding='utf-8') as homework_file:
        new_poem = ""
        for line in homework_file:
            
            new_line = line.replace("e", "9")
            #print(new_line)
            new_poem = new_poem + new_line
        print(new_poem)
        return new_poem

change(args.replace) 


with open('output.txt', mode='w', encoding='utf-8') as output_file:
    output_file.write(change(args.replace))

 


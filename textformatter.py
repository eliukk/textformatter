# Script reads given input text file, reads it words, seperates words and special characters to
#own lines and adds "   O" after every line.
import re
import sys

"""
####Input parameters

* -input filename  (Input  filename.)
* -output filename   (filename where the text is written.)

###Example of use:

python textformatter.py -i sample.txt -o sample_out.txt

"""


if __name__ == "__main__":
    
    from optparse import OptionParser
    parser = OptionParser()

    parser.add_option("-i", "--input", type="string", dest="input",
                help="Input file name", metavar="input")

    parser.add_option("-o", "--outputput", type="string", dest="output",
				help="Output file name", metavar="output")                         


    (options, args) = parser.parse_args()
    inputPath = options.input
    outputPath = options.output
    
    if (not inputPath or len(inputPath)==0 ):
        print("Please give the input file with -i parameter")
        sys.exit()

    if (not outputPath or len(outputPath)==0 ):
        outputPath = inputPath.replace('.txt','_output.txt')
    
    with open(inputPath) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    content = [re.sub('([`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?])',r'\n\1\n',x) for x in content]
    
    result = ''.join(content)
    
    content = result.split()
    content = [x+"  O\n" for x in content]
    
    result = ''.join(content)
    
    print result
    
    outputFile = open(outputPath, "w")
    outputFile.write(result)
    outputFile.close()
    
    print("File %s written." % (outputPath))
    
    

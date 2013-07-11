import optparse
import os
import re

def main():
    p = optparse.OptionParser()
    p.add_option('--jobname')
    p.add_option('--doi')
    options, arguments = p.parse_args()
    citation = ''
    if os.path.isfile(options.jobname+ '.bib'):
        with open(options.jobname+ '.bib', 'r') as searchfile:
            for line in searchfile:
                if options.doi in line:
                    citation = line
    if citation == '':
        curlstring = 'C:\curl -LH "Accept: text/bibliography; style=bibtex" http://dx.doi.org/'
        citation = os.popen(curlstring + options.doi).read()
        if 'Internal Server Error' in citation: 
            citation = '{FETCH ERROR,}'
        else:
            with open(options.jobname+ '.bib', 'a') as myfile:
                myfile.write(citation + '\n \n')
    with open(options.jobname+ '.temp', 'w') as myfile:
                myfile.write('\cite{'+re.split('{|,', citation)[1]+'}') 
				
	
if __name__ == '__main__':
    main()
`doicite.sty` is a very simple LaTeX package that provides the `\doi` command, which has the following functionality. If in a LaTeX source file one writes:

    \doi{10.1098/rstb.1952.0012}

the python script `doicite.py` makes an online request to [dx.doi.org](dx.doi.org) (note that `curl` is used for this, so this tool must be available for `doicite` to work), populates a `.bib` file with  

    @article{10.1098/rstb.1952.0012, title={The Chemical Basis of Morphogenesis}, volume={237}, 
    url={http://dx.doi.org/10.1098/rstb.1952.0012}, DOI={10.1098/rstb.1952.0012}, number={641}, 
    journal={Philosophical Transactions of the Royal Society B: Biological Sciences}, 
    publisher={The Royal Society}, author={Turing, A. M.}, year={1952}, month={Aug}, pages={37-72}}


and then replaces the `\doi` command with an appropriate `\cite` command. See `example.tex` for further use cases. Note that the script only makes a request for a citation if it is not already present in the `.bib` file.

Since the citation key is set to be the DOI, one can mix this functionality with other packages that handle citations. For instance, if the appropriate package is loaded, it is possible to use `\bibentry{10.1098/rstb.1952.0012}` (as long as somewhere in the source file the same DOI appears inside a `\doi` command).  

This code is largely inspired by/based [on](http://tex.stackexchange.com/questions/6848/automatically-dereference-doi-to-bib) 
[two](http://stackoverflow.com/questions/9403661/how-can-i-specify-content-type-accepted-when-requesting-a-http-resource-with-rub/940386) questions/answers from Stack Exchange. The key line of code (in my python script), that actually makes the online request for the BibTeX citation, was posted by user Stian Håklev on StackOverflow.



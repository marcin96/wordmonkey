# wordmonkey
Word crawler , minimal pair builder, wordlist comparator, word groupper
Author: Marcin Cherek, Floris Staub
Language: Python 3.4
no 3 party packages
tested on: Windows

-i					Input parameter-> file except -gp directory
-o					Output paramter alway file
-wx					Wordextractor mode [-i,-o]
	-stri				[optional] startindex
	-end				[optional] end word
-lc					list comparator [-i,-o]
	-f				fusion mode makes out from all files in a dir one list
	-diff				difference mode, shows the difference of two lists
	-c				[not-optional] for -diff the file to compare
-mp					minimalpair mode [-i-o]
-gp					grouping mode: searcher for the same wort with different post/-prefix
-sort					sort mode [-i,-o]
-crwl					crawling mode
	-w				website crawl mode
	   -url				[not-optional] url for -w
	-b				book crawl mode
	-phon				phonetic mode [-i,-o]
	-spell				synthesizer mode [-i]
	-deff				deffinition mode [-i]
	-wikipedia			standart crawling mode of wikipedia [-]

--prntOut				prints the changed data out
-v					shows the version
-h					print out the help
-bye					exit
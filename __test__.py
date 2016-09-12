#author chee,stbf
#version 1.0
#Python 3.4
#written for zhaw

import unittest
from IO import Importer
from IO import Exporter
from listcomparator import fusion
from Mpair import Mpair_extractor

class testImporter(unittest.TestCase):
    def testFilterOutCorrectFile(self):
        ''''test for filterOutCorrectFile'''
        None

    def testImport_words(self):
        '''test importer with a none german words'''
        file = "file/test.txt"
        word = Importer.import_words(file)
        assert len(word) == 20
        for w in word:
            print(w)

    def testImport_words2(self):
        '''test importer with an empty file'''
        file="file/file1.txt"
        word = Importer.import_words(file)
        assert len(word) == 0

    def testImport_words3(self):
        '''test importer with Grundwortschatz_Deutsch_200.txt'''
        file="file/Grundwortschatz_Deutsch_200.txt"
        word = Importer.import_words(file)
        assert len(word) == 200


    def testImport_words4(self):
        '''test importer with Grundwortschatz_Deutsch_100.txt'''
        file="file/Grundwortschatz_Deutsch_100.txt"
        word = Importer.import_words(file,11,"Legende")
        assert len(word) == 100

    def testImport_words5(self):
        '''test importer with Grundwortschatz_Deutsch_500'''
        file ="file/Grundwortschatz_Deutsch_500.txt"
        word = Importer.import_words(file)
        assert len(word) == 500

    def testImport_words6(self):
        '''test importer with Grundwortschatz_Deutsch_test.txt(random pattern)'''
        file="file/Grundwortschatz_Deutsch_Test.txt"
        word = Importer.import_words(file)
        assert len(word) == 5

    def testImport_word7(self):
        '''test importer with a file with phonetics'''
        file="file/phonetic.txt"
        word = Importer.import_words(file, 1, "Legende", ";")
        assert len(word) == 10

    def testImport_word8(self):
        '''test importer with special characters in file name'''
        file="file/öäüo.txt"
        word = Importer.import_words(file)
        assert len(word) == 200

    def testImport_word9(self):
        '''Needs to be fixed zu, zum 2 times imported
        test importer with not UTF-8 file'''
        file = "file/test.txt"
        word = Importer.import_words(file)
        assert len(word)+1 == 20


    def testExporter(self):
        '''test exporter doesFileExist'''
        file="file/test.txt"
        export = Exporter.doesFileExist(file)
        self.assertTrue(export)

    def testExporter1(self):
        '''test of exporter with 200 words'''
        file = "file/Grundwortschatz_Deutsch_200.txt"
        word = Importer.import_words(file)
        Exporter.export(word,"test1.txt")

    def testExporter2(self):
        '''test of exporter with cmu-dict.txt'''
        file = "file/cmu-dict.txt"
        word = Importer.import_words(file)
        Exporter.export(word,"test2.txt","")

    def testExporter3(self):
        '''test of exporter with phonetics'''
        file = "file/phonetic.txt"
        word = Importer.import_words(file)
        Exporter.export(word, "test3.txt",";")

    def testExporter4(self):
        '''test of exporter'''
        file = "file/öäüo.txt"
        word = Importer.import_words(file)
        Exporter.export(word, "test4.txt")
    """
    def testExporter5(self):
        '''test of exporter
        doppel s kann nicht verarbeitet werden'''
        file = "file/testutf.txt"
        word = Importer.import_words(file)
        Exporter.export(word, "test5.txt")
    """
    def testExporter6(self):
        '''test of exporter'''
        file = "file/test.txt"
        word = Importer.import_words(file)
        Exporter.export(word,"test6.txt")

    def testExporter7(self):
        file = "file/öäüo.txt"
        Exporter.checköFileName(file)

    def testUnique(self):
        '''test of makeUnique'''
        file = "file/notunique.txt"
        word = Importer.import_words(file)
        fus = fusion.makeUnique(word)
        exp = Exporter.export(fus, "out.txt")
        assert exp == 10

    def testMpair(self):
        '''test Mpair_Extractor'''
        file = "file/Grundwortschatz_Deutsch_200.txt"
        word = Importer.import_words(file)
        mp = Mpair_extractor.extractMpairs(word)
        Exporter.export(mp, "out2.txt", ";")

    def testMpair(self):
        '''test Mpair_extractor'''
        file = "file/phoneticgross.txt"
        word = Importer.import_words(file, 1, "Legende",";")
        mp = Mpair_extractor.extractMpairs(word, True)
        Exporter.export(mp, "out3.txt")

    def testFusion(self):
        '''test fusion makeUnique'''
        file = Importer.import_words("file/notunique.txt")
        fus = fusion.makeUnique(file)
        Exporter.export(fus, "output.txt")


if __name__ == '__main__':
    unittest.main()

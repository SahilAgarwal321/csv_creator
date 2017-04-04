import random
from config import headers, rows, files, names, surnames, subjects, categories, filename


class csv_file_creator(object):
    """
        Class that contains attributes and methods to create csv file. \n
        Attributes : \n
            headers : CSV File Headers \n
            n : number of rows \n
            m : number of files \n
            names : list of names \n
            surnames : list of surnames \n
            subjects : list of subjects \n
            categories : list of categories \n
            filename : file name format
    """
    def __init__(self, headers, rows, files, names, surnames, subjects, categories, filename):
        self.headers = headers
        self.rows = rows
        self.files = files
        self.names = names
        self.surnames = surnames
        self.subjects = subjects
        self.categories = categories
        self.filename = filename
        self.max_score = rows * files

    def create_files(self):
        '''
            Writes to multiple files.
        '''
        for j in xrange(self.files):
            self.create_file(j)
        self.print_message()

    def create_file(self, j):
        '''
            Writes to single file.
            Edit this function to change headers and format of rows.
            j : file number being written.
        '''
        n = self.rows
        m = self.files
        with open(self.filename.format(j+1), "w") as w:
            w.write(headers)
            for i in xrange(j*n, (j*n)+n):
                w.write('\n{0},{1} {2},{3},{4},{5}'.format(i+1, random.choice(self.names), random.choice(self.surnames), random.choice(self.subjects), random.randint(1, self.max_score), self.categories[0]))


    def print_message(self):
        '''
            Prints status message to system.
        '''
        print "{0} CSV files created with {1} rows per file.".format(self.files, self.rows)
        print "Total rows = {}".format(self.max_score)
        print "Names = {} \nSurnames = {} \nSubjects = {} \nCategories = {}".format(self.names, self.surnames, self.subjects, self.categories)


if __name__ == '__main__':
    csv = csv_file_creator(headers, rows, files, names, surnames, subjects, categories, filename)
    csv.create_files()

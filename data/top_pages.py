from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopPages(MRJob):

    def mapper(self, line_no, line):
        """Extracts the Vroot that was visited"""
        cell = csv_readline(line)
        if cell[0] == 'V':
            yield cell[1], 1 

    def reducer(self, vroot, visit_counts):
        """Sumarizes the visit counts by adding them together.  If total visits
        is more than 400, yield the results"""
        total = sum(visit_counts)

        if total > 400:
            yield vroot, total

if __name__ == '__main__':
    TopPages.run()

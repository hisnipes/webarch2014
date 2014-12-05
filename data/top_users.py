from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopUsers(MRJob):

    def mapper(self, line_no, line):
        """Extracts the User that was visited"""
        cell = csv_readline(line)
        if cell[0] == 'V':
            yield cell[3], 1

    def reducer(self, vroot, visit_counts):
        total = sum(visit_counts)
        if total > 20:
            yield vroot, total

if __name__ == '__main__':
    TopUsers.run()

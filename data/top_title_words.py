from mrjob.job import MRJob
from combine_user_visits import csv_readline

class TopTitleWords(MRJob):

    def mapper_get_words(self, _, line):
        cell = csv_readline(line)
        if cell[0] == 'A':
            for word in cell[3].split():
                yield word.lower(), 1

    def reducer_count_words(self, word, counts):
        yield None, (sum(counts), word)

    def reducer_find_top_title_words(self, _, word_count_pairs):
        top_title_words = [ word for word in word_count_pairs ]
        top_title_words.sort()
        top_title_words.reverse()
        for i in range(10):
            yield top_title_words[i]

    def steps(self):
        return [
            self.mr(mapper=self.mapper_get_words,
                    reducer=self.reducer_count_words),
            self.mr(reducer=self.reducer_find_top_title_words)
        ]

if __name__ == '__main__':
    TopTitleWords.run()

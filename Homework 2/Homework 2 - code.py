""""
1. reads a text file containing some English text and counts all words that are:
a) at least 4 letters long and
b) start with a capital letter or are all capitalized (abbreviations etc.)
"""""
# Here we read the file and we remove any special characters and also make a list of the words in order to count the items
my_file = 'English text'

with open(my_file, 'r') as f:
    content = f.read()
mod = content.replace('.', '').replace(',', '')
words = mod.split()


# Here we set the needed conditions of our words (4-long length + contain any capital letters)
count_of_words = 0
capital_letters = []
for word in words:
    if len(word) >= 4 and (any(letter.isupper() for letter in word)):
        count_of_words += 1
        capital_letters.append(word)

print("Count of words: ", count_of_words)
print("List of words: ", capital_letters)


""""
2. Print a list of those words and the number of their occurrences 
Hint: Please note you can use a dictionary structure.
"""""
# Here we show words and their occurrences
from collections import Counter

word_occurrence = Counter(capital_letters)
print(word_occurrence)


""""
3. Use matplotlib or plotly and generate a bar chart showing the top 10 most common words (same conditions 1a) and 1b) apply) 
with the number of their occurrences in descending order.
Save this plot to a file and submit it along the code.
"""""

top_common = word_occurrence.most_common(10)
print(top_common)

import matplotlib.pyplot as plt

top_ten_words = [i[0] for i in top_common]
number_of_occurrence = [i[1] for i in top_common]

plt.bar(top_ten_words, number_of_occurrence)
plt.xlabel('Top Words')
plt.ylabel('Occurrences')
plt.show()
plt.savefig('top_ten_with_occur - bar chart.')



""""
4. For an extra 1 point play with packages that generate clouds of words and generate one for this set of words (conditions 1a) and 1b))
as well as for the whole text.
"""""

# filtering the list based on 2 conditions into words and creating a wordcloud and it's plot
word_list_string = ' '.join(capital_letters)

from wordcloud import WordCloud

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(word_list_string)


plt.figure(figsize=(10, 5))
plt.imshow(wordcloud)
plt.axis('off')
plt.title('Word Cloud Based on Conditions')
plt.show()
plt.savefig('wordcloud_conditions')


# Filtering the list of the whole text and creating a word cloud for it and plot it.
words_in_string = ' '.join(words)

wordcloud_whole_text = WordCloud(width=800, height=400, background_color='white').generate(words_in_string)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud_whole_text)
plt.axis('off')
plt.title('Word Cloud for the whole text')
plt.show()
plt.savefig('wordcloud_whole_text')

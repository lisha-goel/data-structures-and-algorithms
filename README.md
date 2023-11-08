# data-structures-and-algorithms
Suppose you have a large corpus consisting of several books and documents. This could be a corpus of legal
documents, novels, textbooks, research papers, etc. For this assignment, we have provided you with two
different corpuses.
The first corpus is The Collected Works of Mahatma Gandhi which contains 98 books attempting to cover
everything he said or wrote, translated to English. The second corpus contains books by Mahrishi Ramana
(30 December 1879 – 14 April 1950) – a recent spiritual powerhouse who taught the method of self-enquiry
to find out the answers to hard questions of life and this world. According to him ”Our real nature is
Liberation, but we imagine that we are bound and we make strenuous efforts to get free, although all the
while we are free. This is understood only when we reach that state. Then we shall be surprised to find
that we were frantically striving to attain that we already were and are”. His writings contain several deep
spiritual, psychological and practical insights that have helped many people from all walks of life and from
all over the world. While we were unable to get access to the complete works of Mahrishi Ramana, the
current president of Ramanashram has contributed two books for this project. For part 2 of the assignment
(”Quering the LLM”) you must choose one of the two corpuses and fine tune your algorithm and prompts
for getting best possible results. This part will be evaluated subjectively during viva where the quality of
1
your results will play a significant part in your evaluations.
Suppose we would like to know what were the Mahatma’s views on the Partition of India. Or we would
like to find out what was his state of mind in months around Independence of India, we should be able to
answer such questions using the first corpus. We would expect that the answer to such questions somewhere
lies within this huge corpus of 98 books. It may be distributed throughout several paragraphs across the
different books of the corpus. To learn the answer, we would have to painstakingly go through thousands of
paragraphs throughout the corpus, which seems hopelessly inefficient.
However, we now have powerful Large Language Models (LLMs) such as ChatGPT at our disposal, and
this seems like something they would be good at. Unfortunately, one can only provide these LLMs with a
limited context, i.e. amount of information on which they can provide a response. Here is where you will get
to apply your data structures and algorithm skills. Before we begin, here are some notes.
this repository includes my codes for data structure projects such as compiler design and search engine

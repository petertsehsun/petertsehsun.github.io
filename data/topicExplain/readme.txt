The files contain the topic information generated using MALLET for the paper "Topic-based Defect Explanation". 

<MALLET Command>

The command that we use for running MALLET is as follow:

~/mallet/bin/mallet import-dir --input $sourceCode --output output-bigram.mallet --keep-sequence --remove-stopwords --gram-sizes 1,2
~/mallet/bin/mallet run cc.mallet.topics.tui.TopicTrainer --config ~/train-topics.config --input output-bigram.mallet --num-topics $num_topics
, where $sourceCode is the path to the directory that contains the preprocessed source code, and $num_topics is the number of topics.

The train-topics.config contains the configuration for running MALLET, which is shown below:
random-seed = 1
num-iterations = 10000
optimize-burn-in = 1000
optimize-interval = 100
show-topics-interval = 500
output-doc-topics = allfiles1.txt
xml-topic-phrase-report = topic-phrases.xml
 

Each XML file in the folder contains the topic information generated using MALLET. 
For example, eclipse2.0.xml contains the topic information from executing the MALLET 
tool as described above on source code of Eclipse 2.0. 

A topic is a collection of co-occurred words in the preprocessed source code. 
To preprocess the source code, we take out the identifier names and comments from the source code,
 remove common English stopwords, and then stem the words.


<Definition of the XML Tags and Attributes>
We now describe the meaning of each attribute in each of the above defined tags of the XML file.

top_file: The file in the given system that has the highest topic membership with respect to that topic.

post_defect_density: The defect density of a source code file is a well-known software metric,
 defined as the ratio of the number of defects in the file to its size. Using this ratio as motivation,
 we define the post-release topic defect density calculated using post-release defects 
and topic memberships (more details are in the paper).

pre_defect_density: The defect density of a source code file is a well-known software metric,
 defined as the ratio of the number of defects in the file to its size. Using this ratio as motivation,
 we define the pre-release topic defect density calculated using pre-release defects and topic memberships 
(more details are in the paper).

titles: auto generated phrases that represent the title (i.e., label) of the topic.

totalTokens: total number of tokens (i.e., number of unigrams or bigrams in our study) in this topics.

alpha: LDA smoothing parameter on the per-file topic distributions.

id: topic id, which is auto-generated sequentially. Only used for helping refer to topics.

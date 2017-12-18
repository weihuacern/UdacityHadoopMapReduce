# UdacityHadoopMapReduce

# DOCS
```
https://hadoop.apache.org/docs/r2.9.0/
https://hadoop.apache.org/docs/r2.9.0/hadoop-project-dist/hadoop-common/FileSystemShell.html
```

```
/home/hua/hadoop-2.9.0/bin/hadoop fs -ls
/home/hua/hadoop-2.9.0/bin/hadoop fs -put FileName.xxx
/home/hua/hadoop-2.9.0/bin/hadoop fs -tail FileName.xxx
```

# Download dataset
```
mkdir data
cd data
wget http://content.udacity-data.com/courses/ud617/purchases.txt.gz
wget http://content.udacity-data.com/courses/ud617/access_log.gz
```
# L5 MapReduce Code
# Local test without hadoop
```
cd L5MapReduceCode
head -n 50 ../data/purchases.txt >> TestFile
cat TestFile
cat TestFile | ./mapper.py
cat TestFile | ./mapper.py | sort | ./reducer.py
```

# Run with hadoop
```
/home/hua/hadoop-2.9.0/bin/hadoop fs -ls
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input TestFile -output Output
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py -input ../data/purchases.txt -output Output
```

# L6 Project

# Part 1 Purchases
```
cd L6Project/Par1_Purchases
cat ../TestFile | ./mapper_p1q1.py
cat ../TestFile | ./mapper_p1q1.py | sort | ./reducer_p1q1.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p1q1.py -reducer reducer_p1q1.py -file mapper_p1q1.py -file reducer_p1q1.py -input ../TestFile -output Output_p1q1
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p1q1.py -reducer reducer_p1q1.py -file mapper_p1q1.py -file reducer_p1q1.py -input ../../data/purchases.txt -output Output_p1q1
cat ../TestFile | ./mapper_p1q2.py
cat ../TestFile | ./mapper_p1q2.py | sort | ./reducer_p1q2.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p1q2.py -reducer reducer_p1q2.py -file mapper_p1q2.py -file reducer_p1q2.py -input ../../data/purchases.txt -output Output_p1q2
cat ../TestFile | ./mapper_p1q3.py
cat ../TestFile | ./mapper_p1q3.py | sort | ./reducer_p1q3.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p1q3.py -reducer reducer_p1q3.py -file mapper_p1q3.py -file reducer_p1q3.py -input ../../data/purchases.txt -output Output_p1q
```

# Part 2 Access Log
```
cd L6Project/Par2_AccessLog
cat ../TestLog | ./mapper_p2q1.py
cat ../TestLog | ./mapper_p2q1.py | sort | ./reducer_p2q1.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p2q1.py -reducer reducer_p2q1.py -file mapper_p2q1.py -file reducer_p2q1.py -input ../TestLog -output Output_p2q1
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p2q1.py -reducer reducer_p2q1.py -file mapper_p2q1.py -file reducer_p2q1.py -input ../../data/access_log -output Output_p2q1
cat ../TestLog | ./mapper_p2q2.py
cat ../TestLog | ./mapper_p2q2.py | sort | ./reducer_p2q2.py                                                                                                                                                
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p2q2.py -reducer reducer_p2q2.py -file mapper_p2q2.py -file reducer_p2q2.py -input ../../data/access_log -output Output_p2q2
cat ../TestLog | ./mapper_p2q3.py
cat ../TestLog | ./mapper_p2q3.py | sort | ./reducer_p2q3.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper mapper_p2q3.py -reducer reducer_p2q3.py -file mapper_p2q3.py -file reducer_p2q3.py -input ../../data/access_log -output Output_p2q3
```
Note, the correct answer for part 2 quiz 3 is: 
Most popular path:  /assets/css/combined.css;
Count of most popular  117352;

However, my solution is:
Most popular path:  /assets/css/combined.css;
Count of most popular  117353;

# L7 MapReduce Design Patterns

```
cd L7MapReduceDesignPatterns
cat Test/TestForumNode.tsv | ./Q1_FilteringExercise.py
cat Test/TestForumNode.tsv | ./Q1_FilteringExercise.py | sort | ./Identity_reducer.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper Q1_FilteringExercise.py -reducer Identity_reducer.py -file Q1_FilteringExercise.py -file Identity_reducer.py -input ../data/forum_node.tsv -output Output_q1
cat Test/TestForumNode.tsv | ./Q2_TopN.py
cat Test/TestForumNode.tsv | ./Q2_TopN.py | sort | ./Identity_reducer.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper Q2_TopN.py -reducer Identity_reducer.py -file Q2_TopN.py -file Identity_reducer.py -input ../data/forum_node.tsv -output Output_q2
cat Test/TestForumNode.tsv | ./Q3_InvertedIndex_mapper.py
cat Test/TestForumNode.tsv | ./Q3_InvertedIndex_mapper.py | sort | ./Q3_InvertedIndex_reducer.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper Q3_InvertedIndex_mapper.py -reducer Q3_InvertedIndex_reducer.py -file Q3_InvertedIndex_mapper.py -file Q3_InvertedIndex_reducer.py -input ../data/forum_node.tsv -output Output_q3
cat ../L6Project/TestFile | ./Q4_Mean_mapper.py
cat ../L6Project/TestFile | ./Q4_Mean_mapper.py | sort | ./Q4_Mean_reducer.py
/home/hua/hadoop-2.9.0/bin/hadoop jar /home/hua/hadoop-2.9.0/share/hadoop/tools/lib/hadoop-streaming-2.9.0.jar -mapper Q4_Mean_mapper.py -reducer Q4_Mean_reducer.py -file Q4_Mean_mapper.py -file Q4_Mean_reducer.py -input ../data/purchases.txt -output Output_q4
```


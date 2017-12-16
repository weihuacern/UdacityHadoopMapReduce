# UdacityHadoopMapReduce

# DOCS
https://hadoop.apache.org/docs/r2.9.0/
https://hadoop.apache.org/docs/r2.9.0/hadoop-project-dist/hadoop-common/FileSystemShell.html

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
```


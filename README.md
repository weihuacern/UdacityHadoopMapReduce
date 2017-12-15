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

# Locat test without hadoop
```
cd L3MapReduceCode
head -n 50 ../data/purchases.txt >> TestFile
cat TestFile
cat TestFile | ./mapper.py
cat TestFile | ./mapper.py | sort | ./reducer.py
```

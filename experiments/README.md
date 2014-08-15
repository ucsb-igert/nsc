# Experiments

These experiments include tests and comparisons such as determining the
scalability or accuracy of an algorithm.

To run all of the experiments, do
```bash
$ ./run_all
```

Because this may take a very long time, it is better to write the progress of
the script to a file:
```bash
$ ./run_all &> progress &
```

# Possible Future Experiments

 1. Outlier detection

    Finding node values that are outliers. The idea is that Slice Tree should
    put outliers into a partition of their own.

 2. Value prediction

    Predicting the value of a node based on the values of its neighbors.

 3. Trend analysis/change

    Analysis of how node values are changing over time.

# time_delta

### Requerments:

- Python2.7 or newer.

- Pandas library installed with version >= 0.23.0.

Pandas installation manual: https://pandas.pydata.org/pandas-docs/stable/install.html

____________________________________________________________________________________________



### Hi!

Say you need to calculate performance and obtain time delta of two durations and do this instantly without complex manual calculations. 

If so, this wonderful script is for you!

All you need to do is prepare two files with time durations in them (for instance like timestamp_file1 and timestamp_file2 in this repo) and use them as arguments:


    ./time_delta.py timestamp_file1 timestamp_file2
    
And the output will be like this:

        timestamp_file1  timestamp_file2   TimeDelta
    0   00:01:09.881968  00:00:28.754326  -0:00:41.127642
    1   00:28:09.376129  00:28:37.043199   0:00:27.667070
    2   02:31:09.080779  02:33:59.673946   0:02:50.593167


The math is simple: 

    current run (timestamp_file2) - past run (timestamp_file1) = TimeDelta.

And if the result is negative - you have an improvement, if not - degradation.

Please note that you can use any naming for the input files:

    ./time_delta.py first second

It will just change headers names of the table:

        first            second            TimeDelta
    0   00:01:09.881968  00:00:28.754326  -0:00:41.127642
    1   00:28:09.376129  00:28:37.043199   0:00:27.667070
    2   02:31:09.080779  02:33:59.673946   0:02:50.593167

And all your outputs are conveniently stored in CSV files to use it in your further work:

    20191024_11_05_49_first_vs_second.csv
    
 
Any feedback or notes will be welcomed!

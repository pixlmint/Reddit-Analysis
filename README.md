# Reddit-Analysis
A program to save reddit data to csv files for analytics

### How to use:
1. Clone/ Download Repository
2. Create folder "Data" in root directory
<pre>
-Reddit-Analysis
--Code
---Python scripts
--Data
---generated sub folders
</pre>

3. In "Code" folder create file "keys.txt", insert:
<pre>
personal
[Reddit API personal token]
secret
[Reddit API secret token]
password
[Reddit User Account password]
(if you want to connect to ftp server:)
ftp-password
[password]
</pre>

4. Run Script "Main".
* Currently, it will first start the thread then download the 20 newest posts of the subreddits in the list at the very top.

### Configurations:

#### SQL
This version of the program needs the connection to a mySql Database which runs on the user's machine (localhost)
The name of the database is 'reddit_analysis', password is nothing.

#### Subreddits:
If you want data to different subreddits, just insert it into the array in <code>main.py</code>

#### Filter:
(depracated -> it now gets newest posts by default and updates them continually)

#### FTP:
Currently it points at my server, hosted on bplaced. To change this, go into <code>ftp_writer.py</code>

In there just configure the host and username. The next line in the code directs to the directory on the server where the files will be saved.

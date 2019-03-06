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
#### Subreddits:
If you want data to different subreddits, just insert it into the array in <code>main.py</code>

#### Filter:
Reddit has a couple of filters for how the posts are sorted:
<pre>
* Hot
* Top
* New</pre>

By default, it will get posts of new and hot with a limit of 20 (for better performance)

To change that, go in <code>main.py MyThread.run</code> and change string within function call <code>run()</code>

#### FTP:
Currently it points at my server, hosted on bplaced. To change this, go into <code>ftp_writer.py</code>

In there just configure the host and username. The next line in the code directs to the directory on the server where the files will be saved.

# 0x02-shell_redirections

##0. Hello World
*A script that prints “Hello, World”, followed by a new line to the standard output.

##1. Confused smiley
*A script that displays a confused smiley "(Ôo)'.

##2. Let's display a file
*A script that display the content of the /etc/passwd file.

##3. What about 2?
*A Script that display the content of /etc/passwd and /etc/hosts

##4. Last lines of a file
*A Script that display the last 10 lines of /etc/passwd

##5. I'd prefer the first ones actually
*A Script that display the first 10 lines of /etc/passwd

##6. Line #2
*A Script that displays the third line of the file iacta.

##7. It is a good file that cuts iron without making a noise
*A Shell Script  that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

##8. Save current state of directory
*A Script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

##9. Duplicate last line
*A Script that duplicates the last line of the file iacta

##10. No more javascript
*A Script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

##11. Don't just count your directories, make your directories count
*A Script that counts the number of directories and sub-directories in the current directory.
**The current and parent directories should not be taken into account
**Hidden directories should be counted

##12. What’s new
*A Script that displays the 10 newest files in the current directory.
**Requirements:
***One file per line
***Sorted from the newest to the oldest

#13. Being unique is better than being perfect
*A Script that takes a list of words as input and prints only words that appear exactly once.
**Input format: One line, one word
**Output format: One line, one word
**Words should be sorted

#14. It must be in that file
*Display lines containing the pattern “root” from the file /etc/passwd

#15. Count that word
*Display the number of lines that contain the pattern “bin” in the file /etc/passwd

#16. What's next?
*Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

#17. I hate bins
*Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.

#18. Letters only please
*Display all lines of the file /etc/ssh/sshd_config starting with a letter.
**include capital letters as well

#19. A to Z
*Replace all characters A and c from input to Z and e respectively.

#20. Without C, you would live in hiago
*A script that removes all letters c and C from input.

#21. esreveR
*A script that reverse its input.

#22. DJ Cut Killer
*A script that displays all users and their home directories, sorted by users.
**Based on the the /etc/passwd file

## 23. Empty casks make the most noise
* Write a command that finds all empty files and directories in the current directory and all sub-directories.
* Only the names of the files and directories should be displayed (not the entire path)
* Hidden files should be listed
* One file name per line
* The listing should end with a new line
* You are not allowed to use basename, grep, egrep, fgrep or rgrep

## 24. A gif is worth ten thousand words
* Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
* Hidden files should be listed
* Only regular files (not directories) should be listed
* The names of the files should be displayed without their extensions
* The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
* One file name per line
* The listing should end with a new line
* You are not allowed to use basename, grep, egrep, fgrep or rgrep

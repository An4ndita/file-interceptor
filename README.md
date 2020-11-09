# file-interceptor
program to intercept and modify files

An elaborated description of the usage of this tool is available in the following article, please visit this link for more details.

https://an4ndita.medium.com/writing-a-file-interceptor-program-in-python-coding-for-cyber-security-program-6-mitm-16b590be2f69


# Usage :

Run the ARP Spoofer program to work as Man In The Middle.
 
Run the iptables command :

For remote computers, run the following command in the terminal.

"iptables -I FORWARD -j NFQUEUE --queue-num 0"

and for local computers, run the following commands in the terminal.

"iptables -I INPUT -j NFQUEUE --queue-num 0"

"iptables -I OUTPUT -j NFQUEUE --queue-num 0"

Then download and run this code :

 "git clone https://github.com/An4ndita/file-interceptor.git"

 "cd file-interceptor"

 "mousepad replace-downloads.py"

Edit the Location: & Replace it with the file that you want the victim to download.

 "python3 replace-downloads.py"

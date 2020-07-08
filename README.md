# XML parser with multiprocessor usage

### Description

This is the test task for the technical interview.
The point is: demonstrate how multiprocessing could affect to parsing XML-files. 

I was surprised: disk IO performance also was improved, 
up to 6 times at strong droplet, see in the test section at the end.

### Installation (fresh Ubuntu example)


sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8


sudo apt install python3-pip
pip3 install pipenv

git clone https://github.com/dremdem/xml_parse_with_multicore.git
cd xml_parse_with_multicore

pipenv install 
pipenv shell




### TESTS

MAC: MacOs 10.15.4, 2,6 GHZ, 4-core i7

[2020-07-08 21:09:43,307]  Started with the following parameters:
            - multiprocessing: False
            - number of ZIP-files: 1000
            - number of XML-files: 100
            - number of cores: 8
[2020-07-08 21:10:26,712]  The ZIP-generation is done. Execution time is 43.367 seconds.
[2020-07-08 21:10:33,203]  sys.getsizeof(main_list): 829000, len: 100000
[2020-07-08 21:10:34,480]  The ZIP-parsing is done. Execution time is 7.768 seconds.
[2020-07-08 21:10:41,334]  Started with the following parameters:
            - multiprocessing: True
            - number of ZIP-files: 1000
            - number of XML-files: 100
            - number of cores: 8
[2020-07-08 21:11:24,989]  The ZIP-generation is done. Execution time is 43.631 seconds.
[2020-07-08 21:11:26,828]  sys.getsizeof(main_list): 829000, len: 100000
[2020-07-08 21:11:27,803]  The ZIP-parsing is done. Execution time is 2.814 seconds.

DO: Droplet minmal: 
2 CPU/ 4 GB Memory / 25 GB Disk / AMS3 - Ubuntu 18.04.3 (LTS) x64

[2020-07-08 16:07:46,449]  Started with the following parameters:
            - multiprocessing: False
            - number of ZIP-files: 50
            - number of XML-files: 100
            - number of cores: 2
[2020-07-08 16:07:47,223]  The ZIP-generation is done. Execution time is 0.766 seconds.
[2020-07-08 16:07:47,482]  sys.getsizeof(main_list): 44200, len: 5000
[2020-07-08 16:07:47,517]  The ZIP-parsing is done. Execution time is 0.294 seconds.
[2020-07-08 16:08:04,370]  Started with the following parameters:
            - multiprocessing: True
            - number of ZIP-files: 50
            - number of XML-files: 100
            - number of cores: 2
[2020-07-08 16:08:05,148]  The ZIP-generation is done. Execution time is 0.771 seconds.
[2020-07-08 16:08:05,394]  sys.getsizeof(main_list): 44200, len: 5000
[2020-07-08 16:08:05,439]  The ZIP-parsing is done. Execution time is 0.29 seconds.
[2020-07-08 16:08:57,015]  Started with the following parameters:
            - multiprocessing: False
            - number of ZIP-files: 300
            - number of XML-files: 100
            - number of cores: 2
[2020-07-08 16:09:01,713]  The ZIP-generation is done. Execution time is 4.691 seconds.
[2020-07-08 16:09:03,258]  sys.getsizeof(main_list): 253000, len: 30000
[2020-07-08 16:09:03,559]  The ZIP-parsing is done. Execution time is 1.845 seconds.
[2020-07-08 16:09:11,406]  Started with the following parameters:
            - multiprocessing: True
            - number of ZIP-files: 300
            - number of XML-files: 100
            - number of cores: 2
[2020-07-08 16:09:16,080]  The ZIP-generation is done. Execution time is 4.667 seconds.
[2020-07-08 16:09:17,552]  sys.getsizeof(main_list): 253000, len: 30000
[2020-07-08 16:09:17,945]  The ZIP-parsing is done. Execution time is 1.865 seconds.

DO: Droplet maximal: 

32 CPU/64 GB Memory / 400 GB Disk / AMS3 - Ubuntu 18.04.3 (LTS) x64

[2020-07-08 18:06:03,924]  Started with the following parameters:
            - multiprocessing: False
            - number of ZIP-files: 1000
            - number of XML-files: 100
            - number of cores: 32
[2020-07-08 18:06:19,529]  The ZIP-generation is done. Execution time is 15.575 seconds.
[2020-07-08 18:06:24,508]  sys.getsizeof(main_list): 829000, len: 100000
[2020-07-08 18:06:25,792]  The ZIP-parsing is done. Execution time is 6.263 seconds.
[2020-07-08 18:06:31,180]  Started with the following parameters:
            - multiprocessing: True
            - number of ZIP-files: 1000
            - number of XML-files: 100
            - number of cores: 32
[2020-07-08 18:06:47,028]  The ZIP-generation is done. Execution time is 15.818 seconds.
[2020-07-08 18:06:47,619]  sys.getsizeof(main_list): 829000, len: 100000
[2020-07-08 18:06:48,580]  The ZIP-parsing is done. Execution time is 1.553 seconds.




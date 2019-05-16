# Snake in the box
This algorithm solves snake in the box problem in exact way. It will work in acceptable time for input size less than 8.

### Prequisites
Execute following command in order to make setup script executable
```
chmod +x setup.sh
```
 
### Installation
Run script setup.sh which will create necessary virtual environment for python and create NumPy library

### Usage
In order to enter virtual environment pleae enter this into terminal
```
source venv/bin/activate
```
After executing this line, to use this program just type 
```
python3 solution.py [-n][--length-of-the-word]
```

### How to parse output
For n = 3, output should look like this 
```
[0, 1, 2, 5, 4]
['000', '001', '011', '111', '110']
4
Time passed 6.4000000000064e-05s
```
First list represent indices of binary words of lenght n which solves snake in the box problem.

Second list shows binary these words itself.

Third line with single number presents length of snake obtained from computations

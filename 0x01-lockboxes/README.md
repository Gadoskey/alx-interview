# **Lockboxes Unlocking Algorithm**

**Author**

Yusuf Mustapha Opeyemi [mustopha.yusufope@gmail.com]

**Overview**

This project solves the problem of determining if all locked boxes can be opened given that some boxes contain keys to others. The function `canUnlockAll` takes a list of lists, where each inner list represents a box, and each element in the list represents a key to another box. The goal is to determine whether all the boxes can be unlocked starting from the first box.

**Table of Contents**

- Installation
- Usage
- Example
- Explanation
- Contributing
- License

---

**Installation**

### Prerequisites

Ensure you have the following installed:

- `Python 3.x`

### Steps

Clone the repository to your local machine:

`git clone https://github.com/your-username/0x01-lockboxes.git`


Navigate to the project directory:

`cd 0x01-lockboxes`

Usage

To check if all the boxes can be unlocked, you need to run the main_0.py script, which contains test cases. Modify the script as necessary to input your own boxes configuration.


python3 main_0.py
Inside main_0.py, you can modify the boxes variable to test other configurations. For example:

boxes = [[1], [2], [3], [4], []]
In this case, the function checks if all the boxes can be unlocked starting from box 0.

Suppose you have the following boxes:

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

python3 main_0.py
The output will be:

True
This means all boxes can be unlocked.

Explanation

The program works by simulating the process of unlocking the boxes:

You always start with box 0 unlocked.
Each box may contain keys to other boxes.
You can use the keys you find to unlock the respective boxes.
The function checks if you can unlock all the boxes, and it returns True if successful, or False if not.
The algorithm tracks the keys you collect and the boxes you open. It avoids repeatedly opening boxes that are already unlocked.

For a detailed explanation, refer to the comments inside the script.


**Contributing**

Contributions are welcome! If you'd like to improve the project or add new features, feel free to submit a pull request.

***To contribute:***

Fork the repository.

Create a new branch with your feature or fix:

`git checkout -b feature-name`

Commit your changes:

`git commit -m "Added a new feature"`

Push to the branch:

`git push origin feature-name`

Open a pull request.
# **Pascal's Triangle Generator**

**Author**

Yusuf Mustapha Opeyemi [mustopha.yusufope@gmail.com]

**Overview**

This project generates Pascal's Triangle up to a given number of rows. Pascal's Triangle is a triangular array where each element is the sum of the two elements directly above it in the previous row. This Python script calculates the values for each row and displays the triangle.

**Table of Contents**

Installation
Usage
Example
Explanation
Contributing
License

**Installation**

Prerequisites

`Python 3.x`

**Steps**

Clone the repository to your local machine:

`git clone https://github.com/your-username/pascal-triangle-generator.git`

Navigate to the project directory

`cd 0x00-pascal_triangle`


**Usage**

To use the Pascal's Triangle generator, simply run the script and provide the number of rows you'd like to generate.

`python3  0-pascal_triangle.py (number of rows)`

The program will print Pascal's Triangle up to the number of rows you specify inside the script.

***For Example***

If you modify the script to call `python3  0-pascal_triangle.py 5` and run the program, the output will look like this:

[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]

This is Pascal's Triangle with 5 rows.

**Explanation**

The program works by generating each row of Pascal's Triangle based on the values from the previous row:

The first and last element of each row is always 1.
The remaining elements are the sum of the two elements directly above it in the previous row.
For a detailed explanation of how the code works, refer to the Comments in Code section within the script.

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
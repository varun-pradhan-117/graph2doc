# graph2doc

`graph2doc` converts a text-based tree diagram into a real directory structure on disk.

It takes input like:
```
python_app
├── README.md
├── requirements.txt
├── setup.py
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   └── utils.py
└── tests
    ├── __init__.py
    └── test_main.py

```
and creates actual folders/files matching that structure.

---

## Installation

### Install from PyPI
```
pip install graph2doc
```

---

## How to Use

After installing, you can run the tool from anywhere using the command:
```
graph2doc
```
By default, it looks for a file named `tree.txt` in the current directory and creates the folder structure in the current working directory.

### Use a custom input file
```
graph2doc -i path/to/your_tree.txt
```

### Use a custom output directory
```
graph2doc -o path/to/output_folder
```

### Specify both input and output explicitly
```
graph2doc -i path/to/tree.txt -o path/to/output_folder
```

### Example input .txt
```
project
├── README.md
├── requirements.txt
├── setup.py
├── app
│   ├── init.py
│   ├── main.py
│   ├── config.py
│   └── utils.py
└── .gitignore
```


### What it does

`graph2doc` reads a “tree-like” structure and generates real folders and files matching it.  
If intermediate directories don’t exist, they are created automatically.
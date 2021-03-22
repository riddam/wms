# Warehouse Management

This console application provides three warehouse options:
- Add new container in warehouse
- Display existing containers
- Ship the container 

Table of Contents:
--------------------
- [Installation](#Installation)
- [Tests](#Tests)
- [Usage](#Usage)
- [Assumptions](#Assumptions)
- [Example](#Example)


## Installation

**Docker:**   
- Build docker image using docker build command
```shell
$ docker build -t image_name .
```

**Virtual environment**   
- Activate virtual environment:
```shell
$ python3 -m venv venv
$ . venv/bin/activate 
```

- Install package requirements:
```shell
$ pip3 install -r requirements.txt
```

## Tests
**Docker:**     
- Docker Command to run application test cases:
```shell
$ docker run -e RUNTEST=yes image_name
```

**Virtual environment**  
- Command for virtual environment:
```shell
wms$ pytest core/tests.py
```

## Usage
**Docker:**  
- Run the command line application in Docker using following command:
```shell
wms$ docker run -ti image_name
```

**Virtual environment**  
- Command for virtual environment:
```shell
wms$ python main.py
```

## Assumptions
- Infinite warehouse capacity
- there are only 2 methods of shipping 
    - car for box delivery
    - bike for bag delivery
- Available containers - Bag, Box(normal), Box(cold)
- 3 main types of containers -that will be increased - normal boxes, cold
boxes and bags. For the boxes, it is important to know the height, width and
depth. For the bags, besides height and width, weight is important.


## Example
Command line application running in terminal:
```shell
wms$ python main.py
----------Welcome to Warehouse Management System------------
Available options: 
1. Add new container 
2. Total container available 
3. Ship container 
Enter your choice(-1 to exit): 1
Enter container type based on available choices
1. Bag
2. Box
3. ColdBox
Enter container number: 1
Enter length: 1
Enter width: 2
Enter weight: 3
Container Bag(1) added successfully
Enter your choice(-1 to exit): 1
Enter container type based on available choices
1. Bag
2. Box
3. ColdBox
Enter container number: 2
Enter length: 3
Enter width: 1
Enter depth: 2
Container Normal Box: 2 added successfully
Enter your choice(-1 to exit): 1
Enter container type based on available choices
1. Bag
2. Box
3. ColdBox
Enter container number: 3
Enter length: 1
Enter width: 3
Enter depth: 2
Enter temp: -12
Container Cold Box: 3 added successfully
Enter your choice(-1 to exit): 2
[Bag: 1, Normal Box: 2, Cold Box: 3]
Containers count of each type: 
Bag : 1
Box : 1
ColdBox : 1
total containers: 3
Enter your choice(-1 to exit): 3
Enter container id to deliver: 2
Box 2 delivered by Car
Enter your choice(-1 to exit): -1
Bye!!


```


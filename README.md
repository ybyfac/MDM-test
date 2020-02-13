# Sparse Arrays
## Context:
There is a collection of input *strings* and a collection of *query* strings. For each query string, determine how many times it occurs in the list of input strings.
   input: **str**  => output: **Dict[str,int]** as following:
 
##
 
### Prerequisites
 - docker  (https://docs.docker.com/install/)  
 - docker-compose (https://docs.docker.com/install/)  
 - python 3.7+ (https://www.python.org/downloads/)
 
##
 
### Step 1 - Clone projet
#### Launch:
      git clone https://github.com/ybyfac/MDM-test.git
      cd MDM-test
#### Result:
      Cloning into 'MDM-test'...
      ...
      Resolving deltas: 100% (149/149), done.
 
##
 
### Step 2 - Build our Docker Image
#### Launch:
      docker build . -t test_mdm
#### Result:
 
    Sending build context to Docker daemon 7.874MB
    Step 1/12 : FROM python:3.7-buster
   
    ...
   
    Step 12/12 : ENTRYPOINT ["python", "main.py"]
     ---> Running in 374ed23dcdd1
    Removing intermediate container 374ed23dcdd1
     ---> 7afbef8017ff
    Successfully built 7afbef8017ff
    Successfully tagged test_mdm:latest
 
## 
       
### Step 3  - Run a 'test-mdm' container
#### Launch: (outdated since part 4)
      docker run -t test_mdm ab,abc,bc
#### Result:
      {ab: 2, abc: 1, bc: 0}
##  
### Step 4 - Start a 'test-mdm' and serve Flask server & Swagger-ui
 
#### Launch:
 
      docker-compose up
#### Result:
    Creating mdm-test_test-mdm_1 ... done
    Attaching to mdm-test_test-mdm_1
    test-mdm_1  |  * Serving Flask app "main" (lazy loading)
    test-mdm_1  |  * Environment: production
    test-mdm_1  |    WARNING: This is a development server. Do not use it in a production deployment.
    test-mdm_1  |    Use a production WSGI server instead.
    test-mdm_1  |  * Debug mode: off
    test-mdm_1  | 2020-02-12 19:14:28,673 :: INFO ::  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 
### Step 5  - Open Swagger UI
 
![enter image description here](https://image.noelshack.com/fichiers/2020/07/3/1581536610-screenshot-2020-02-12-sparcearraycreator.png)
Open in a browser http://127.0.0.1:5000/ and Try out the GET method:
     
    /sparsearray/compute/{query}
 
with ***query*** as input
##### Changing the string to query:
to change the value of the string you have to go:
 
    nano docker-compose.yaml
   
and edit this environement value:
   
       version: "3"
       services:
           test-mdm:
            image: test_mdm:latest
            environment:
                STRINGS:  ab,ab,ab,abc,abc,abc
            ports:
                - "5000:5000"
       
#####  Scenario:
The API gives this two possible output:
 - Code 200     OK    
 - Code 400     Bad Request / Invalid Format
 
##### Improvement to do:

- test with Mock
- inspect with SonarQube
# Sparse Arrays
#####Context:
There is a collection of input *strings* and a collection of *query* strings. For each query string, determine how many times it occurs in the list of input strings.
   input: **str**  => output: **Dict[str,int]** as following:

##### PART 2 - How to call the program with python:
      
     python -m main ab,abc,bc
     
##### PART 3 - How to call the program with docker: 
(outdated since part 4)
      
      docker build . -t test_mdm
      
and then:
      
      docker run -t test_mdm ab,abc,bc
     
#####Result:
      
    {ab: 2, abc: 1, bc: 0}
      
##### PART 4 - How to call the program with docker-compose:
      
      docker-compose up --build 
      
##### Result:
go to http://127.0.0.1:5000/ and check the get method:
      
    /SparseArray/create/{query}
     
with ***query*** as input 
##### Changing the string to query:
to change the value of the string you have to go:

    deployments/test-mdm.env
    
and edit this environement value:
    
    STRINGS=<your value>
       
##### Scenario:
The API gives this two possible output:
    
    1. Code 200 everything is fine 
    
    2. COde 400 Invalid Format 
    
![Image](dataIsComing.png "icon")


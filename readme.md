## Day 2
### Your first LLM call and understanding response.

### venv (virtual envorment)

```
Activate command:- source env/bin/activate

In virtual envorment we can create a seprate room where we can install a all depencency
version all the things those are not affect to outside the virtual env

```

### LLM Calls (Large language mode)

how to call LLM ?

```
1) we need a API Key. (make your own api key on grok website :- https://console.groq.com/keys)
2) make a client (we used groq as a server so we make a one client they interact with a grok)
3) choose a models
4) messages: In message two important things are there 

            1. role: In api call 3 types of role are there
                        i) User role: (message that was sended to GPT from your side.)
                        ii) Assistance role: (GPT respose back your query)
                        iii) System role: (you can assing any role like "give all the answer in one words")
                        
            2. content
             
4) Response: In response many types of response are there but we deals with 2 important things
            1. choices: this is the main answer (Array of answers)
            2. Usage: for handling your message how much Token is used.      
```

## Day 3
### System role and Temprature

```
System role: system role tell a LLM. (whats the relation between you and system in this chat)

for example: role -> system
             content -> you are my gf

             role -> user
             content -> i love you


Temprature: (personality)

In gork ai you can pass {0 to 2} temps (0,1,2)
t=0         t=2
0 : safe    2: Risk taker(creative)

LLM are predection machine. not a truth telling machine.
```


## Day 4
### Token

```
token means Comman reusable words

LLM {computer program} they only understand 0/1

eg: you give some query "Hello" -> it converted your query into a number and then it start processing
    give a output as a number -> and it convert into your language.

- how to convert letter in number??

few method are there like 
1) letter to number (worst method)
   for eg:- "HELLO" => [H->12 E->23 L->43 O->34] => 12+23+43+34 => ....  

2) words to number -> this is also not good because english word is infinite
   for eg:- "i am rahul kumar singh" => ["i"," am"," rahul"," kumar"," singh"] 


Token -> Comman reusable words

they scan all the word those are present in internet and take a common words and treate like a tokens.

For eg:- "The" -> Token   "rahul" -> not a token, so they break "rahul" into sub token.
         "In" -> Token.   "Banglore" -> Token
         "name" -> Token


You write some prompt and it will break into a token and that Token converted into a number and send to a GPT
GPT generate some answer and that answer also break into a Token 

for eg:- Input Token(100 token) + Output Token(200 token) = Total token cost(300 token)

Input Token -> Prompt token
Output Token -> completation Token

```



## Day 5
### Structured Output
#### we learn Pydantic + JSON

```
prompt ----> (LLM) ----> paragraph
(String)    (chatGPT)    (String)

We can easily understand String and read it. but it is very difficult to a 
machine understand the String

AI Agents ---> Code ---> decision
         output          output

so we generate something they give response as a String and that output we pass to a
computer system but there is the problem computer not understand String
so, we need to Structure your output then we can give to a machine for any operations.

that's the biggest problem then JSON will come for solve this problem

JSON (Javascript Object Notations)

for store any data in JSON formate we can take a help of pydantic
```





## Day 6
### Mini Project

```
LLM Resume Evaluator

class for Job_D
   1) role
   2) required skills
   3) preffered skills
   4) Min experience
   5) Eductional requirment
   6) Responsibilities

write a system prompt- we can tell to a llm your are expert hr assistance take a {Job_D}
                       i will provide job description you work is based on Job_D you can 
                       give all the information to a job description.
Write a user prompt
```



## week 2
## Day 7
### Prompt Engineering

```
- Why we need Prompt Engineering?
LLM always give different answer. so when we are used in a production level
we don't need different answer so for stable the LLM solution we used prompt
engineering.

1> for stable the answer
2> You can limit your chatbot what types of question they can response back 


- Bad Prompt
This is a user complain: My laptop is not working handle this.


For write a good prompt we can follow 6 steps

1> role
2> Task
3> constraints
4> output formate
5> Zero/ one Sort
6> Fallback


1> Role:- who are you?
          your role should be domain or responsibility related?

          eg:- you are seniour engineer responsible for reviewing a code.


2> Task:- what you should do?
          eg:- classification the issue

3> Constraints :- set a boundry
                   eg:- issue should be only 3 types 
                        1) Billing.  2) technical.  3) return. 

4> output formate :- what types of response we needed
                     eg:- one word answer

5> Zero/ one Sort/ Few sort:- you can gives a example to a LLM to understand
                    if(you provide example to understand llm how they can do the task) -> one sort
                    if(you not give any example) -> then zero sort               
                    if(you give more they one example to understand llm how they respond back) -> few sort

6> fallback :- if unrelated query are asking then they not give any answer

```


## Day 7
### Re Act (Reasoning + Action)

```
With help of training data you can't know the current news or anything because that data are one 
type of historical data. 

so solving this types of problem we make tools under a chatGPT
like we can give a access to different APIs to get a current data
eg:- we can give a current weather apis to a GPT (with help of this they can display the current wether reports)

chatGPT have access: [Historical data + Tools]

-- Then what the problem will occur and how we can solve the problems??

1) chatGPT have many tools :- how we can know this tools is used for solving this problem
                              (This is main problem which tools they can used, and when this tools will used
                              and how much they can used)
                              

-- For Solving this problem ReAct (Reasoning + Action) comes into the pitcher

LLM see your prompts
   eg: <I want to buy a iphone7, I have ₹5,000. If i buy it. then how much money will have i left with?>

      (i) They need to check the apple price list -> whats the price of iphone7 -> 2,000
      (ii) store the user price ammount data -> user have 5,000 
      (iii) They used calculator tools for geeting the result -> 5,000 - 2,000 = 3,000


So, LLM reasoning your prompt and check 
   1) they need whats types of tools and get a answer
   2) and take that answer and used different tool and finds the answer
   3) ...This is the continue loop where they used many tools for geetings a main results

   That's we call ReAct Loop ((Reasoning + Action))

   You just give a PROMPT
   LLM read your PROMPT and they decide how and which tools they used for geeting the results


So, if we want to making a Agents then it important to used tools. because only based on LLM we can't 
able to build Agents.



1> First we need to gives a tools (simple python program)

2> Then you write a System prompt (dicide your works                                     
                                   for that work which avaliable tools is usefull         
                                   if you find out then execute the tool                 
                                   and those observation/solution will come              
                                   then reused the solution for geeting the main result)  

```



## Day 8
### Prompt Chaining

```
We write a prompt --> give to a LLM --> they provide us output.

When we are in production then your task is very complex
so, we have two method for assing a task
1) you can explain all the complete task in one single prompt and give to a LLM
    [prompt] --> [LLM] --> [sol]
2) you can divide your prompt in different different sub prompt and give to there specific LLM 
    (i) query
        <i> [prompt1] --> [LLM] --> [solution1] 
        <ii> [prompt2] --> [LLM] --> [solution2]  {solution1 help to prompt2 to find a answer}
        .
        .

In this you basically divide prompt into different sub prompt and all sub prompt have different LLM
they find answer and pass to a another prompt.

Let's take a example 
parsing a resume

prompt 1:- Extract a skill from resume --> LLM call1
prompt 2:- Extract JD skills --> LLM call2
prompt 3:- Match the skill and generate the score --> LLM call3
prompt 4:- if score>60 call HR else reject --> LLM call4

This is call prompt chaining


- Why it is used?
1) Debugging
2) Modularity
3) Different models {for complex task --> good models, easy task --> normal models}
4) Retry steps


- mostly similar to ReAct?
No, in ReAct we make a tools or function
{we don't tell LLM what to do. they decide what tools i need to used.}

In prompt chaining, devloper decide in which step what they can do. and what's the next steps

```


## Day 9
### Streaming

```
when you search any thing in chatGPT then they generate some answer
when they generate they give you line by line or chunk by chunk thats 
called streaming.

stream = false {They take a time and generate whole content first then send it to you}

stream = true {They generate output chunk by chunk and send it to you}

- why we do streaming? 
Because we can send output in faster manner. 
chunk by chunk output will be generated and we can see it. line by line
so, basically our waiting time will be decrease.

when your end-user is human --> then you can used streaming✅
when your end-user is computer --> dont used streaming❌

when we used streaming then code will generate line by line 
if your user is computer or chatBot then we not used streaming because
computer or chatBot make read data in JSON formate

if we can used streaming then code come line by line and JSON will be break
thats why we not user streaming when end-user is any chatBot or any llm models
```


## Week 3
## Day 10
### RAG (Retrieval-Augmented Generation)

```
In simple language it means you can provide a extra information and they can take your extra information
and read and they response back to you

```

## Day 11 Embeddings {Retrieval}

```
No matter exect words

- Why embedding come?
In previous we can see retrieval concept and see how to search words by words. its very rigide search.
computer not understand word they understand number

So we can convert words in vector

<Embedding> --> if you convert some word in based on some feature
apple --> (sweet, crunchi) --> (8,7)
cake --> (sweet, crunchi) --> (10,2)
kurkura --> (sweet, crunchi) --> (1,9)

if computer find difference between two words called cosine difference

Embedding is a smart process they can convert string to array and match the array is easy 


add extra dependency 
uv add numpy sentence_transformers
```


## Day 14 Quadrant {Vector DB}

```
- Why embeddings?

Retrieval function are faster.
They convert string to array and we can easily match the array as compare to string.

- Why vector DB?

when your knowledge based will increase then some problem will come
1) Time:- Embedding check line by line {basically they do linear search}
2) Persistence:- when your machine off all vector will be loss 
3) Memory


Quadrant is a vector database
   In sql we have a table, but in vector database we have a collections
   table store rows and cols, but collection store vector (Arrays)
   In sql they store row1, row2 etc, but in vector we called point
      and point store three things
                     1> ID
                     2> Actual vector:- 384 or any size of embedding those you can make 
                     3> payload:- vector ka actual data {eg:- "hey, how are you" }

```



## Day 15
### FILTERS and HNSW Quadrant

```
(HNSW) Hierarchical Navigable Small World
It is a algo.

- How to Quadrant search?

when we have a {5 no of vector} and {one query} are there then one query check 5 no of all the vector
and take a 5 sec
But think, when {no of verctor are 10 crore} then they take how much time for search because they search
in linear they take lots of time
that's why HNSW will come

HNSW tell don't search line by line or ramdomly first go to "as closed as possible" then start to search.

For example:- 
   you stay in:- Bengaluru
   target location:- Delhi NCR chok

   if you do normally linear search:
      then you come outside your PG and asked its "Delhi NCR chok" then they told no
      then you go different gali and asked its "Delhi NCR chok" then they told no
      after few months or year you actually go to "Delhi NCR chok" then they told Yes

   so, its very poor method

   if you used HNSW
      then first you go and asked where is "Bengaluru Airpot" then you Book a ticket and Go To Delhi
      when you are in Delhi then you can start to asked its is "Delhi NCR chok" NO
      after few time you find "Delhi NCR chok"


so, In sort 
   vectore have a internal connections, when we search(HNSW) anything then they check which vectore are 
   closest to your query. then they start to search.



Filter:-
   item 1:
      text -> "24 days of leaves"
      category -> "vacation"
      is_active -> true   

   item 2:
      text -> "8 hours of workings"
      category -> "work_life_balance"
      is_active -> true  

   item 3:
      text -> "16 days of leaves"
      category -> "vacation"
      is_active -> false        

all three iteams are store in your vectore DB and Quadrant

query:- How many days of leaves?
-> they search with respect to these two items {category = vacation, is_active = true}  


step 1:- first your collections are created {collection name:- Knowledge}
step 2:- from first you need to know which types of field you can search {for eg:- gender, category, etc}

- How to make a index.

step 3:- Make a index 
         Assume you have 6 vector in quadrant [[1,[],"....."],[2],[3],[4],[5],[6]];

         Quadrant know at first which types of category present in which no of index

         "vacation" -> 1,4
         "work_life_balance" -> 2,3,5
         True -> 1,3,5
         False -> 2,4,6

- How to used these filter.
for using these filter you need three things
   (1) must (you can write more then one conditions) 
            {category -> "vacation", is_active -> true}  -> both are needed to be true
   (2) must_not (you can write any condition then they check as !condition)
   (3) should {category -> "vacation", is_active -> true} -> if any one condition are true then its true.
   
    

```



## week 4
## Day 16
### RAG Evaluation

```
RAG Evaluation means your RAG working correct or not.

What is RAG?


   with help of Embedding
            |
Knowledge -------> vector --------> vectorDB ---
                                                |
                                                | --> VectorDB + vector => check the relevent chunk 
   with help of Embedding                       |      jinka high match hai, jinka cosine similarity is high
         |                                      |      wha vector {CONTEXT} banta hai.
Query -----------> vector -----------------------                    |
                                                                    {LLM} --> Answer



So, In this whole arch. there are 3 places where error chances is high 
1> Knowledge based will be wrong
2> Maybe your context will be wrong
3> or else your LLM generate a wrong answer



Evaluation process

step1: Make a RAG
step2: make a {Golden Dataset}
                 |__ write a {question} and {ground truth} based upon your knowledge based
                        for eg:- {
                                    question:- Akamai company give how many leaves?
                                    ground truth:- 12 days
                                 },

step3: Layer by Layer checking:-
      (i) context checking: 
         Query ---> based upon your query Quadrant gives you top 3 vector
            a. precision -> accuracy { (relevent/total)*100 } 

            for eg:- query: Akamai company give how many leaves?

                     from quadrant 3 vector are come
                     (i) 12 days paid leaves
                     (ii) Additional 3 days
                     (iii) 50,000 salary

                     (i) and (ii) are relevent informations but (iii) are not relevent

                     (relevent/total)*100 => (2/3)*100 => 66% precision


      (ii) Recall:- 
         Query ---> Akamai company give how many leaves?
         based upon this query your knowledge based have 2 answer
         {
            (i) 12 days paid leaves
            (ii) Additional 3 days or sick leaves
         }             

         but you get a answer is 12 days leaves but you miss 3 days leaves and
         your accuracy come 100% because
         quadrant gives only 12 days leaves => (relevent/total)*100 => (1/1)*100 => 100%
         but they miss { (ii) Additional 3 days or sick leaves } these line

         In sort quadrant DB not give you relevent lines

         So, here recall can do there work
         they can check the actuall relevent line => 2
         how many line quadrant gives => 1
         (1/2)*100 => 50% recall 


         So in these case precision => 100%
                          recall => 50%
         here quadrant do the mistake   


      { Context checking + Recall } -> both are used for (Context Retrieval)


step4: if your context will be correct and your precision and recall are also correct then
       your LLM have a problem
       there are 3 types of check to know your LLM is wrong

      (i) Faith fullness
      (ii) relevancy
      (iii) correctness

      (i) Faith fullness:
         your LLM get a context:- 12 days of paid leaves
         your Query:- how many leaves?
         LLM as give a Answer:- 10 days of paid leaves

         Your LLM not read context properly they Hallucinate 

      (ii) correctness:
         your LLM get a context:- 10 days of paid leaves (❌ wrong context)
         your Query:- how many leaves?
         LLM as give a Answer:- 10 days 

         Not correct but your LLM are faithfull


         ┌──────────────────────────────────────────────┐
         │              Faithfull --> Incorrect         │
         |              Context❌                       |
         ├──────────────────────────────────────────────┤
         │              unFaithhull --> correct         │
         │                              (Hallucinate)   │
         └──────────────────────────────────────────────┘


      (iii) relevancy:
             context:- Promotion happend in Akamine in November
             question:- when Promotion is happend?
             Answer:- { give a promotion defination }

             this is not a wrong answer but this is not relevent to your question
             So, that are also a LLM problem they not understand question or context



Summary:
         Precision -> low -> top k -> reduce
                          -> threshold -> similirity score > 0.5

         recall -> quadrant gives a result/total relevent line => 1/2 => 50% recall
         how to increase -> increase your top k value
                         -> thresold ko kaam kar do >0.9


         faithfull -> write a good System prompt tell no hallucinate

         correct nhi hai -> correct knowledge based

         relevent -> correct a system prompt                                               



```


## Day 17
### First AI agent 

```
Agent = LLM + functions/api

for websearch we can call a API called Tavily

Agent mens you can used a LLM and provide some tools 

- How to call a tools and tell the LLM?

step1: write a function(for tools)

step2: make a Avalable_tools (tell the LLM you have this avaliable tools to used)
         Avalable_tools = {
            "web_search": web_search,
            "calculate": calculate
         }

step3: Make a tools or JSON object type where you can define all the things
      eg:- tools = []
           -> type = function
           -> name = web_search
           -> description = kab used karna hai and kaise karna hai or kya hai ye 
           -> parameter = kya leta hai parameter mein 
                  -> query
                  -> parameter_description

step4: give instruction to your Agent through system prompt

         grok.chat.completions.create(
            message, models,
            tools = tools,
            tools_choice = auto 
         );



```
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
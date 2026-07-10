## Day 2
### venv (virtual envorment)

```
Activate command:- source env/bin/activate

In virtual envorment we can create a seprate room where we can install a all depencency
version all the things those are not affect to outside the virtual env

```

### LLM Calls (Large language mode)

how to call LLM ?hpwho

```
1) we need a API Key.
2) make a client (for eg you used grok then make a one client those intract with grook)
3) choose a models
4) messages: In this two things are there 

            1. role: In api call 3 types of role are there
                        i) User role: (message that was sended to GPT from your side.)
                        ii) Assistance role: (GPT respose back your query)
                        iii) System role: (you can assing any role like "give all the answer in one words")
                        
            2. content
4) Response: In response many types of response are there but we deals with 2 important things
            1. choices: this is the main answer (Array or answers)
            2. Usage: for handling your message how much Token is used.bb            
```

## Day 3
### System role and Temprature

```
System role: system role tell a LLM. (whats the relation between you and system in that chat)

for example: role -> system
             content -> you are my gf

             role -> user
             content -> i love you


Temprature: (personality)

In gork ai you can pass {0 to 2} temps (0,1,2)
t=0         t=2
0 : safe    2: Risk taker(creative)

LLM are predection machine
```


## Day 4
### Token

```
token means Comman reusable words

LLM {computer program} they only understand 0/1

eg: you give some query "Hello" -> it converted your query into a number and then it start processing
    give a output as a number -> and it convert into your language.


few method are there like 
1) letter to number (worst method)
   for eg:- "HELLO" => [H->12 E->23 L->43 O->34] => 12+23+43+34 => ....  

2) words to number -> this is also not good because english word is infinite
   for eg:- "i am rahul kumar singh" => ["i"," am"," rahul"," kumar"," singh"] 


Token -> Comman reusable words

They search all the word aver a internet and they take a common word and make a one token

For eg:- "The" -> Token   "rahul" -> not a token, so they break "rahul" into sub token.
         "In" -> Token.   "Banglore" -> Token
         "name" -> Token


Input Token + Output Token = Total token

Input Token -> Prompt token
Output Token -> completation Token

```
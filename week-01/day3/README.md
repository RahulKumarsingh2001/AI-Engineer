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
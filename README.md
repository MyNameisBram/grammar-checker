# grammar-checker
grammar-checker

Detect and correct grammar using transformers

# instructions
## clone repository
- open terminal > copy repo > `git clone {repo_name}`

## pulling `docker image` 
- in terminal 
- cd into directory where `api` folder resides > type ... `docker compose up --build` 

## test connection with `postmate`
- `create new collection` 
  - `POST`
  - add `Headers` > `Content-Type = application/json`
  - `Body` select `raw : Text`
  - enter: `{"text":"enter sample sentence here"}`
  - you should see an `output` ... example below


## Code snippet
```json

curl --location --request POST 'http://localhost:5005/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "As you know, microservices, if done correctly, will solve most of your scalability challenges."
}'


```

## output
```
{
    "confidence": "pretty confident",
    "confidence level": "mid",
    "label": "casual",
    "score": 0.8830444812774658
}
```

# pancakeswapBot

# Instalation:

1. create a virtual environment
```shell
> virtualenv venv
```
2. run the environment

```shell
> source venv/bin/activate
```
3. install the project requirements
```shell
> pip install -r requirements.txt
```

# Project Structure and run
## config.py 
all static data and urls set here,
add your source and destination wallet address and private key, etc.

## UrlScrapper.py

```shell
> (venv) ➜  pancakeswapBot git:(main) ✗ python UrlScraper.py

 The Program is started
Press [ Ctrl + c ] to stop.
2021-10-30 16:53:50.501538 first element found.

```
the program will listen to the binance url for the conditions.
if all ideal condition will happen, the trade-bot automatically will start.

## telegram.py

```shell
> (venv) ➜  pancakeswapBot git:(main) ✗ python telegram.py 


```

telegram.py will listen to the telegram msg.

### ATTENTION: 
Your message must follow the below pattern:
```javascript
line 1 : the token contract address

line 2 : the Network name ('eth'or 'bsc' or 'trx')

line 3 : the amount (in 'eth')
```

---
#### try to run telegram.py and UrlScrapper.py in two difference envs

## Markov chains generating tweets

Generate tweets from existing tweets using Markov chains.

Markov chain is a stochastic process, where the next event is depending only on the previous event.

### Setup


```
$ cd markovchain
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Add your Twitter consumer keys and access tokens in `twitter_parser.py`.

### Run

You can list as many usernames as you wish. They will serve as a source for the data.

```
$ python run.py username1 username2 username3
```

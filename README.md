<p align="center">
  <img width="200" src="static/logo.png">
</p>

---

`tweet` can tweet your current status from CLI easily.

`tweet` cat tweet `only`, therefore you will not be distracted.

## How to Install

[pipx](https://github.com/pypa/pipx) is good for running python applications in isolated environments.

```
pipx install tweet
```

## How to Use

```
# Post Tweet
tweet tweet `your-status`

# Endless Mode
tweet endless
```

## How to set up

You have to set up `~/.twitter-env` file to your home directory yourself.
You get tokens from [Twitter Developer](https://developer.twitter.com/en/portal/projects-and-apps).

`~/.twitter-env`

```env
CONSUMER_TOKEN=.......
CONSUMER_SECRET=.......
ACCESS_TOKEN=.......
ACCESS_SECRET=.....
```

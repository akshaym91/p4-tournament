#Swiss style tournament lot generator

This project is a postgre database driven python application that exposes API for generating lots for [Swiss style](https://en.wikipedia.org/wiki/Swiss-system_tournament) tournament.
Completed as part of the Udacity Full Stack Web Developer Nanodegree program.

## API Details

`registerPlayer(name)`
> Adds a player to the tournament by putting an entry in the database.

`countPlayers()`
> Returns the number of currently registered players.

`deletePlayers()`
> Clear out all the player records from the database.

`reportMatch(winner, loser)`
> Stores the outcome of a single match between two players in the database.

`deleteMatches()`
> Clear out all the match records from the database.

`playerStandings()`
> Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

`swissPairings()`
> Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system.

## Getting started guide -

### Environment setup

- VirtualBox installation (https://www.virtualbox.org/wiki/Downloads)
- Vagrant installation (https://www.vagrantup.com/downloads)
- Clone of Vagrant VM (git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack)


### Running the test suite

From a GitHub shell:
```
cd fullstack/vagrant
vagrant up
vagrant ssh
cd /vagrant/tournament
psql -f tournament.sql
python tournament_test.py
```

##Author
Akshay Menon

##License
MIT

##Credits
1. Test suite provided by Udacity.
2. [Iterator tools](http://stackoverflow.com/questions/434287/what-is-the-most-pythonic-way-to-iterate-over-a-list-in-chunks)

##Copyright
Copyright &copy; 2016 Akshay Menon
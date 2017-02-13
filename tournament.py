#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
# author: Akshay Menon
#

import psycopg2
import itertools


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    QUERY = "DELETE from matches"
    db = connect()
    cursor = db.cursor()
    cursor.execute(QUERY)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    QUERY = "DELETE from players"
    db = connect()
    cursor = db.cursor()
    cursor.execute(QUERY)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    QUERY = "SELECT count(*) as player_count from players"
    db = connect()
    cursor = db.cursor()
    cursor.execute(QUERY)
    player_count = cursor.fetchone()
    db.close()
    return player_count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    QUERY = "INSERT into players (name) VALUES (%s)"
    db = connect()
    cursor = db.cursor()
    cursor.execute(QUERY, (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Uses sub-query applied on the view standings.
    QUERY = '''
    SELECT players.id, players.name, COUNT(matches.winner) AS wins,
    (SELECT played FROM standings WHERE standings.id = players.id)
    FROM players LEFT JOIN matches
    ON players.id = matches.winner
    GROUP BY players.id, players.name
    ORDER BY wins DESC
     '''
    db = connect()
    cursor = db.cursor()
    cursor.execute(QUERY)
    player_standings = cursor.fetchall()
    db.close()
    return player_standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    QUERY = ("INSERT into matches (winner, loser) values (%s, %s)")
    db = connect()
    cursor = db.cursor()
    cursor.execute(QUERY, (winner, loser,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    current_standings = playerStandings()
    pairingsiterator = itertools.izip(*[iter(current_standings)] * 2)
    pair_list = []
    pairings = list(pairingsiterator)
    for pair in pairings:
        id1 = pair[0][0]
        name1 = pair[0][1]
        id2 = pair[1][0]
        name2 = pair[1][1]
        clash = (id1, name1, id2, name2)
        pair_list.append(clash)
    return pair_list

-- Table definitions for the tournament project.
--
-- Put your SQL 'create TABLE' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;

-- Create the database and tables
CREATE DATABASE tournament;
\connect tournament;

-- Creates the players table with player-id and name
CREATE TABLE players (
    id SERIAL primary key,
    name TEXT);

-- Creates the matches table with match-id, winner and loser
CREATE TABLE matches (
    id SERIAL primary key,
    winner SERIAL references players(id),
    loser SERIAL references players(id));

-- Temporary view to list the number of played matches along with player table entries
CREATE OR REPLACE VIEW standings AS
SELECT players.id as id,
       players.name as name,
       count(matches.*) as played
FROM players LEFT JOIN matches
ON matches.winner = players.id  OR matches.loser = players.id
GROUP BY players.id
ORDER BY played DESC;


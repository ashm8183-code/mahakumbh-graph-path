# Mahakumbh - Graph Path Queries

## Problem Statement

Kumbh is a massive spiritual event held every 12 years in India, attracting millions of pilgrims. During the event, the railway network experiences heavy demand, making efficient route management important.

The railway network consists of stations connected by railway tracks. Some stations may have restrictions that prevent trains from passing through them.

Given the railway connections, restrictions, and a series of queries, determine whether a valid route exists between two stations.

The system also allows railway connections to be added or removed dynamically.

## Task

For each travel query, print `yes` if the journey is possible without passing through a restricted station. Otherwise, print `no`.

The following types of operations are supported:

- `source destination` - Check whether a route exists.
- `source connects destination` - Connect two stations.
- `source disconnects destination` - Disconnect two stations.

## Approach

The railway network is represented using an adjacency list.

Breadth-First Search (BFS) is used to check whether a route exists between two stations while avoiding restricted stations.

Connections can also be updated when `connects` or `disconnects` queries are encountered.

## Input

- First line contains `N`, the number of railway connection lines.
- The next `N` lines describe the stations and their connections.
- The next line contains `Q`, the number of queries.
- The next `Q` lines contain the queries.
- The next line contains `R`, the number of restriction lines.
- The next `R` lines describe the restricted stations.

## Output

For every travel query, print:

```text
yes

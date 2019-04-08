#!/usr/bin/env python3
# My Anwser:
def points(games):
  score = 0
  for result in games:
    match_result = result.split(":")
    if match_result[0] > match_result[1]:
        score += 3
    elif match_result[0] == match_result[1]:
        score += 1
  return score

games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
points(games)

# Best anwser:
# def points(a):
#   return sum((x >= y) + 2 * (x > y) for x, y in (s.split(":") for s in a))
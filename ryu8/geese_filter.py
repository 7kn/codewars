#!/usr/bin/env python3
# My anwser:
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
  filtered_list = []
  for bird in birds:
    if bird not in geese and bird not in filtered_list:
      filtered_list.append(bird)
  
    return filtered_list

# Best awnser:
#def goose_filter(birds):
#    return [bird for bird in birds if bird not in geese]
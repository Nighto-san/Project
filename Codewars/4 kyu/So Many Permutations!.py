def permutations(s):
  if len(s) <= 1:
    return [s]
  else:
    res = []
    for idx, char in enumerate(s):
      for perm in permutations(s[:idx] + s[idx+1:]):
        res.append(char + perm)
    return sorted(set(res))









print(sorted(permutations('aabb')),'\n',['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
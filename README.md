# Path-Pattern-Matcher

This module takes pattern and path data from stdin and
prints best matching pattern or NO MATCH to stdout for each path.

Matches are ordered based on the following parameters.

1. Least wildcard symbol count is preferred
2. If there is a tie for #1, match with furthest right, left most wildcard preferred
3. If the wildcards have the same indices, contiue looking at the next furthest right wildcard and apply #2

### Complexity

1. The time complexity of this algorithm is O(n^2), n being the larger
of the count of patterns and the count of paths, and the length of the patterns
and paths being constant.
The space complexity is O(n) because copies are made of the paths and patterns.
2. Given hundreds of thousands of patterns and paths, this program would
probably break. There is definitely a faster solution. One approach to
making lookups faster in cases where there are similar patterns would be 
to store the patterns in a trie.
Other approaches could use dynamic programming, recursion with
memoization, or a distributed system.

### To Run
`cat input_file | python get_best_matches.py > output_file`

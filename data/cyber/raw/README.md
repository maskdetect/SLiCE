# Data description
These datasets are a graph version of the University of New Brunswick dataset generated by Shiravi et al.[1] and used for graph-based analysis for intrusion detection by Chen et al [2]. Please consider citing these papers if you find the dataset useful.

Each line in the files with ".edges" extension represents a communication between two IP addresses.  The mapping between IP addresses in the original dataset and graph node ids are provided in ".ids.tsv".

The details of the events in the dataset is provided below:
Day 1 (normal activity): Graph(nodes=5357, edges=12887)
Day 2 (normal activity): Graph(nodes=2631, edges=5614)
Day 3 (infiltration attack and normal activity): Graph(nodes=3052, edges=5406)
Day 4 (HTTP denial of service attack and normal activity): Graph(nodes=8221, edges=12594)
Day 5 (distributed denial of service attack with botnets): Graph(nodes=24062, edges=32848)
Day 6 (normal activity): Graph(nodes=5638, edges=13958)
Day 7 (brute force SSH attack and normal activity): Graph(nodes=4738, edges=11492)

# References
1. Shiravi, A., Shiravi, H., Tavallaee, M. and Ghorbani, A.A., 2012. Toward developing a systematic approach to generate benchmark datasets for intrusion detection. computers & security, 31(3), pp.357-374.
2. Chen, P.Y., Choudhury, S. and Hero, A.O., 2016, March. Multi-centrality graph spectral decompositions and their application to cyber intrusion detection. In 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 4553-4557). IEEE.
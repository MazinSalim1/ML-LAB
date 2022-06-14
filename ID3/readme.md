# ID3
### Steps
- ```Step 1```: Calculate the Information Gain of each feature.
- ```Step 2```: Considering that all rows don’t belong to the same class, split the dataset S into subsets using the feature for which the Information Gain is maximum.

- ```Step 3```:Make a decision tree node using the feature with the maximum Information gain.
- ```Step 4```: If all rows belong to the same class, make the current node as a leaf node with the class as its label.
- ```Step 5```:Repeat for the remaining features until we run out of all features, or the decision tree has all leaf nodes.



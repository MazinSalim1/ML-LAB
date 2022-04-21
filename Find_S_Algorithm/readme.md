# ML – Find S Algorithm
### Steps
- ```Step 1```: Initialize h to the most specific hypothesis in H
- ```Step 2```:
-                   For each positive training instance x
                        For each attribute constraint a, in h
                            If the constraint a, is satisfied by x
                            Then do nothing
                            Else replace a, in h by the next more general constraint that is satisfied by x
- ```Step 3```:   Output hypothesis h 

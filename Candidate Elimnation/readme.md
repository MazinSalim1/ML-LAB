# ML – Candidate Elimination Algorithm
### Steps
- ```Step 1```: Load Data set
- ```Step 2```: Initialize General Hypothesis  and Specific  Hypothesis.
- ```Step 3```: For each training example  
- ```Step 4```:
-                   If example is positive example  
                       if attribute_value == hypothesis_value:
                         Do nothing  
                      else:
                         replace attribute value with '?' (Basically generalizing it)
- ```Step 5```:
-          If example is Negative example  
            Make generalize hypothesis more specific.

import numpy as np 
import pandas as pd 
from sklearn.linear_model import LogisticRegression

work_data = pd.read_csv("/users/schma/model_predictions/level_up_data.csv")

y = work_data['separatedNY']

X = work_data['workDistance']

X = X.to_numpy()

X = X.reshape(-1, 1)

simple_logistic = LogisticRegression(solver="liblinear", random_state=1001)

simple_logistic.fit(X, y)

predicted_probs = simple_logistic.predict_proba(X)[:, 1]

pred_df = pd.DataFrame({"preds":predicted_probs})

pred_df.to_csv("/users/schma/model_predictions/model_predictions.csv")

/users/schma/model_predictions

And run:
touch make_predictions.py
```

And then:

vim make_predictions.py

Now we can go into paste mode:

ESC
:set paste
i
SHIFT + INS
```

You'll now be able to navigate over the file with `h`, `j`, `k`, and `l`.

For now, though, let's just write and quit that file:

```
:wq
```

We need to move our model into our directory now, which is where the program that we are using becomes helpful!

Finally, we need to use the appropriate path within our code!

Now we can deal with getting python going! 

We have some libraries to install:

```
module load python

pip3 install --user imblearn pandas scikit-learn joblib
```

The hard work is done, so now we can create a bash script to submit our job!

We will touch a file:

```
touch prediction_job.script
```

And paste in the following:

```
#!/bin/bash
#$ -M sberry5@nd.edu    # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -q long              # Specify queue
#$ -pe smp 1            # Specify number of cores to use.
#$ -N predictions       # Specify job name

module load python

python3 make_predictions.py
```

Now, we can submit our job:

```
qsub prediction_job.script
```

## Retrieving Results

You can use either of the programs to transfer files back to your local machine. 

If you're on a Mac or Linux machine, you can just use `scp` on your local machine:

```
scp schma@crcfe02.crc.nd.edu:/users/schma/model_predictions/model_predictions.csv Documents/
```





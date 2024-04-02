# Machine
Öncelikle readme dosyasını okuduktan sonra bizden bulunan değerler ile basit bir makine öğrenmesi modeli kurmamızı istediğini anlıyoruz.
<br> Bu modeli oluşturmak için istersek scikit-learn, tensorflow, pytorch kullanabiliriz.

# Tensorflow
```python
import numpy as np
import pandas as pd
import tensorflow as tf

in_data = pd.read_csv('in.csv')
out_data = pd.read_csv('out.csv')

X_train = in_data.values
y_train = out_data.values

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, verbose=0)
pred_data = pd.read_csv('pred.csv')
X_pred = pred_data.values
predictions = model.predict(X_pred)
print(predictions)
```

# Scikit-Learn
```python
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

in_data = pd.read_csv('in.csv')
out_data = pd.read_csv('out.csv')

X = in_data.values  # Input features
y = out_data.values.flatten()  # Target variable (flattened to 1D array)

model = LinearRegression()
model.fit(X, y)

pred_data = pd.read_csv('pred.csv')

pred_X = pred_data.values
predictions = model.predict(pred_X)

predictions_df = pd.DataFrame({'Predictions': predictions})
predictions_df.to_csv('predictions.csv', index=False)
```

# Pytorch
```python
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim

in_data = pd.read_csv('in.csv')
out_data = pd.read_csv('out.csv')

X_train = torch.tensor(in_data.values, dtype=torch.float32)
y_train = torch.tensor(out_data.values, dtype=torch.float32)

class LinearRegressionModel(nn.Module):
    def __init__(self, input_size, output_size):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(input_size, output_size)
        
    def forward(self, x):
        return self.linear(x)

input_size = X_train.shape[1]
output_size = y_train.shape[1]
model = LinearRegressionModel(input_size, output_size)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

num_epochs = 100
for epoch in range(num_epochs):
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

pred_data = pd.read_csv('pred.csv')

X_pred = torch.tensor(pred_data.values, dtype=torch.float32)

predictions = model(X_pred).detach().numpy()

print(predictions)
```

# Çözüm
Ardından burada bulunan değerleri ASCII değeri olarak stringe çevirince flag karşımıza çıkıyor.
Flag 'SKYSEC' ile başlamalı. Kullandığınız makine öğrenmesi modeline ve random_state'e göre 3 flagten birini bulacaksınız: 
<br>
<strong>SKYSEC{MACHINE-A333}</strong>
<br>
<strong>SKYSEC{MACHINE-A252}</strong>
<br>
<strong>SKYSEC{MACHINE-A306}</strong>

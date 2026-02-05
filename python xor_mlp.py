# xor_mlp.py
# Simple MLP to solve XOR using PyTorch (single file version)

import torch
import torch.nn as nn


# ----- Model definition -----
class XORNet(nn.Module):
    # 2 -> 4 -> 1 MLP for XOR
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 4)   # input to hidden
        self.fc2 = nn.Linear(4, 1)   # hidden to output

    def forward(self, x):
        x = torch.tanh(self.fc1(x))     # hidden layer + tanh
        x = torch.sigmoid(self.fc2(x))  # output layer + sigmoid
        return x


# ----- Main script -----
if __name__ == "__main__":
    # 1. Device select
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    # 2. XOR data
    X = torch.tensor([
        [0.0, 0.0],  # 0 XOR 0 = 0
        [0.0, 1.0],  # 0 XOR 1 = 1
        [1.0, 0.0],  # 1 XOR 0 = 1
        [1.0, 1.0],  # 1 XOR 1 = 0
    ], dtype=torch.float32, device=device)

    y = torch.tensor([
        [0.0],
        [1.0],
        [1.0],
        [0.0],
    ], dtype=torch.float32, device=device)

    # 3. Model, loss, optimizer
    model = XORNet().to(device)
    criterion = nn.BCELoss()                     # loss function
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)  # optimizer

    # 4. Training loop
    epochs = 5000
    for epoch in range(epochs + 1):
        outputs = model(X)           # forward pass
        loss = criterion(outputs, y) # compute loss

        optimizer.zero_grad()
        loss.backward()              # backpropagation
        optimizer.step()             # update weights

        if epoch % 1000 == 0:
            print(f"Epoch {epoch}/{epochs}  Loss: {loss.item():.6f}")

    # 5. Evaluation
    with torch.no_grad():
        outputs = model(X)
        preds = (outputs > 0.5).float()

        print("\nFinal outputs (probabilities):")
        print(outputs.cpu().numpy())

        print("\nPredicted classes:")
        print(preds.cpu().numpy())

        print("\nTrue labels:")
        print(y.cpu().numpy())

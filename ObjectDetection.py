from torch import nn, save, load, argmax, no_grad
from torch.optim import Adam
from torch.utils.data import DataLoader
from torchvision import datasets
import torchvision.transforms as transforms

train = datasets.CIFAR10(root='data',download=True,train=True,transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.RandomResizedCrop(32, scale=(0.8, 1.0)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]))
train_dataset = DataLoader(train,batch_size=128)

class ImageClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Flatten(),
            nn.Linear(128 * 4 * 4, 512),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        return self.model(x)

device = 'cuda' # cuda for gpu

clf = ImageClassifier().to(device) #set to "cpu" if no gpu; clf ==> Classifier
opt = Adam(clf.parameters(), lr=1e-3, weight_decay = 1e-4)  # lr ==> learning rate; opt ==> Optimizer
loss_fn = nn.CrossEntropyLoss()

print(len(train_dataset))
epochs = 10
for epoch in range(epochs):
    clf.train()
    avg_loss = 0
    for batch_num,batch in enumerate(train_dataset):
        X,y = batch
        X, y = X.to(device), y.to(device)

        y_pred = clf(X)
        loss = loss_fn(y_pred,y)

        #Zero out the previous gradients
        opt.zero_grad()

        #Calculate backwards gradients
        loss.backward()

        #Step in the opp direction of gradient
        opt.step()

        if (batch_num+1) %100==0:
            print(f"Batch {batch_num+1} : {avg_loss/(batch_num)}")

        avg_loss += loss.item()

    print(f"Epoch {epoch+1} : {avg_loss/len(train_dataset)}")

with open('model_state.pt','wb') as f:
    save(clf.state_dict(),f)

test = datasets.CIFAR10(root='data', download=True, train = False,transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.RandomResizedCrop(32, scale=(0.8, 1.0)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
]))
test_dataset = DataLoader(test,32)

total = 0
correct = 0

clf.eval()
with no_grad():
    for batch_num, (X, y) in enumerate(test_dataset):
        X, y = X.to(device), y.to(device)
        # Get predictions
        y_pred = clf(X)

        # Take the index with the maximum logit value (predicted class)
        y_pred = argmax(y_pred, dim=1)

        # Update total number of samples
        total += y.size(0)

        # Count correct predictions
        correct += (y_pred == y).sum().item()

        # Print progress every 100 batches
        if (batch_num + 1) % 100 == 0:
            print(f"Processed {total} samples")

# Print final accuracy
print(f"Accuracy: {correct / total * 100:.2f}%")
print(f"Total correct predictions: {correct}")
print(f"Total samples: {total}")


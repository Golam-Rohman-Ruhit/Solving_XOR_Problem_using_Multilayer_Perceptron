# <u>Solving the XOR Problem Using a Multilayer Perceptron</u>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Neural%20Network-MLP-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

## 📌 Part 1: Problem Introduction

### **Objective**
The aim here was creating a Multilayer Perceptron (MLP) capable of learning the XOR function, which one-layer networks simply can't handle due to their structural limits.

### **Background Context**
Truth is, XOR acts like a basic test for neural nets - and there’s a clear explanation why. This task reveals how limited simple perceptrons really are. Imagine placing the four possible inputs (00, 01, 10, 11) on a flat grid - you’d quickly notice the two correct answers sit across corners, so no straight cut can isolate them. 

Back in ’69, Minsky and Papert pointed out this barrier, slowing down progress in the field for quite some time. A turning point arrived once researchers saw that inserting an internal layer allows the model to reorganize input patterns - building new forms in between that turn complex cases into ones a line can divide.

### **Lab Objectives**
* 🧪 **Experiment:** Show through experiments that hidden layers handle non-linear patterns.
* ⚡ **Activation:** Learn how activation functions make this possible by shaping signal output in neural networks.
* 🛠️ **Implementation:** Build a functioning MLP using PyTorch; reach full accuracy on classification tasks.

---

## ⚙️ Part 2: Model Description

### **Objective**
Describe how you built the system. Use a network with several layers and units - detail their count. Include core parts like activation methods. Train it using an optimization technique plus a metric for error. Outline each step clearly without extra terms.

### **Model’s Architecture**
I choosed compact 2-4-1 feedforward network architecture. I took two input neurons that accept the binary pairs which can feed into a hidden layer of four neurons. This model’s width offers sufficient space to capture key changes - nothing more. One output neuron combines those traits for the last decision. In total, both layers hold merely 17 adjustable values, so it stays compact but still effective here.

### **Key Components**
* **Hidden Layer:** Applies **tanh activation**, as its gradual S-curve helps gently warp the input structure. Instead of ReLU, which may overreact in tiny networks, tanh delivers balanced outputs to support steady training.
* **Output Side:** **Sigmoid** plays a key role - mapping estimates to values between 0 and 1, fitting neatly with the loss setup.
* **Loss Function:** **Binary Cross-Entropy** fits best for yes/no tasks; it strongly discourages errors, guiding the model toward clear, accurate decisions.
* **Optimizer:** **SGD at 0.1 learning rate** ensures straightforward weight changes - no complex adjustments like momentum or variable rates required.

### **Training Process**
I trained using all four XOR examples at once across **5,000 epochs** - sure, that’s excessive, yet it lets us observe how convergence progresses step by step. Since the data is minimal, splitting into batches or randomizing order isn’t necessary. Instead of manual steps, PyTorch manages the forward computation, derives gradients, then adjusts weights accordingly. Whenever possible, I used a GPU for execution; however, given the model’s simplicity, running on CPU gives almost the same speed.

---

## 📊 Part 3: Experimental Results

### **Objective**
Show results using images. Use main screenshots from running the code - like accuracy or loss graphs, predicted outputs - to back up your conclusions.

The training story appears clearly in the loss curve. Starting from a modest 0.740646, after 1,000 epochs, performance drops sharply - to just 0.005161 - showing the system began grasping patterns. By the last round, error reaches only 0.000481, suggesting output isn't merely accurate, yet highly precise.

### **Comparison Table: Predictions vs. Reality**

| Input Sample | Final Output (Prob.) | Predicted Class | True Label | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Input 1** | 8.956160e-04 | 0 | 0 | ✅ Match |
| **Input 2** | 9.950519e-01 | 1 | 1 | ✅ Match |
| **Input 3** | 9.927043e-01 | 1 | 1 | ✅ Match |
| **Input 4** | 7.370279e-03 | 0 | 0 | ✅ Match |

Perfect result - full marks across all four examples. Look at the confidence levels: they’re not close to the threshold, but pushed fully toward 0 or 1, meaning clear-cut decisions were made. The drop in error is steady without sudden spikes, suggesting solid design and settings. Each output matches reality exactly, showing the middle layer reshaped inputs so classes could be cleanly split.

---

## 💡 Part 4: Discussion and Analysis

### **Objective**
Look closely at how the method worked alongside the framework used. While reviewing, highlight challenges that came up during work, then explain what the outcomes suggest. Consider weak points the approach might have when applied further.

Looking at these outcomes calls for caution. True, the system handled XOR without errors - yet in reality, it just stored a small set of fixed answers. Given 20 weights for only four data points, it had more capacity than needed to recall instead of adapt. It doesn’t grasp what XOR means - it forms a sharp dividing line that fits exactly those input positions. If I changed one weight - even just a bit - the output might fail completely. Without a validation group (splitting four points isn’t possible), there’s no way to check stability. So, we lack proof that it works beyond these cases.

### **Difficulties Faced**
The primary difficulty wasn’t about tools - it stemmed from thinking. Early attempts using learning rates higher than 0.3 made the loss spike suddenly, pushing me to recognize how easily SGD becomes unstable in tight model settings. A quieter problem emerged too: knowing when to halt training. Beyond 500 epochs, improvements stalled nearly completely; continuing up to 5,000 felt like unnecessary overhead - clearly inefficient upon reflection.

### **Critical Limitations**
* **No generalization check:** claims about model understanding of XOR need tests on distorted or intermediate inputs.
* **Too many parameters:** 17 for just 4 data points - means the model fits training data exactly but fails on new data. This imbalance shows classic overfitting where complexity outweighs evidence.
* **Brittleness:** This happens when the answer sits in a steep, tight dip - so fragile it can't handle small changes. It doesn’t reflect stability or strength under variation.
* **Toy issues reflect real gaps:** XOR’s ease overlooks current hurdles - gradients fading, models fitting too closely on big data, or relying on constraint techniques.

### **What I'd Do Differently**
In practice, I’d try a 2-2-1 setup to check consistent convergence - it handles XOR yet sometimes stalls. Inputs would include 5% Gaussian noise so robustness could be assessed; training would halt early to skip unnecessary rounds. Crucially, this shows high accuracy on small data may signal overfitting rather than success. Real skill means creating systems that adapt beyond the given examples.

---

## 📁 Files
* **Full Documentation:** [NLDP_EX1.docx](https://github.com/user-attachments/files/25098315/NLDP_EX1.docx)
---
<p align="center">Made with ❤️ for Neural Network Learning</p>

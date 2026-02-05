# <u>Solving the XOR Problem Using a Multilayer Perceptron</u>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" />
  <img src="https://img.shields.io/badge/Neural%20Network-MLP-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

## 📌 Part 1: Problem Introduction

### **Objective**
[cite_start]The aim here was creating a Multilayer Perceptron (MLP) capable of learning the XOR function, which one-layer networks simply can't handle due to their structural limits[cite: 4].

### **Background Context**
[cite_start]Truth is, XOR acts like a basic test for neural nets - and there’s a clear explanation why[cite: 6]. [cite_start]This task reveals how limited simple perceptrons really are[cite: 7]. [cite_start]Imagine placing the four possible inputs (00, 01, 10, 11) on a flat grid - you’d quickly notice the two correct answers sit across corners, so no straight cut can isolate them[cite: 7]. 



[cite_start]Back in ’69, Minsky and Papert pointed out this barrier, slowing down progress in the field for quite some time[cite: 8]. [cite_start]A turning point arrived once researchers saw that inserting an internal layer allows the model to reorganize input patterns - building new forms in between that turn complex cases into ones a line can divide[cite: 9].

### **Lab Objectives**
* [cite_start]🧪 **Experiment:** Show through experiments that hidden layers handle non-linear patterns[cite: 11].
* [cite_start]⚡ **Activation:** Learn how activation functions make this possible by shaping signal output in neural networks[cite: 12].
* [cite_start]🛠️ **Implementation:** Build a functioning MLP using PyTorch; reach full accuracy on classification tasks[cite: 13].

---

## ⚙️ Part 2: Model Description

### **Objective**
Describe how you built the system. [cite_start]Use a network with several layers and units - detail their count[cite: 16]. [cite_start]Include core parts like activation methods[cite: 17]. [cite_start]Train it using an optimization technique plus a metric for error[cite: 17]. [cite_start]Outline each step clearly without extra terms[cite: 18].

### **Model’s Architecture**
[cite_start]I choosed compact 2-4-1 feedforward network architecture[cite: 19]. [cite_start]I took two input neurons that accept the binary pairs which can feed into a hidden layer of four neurons[cite: 19]. [cite_start]This model’s width offers sufficient space to capture key changes - nothing more[cite: 19]. [cite_start]One output neuron combines those traits for the last decision[cite: 20]. [cite_start]In total, both layers hold merely 17 adjustable values, so it stays compact but still effective here[cite: 21].



### **Key Components**
* [cite_start]**Hidden Layer:** Applies **tanh activation**, as its gradual S-curve helps gently warp the input structure[cite: 23]. [cite_start]Instead of ReLU, which may overreact in tiny networks, tanh delivers balanced outputs to support steady training[cite: 24].
* [cite_start]**Output Side:** **Sigmoid** plays a key role - mapping estimates to values between 0 and 1, fitting neatly with the loss setup[cite: 25].
* [cite_start]**Loss Function:** **Binary Cross-Entropy** fits best for yes/no tasks; it strongly discourages errors, guiding the model toward clear, accurate decisions[cite: 26].
* [cite_start]**Optimizer:** **SGD at 0.1 learning rate** ensures straightforward weight changes - no complex adjustments like momentum or variable rates required[cite: 27].

### **Training Process**
[cite_start]I trained using all four XOR examples at once across **5,000 epochs** - sure, that’s excessive, yet it lets us observe how convergence progresses step by step[cite: 29]. [cite_start]Since the data is minimal, splitting into batches or randomizing order isn’t necessary[cite: 30]. [cite_start]Instead of manual steps, PyTorch manages the forward computation, derives gradients, then adjusts weights accordingly[cite: 31]. [cite_start]Whenever possible, I used a GPU for execution; however, given the model’s simplicity, running on CPU gives almost the same speed[cite: 32].

---

## 📊 Part 3: Experimental Results

### **Objective**
Show results using images. [cite_start]Use main screenshots from running the code - like accuracy or loss graphs, predicted outputs - to back up your conclusions[cite: 35].

[cite_start]The training story appears clearly in the loss curve (refer to Screenshot 1)[cite: 36]. [cite_start]Starting from a modest 0.740646, after 1,000 epochs, performance drops sharply - to just 0.005161 - showing the system began grasping patterns[cite: 37]. [cite_start]By the last round, error reaches only 0.000481, suggesting output isn't merely accurate, yet highly precise[cite: 38].

> **[Insert Screenshot 1: Loss Curve Graph Here]**

### **Comparison Table: Predictions vs. Reality**

| Input Sample | Final Output (Prob.) | Predicted Class | True Label | Result |
| :--- | :--- | :--- | :--- | :--- |
| **Input 1** | 8.956160e-04 | 0 | 0 | ✅ Match |
| **Input 2** | 9.950519e-01 | 1 | 1 | ✅ Match |
| **Input 3** | 9.927043e-01 | 1 | 1 | ✅ Match |
| **Input 4** | 7.370279e-03 | 0 | 0 | ✅ Match |

[cite_start]Perfect result - full marks across all four examples[cite: 54]. [cite_start]Look at the confidence levels: they’re not close to the threshold, but pushed fully toward 0 or 1, meaning clear-cut decisions were made[cite: 54]. [cite_start]The drop in error is steady without sudden spikes, suggesting solid design and settings[cite: 55]. [cite_start]Each output matches reality exactly, showing the middle layer reshaped inputs so classes could be cleanly split[cite: 56].

---

## 💡 Part 4: Discussion and Analysis

### **Objective**
Look closely at how the method worked alongside the framework used. While reviewing, highlight challenges that came up during work, then explain what the outcomes suggest. [cite_start]Consider weak points the approach might have when applied further[cite: 59].

[cite_start]Looking at these outcomes calls for caution[cite: 60]. [cite_start]True, the system handled XOR without errors - yet in reality, it just stored a small set of fixed answers[cite: 60]. [cite_start]Given 20 weights for only four data points, it had more capacity than needed to recall instead of adapt[cite: 60]. [cite_start]It doesn’t grasp what XOR means - it forms a sharp dividing line that fits exactly those input positions[cite: 60]. [cite_start]If I changed one weight - even just a bit - the output might fail completely[cite: 60]. [cite_start]Without a validation group (splitting four points isn’t possible), there’s no way to check stability[cite: 60]. [cite_start]So, we lack proof that it works beyond these cases[cite: 60].

### **Difficulties Faced**
[cite_start]The primary difficulty wasn’t about tools - it stemmed from thinking[cite: 62]. [cite_start]Early attempts using learning rates higher than 0.3 made the loss spike suddenly, pushing me to recognize how easily SGD becomes unstable in tight model settings[cite: 63]. [cite_start]A quieter problem emerged too: knowing when to halt training[cite: 64]. [cite_start]Beyond 500 epochs, improvements stalled nearly completely; continuing up to 5,000 felt like unnecessary overhead - clearly inefficient upon reflection[cite: 64, 65].

### **Critical Limitations**
* [cite_start]**No generalization check:** claims about model understanding of XOR need tests on distorted or intermediate inputs[cite: 67].
* [cite_start]**Too many parameters:** 17 for just 4 data points - means the model fits training data exactly but fails on new data[cite: 68]. [cite_start]This imbalance shows classic overfitting where complexity outweighs evidence[cite: 69].
* [cite_start]**Brittleness:** This happens when the answer sits in a steep, tight dip - so fragile it can't handle small changes[cite: 70]. [cite_start]It doesn’t reflect stability or strength under variation[cite: 71].
* [cite_start]**Toy issues reflect real gaps:** XOR’s ease overlooks current hurdles - gradients fading, models fitting too closely on big data, or relying on constraint techniques[cite: 72].

### **What I'd Do Differently**
[cite_start]In practice, I’d try a 2-2-1 setup to check consistent convergence - it handles XOR yet sometimes stalls[cite: 74]. [cite_start]Inputs would include 5% Gaussian noise so robustness could be assessed; training would halt early to skip unnecessary rounds[cite: 75]. [cite_start]Crucially, this shows high accuracy on small data may signal overfitting rather than success[cite: 76]. [cite_start]Real skill means creating systems that adapt beyond the given examples[cite: 77].

---

## 📂 Files
* **Full Documentation:** [Download NLDP_EX1.docx](./NLDP_EX1.docx)
* **Source Code:** [Insert Link to Repository/File]

---
<p align="center">Made with ❤️ for Neural Network Learning</p>

# 🧠 Solving the XOR Problem Using a Multilayer Perceptron

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/Neural%20Network-MLP-blue?style=for-the-badge" alt="MLP">
</p>

---

## 📌 Part 1: Problem Introduction

### **Objective**
[cite_start]The primary goal was to design and implement a **Multilayer Perceptron (MLP)** capable of learning the non-linear XOR function, a task that simple one-layer networks cannot achieve due to structural limitations[cite: 4].

### **Background Context**
[cite_start]XOR is a fundamental benchmark for neural networks because it demonstrates the limitations of simple perceptrons[cite: 6, 7].
* **Linear Inseparability:** If you plot the inputs (00, 01, 10, 11) on a grid, the correct answers sit at opposite corners. [cite_start]No single straight line can separate them[cite: 7].
* [cite_start]**Historical Significance:** In 1969, Minsky and Papert identified this barrier, which temporarily slowed neural network research[cite: 8].
* [cite_start]**The Solution:** Adding an **internal (hidden) layer** allows the model to reorganize input patterns into a new space where they become linearly separable[cite: 9].


### **Lab Objectives**
* [cite_start]🧪 **Experiment:** Prove hidden layers can handle non-linear patterns[cite: 11].
* [cite_start]⚡ **Activation:** Understand how activation functions shape signal output[cite: 12].
* [cite_start]🛠️ **Implementation:** Build a fully functioning MLP using PyTorch[cite: 13].

---

## 🛠️ Part 2: Model Description

### **Model Architecture**
[cite_start]I implemented a compact **2-4-1 feedforward network**[cite: 19].
* [cite_start]**Input Layer:** 2 neurons (accepts binary pairs)[cite: 19].
* [cite_start]**Hidden Layer:** 4 neurons (provides enough width to capture complexity)[cite: 19].
* [cite_start]**Output Layer:** 1 neuron (final decision)[cite: 20].
* [cite_start]**Total Parameters:** Only 17 adjustable values, keeping it lightweight yet effective[cite: 21].


### **Key Components**
| Component | Choice | Reason |
| :--- | :--- | :--- |
| **Hidden Activation** | `tanh` | [cite_start]Gradual S-curve helps warp input structure gently[cite: 23]. |
| **Output Activation** | `sigmoid` | [cite_start]Maps outputs to 0-1 range for probability[cite: 25]. |
| **Loss Function** | `BCE Loss` | [cite_start]Ideal for binary classification (yes/no) tasks[cite: 26]. |
| **Optimizer** | `SGD` (0.1 LR) | [cite_start]Simple, straightforward weight updates[cite: 27]. |

### **Training Process**
* [cite_start]**Epochs:** 5,000 (Excessive, but useful for observing step-by-step convergence)[cite: 29].
* [cite_start]**Batching:** None (Trained on all 4 examples simultaneously due to minimal data)[cite: 30].
* [cite_start]**Hardware:** Executed on GPU for efficiency, though CPU speed is comparable for this scale[cite: 32].

---

## 📊 Part 3: Experimental Results

### **Performance Analysis**
[cite_start]The model showed a sharp drop in error, moving from a modest **0.740646** loss to a highly precise **0.000481**[cite: 37, 38].

> **[Insert Screenshot 1: Loss/Accuracy Curve Here]**

### **Final Output Verification**
[cite_start]The model achieved **perfect results** with high confidence levels[cite: 54].

| Input | True Label | Predicted Prob. | Class | Result |
| :--- | :--- | :--- | :--- | :--- |
| [0,0] | 0 | 8.95e-04 | 0 | ✅ Match |
| [0,1] | 1 | 9.95e-01 | 1 | ✅ Match |
| [1,0] | 1 | 9.92e-01 | 1 | ✅ Match |
| [1,1] | 0 | 7.37e-03 | 0 | ✅ Match |

---

## 🧐 Part 4: Discussion & Analysis

### **Critical Reflections**
[cite_start]While the system solved XOR perfectly, it likely **memorized** the answers rather than "understanding" the logic[cite: 60]. 
* [cite_start]**Overfitting:** 17 parameters for only 4 data points is a classic imbalance[cite: 68, 69].
* [cite_start]**Brittleness:** The model is fragile; a small weight change could cause total failure[cite: 70].

### **Challenges Faced**
* [cite_start]**Optimizer Instability:** Learning rates > 0.3 caused sudden loss spikes[cite: 63].
* **Efficiency:** Improvements stalled after 500 epochs; [cite_start]5,000 was unnecessary overhead[cite: 64, 65].

### **Future Improvements**
* [cite_start]🔄 Try a **2-2-1 setup** to test minimal convergence[cite: 74].
* [cite_start]🎲 Add **5% Gaussian noise** to inputs to test robustness[cite: 75].
* [cite_start]⏹️ Use **Early Stopping** to save computational resources[cite: 75].

---

## 📁 Project Resources
* 📄 **Documentation:** [Download Document File](./NLDP_EX1.docx)
* 💻 **Source Code:** [View Code](link-to-your-code)

---
<p align="center">
  [cite_start]<i>"Real skill means creating systems that adapt beyond the given examples." [cite: 77]</i>
</p>

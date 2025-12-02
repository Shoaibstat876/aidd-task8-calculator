# AIDD 30-Day Challenge — Task 8

Spec-Driven Python CLI Calculator using SpecKitPlus phases:

- /constitution  
- /specify  
- /plan  
- /tasks  
- /implement  

This repo contains my Task 8 submission files.

---

## ✨ Constitution Phase

### **Prompt:**  
Write a short Constitution for a Python CLI Calculator using SpecKitPlus.  
Mention project purpose, learning goals, and key principles of SDD.

---

### **Claude Output:**  

## 🧱 Project Constitution — Python CLI Calculator

### **Purpose**  
The goal of this project is to build a simple and reliable calculator using Python and the five phases of SpecKitPlus. The project helps me practice Spec-Driven Development (SDD) by breaking work into clear steps instead of coding directly.

### **Learning Goals**
- Understand all 5 SpecKitPlus phases  
- Learn how to define requirements before implementation  
- Build confidence in AI-assisted coding  
- Produce a clean, testable calculator program  
- Practice creating structured markdown documentation  

### **Scope**
- Take two numeric inputs  
- Perform Addition, Subtraction, Multiplication, and Division  
- Prevent division-by-zero errors  
- Show results clearly in the terminal  

### **Core Principles**
- Clarity over complexity  
- Step-by-step SDD workflow  
- Testability of each operation  
- Reliability and error handling  

### **Success Criteria**
- All four operations give correct results  
- Calculator handles invalid input safely  
- Program is easy to test and modify  
- All five phases are documented inside README.md

---

## ✨ Specify Phase

### **Prompt:**  
Write clear specifications for a Python CLI calculator using SpecKitPlus.

---

### **Claude Output:**  

## 📌 Specification — Calculator Requirements

### **1. Functional Requirements**
- Accept two numeric inputs  
- Allow user to choose an operation  
- Perform the calculation  
- Display clean output  

### **2. Input Requirements**
- Accept decimals  
- Reject non-numeric input  
- Re-ask for invalid values  

### **3. Operation Rules**
- Addition, Subtraction, Multiplication, Division  
- Protect division with zero  

### **4. Output Requirements**
- Print formatted result:  
  `Result: 7 + 3 = 10`

### **5. Error Handling**
- Non-numeric inputs  
- Invalid menu choice  
- Division by zero  

### **6. User Experience**
- Fast, simple, readable  

---

## ✨ Plan Phase

### **Prompt:**  
Create a technical plan for the calculator.

---

### **Claude Output:**

## 🛠️ Technical Plan

### **1. Flow**
1. Ask for num1  
2. Ask for num2  
3. Show menu  
4. Perform operation  
5. Display result  

### **2. Components**
- Input handler  
- Operation selector  
- Four operation functions  
- Output formatter  

### **3. Error Handling**
- Invalid numbers  
- Invalid menu  
- Division by zero  

### **4. Testing**
- 10 + 5 = 15  
- 20 - 4 = 16  
- 6 * 7 = 42  
- 12 / 3 = 4  

---

## ✨ Tasks Phase

### **Prompt:**  
Break the calculator into tasks.

---

### **Claude Output:**

## ✅ To-Do Checklist

### **Setup**
- Create `calculator.py`  
- Print “Calculator Ready”  

### **Input**
- Ask for two numbers  
- Convert to float  
- Validate errors  

### **Operations**
- Show menu  
- Validate choice  

### **Logic**
- Implement: add, subtract, multiply, divide  
- Protect division  

### **Output**
- Print formatted result  

### **Testing**
- Run all four operations  
- Save screenshots  

### **Documentation**
- Update README  
- Add final screenshots  

---

## ✨ Implement Phase

### **Prompt:**  
Write the final implementation following the previous phases.

---

### **Claude Output (Summary Only):**  
The complete working calculator code is provided separately in `calculator.py`.  
It includes:  
- Input handling  
- Operation menu  
- Four calculation functions  
- Error checking  
- Final result printing  

The implementation strictly follows the Constitution, Specify, Plan, and Tasks phases.

---

## ✨ Final Testing Screenshots

Below are the results of testing all four operations.  
Screenshots are provided as required.

### 💫 Addition Test  
File: `screenshots/addition.png`

### 💫 Subtraction Test  
File: `screenshots/subtraction.png`

### 💫 Multiplication Test  
File: `screenshots/multiplication.png`

### 💫 Division Test  
File: `screenshots/division.png`

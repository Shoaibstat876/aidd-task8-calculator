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
Define the inputs, outputs, operations, rules, constraints, and error-handling requirements.

---

### **Claude Output:**  

## 📌 Specification — Calculator Requirements

### **1. Functional Requirements**
- The program must accept **two numeric inputs** from the user.  
- The program must allow the user to choose **one operation**:
  - Addition  
  - Subtraction  
  - Multiplication  
  - Division  
- The program must compute the result based on the selected operation.  
- The program must display the final output clearly in the terminal.

---

### **2. Input Requirements**
- Accept integers and decimal numbers.  
- Reject non-numeric input with a friendly message.  
- Request input again if the user enters invalid data.

---

### **3. Operation Rules**
- **Addition:** num1 + num2  
- **Subtraction:** num1 − num2  
- **Multiplication:** num1 × num2  
- **Division:** num1 ÷ num2  
- For division, if num2 = 0 → show “Error: Cannot divide by zero.”

---

### **4. Output Requirements**
- Show the full expression and result, for example:  
  - `Result: 7 + 3 = 10`  
  - `Result: 9 / 3 = 3.0`
- Output must always appear on a new line with clean formatting.

---

### **5. Error Handling Requirements**
- Handle division by zero gracefully.  
- Handle invalid numeric input.  
- Handle invalid operation selection.  
- Program must not crash for any wrong input.

---

### **6. User Experience Requirements**
- The program should be simple, fast, and easy to use.  
- Messages must be clear and beginner-friendly.  
- After displaying the result, the program may exit normally.

---

### **7. Success Conditions**
- All four operations work correctly.  
- All invalid inputs are handled safely.  
- Output is readable and consistent.  
- Specification matches implementation in later phases.

---

## ✨ Plan Phase

### **Prompt:**  
Create a simple and clear technical plan for a Python CLI calculator using SpecKitPlus.  
Explain the architecture, program flow, calculations, and how input/output will work.

---

### **Claude Output:**

## 🛠️ Technical Plan — Calculator Architecture & Flow

### **1. Program Structure**
The calculator will follow a linear, step-by-step structure:
1. Ask the user for the first number  
2. Ask the user for the second number  
3. Show a menu of operations ( + , − , × , ÷ )  
4. Perform the chosen calculation  
5. Display the result  
6. Exit safely

---

### **2. Core Components**
- **Input Handler**  
  Reads two values from the user and converts them to numbers.

- **Operation Selector**  
  Lets the user choose between addition, subtraction, multiplication, and division.

- **Calculator Functions**  
  Four small functions, one for each operation:
  - `add(a, b)`  
  - `subtract(a, b)`  
  - `multiply(a, b)`  
  - `divide(a, b)` (with zero-check)

- **Output Formatter**  
  Displays the result in a clear, readable format.

---

### **3. Calculation Flow**
1. Convert both inputs to `float`.  
2. Match the user’s choice to the correct function.  
3. Perform the selected operation.  
4. Handle any errors (invalid input or division by zero).  
5. Print the full expression and result.

---

### **4. Error Handling Plan**
- If the user enters a non-number → show a friendly error message.  
- If the user chooses an invalid operation → show a message and stop.  
- If division by zero is attempted → block it and show “Error: Cannot divide by zero.”  
- The program must never crash due to bad input.

---

### **5. Testing Plan**
The calculator will be tested using four sample operations:
- `10 + 5 = 15`  
- `20 - 4 = 16`  
- `6 * 7 = 42`  
- `12 / 3 = 4`  

These test results will be captured as screenshots for submission.

---

### **6. Output Format**
The final result will follow this template:

```text
Result: <num1> <operator> <num2> = <answer>

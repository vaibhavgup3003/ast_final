# Rule Engine Application

This application is a 3-tier rule engine designed to evaluate user eligibility based on specific rules involving attributes like age, department, income, and experience. Utilizing an Abstract Syntax Tree (AST), the application supports rule creation, combination, and evaluation, with a simple UI and backend built using Flask. The application can store rules in a MySQL database for persistence and uses various operations for rule evaluation.

---
## Demonstration
[![Demo Video](https://img.youtube.com/vi/0_ShqBxrZ6M/0.jpg)](https://www.youtube.com/watch?v=0_ShqBxrZ6M)


## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [AST Logic](#ast-logic)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [Dependencies](#dependencies)
8. [Design Choices](#design-choices)
9. [Future Enhancements](#future-enhancements)

---

### Overview
The Rule Engine Application allows users to create logical rules, combine multiple rules, and evaluate data against these rules. Each rule is represented as an AST, which enables flexible rule modification and dynamic evaluation. Rules are stored in a MySQL database, allowing users to access and modify them as needed.

### Features
- **Rule Creation**: Users can define custom rules with logical operators (AND, OR, >, <, =).
- **Rule Combination**: Multiple rules can be combined to create complex logic.
- **Data Evaluation**: Evaluate data entries against created rules to determine eligibility.
- **Persistent Storage**: Rules are stored in MySQL for persistent access and retrieval.
- **User Interface**: A simple HTML/JavaScript interface allows interaction with the rule engine.

---

### Architecture
1. **Data Source**: Utilizes a MySQL database for storing rule definitions.
2. **Backend Logic**:
   - **AST Class**: Builds an AST from rule strings and evaluates data against the tree structure.
   - **Node Structure**: Represents each logical operation or operand in the rule.
   - **Operations**: Supports AND, OR, >, <, >=, <=, and = operators.
   - **Flask Server**: Provides endpoints to create, combine, and evaluate rules.
3. **Frontend**: HTML/JavaScript interface for user interaction.

---

### AST Logic

1. **AST Structure**:
   - Operators (e.g., AND, OR, >, <, =) are represented in the internal nodes of the tree.
   - Values or operands (e.g., numbers, strings) are stored in the leaf nodes.

2. **Rule Parsing and Precedence**:
   - The AST is built by parsing rule strings, identifying operators with the highest precedence within the context of parentheses and quotes, and placing them in the correct node hierarchy.
   - This process evaluates the “web” of parentheses and quotes to ensure operators are applied in the correct order.
   - Operators are prioritized by custom precedence levels, ensuring that higher-precedence operations are nested deeper within the tree.

3. **Combining Rules**:
   - The `combine_rules` method first parses and breaks down each rule individually, creating separate ASTs.
   - These separate ASTs are then combined into a single tree structure using the `AND` operator as the default, ensuring all conditions must be satisfied for evaluation.
   - This operator can be modified based on user preference, allowing different combinations of rules with custom logical connectors.

---

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vaibhavgup3003/ast_final.git
   cd <repository-directory>
   ```
2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Environment Setup**:
   - Update MySQL database credentials in `server.py`:
   ```python
   db_config = {
    "user": "root",
    "password": "<your_password>",
    "host": "localhost",
    "database": "rule_engine",
   }
   ```

   - Create a MySQL database and table:
   ```sql
   CREATE DATABASE rule_engine;
   CREATE TABLE rules (name VARCHAR(255), rule TEXT);
   ```


4. **Run the Server**:
   ```bash
   python server.py
   ```

5. **Access the UI**:
   - Open `index.html` in a web browser to access the UI.

### Usage

1. **Creating a Rule**:
   - In the UI, select **Create**, enter a rule name and definition, and click **Create Rule**.
   - Example rule: `(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')`

2. **Combining Rules**:
   - Select **Combine** in the UI, enter a combined rule name and list of rule names to combine.

3. **Evaluating Data**:
   - Select **Evaluate** in the UI, enter the rule name, and provide a JSON object with data attributes.

### Dependencies

- `Flask`: For backend API endpoints.
- `mysql-connector-python`: For MySQL database connections.

To install these packages, run:
```bash
pip install -r requirements.txt
```

### Design Choices

1. **AST for Rule Representation**: Each rule is parsed into an AST, enabling flexible manipulation and evaluation.
2. **MySQL for Persistent Storage**: Rules are stored in a MySQL database, ensuring persistence and easy retrieval.
3. **Operator Functions**: Supports common logical and comparison operations (`AND`, `OR`, `>`, `<`, `=`, etc.).

### Future Enhancements

1. **Error Handling**: Improve validation for rule syntax and data format.
2. **Enhanced UI**: Add styling and improved interactions for a more intuitive user experience.
3. **Additional Operators**: Support complex logical constructs and additional data types.
4. **Dockerize the Application**: Resolve current issues with the Docker setup for better portability.




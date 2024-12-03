# Bank Churn Data Analysis - team 9

## **Overview** 
This project dived into a bank's customer data to uncover interesting patterns. It read data from a default CSV file or one provided by the user, analyzing things like how credit scores vary based on age and gender, and how the number of products a customer has affects their points. We also looked at how long a customer has been with the bank and how it might relate to their credit score. To efficiently handle and display large datasets, we used a technique called pagination. Finally, we presented our analysis in a clear and concise JSON format.

## **Setup**  

### **Prerequisites**  
- Python 3.12 or newer
- More datasets (Project provides datasets, but you can use your own. Make sure it has the following columns: 
RowNumber,CustomerId,Surname,CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Exited,Complain,Satisfaction Score,Card Type,Point Earned) 

### **Installation**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/241111-Python/team9-p2.git 
   cd team9-p2
   ```

### **Start the app**  
1. Main method 
   ```bash 
   python main.py
   ```
2. Optional method
    ```bash 
   python main.py --load-dataset ./datasets/dataset-name.csv --display-analyze (either display or analyze)
   ```
   This way it can run the app using a different dataset from the ones the project provides.

### **Optional**

### **Prerequisites**  
- Linux/Unix environment. 

### *Set up the cron job for leaderboard updates:* 
1. Open Cron:
    ```bash 
    crontab -e
    ```

2.    Add the following line to schedule the     leaderboard update script (adjust timing as needed):

        ```bash 
        * * * * * python /path/to/crontab.py  
        ```

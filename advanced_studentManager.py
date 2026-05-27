import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ------------------ DATABASE SETUP ------------------
conn = sqlite3.connect("student_marks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    name TEXT PRIMARY KEY,
    marks INTEGER NOT NULL
)
""")
conn.commit()

# ------------------ FUNCTIONS ------------------
def add_student(name, marks):
    try:
        cursor.execute("INSERT INTO students VALUES (?, ?)", (name, marks))
        conn.commit()
        print("Student has successfully been added!!")
    except sqlite3.IntegrityError:
        print("Student already exists!")

def check_result(name):
    cursor.execute("SELECT marks FROM students WHERE name=?", (name,))
    result = cursor.fetchone()
    if result:
        marks = result[0]
        if marks >= 40:
            print(f"STUDENT {name} PASS SUCCESSFULLY!!")
        else:
            print(f"STUDENT {name} FAIL!!")
    else:
        print("Student not found!!")

def show_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\n--- Student Records ---")
        for row in rows:
            print(f"Name: {row[0]}, Marks: {row[1]}")
    else:
        print("No records found!")

def visualize_performance():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No data to visualize!")
        return
    
    df = pd.DataFrame(rows, columns=["Name", "Marks"])
    
    # Bar chart
    plt.figure(figsize=(8,5))
    sns.barplot(x="Name", y="Marks", data=df, palette="viridis")
    plt.title("Student Performance")
    plt.xticks(rotation=45)
    plt.show()
    
    
    # --- Pass vs Fail Pie Chart ---
    pass_count = (df["Marks"] >= 40).sum()
    fail_count = (df["Marks"] < 40).sum()
    plt.figure(figsize=(6,6))
    plt.pie([pass_count, fail_count], labels=["Pass", "Fail"], autopct="%1.1f%%", colors=["green","red"])
    plt.title("Pass vs Fail Distribution")
    plt.show()
    
    # --- Top Performers Chart ---
    top_students = df.sort_values(by="Marks", ascending=False).head(5)
    plt.figure(figsize=(8,5))
    sns.barplot(x="Marks", y="Name", data=top_students, palette="mako")
    plt.title("Top 5 Performers")
    plt.show()
    
    # Distribution plot
    plt.figure(figsize=(6,4))
    sns.histplot(df["Marks"], bins=10, kde=True, color="blue")
    plt.title("Marks Distribution")
    plt.show()

# ------------------ MAIN MENU ------------------
while True:
    print("\nSTUDENT MANAGER APP")
    print("1. Add Student")
    print("2. Check Student Result")
    print("3. Show All Students")
    print("4. Visualize Performance")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))
        add_student(name, marks)
    elif choice == '2':
        name = input("Enter student name: ")
        check_result(name)
    elif choice == '3':
        show_all_students()
    elif choice == '4':
        visualize_performance()
    elif choice == '5':
        print("EXITING...")
        break
    else:
        print("Invalid input!!!")

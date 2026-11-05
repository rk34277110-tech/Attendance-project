import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
data = pd.read_csv("attendance.csv")

# Calculate Attendance
data["Percentage"] = (
    data["Classes_Attended"] /
    data["Classes_Held"] * 100
)

while True:

    print("\n===== COLLEGE ATTENDANCE ANALYZER =====")
    print("1. Show All Students")
    print("2. Students Below 75%")
    print("3. Subject Average")
    print("4. Show Graph")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(data[["Name", "Percentage"]].round(2))

    elif choice == "2":
        result = data[data["Percentage"] < 75]

        if result.empty:
            print("No student below 75%")
        else:
            print(result[["Name", "Percentage"]].round(2))

    elif choice == "3":
        result = data.groupby("Subject")["Percentage"].mean()
        print(result.round(2))

    elif choice == "4":
        result = data.groupby("Subject")["Percentage"].mean()
        result.plot(kind="bar", title="Attendance Chart")
        plt.ylabel("Percentage")
        plt.show()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
import pandas as pd

def analyze_excel(excel_file_path):
    try:
        df = pd.read_csv(excel_file_path)

        summary_stats = df.describe()

        # Display the results
        print("Summary Statistics:")
        print(summary_stats)

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    excel_file_path = 'myfile.csv'
    
    analyze_excel(excel_file_path)

# Run the script if executed directly
if __name__ == "__main__":
    main()

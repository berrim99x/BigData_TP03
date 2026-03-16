from src.data_cleaning import load_and_clean_data
from src.eda import perform_eda
from src.analysis import customer_segmentation

def main():

    data = load_and_clean_data()

    perform_eda(data)

    data = customer_segmentation(data)

    # ✅ حفظ الملف النهائي
    data.to_csv("cleaned_sales_data.csv", index=False)

    print("\nFile cleaned_sales_data.csv created successfully!")

if __name__ == "__main__":
    main()
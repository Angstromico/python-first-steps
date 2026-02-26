def main(): 
    total_amount = float(input("Enter the total amount to be charged in $: "))

    if(total_amount > 100):
        discount = total_amount * 0.1  # 10% discount
        final_amount = total_amount - discount
        print(f"You get a discount of ${discount:.2f}. The final amount to be charged is ${final_amount:.2f}.")
    else:
        print(f"No discount applied. The total amount to be charged is ${total_amount:.2f}.")


if __name__ == "__main__":
    main()

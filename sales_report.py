def generate_sales_report(file_name):
    """Generate sales report showing total melons each salesperson sold.
    
    Return in a string the salesperson's name and how many watermelons they sold.

    The output should look like this:

        Ann Smith sold 13 melons
        Linda Reynolds sold 169 melons
        Doris Miller sold 17 melons
    
    """
    sales_dict = {}

    sales_file = open(file_name)

    for line in sales_file:
        entries_list = line.rstrip().split('|')
        client_name, total_cost, num_melons = entries_list
        sales_dict.update({client_name: {"total cost": total_cost, "number of melons sold": num_melons}})

    for name, attributes in sales_dict.items():
        print(f'{name} sold {attributes["number of melons sold"]} melons')


generate_sales_report("sales-report.txt")


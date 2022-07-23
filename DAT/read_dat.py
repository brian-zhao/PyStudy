import csv
import glob
import os

my_suburb = [
    "enfield",
    "burwood",
    "croydon",
    "croydon park",
    "burwood height",
    "ashfield",
    "canada bay",
    "ashbury",
]

rel_paths = [
    "20220606",
    "20220613",
    "20220620",
    "20220627",
    "20220704",
    "20220711",
    "20220718",
]

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    files = []
    for rel_path in rel_paths:
        abs_file_path = os.path.join(script_dir, rel_path)
        files.extend([file for file in glob.glob(abs_file_path + "/*")])
    result = []
    result.append(
        "addr1,addr2,addr3,addr4,suburb,postcode,area,area_unit,price,type,contract_date,settle_date"
    )
    for file_name in files:
        with open(file_name) as file:
            lines = file.readlines()
            for line in lines:
                columns = line.split(";")
                if columns[0] == "B" and columns[9].lower() in my_suburb:
                    result.append(
                        ",".join(
                            [
                                columns[5],
                                columns[6],
                                columns[7],
                                columns[8],
                                columns[9],
                                columns[10],
                                columns[11],
                                columns[12],
                                columns[15],
                                columns[18],
                                columns[13],
                                columns[14],
                            ]
                        )
                    )

            # lines = [line.rstrip() for line in lines]
            # result.extend([line.rstrip() for line in lines])

    with open("my_surburb_sold_price.csv", "w") as f:
        # create the csv writer
        writer = csv.writer(
            f,
            delimiter=",",
        )
        for row in result:
            # write a row to the csv file
            writer.writerow([x for x in row.split(",")])

import table


details = [
    ["Passenger Name", "Price", "Age", "Gender"],
    ["sadhvik", "2065.0", "18", "male"],
    ["rithvik", "1475.0", "10", "male"],
]

printable_version = table.create_table(details, 5)


table.print_table(printable_version)


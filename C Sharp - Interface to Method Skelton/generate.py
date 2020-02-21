return_values = {
    "bool": "true",
    "int": "1",
    "string": '"string"',
    "float": "1.0",
    "char": "'a'",
}


def convert():
    try:
        with open("data.txt", "r") as f:
            file_data = f.readlines()

        with open("out.txt", "w") as f:
            for item in file_data:
                f.write("public ")
                f.write(item.replace(";", "{"))
                f.write(
                    """
        try{

        }catch(Exception e){
            Console.WriteLine(" """
                )
                f.write(item.split()[1].split("(")[0])
                f.write(' :- {0}",e);\n\t}\n')
                f.write("\treturn ")
                if item.split()[0] in return_values.keys():
                    f.write(return_values[item.split()[0]]+";")
                f.write("\n}")

        print("Success")

        with open("out.txt", "r") as f:
            print(f.read())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    convert()


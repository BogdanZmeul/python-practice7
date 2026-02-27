from app.io import input as inp
from app.io import output as out
import os


def main():
    data_dir = "data"
    input_txt = os.path.join(data_dir, "text.txt")
    input_csv = os.path.join(data_dir, "input.csv")
    output_res = os.path.join(data_dir, "results.txt")

    text_console = inp.get_input_from_console()
    text_builtin = inp.read_from_file(input_txt)
    text_pandas = inp.read_from_file_pandas(input_csv)

    all_results = (
        f"Console: {text_console}\n"
        f"Built-in: {text_builtin}\n"
        f"Pandas:\n {text_pandas}"
    )

    out.write_to_console(all_results)
    out.write_to_file(all_results, output_res)
    print(f"Results are saved to {output_res}")


if __name__ == "__main__":
    main()
import os

file_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.join(file_dir, "../../")


def get_repo_dir():
    return repo_dir


def print_char_line(char, num_chars):
    out = ""
    for x in range(num_chars):
        out = out + char
    return out


def print_frame(str, data_dict):
    char_div1 = "="
    char_div2 = "-"
    char_div3 = "·"

    spacing = 2
    dash_margin = 6
    totwidth = len(str) + spacing + dash_margin

    heading_dash_unit = print_char_line(char_div1, dash_margin)
    footer_line = print_char_line(char_div2, totwidth)
    divider_line = print_char_line(char_div3, totwidth)

    output = f"\n\n{heading_dash_unit} {str} {heading_dash_unit}\n"

    for dkey, dvalue in data_dict.items():
        output = output + f"{dkey}: {dvalue}\n"

    output = output + f"{footer_line}\n\n"

    print(output)

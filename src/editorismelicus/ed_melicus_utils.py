import os
import json

file_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.join(file_dir, "../../")


def get_cfg_data():
    cfg_data = {
        "gabctk_script_fname": "gabctk.py",
        "doc_dir": os.path.join(repo_dir, "document"),
        "data_dir": os.path.join(repo_dir, "data"),
    }

    with open(f"{cfg_data['data_dir']}/configs.json", "r") as file:
        cfg_json = json.load(file)
        cfg_data["gabctk_dir"] = os.path.join(
            repo_dir, cfg_json["paths"]["gabctkDirectory"]
        )
        cfg_data["output_dir_ly_data"] = os.path.join(
            repo_dir, cfg_json["paths"]["outputDirectoryLyData"]
        )
        cfg_data["output_dir_ly"] = os.path.join(
            repo_dir, cfg_json["paths"]["outputDirectoryLy"]
        )
        cfg_data["output_dir_pdf"] = os.path.join(
            repo_dir, cfg_json["paths"]["outputDirectoryPdf"]
        )

    with open(f"{cfg_data['data_dir']}/input-configs.json", "r") as file:
        input_cfg_json = json.load(file)
        cfg_data["documents"] = input_cfg_json["documents"]

    return cfg_data


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
    totwidth = (spacing + dash_margin) * 2 + len(str)

    heading_dash_unit = print_char_line(char_div1, dash_margin)
    footer_line = print_char_line(char_div2, totwidth)
    divider_line = print_char_line(char_div3, totwidth)

    output = f"\n\n{heading_dash_unit} {str} {heading_dash_unit}\n"

    for dkey, dvalue in data_dict.items():
        output = output + f"{dkey}: {dvalue}\n"

    output = output + f"{footer_line}\n\n"

    print(output)

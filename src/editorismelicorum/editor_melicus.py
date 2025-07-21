#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# The Chief Editor of Music runs the show.

import sys, os, time, json, logging

from praedica_min import praedica_min
from lectormelicus.lector_melicus import lege_tabulae_gabc, copy_conv_gabc_vars
from scriptormelicus.scriptor_melicus import write_song_ly
from ed_melicorum_utils import get_cfg_data

# /////   Loading internal configuration
current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, "../../data", "configs.json")) as f:
    configs_data = json.load(f)


def get_opmode_by_id(input_id):
    for o_mode in configs_data["opModes"]:
        if o_mode["id"] == input_id:
            return o_mode
    return None


def get_dialog_string(dialog_key, variables=None):
    raw_string = configs_data["dialog"][dialog_key]
    if (variables is not None) or variables:
        return raw_string.format(variables[0])
    return raw_string


def print_frame(
    textinput,
    large=False,
    light=False,
    extra_space=False,
    show_top=True,
    show_bottom=True,
):
    formatted_input = textinput
    if extra_space:
        formatted_input = "///\n" + textinput + "///\n"

    if show_top:
        print("///============================================================")
    if large:
        print("///")
    print(formatted_input)
    if large:
        print("///")
    if show_bottom:
        if light:
            print("///····························································")
        else:
            print("///------------------------------------------------------------")


def print_intro():
    main_frame_txt = "///   E D I T O R I S      M E L I C O R U M\n"
    main_frame_txt = (
        main_frame_txt
        + f"///\n///------------------------------------------------------------\n"
    )
    main_frame_txt = main_frame_txt + "///\n///   FABRICA SALVADORIS -- MMXXV\n"
    main_frame_txt = main_frame_txt + "///   Salvador Workshop -- 2025\n"
    main_frame_txt = main_frame_txt + f'///\n///   v{configs_data["version"]}'
    print()
    print_frame(main_frame_txt, large=True)
    print()
    print_frame("///   S E R V I C E S      M E N U", large=True)
    print("///")
    for o_mode in configs_data["opModes"]:
        o_mode_text = f'///   < {o_mode["id"]} >  {o_mode["name"]}\n'
        o_mode_text += (
            f"///····························································\n"
        )
        o_mode_text += f'///   {o_mode["desc"]}\n///\n///'
        print_frame(o_mode_text, show_top=False, show_bottom=False)
    print()


# /////   Main Program

print_intro()
opmode_name = ""

try:
    if len(sys.argv) > 1:
        # user has entered arguments. try to parse-
        # script name is the first arg, num value is 2nd
        arg_input = sys.argv[1]
        input_operation_mode = int(arg_input, 10)

        opmode_name = get_opmode_by_id(input_operation_mode)["nameConfirmation"]
        user_input = input(get_dialog_string("actionConfirmation", [opmode_name]))
        if user_input.lower() != "y":
            print(get_dialog_string("exit"))
            sys.exit()
    else:
        # user has not entered arguments.
        u_input_op_mode = input(get_dialog_string("intro"))
        input_operation_mode = int(u_input_op_mode, 10)

        opmode_name = get_opmode_by_id(input_operation_mode)["nameConfirmation"]
        u_input_confirmation = input(
            get_dialog_string("actionConfirmation", [opmode_name])
        )
        if u_input_confirmation.lower() != "y":
            print(get_dialog_string("exit"))
            sys.exit()

except (TypeError, ValueError):
    logging.exception("TypeError / ValueError -- Integer casting probably failed")
    input_operation_mode = None
except BaseException:
    logging.exception("An exception was thrown!")
    input_operation_mode = None

# TODO -- set up "requirements.txt"
# TODO -- SET UP CODE DOCUMENTATION TOOLS

print(get_dialog_string("performingAction1"))
time.sleep(0.75)
print(get_dialog_string("performingAction2", [opmode_name]))
time.sleep(1.5)

cfg_data = get_cfg_data()


def to_input_cfg_paths(cfg_path):
    return os.path.join(cfg_data["data_dir"], cfg_path)


def to_conv_ly_paths(cfg_path):
    cleaned_path = cfg_path.replace("examples/", "")
    cleaned_path = cleaned_path.replace(".gabc", ".ly")
    return os.path.join(cfg_data["output_dir_ly_data"], cleaned_path)


input_documents = cfg_data["documents"]

if input_operation_mode == 1:
    print("NOTE: Arranging not available!")

elif input_operation_mode == 2:
    for in_doc in input_documents:
        gabc_docs = map(to_input_cfg_paths, in_doc["gabcFiles"])
        conv_gabc_docs = map(to_conv_ly_paths, in_doc["gabcFiles"])
        var_filepath = 0
        template_filepath = 0
        doc_data = 0

        lege_tabulae_gabc(gabc_docs)

        for conv_gabc_doc in conv_gabc_docs:
            out_ly_path = conv_gabc_doc.replace(".ly", "-vars.ly")
            copy_conv_gabc_vars(conv_gabc_doc, out_ly_path)

        write_song_ly(var_filepath, template_filepath, doc_data)

        praedica_min(in_doc["mainDocument"])

elif input_operation_mode == 3:
    print("NOTE: Publishing not available!")

else:
    print(get_dialog_string("error"))

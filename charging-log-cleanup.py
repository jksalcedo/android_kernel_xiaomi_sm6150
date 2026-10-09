#!/usr/bin/env python3
"""Apply selected logging changes from the kernel repository root."""

import argparse
from pathlib import Path
import re
import sys


SAMPLES = (
    "battery capacity is : %d",
    "bq_input_suspend: %d",
    "batt_temp: %d",
    "warm_thres: %d",
    "cool_thres: %d",
    "effective_fcc_val: %d",
    "pdpm->cp.charge_enabled:%d",
    "pdpm->cp_sec.charge_enabled:%d",
    "bypass_en:%d, cp_chg_mode:%d:%d, therm_level:%d, fcc:%d, vbat:%d",
    "chg_mode:%d, curr_ibus_limit:%d, ibus_limit:%d, bat_curr_lp_lmt:%d, effective_fcc_val:%d, apdo_max_curr:%d",
    "vbus:%d, ibus:%d(m:%d,s:%d), vbat:%d(reg:%d), ibat:%d",
    "sw_ctrl_steps:%d, step_vbat:%d, step_ibus:%d, step_ibat:%d, step_bat_reg:%d",
    "hw_ctrl_steps:%d",
    "is_temp_out_fc2_range = %d, thermal_level = %d",
    "steps: %d, sw_ctrl_steps:%d, hw_ctrl_steps:%d",
    "steps:%d, pdpm->request_voltage:%d, pdpm->request_current:%d",
)


def replace_selected(text, pattern, replacement, label, expected=1):
    matches = list(re.finditer(pattern, text, re.MULTILINE))
    if len(matches) != expected:
        raise ValueError("{}: expected {} matches, found {}".format(label, expected, len(matches)))
    return re.sub(pattern, replacement, text, flags=re.MULTILINE)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    args = parser.parse_args()
    plans = []

    # Read and validate both files before making any changes.
    for name in ("maxim/ds28e16.c", "ti/pd_policy_manager.c"):
        path = Path("drivers/power/supply") / name
        original = path.read_bytes()
        text = original.decode("utf-8")
        if name.startswith("maxim/"):
            pattern = r"^([ \t]*#[ \t]*define[ \t]+ds_dbg[ \t]+)pr_(?:err|debug)(?=[ \t]*\r?$)"
            text = replace_selected(text, pattern, r"\1pr_debug", str(path) + ": ds_dbg")
        else:
            for message in SAMPLES:
                pattern = r'^([ \t]*)pr_(?:info|debug)([ \t]*\([ \t]*"' + re.escape(message + r"\n") + r'")'
                # Two temperature samples exist; one is already pr_debug.
                expected = 2 if message == "batt_temp: %d" else 1
                text = replace_selected(text, pattern, r"\1pr_debug\2", str(path) + ": " + message, expected)
        plans.append((path, original, text.encode("utf-8")))

    for path, original, updated in plans:
        if path.read_bytes() != original:
            raise ValueError(str(path) + ": changed during validation; retry")

    for path, original, updated in plans:
        if original == updated:
            print(str(path) + ": already updated")
        elif args.check:
            print(str(path) + ": ready to update")
        else:
            path.write_bytes(updated)
            print(str(path) + ": updated")


if __name__ == "__main__":
    try:
        main()
    except (OSError, UnicodeError, ValueError) as exc:
        sys.exit("ERROR: " + str(exc))

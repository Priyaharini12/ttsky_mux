# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start MUX4 Test")

    # Initialize inputs
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Reset sequence
    dut.rst_n.value = 0
    await Timer(50, units="ns")

    dut.rst_n.value = 1
    await Timer(50, units="ns")

    # Test cases
    # (a, s, expected_y)
    test_cases = [
        (0b1001, 0b00, 1),
        (0b1001, 0b01, 0),
        (0b1001, 0b10, 0),
        (0b1001, 0b11, 1),
    ]

    # Apply test cases
    for a, s, expected_y in test_cases:

        # ui_in mapping
        # ui_in[3:0] = a
        # ui_in[5:4] = s
        dut.ui_in.value = (s << 4) | a

        # Wait for output propagation
        await Timer(20, units="ns")

        try:
            # Read output
            output_val = int(dut.uo_out.value)

            # Extract mux output from bit 0
            actual_y = output_val & 0x1

            dut._log.info(
                f"a={a:04b}, s={s:02b}, y={actual_y}"
            )

            # Assertion
            assert actual_y == expected_y, \
                f"Failed: a={a:04b}, s={s:02b}, expected={expected_y}, got={actual_y}"

        except ValueError:
            dut._log.error(
                f"Conversion Error: uo_out = {str(dut.uo_out.value)}"
            )
            raise

    dut._log.info("All MUX4 test cases passed")

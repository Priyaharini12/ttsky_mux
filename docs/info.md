<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 4:1 Multiplexer (MUX) using Verilog HDL.
The multiplexer selects one of four input bits based on two select lines.
Inputs a[3:0] are provided through ui_in[3:0], and select lines s[1:0] are provided through ui_in[5:4].
The selected input is sent to the output uo_out[0].

## How to test
Provide 4-bit input data through ui_in[3:0] and select values through ui_in[5:4].
Run the cocotb testbench to apply different select combinations and verify the output.
The selected input bit appears on uo_out[0].
You can simulate the design using tools like Icarus Verilog and view waveforms using GTKWave.
## External hardware

No external hardware is required for this project.
The design uses only Tiny Tapeout input and output pins.
Testing is performed through simulation using software tools.

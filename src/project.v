/* 
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,    
    output wire [7:0] uo_out,   
    input  wire [7:0] uio_in,   
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

    // Internal signals
    wire [3:0] a;
    wire [1:0] s;
    wire y;

    // Input mapping
    assign a = ui_in[3:0];
    assign s = ui_in[5:4];

    // MUX logic
    assign y = (s == 2'b00) ? a[0] :
               (s == 2'b01) ? a[1] :
               (s == 2'b10) ? a[2] :
                              a[3];

    // Output mapping
    assign uo_out[0] = y;
    assign uo_out[7:1] = 7'b0000000;

    // Unused IO
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Prevent warnings
    wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule

`default_nettype wire

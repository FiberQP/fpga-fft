from pathlib import Path
from vunit import VUnit

# Create VUnit instance by parsing command line arguments
vu = VUnit.from_argv()
print(f'Using simulator: {vu.get_simulator_name()}')


# Optionally add VUnit's builtin HDL utilities for checking, logging, communication...
# See http://vunit.github.io/hdl_libraries.html.
vu.add_vhdl_builtins()
# or
# vu.add_verilog_builtins()

# Define source path to theVHDL files in FFT library
SRC_PATH = Path(__file__).parents[2]
print(SRC_PATH)

# Create library 'lib'
lib = vu.add_library("lib")

# Add all files ending in .vhd in current working directory to library
lib.add_source_files("*.vhd")
# Include FFT lib sources
#lib.add_source_files(SRC_PATH / "*.vhd")
lib.add_source_files(SRC_PATH / "fft_types.vhd")
lib.add_source_files(SRC_PATH / "twiddle_addr_gen.vhd")
lib.add_source_files(SRC_PATH / "transposer.vhd")
lib.add_source_files(SRC_PATH / "sr.vhd")
lib.add_source_files(SRC_PATH / "complex_ram.vhd")
lib.add_source_files(SRC_PATH / "complex_ram_lut.vhd")
lib.add_source_files(SRC_PATH / "twiddle_generator.vhd")
lib.add_source_files(SRC_PATH / "transposer_addr_gen.vhd")
lib.add_source_files(SRC_PATH / "transposer4.vhd")
lib.add_source_files(SRC_PATH / "reorder_buffer.vhd")
lib.add_source_files(SRC_PATH / "fft4_serial7.vhd")
lib.add_source_files(SRC_PATH / "fft4_serial6.vhd")
lib.add_source_files(SRC_PATH / "xilinx" / "dsp48e1_multadd.vhd")
# Include DUT files
lib.add_source_files(SRC_PATH / "generated" / "twiddle" / "twiddle_rom_1024.vhd")
lib.add_source_files(SRC_PATH / "generated" / "twiddle" / "twiddle_rom_64.vhd")
lib.add_source_files(SRC_PATH / "generated" / "twiddle" / "twiddle_generator_16.vhd")
lib.add_source_files(SRC_PATH / "generated" / "fft1024_wide" / "fft1024_wide_sub64.vhd")
lib.add_source_files(SRC_PATH / "generated" / "fft1024_wide" / "fft1024_wide_sub16.vhd")
lib.add_source_files(SRC_PATH / "generated" / "fft1024_wide" / "fft1024_wide_sub16_2.vhd")
lib.add_source_files(SRC_PATH / "generated" / "fft1024_wide" / "fft1024_wide.vhd")

# Run vunit function
vu.main()
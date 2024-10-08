Module pymake
=============

Functions
---------

`add_assembler_flag(*flags: str)`
:   Adds one or more assembler-specific flags.
    
    Args:
        flags (str): Assembler flags.

`add_compiler_flag(*flags: str)`
:   Adds one or more compiler-specific flags.
    
    Args:
        flags (str): Compiler flags.

`add_extra_arg(*args: str)`
:   Adds one or more extra arguments to the compiler command.
    
    Args:
        args (str): Extra arguments.

`add_includes_directory(*directories: str)`
:   Adds one or more include directories for compilation.
    
    Args:
        directories (str): Paths to the include directories.

`add_library_path(*paths: str)`
:   Adds one or more library search paths.
    
    Args:
        paths (str): Paths to the libraries.

`add_linker_flag(*flags: str)`
:   Adds one or more linker-specific flags.
    
    Args:
        flags (str): Linker flags.

`add_preprocessor_flag(*flags: str)`
:   Adds one or more preprocessor-specific flags.
    
    Args:
        flags (str): Preprocessor flags.

`add_source_file(*file_names: str)`
:   Adds one or more source files for compilation.
    
    Args:
        file_names (str): Names of the source files.

`add_sources_directory(*directories: str)`
:   Adds one or more source directories for compilation.
    
    Args:
        directories (str): Paths to the source directories.

`build(output_file: str = 'output', compiler: str = 'g++', flags: Optional[List[str]] = None, compile_only: bool = False, assembly_only: bool = False, preprocess_only: bool = False)`
:   Compiles the program.
    
    Args:
        output_file (str): Name of the output file.
        compiler (str): Compiler to use.
        flags (list): List of additional compiler flags.
        compile_only (bool): If True, compile and assemble but do not link.
        assembly_only (bool): If True, compile only but do not assemble or link.
        preprocess_only (bool): If True, preprocess only, do not compile, assemble or link.

`define(*macros: str)`
:   Defines one or more macros for compilation.
    
    Args:
        macros (str): Names of the macros.

`link_library(*library_names: str)`
:   Links one or more libraries by name.
    
    Args:
        library_names (str): Names of the libraries.

`run(output_file: str = 'output.exe', args: Optional[List[str]] = None, env: Optional[dict] = None)`
:   Runs the compiled program.
    
    Args:
        output_file (str): Name of the output file.
        args (list, optional): List of arguments to pass to the program.
        env (dict, optional): Dictionary of environment variables to set for the program.

`set_output_directory(directory: str)`
:   Sets the output directory for the compiled binary.
    
    Args:
        directory (str): Directory where the output will be placed.

`set_verbose(verbose: bool)`
:   Enables or disables verbose output.
    
    Args:
        verbose (bool): If True, enables verbose output.



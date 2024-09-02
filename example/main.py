from pymake import *

add_sources_directory("src")
add_includes_directory("inc")

set_verbose(True)

build(compiler="g++")
run()

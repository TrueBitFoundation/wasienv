from setuptools import setup

setup(
    name='wasic',
    description="WASIc is a C/C++ Compiler toolchain for WASI",
    version='0.1.4',
    packages=['wasic'],
    include_package_data=True,
    license="MIT",
    entry_points={'console_scripts': [
        'wasiar = wasic.wasiar:run',
        'wasic = wasic.wasic:run',
        'wasicc = wasic.wasicc:run',
        'wasic++ = wasic.wasicc:run',
        'wasiconfigure = wasic.wasiconfigure:run',
        'wasild = wasic.wasild:run',
        'wasimake = wasic.wasimake:run',
        'wasirun = wasic.wasirun:run',
        'wasinm = wasic.wasinm:run',
        'wasiranlib = wasic.wasiranlib:run',
    ]},
)

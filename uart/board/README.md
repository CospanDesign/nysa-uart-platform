UART Board Folder.

To make your board work with Nysa you need to modify the following files:

config.json
  This describes your board, specifically you must fill out:

  board_nae: DO NOT CHANGE
  vendor: The name of your organization, company, or even yourself!
  host_interface: DO NOT CHANGE
  default_constraint_files: If you would like EVERY project to contain a specific constraint file put the path(s) in this list
    You can also leave this blank and fill in the constraint files within the default.json (default project) and/or required.json What    is required for every project to work
  build_flags: Add any platform specific build flags here
  invert_reset: set to true if you wish to inver the reset pin on the board
  image: Path to a png board image. Used with a GUI, this doesn't need to be set
  clockrate: Clock rate that will be used as the main clock for your board

default.json
  Default project, this is a nice to have for any body trying to use your board
  The following can be filled out or just let the 'required.json' fill out for you

    BASE_DIR: Directory where your output project goes if the use doesn't specifiy another location (Default: "~/projects/ibuilder_project")
    board:uart (Don't change)
    PROJECT_NAME: Name of the project. This is not very important (Default "example_project")
    TEMPLATE: Name of the template to use, currently there is only a wishbone tempalte: (Default: "wishbone_template.json")
    INTERFACE: How the UART will interface between the host device (computer, arduino, etc...) and FPGA this defines the signals
    SLAVES: Slave signals
    MEMORY: Memory bus signals
    bind: Dictionary of bindings of pins to signals such as the clock signal and reset signal
    constraint_files: Constraints that should be included


required.json
  These are values that MUST go on in each project. This usually consists of slaves that should be included on your board. Memory that  should be on your board... etc... If these signals are not specified in the default.json project this file will be used to fill in the missing information


    BASE_DIR: Directory where your output project goes if the use doesn't specifiy another location (Default: "~/projects/ibuilder_project")
    board:uart (Don't change)
    PROJECT_NAME: Name of the project. This is not very important (Default "example_project")
    TEMPLATE: Name of the template to use, currently there is only a wishbone tempalte: (Default: "wishbone_template.json")
    INTERFACE: How the UART will interface between the host device (computer, arduino, etc...) and FPGA this defines the signals
    SLAVES: Slave signals
    MEMORY: Memory bus signals
    bind: Dictionary of bindings of pins to signals such as the clock signal and reset signal
    constraint_files: Constraints that should be included


constraints.json
  An example constraint file that can be used as a starting point for your project

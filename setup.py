import cx_Freeze

executables = [cx_Freeze.Executable("Car_Race_A42346.py")]

cx_Freeze.setup(
    name="CarRace",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["(1).gif"],
                           "include_files":["(2).gif"],
                           "include_files":["(3).gif"],
                           "include_files":["(4).gif"],
                           "include_files":["(5).gif"],
                           "include_files":["(6).gif"],
                           "include_files":["(7).gif"],
                           "include_files":["(8).gif"],
                           "include_files":["(9).gif"],
                           "include_files":["(10).gif"],
                           "include_files":["(11).gif"],
                           "include_files":["(12).gif"],
                           "include_files":["(13).gif"],
                           "include_files":["(14).gif"],
                           "include_files":["(15).gif"],
                           "include_files":["(16).gif"],
                           "include_files":["(17).gif"],
                           "include_files":["(18).gif"],
                           "include_files":["(19).gif"],
                           "include_files":["(20).gif"],
                           "include_files":["(21).gif"],
                           "include_files":["(22).gif"],
                           "include_files":["(23).gif"],
                           "include_files":["(24).gif"],
                           "include_files":["(25).gif"],
                           "include_files":["(26).gif"],
                           "include_files":["(27).gif"],
                           "include_files":["(28).gif"],
                           "include_files":["carro.png"],
                           "include_files":["carro2.png"],
                           "include_files":["car.mp3"],
                           "include_files":["circuit.jpg"],

                           }},
    executables = executables

    )

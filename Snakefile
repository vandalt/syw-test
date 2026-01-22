rule simulation:
    output:
        "src/data/simulation.dat"
    cache:
        True
    script:
        "src/scripts/simulation.py"

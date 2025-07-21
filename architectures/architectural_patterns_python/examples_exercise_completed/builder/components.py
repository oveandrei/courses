# components.py

"""
Dictionary of allowed PC components for use in the CLI builder.
Each key maps to a list of valid options.
"""

COMPONENTS = {
    "CPU": ["I9", "RYZEN 9", "I5", "RYZEN 5"],
    "RAM": ["16GB", "32GB", "64GB"],
    "GPU": ["RTX 3070", "RTX 4090", "RX 7900"],
    "STORAGE": ["500GB SSD", "1TB SSD", "2TB HDD"]
}

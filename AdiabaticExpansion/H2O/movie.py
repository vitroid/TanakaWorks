import gromacs2
import pathlib
import numpy as np

name = "/u/tanaka/r7/lhdl/mdn/100kkm/nev/ht"
cell = np.diag([46.37, 46.37, 46.37 * 5]) / 10  # nm

outfile = open("h2o.gro", "w")

root_directory = pathlib.Path(name)
for path_object in sorted(root_directory.rglob("fort.1[0-9][0-9][0-9]*")):
    if path_object.is_file():
        print(path_object)
        with open(path_object) as f:
            atoms = []
            f.readline()
            for line in f.readlines():
                cols = line.split()[1:]
                atoms.append([float(x) for x in cols])
            atoms = np.array(atoms).reshape(-1, 3) / 10  # nm
            frame = gromacs2.Frame(
                position=atoms,
                atom_name=["O", "H","H"] * (atoms.shape[0] // 3),
                atom_id=np.arange(atoms.shape[0]) + 1,
                cell=cell,
                residue_name=["water"] * atoms.shape[0],
                residue_id=np.arange(atoms.shape[0]) // 3 + 1,
            )
            frame.write_gro(outfile)
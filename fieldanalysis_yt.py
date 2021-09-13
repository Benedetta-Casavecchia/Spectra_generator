def fieldanalysis_yt(file_name, input_directory):
    rho, prs, tr1, vx1, vx2, vx3, temp = pload_vtk(file_name, input_directory)
    
    rho   = rho.reshape(96,192,96)
    temp  = temp.reshape(96,192,96)
    metal = np.full((96,192,96), 1)
    velx  = vx1.reshape(96,192,96)
    vely  = vx2.reshape(96,192,96)
    velz  = vx3.reshape(96,192,96)

    print(np.min(velx), np.max(velx))
    print(np.shape(velx))

    #data = dict(density = rho, temperature = temp, metallicity = metal, velocity_x = velx, velocity_y = vely, velocity_z = velz)
    data = {('gas','density'): (rho, "g/cm**3"), ('gas','velocity_x'): (velx, 'cm/s'),\
           ('gas','velocity_y'): (vely, 'cm/s'), ('gas','velocity_z'): (velz, 'cm/s'),\
           ('gas', 'temperature'): (temp, "K"), ('gas', 'metallicity'): (metal, 'Zsun')}
    bbox = np.array([[-6, 6], [-2, 22], [-6, 6]])

    ds = yt.load_uniform_grid(data, rho.shape, length_unit=3.086e+19, mass_unit = (3.086e+19)**3, bbox=bbox, nprocs=1)
    print(rho.shape)
    #print(ds.field_info["gas", "temperature"].get_units())

    #GENERATE TEMPERATURE MAP
    slc = yt.SlicePlot(ds, "z", ["temperature"])
    slc.set_cmap("temperature", "Blues")
    slc.annotate_grids(cmap=None)
    slc.show()
    
    #GENERATE DENSITY MAP
    slc = yt.SlicePlot(ds, "z", ["density"])
    slc.set_cmap("density", "Blues")
    slc.annotate_grids(cmap=None)
    slc.show()
    
    return ds

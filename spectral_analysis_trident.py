def spectral_analysis_trident(file_name, input_directory, output_directory, ds, tstep):
    trident.add_ion_fields(ds, ions=['C', 'Fe', 'H', 'N', 'Ne', 'O', 'Mg', 'S', 'Si'])
    #[field for field in ds.derived_field_list if field[0] == 'gas' and field[1].startswith('H_')]
    ad = ds.all_data()
    
    #CARBON
    
    #number density
    print(tstep)

    CII_p  = yt.ProjectionPlot(ds, "z", "C_p1_number_density")
    CIII_p = yt.ProjectionPlot(ds, "z", "C_p2_number_density")
    CIV_p  = yt.ProjectionPlot(ds, "z", "C_p3_number_density")
    
    print('ciao')
    print(output_directory + 'C_rad'+ str(tstep) +'/')
    
    CII_p.save()
    CIII_p.save(output_directory + 'C_rad'+ str(tstep) +'/')
    CIV_p.save(output_directory + 'C_rad'+ str(tstep) +'/')
    
    #2d plot
    CII_phase  = yt.PhasePlot(ad, "density", "temperature", ["C_p1_mass"],
                     weight_field="C_p1_mass", fractional=True)
    CIII_phase = yt.PhasePlot(ad, "density", "temperature", ["C_p2_mass"],
                     weight_field="C_p2_mass", fractional=True)
    CIV_phase  = yt.PhasePlot(ad, "density", "temperature", ["C_p3_mass"],
                     weight_field="C_p3_mass", fractional=True)
    
    CII_phase.save(output_directory + 'C_rad'+ str(tstep) +'/')
    CIII_phase.save(output_directory + 'C_rad'+ str(tstep) +'/')
    CIV_phase.save(output_directory + 'C_rad'+ str(tstep) +'/')
    
    #HYDROGEN
    
    #number density
    HI_p  = yt.ProjectionPlot(ds, "z", "H_p0_number_density")
    HII_p = yt.ProjectionPlot(ds, "z", "H_p1_number_density")
    
    HI_p.save(output_directory + 'H_rad'+ str(tstep) +'/')
    HII_p.save(output_directory + 'H_rad'+ str(tstep) +'/')
    
    #2d plots
    HI_phase  = yt.PhasePlot(ad, "density", "temperature", ["H_p0_mass"],
                     weight_field="H_p0_mass", fractional=True)
    HII_phase = yt.PhasePlot(ad, "density", "temperature", ["H_p1_mass"],
                     weight_field="H_p1_mass", fractional=True)
    
    HI_phase.save(output_directory + 'H_rad'+ str(tstep) +'/')
    HII_phase.save(output_directory + 'H_rad'+ str(tstep) +'/')
    
    #IRON
    
    #number density
    FeII_p   = yt.ProjectionPlot(ds, "z", "Fe_p1_number_density")
    FeIII_p  = yt.ProjectionPlot(ds, "z", "Fe_p2_number_density")
    
    FeII_p.save(output_directory + 'Fe_rad'+ str(tstep) +'/')
    FeIII_p.save(output_directory + 'Fe_rad'+ str(tstep) +'/')
    
    #MAGNESIUM
    
    #number density
    MgII_p   = yt.ProjectionPlot(ds, "z", "Mg_p1_number_density")
    
    MgII_p.save(output_directory + 'Mg_rad'+ str(tstep) +'/')
    
    #NITROGEN
    
    #number density
    NI_p     = yt.ProjectionPlot(ds, "z", "N_p0_number_density")
    NII_p    = yt.ProjectionPlot(ds, "z", "N_p1_number_density")
    NIII_p   = yt.ProjectionPlot(ds, "z", "N_p2_number_density")
    NIV_p    = yt.ProjectionPlot(ds, "z", "N_p3_number_density")
    NV_p     = yt.ProjectionPlot(ds, "z", "N_p4_number_density")
    
    NI_p.save(output_directory + 'N_rad'+ str(tstep) +'/')
    NII_p.save(output_directory + 'N_rad'+ str(tstep) +'/')
    NIII_p.save(output_directory + 'N_rad'+ str(tstep) +'/')
    NIV_p.save(output_directory + 'N_rad'+ str(tstep) +'/')
    NV_p.save(output_directory + 'N_rad'+ str(tstep) +'/')
    
    #NEON
    
    #number density
    NeII_p   = yt.ProjectionPlot(ds, "z", "Ne_p1_number_density")
    NeIII_p  = yt.ProjectionPlot(ds, "z", "Ne_p2_number_density")
    NeIV_p   = yt.ProjectionPlot(ds, "z", "Ne_p3_number_density")
    NeVI_p   = yt.ProjectionPlot(ds, "z", "Ne_p5_number_density")
    
    NeII_p.save(output_directory + 'Ne_rad'+ str(tstep) +'/')
    NeIII_p.save(output_directory + 'Ne_rad'+ str(tstep) +'/')
    NeIV_p.save(output_directory + 'Ne_rad'+ str(tstep) +'/')
    NeVI_p.save(output_directory + 'Ne_rad'+ str(tstep) +'/')
    
    #OXIGEN
    
    #number density
    OI_p     = yt.ProjectionPlot(ds, "z", "O_p0_number_density")
    OII_p    = yt.ProjectionPlot(ds, "z", "O_p1_number_density")
    OIII_p   = yt.ProjectionPlot(ds, "z", "O_p2_number_density")
    OIV_p    = yt.ProjectionPlot(ds, "z", "O_p3_number_density")
    OV_p     = yt.ProjectionPlot(ds, "z", "O_p4_number_density")
    OVI_p    = yt.ProjectionPlot(ds, "z", "O_p5_number_density")
    
    OI_p.save(output_directory + 'O_rad'+ str(tstep) +'/')
    OII_p.save(output_directory + 'O_rad'+ str(tstep) +'/')
    OIII_p.save(output_directory + 'O_rad'+ str(tstep) +'/')
    OIV_p.save(output_directory + 'O_rad'+ str(tstep) +'/')
    OV_p.save(output_directory + 'O_rad'+ str(tstep) +'/')
    OVI_p.save(output_directory + 'O_rad'+ str(tstep) +'/')
    
    #SULPHUR
    
    #number density
    SII_p    = yt.ProjectionPlot(ds, "z", "S_p1_number_density")
    SIII_p   = yt.ProjectionPlot(ds, "z", "S_p2_number_density")
    SIV_p    = yt.ProjectionPlot(ds, "z", "S_p3_number_density")
    SVI_p    = yt.ProjectionPlot(ds, "z", "S_p5_number_density")
    
    SII_p.save(output_directory + 'S_rad'+ str(tstep) +'/')
    SIII_p.save(output_directory + 'S_rad'+ str(tstep) +'/')
    SIV_p.save(output_directory + 'S_rad'+ str(tstep) +'/')
    SVI_p.save(output_directory + 'S_rad'+ str(tstep) +'/')
    
    #SILICUM
    
    #number density
    SiII_p   = yt.ProjectionPlot(ds, "z", "Si_p1_number_density")
    SiIII_p  = yt.ProjectionPlot(ds, "z", "Si_p2_number_density")
    SiIV_p   = yt.ProjectionPlot(ds, "z", "Si_p3_number_density")
    
    SiII_p.save(output_directory + 'Si_rad'+ str(tstep) +'/')
    SiIII_p.save(output_directory + 'Si_rad'+ str(tstep) +'/')
    SiIV_p.save(output_directory + 'Si_rad'+ str(tstep) +'/')

def spectra(output_directory, ds, tstep, simultype, orient, ray_start, ray_end):
    ray_start = ds.domain_left_edge  #ray_start
    ray_end   = ds.domain_right_edge #ray_end
    
    print(ray_start)
    
    #CARBON
    
    #spectrum
    
    line_list_C = ['C II', 'C III', 'C IV']
    rayC = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayC.h5",\
lines=line_list_C, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayC, arrow=True)
    #print(output_directory + 'C'+ simultype[0] +'/projectionC' + orient + simultype[0] + str(tstep) + '.png')
    p.save(output_directory + 'C'+ simultype[0] +'/projectionC' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayC, lines=line_list_C)
    sg.save_spectrum(output_directory + 'C' + simultype[0] + '/spec_rawC' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'C' + simultype[0] + '/spec_rawC' + orient + str(tstep) + '.png')
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'C' + simultype[0] + '/spec_raw1C' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayC.h5", lines=line_list_C)
    sg.plot_spectrum(output_directory + 'C' + simultype[0] + '/spec_velocityC' + orient + str(tstep) + '.png')
        
    #HYDROGEN
    
    #spectrum
    
    line_list_H = ['H I', 'H II']
    rayH = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayH.h5",\
    lines=line_list_H, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayH, arrow=True)
    p.save(output_directory + 'H' + simultype[0] + '/projectionH' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayH, lines=line_list_H)
    sg.save_spectrum(output_directory + 'H' + simultype[0] + '/spec_rawH' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'H' + simultype[0] + '/spec_rawH' + orient + str(tstep) + '.png')
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'H' + simultype[0] + '/spec_raw1H' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayH.h5", lines=line_list_H)
    sg.plot_spectrum(output_directory + 'H' + simultype[0] + '/spec_velocityH' + orient + str(tstep) + '.png')
    
    #IRON
    
    #spectrum
    
    line_list_Fe = ['Fe II', 'Fe III']
    rayFe = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayFe.h5",\
    lines=line_list_Fe, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayFe, arrow=True)
    p.save(output_directory + 'Fe' + simultype[0] +'/projectionFe' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayFe, lines=line_list_Fe)
    sg.save_spectrum(output_directory + 'Fe' + simultype[0] + '/spec_rawFe' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'Fe' + simultype[0] + '/spec_rawFe' + orient + str(tstep) + '.png')
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'Fe' + simultype[0] + '/spec_raw1Fe' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayFe.h5", lines=line_list_Fe)
    sg.plot_spectrum(output_directory + 'Fe' + simultype[0] + '/spec_velocityFe' + orient + str(tstep) + '.png')

    #MAGNESIUM
    
    #spectrum
       
    line_list_Mg = ['Mg II']
    rayMg = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayMg.h5",\
    lines=line_list_Mg, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayMg, arrow=True)
    p.save(output_directory + 'Mg' + simultype[0] + '/projectionMg' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayMg, lines=line_list_Mg)
    sg.save_spectrum(output_directory + 'Mg' + simultype[0] + '/spec_rawMg' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'Mg' + simultype[0] + '/spec_rawMg' + orient + str(tstep) + '.png')
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'Mg' + simultype[0] + '/spec_raw1Mg' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayMg.h5", lines=line_list_Mg)
    sg.plot_spectrum(output_directory + 'Mg' + simultype[0] + '/spec_velocityMg' + orient + str(tstep) + '.png')
    
    #NITROGEN
    
    #spectrum

    line_list_N = ['N I', 'N II', 'N III', 'N IV', 'N V']
    rayN = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayN.h5",\
    lines=line_list_N, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayN, arrow=True)
    p.save(output_directory + 'N' + simultype[0] + '/projectionN' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayN, lines=line_list_N)
    sg.save_spectrum(output_directory + 'N' + simultype[0] + '/spec_rawN' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'N' + simultype[0] + '/spec_rawN' + orient + str(tstep) + '.png')
    print(sg)
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'N' + simultype[0] + '/spec_raw1N' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayN.h5", lines=line_list_N)
    sg.plot_spectrum(output_directory + 'N' + simultype[0] + '/spec_velocityN' + orient + str(tstep) + '.png')
    
    #NEON
    
    #spectrum
    
    line_list_Ne = ['Ne II', 'Ne III', 'Ne IV', 'Ne VI']
    rayNe = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayNe.h5",\
    lines=line_list_Ne, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayNe, arrow=True)
    p.save(output_directory + 'Ne' + simultype[0] +'/projectionNe' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayNe, lines=line_list_Ne)
    sg.save_spectrum(output_directory + 'Ne' + simultype[0] + '/spec_rawNe' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'Ne' + simultype[0] + '/spec_rawNe' + orient + str(tstep) + '.png')
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'Ne' + simultype[0] + '/spec_raw1Ne' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayNe.h5", lines=line_list_Ne)
    sg.plot_spectrum(output_directory + 'Ne' + simultype[0] + '/spec_velocityNe' + orient + str(tstep) + '.png')
    
    #OXIGEN
    
    #spectrum
    
    line_list_O = ['O I', 'O II', 'O III', 'O IV', 'O V', 'O IV']
    rayO = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayO.h5",\
    lines=line_list_O, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayO, arrow=True)
    p.save(output_directory + 'O' + simultype[0] + '/projectionO' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayO, lines=line_list_O)
    sg.save_spectrum(output_directory + 'O' + simultype[0] + '/spec_rawO' + orient + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'O' + simultype[0] + '/spec_rawO' + orient + str(tstep) + '.png')
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'O' + simultype[0] + '/spec_raw1O' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayO.h5", lines=line_list_O)
    sg.plot_spectrum(output_directory + 'O' + simultype[0] + '/spec_velocityO' + orient + str(tstep) + '.png')
    
    #SULPHUR
    
    #spectrum
    
    line_list_S = ['S II', 'S III', 'S IV', 'S VI']
    rayS = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="rayS.h5",\
    lines=line_list_S, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(rayS, arrow=True)
    p.save(output_directory + 'S' + simultype[0] + '/projectionS' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(rayS, lines=line_list_S)
    sg.save_spectrum(output_directory + 'S' + simultype[0] + '/spec_rawS' + orient + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'S' + simultype[0] + '/spec_rawS' + orient + str(tstep) + '.png')
    print(sg)
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'S' + simultype[0] + '/spec_raw1S' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("rayS.h5", lines=line_list_S)
    sg.plot_spectrum(output_directory + 'S' + simultype[0] + '/spec_velocityS' + orient + str(tstep) + '.png')
    
    #SILICUM
    
    #spectrum
    
    line_list_Si = ['Si II', 'Si III', 'Si IV']
    raySi = trident.make_simple_ray(ds, start_position=ray_start, end_position=ray_end, data_filename="raySi.h5",\
    lines=line_list_Si, ftype="gas", redshift=0)
    
    p = yt.ProjectionPlot(ds, 'x', ('gas','density'))
    p.annotate_ray(raySi, arrow=True)
    p.save(output_directory + 'Si' + simultype[0] + '/projectionSi' + orient + simultype[0] + str(tstep) + '.png')
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto', dlambda=0.1)
    sg.make_spectrum(raySi, lines=line_list_Si)
    sg.save_spectrum(output_directory + 'Si' + simultype[0] + '/spec_rawSi' + orient + str(tstep) + '.txt')
    sg.plot_spectrum(output_directory + 'Si' + simultype[0] + '/spec_rawSi' + orient + str(tstep) + '.png')
    print(sg)
    
    sg.add_qso_spectrum(emitting_redshift=0.1)
    sg.add_gaussian_noise(30)
    sg.plot_spectrum(output_directory + 'Si' + simultype[0] + '/spec_raw1Si' + orient + str(tstep) + '.png')
    
    #velocity space
    
    sg = trident.SpectrumGenerator(lambda_min='auto', lambda_max='auto',
                               dlambda=1., bin_space='velocity')
    sg.make_spectrum("raySi.h5", lines=line_list_Si)
    sg.plot_spectrum(output_directory + 'Si' + simultype[0] + '/spec_velocitySi' + orient + str(tstep) + '.png')

from PythonTasksScripts.csvFunc import processFile
from PythonTasksScripts.generate_pdf import getData
from PythonTasksScripts.genZip import zip_folder

async def ProcessData(eventname, orgname, certType, certificate_choice, oprchoice, csvPath, logo1Path, logo2Path, organizer1_designation, organizer1Path, organizer2_designation, organizer2Path):  # which get data from operated csv files:
    
    csvData = []
    csvData = processFile(f"{csvPath}")
    finalTemplatePath = f""

    from PythonTasksScripts.getPath import get_Choice_data

    from PythonTasksScripts.redesignTemplate import templatedesign1_2_3, templatedesign4, templatedesign5
    match oprchoice:

        case "Generate":
            if certificate_choice == "Choice1":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice2":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice3":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice4":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign4(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)
            
            if certificate_choice == "Choice5":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign5(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)


            i=0
            for CSV in csvData:
                    i+=1
                    await getData(CSV.name, CSV.sId, CSV.emailId, CSV.course, CSV.semester, CSV.date, i, eventname, orgname, certType, certificate_choice, oprchoice, organizer1_designation, organizer2_designation, finalTemplatePath)

            zip_folder(f"./static/PDFFolder", f"./static/{oprchoice}Certificate.zip")


        case "Preview":
            if certificate_choice == "Choice1":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)
                
            if certificate_choice == "Choice2":
                pathkey = get_Choice_data(certificate_choice)
                print(f"path:{pathkey}")
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice3":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign1_2_3(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice4":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign4(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)

            if certificate_choice == "Choice5":
                pathkey = get_Choice_data(certificate_choice)
                finalTemplatePath = templatedesign5(pathkey["TemplatePath"], logo1Path, logo2Path, pathkey["linepath"], organizer1Path, organizer2Path)
            
            
            i=0
            for CSV in csvData:
                    i+=1
                    await getData(CSV.name, CSV.sId, CSV.emailId, CSV.course, CSV.semester, CSV.date, i, eventname, orgname, certType, certificate_choice, oprchoice, organizer1_designation, organizer2_designation, finalTemplatePath)
                    if i == 1:
                        break        

    print(f"\nThere are {i} rows of data in given csv file.\n")
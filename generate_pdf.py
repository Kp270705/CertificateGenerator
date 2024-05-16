from fpdf import FPDF
import os
import shutil
import datetime as dt

FONTS = {
        # poppins:
        "Poppins" :  {
            "poppinsExtraBold":f"/usr/share/fonts/truetype/Poppins/Poppins-ExtraBold.ttf",
            "poppinsBold":f"/usr/share/fonts/truetype/Poppins/Poppins-Bold.ttf",
            "poppinsMedium":f"/usr/share/fonts/truetype/Poppins/Poppins-Medium.ttf",
            "poppinsLight":f"/usr/share/fonts/truetype/Poppins/Poppins-Light.ttf",
            "poppinsExtraLight":f"/usr/share/fonts/truetype/Poppins/Poppins-ExtraLight.ttf",
            "poppinsRegular":f"/usr/share/fonts/truetype/Poppins/Poppins-Regular.ttf",
            "poppinsSemiBold":f"/usr/share/fonts/truetype/Poppins/Poppins-SemiBold.ttf"
        },

        # MontSerrat:
        "Montserrat" : {
            "MontserratBlack": f"/usr/share/fonts/truetype/Montserrat/Montserrat-Black.ttf",
            "MontserratBold" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-Bold.ttf",
            "MontserratExtraBold" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-ExtraBold.ttf",
            "MontserratSemiBold" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-SemiBold.ttf",
            "MontserratExtraLight" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-ExtraLight.ttf",
            "MontserratLight" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-Light.ttf",
            "MontserratMedium" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-Medium.ttf",
            "MontserratRegular" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-Regular.ttf",
            "MontserratThin" : f"/usr/share/fonts/truetype/Montserrat/Montserrat-Thin.ttf"
        }


}

def add_spacing(input_string, spacing):
    """
    Add spacing between characters in a string.

    Args:
    input_string (str): The input string.
    spacing (int): The number of spaces to add between characters.

    Returns:
    str: The input string with spacing added between characters.
    """
    spaced_string = ""
    for char in input_string:
        spaced_string += char + " " * spacing
    return spaced_string

class PDF(FPDF):
    
    def header(self):
        # Add logo or header here if needed
        pass
    
    def footer(self):
        # Add footer here if needed
        pass     
        
# certificate design1:-        
    def certificate1(self, name, sId, course, sem, eventname, orgname, certificateChoice, templatePath, logoPath, logo2Path, ccPath, hodPath, opertype):
        print(f"in {certificateChoice}")
        date= dt.date.today()
        
        # Add page with landscape orientation
        self.add_page(orientation="L")
        
        w = self.w
        h = self.h
        
        from redesignTemplate import templatedesign

        if certificateChoice == "Choice1":
            linepath = f"./static/Images/CertificateEssentials/line1.png"
            text_color= 220
            print(f"\t\t(in gen pdf)hod path is: {hodPath}")
            finalTemplatePath = templatedesign(templatePath, logoPath, logo2Path, linepath, ccPath, hodPath)

        if certificateChoice == "Choice3":
            linepath = f"./static/Images/CertificateEssentials/line1b.png"
            text_color = 0
            print(f"\t\t(in gen pdf)hod path is: {hodPath}")
            finalTemplatePath = templatedesign(templatePath, logoPath, logo2Path, linepath, ccPath, hodPath)

        print(f"\t\t\t{opertype} template generated. 👌 ")
        
        self.image(f"{finalTemplatePath}", 0, 0, w, h)

        # Calculate margins and text width for centering (optional)
        left_margin = 20  # Adjust this value for desired left padding
        right_margin = self.w - left_margin  # Calculate right margin based on page width

        #adding fonts:        

        # poppins:
        self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # montserrat:
        self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )

        # Set font
        self.ln(30)
        # self.section1 = f"C E R T I F I C A T E\n"
        sec1 = f"CERTIFICATE"
        # spacedSection1 = add_spacing(sec1, 1)
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Bold", size=38, style="B")
        self.set_text_color(text_color)
        self.multi_cell(270, 8, txt=self.section1, align='C')
        self.ln(4)
        print(f"\n\t1st heading created...")
        
        sec2 = f"OF PARTICIPATION"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font(f"Montserrat-Medium", size=28)
        self.multi_cell(277, 8, txt=self.section2, align='C')
        self.ln(3)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        # spacedSection3 = add_spacing(sec3, 2)
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 20, txt=self.section3, align='C')
        self.ln(5)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"

        self.set_font("Montserrat-Bold", size=30, style="UB")
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        print(f"course in cer: {spacedSection5a}")
        self.section5 = f"{spacedSection5a}                     {spacedSection5b}"
        self.set_font("Montserrat-Black", size=18, style="")
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(10)
        
        # self.section6 = f"F O R   P A R T I C I P A T I N G  I N"
        sec6 = f"FOR  PARTICIPATING  IN"
        # spacedSection6 = add_spacing(sec6, 2)
        self.section6 = f"{sec6}"
        # self.set_font("Poppins-Bold", size=16, style="B")
        self.set_font("Montserrat-Regular", size=18)
        self.multi_cell(277, 8, txt=self.section6, align='C')
        self.ln(10)

        spacedSection7 = add_spacing(eventname.upper(), 1)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 7, txt=self.section7, align='C')
        self.ln(2)

        sec8 = f"ON"
        spacedSection8 = add_spacing(sec8, 2)
        self.section8 = f"{spacedSection8}"
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 7, txt=self.section8, align='C')

        self.section9 = f"{date}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 10, txt=self.section9, align='C')
        self.ln(21)  # Add some space after title

        auth1 = f"C.C."
        auth2 = f"H.O.D."
        spacedSection10a = add_spacing(auth1.upper(), 1)
        spacedSection10b = add_spacing(auth2.upper(), 1)
        self.section10 = f"{spacedSection10a}                   {spacedSection10b}"
        self.set_font("Montserrat-SemiBold", size=18, style="B")
        self.set_left_margin(95)
        self.cell(80, 3, txt=f"{spacedSection10a}", align='L')
        self.set_left_margin(50)
        self.cell(50, 3, txt=f"{spacedSection10b}", align='L')

        print(f"Certificate generated successfully...")

# --------------------------------------------------------------------------     
     
    #  design2   
    def certificate2(self, name, sId, course, sem, eventname, orgname, certificateChoice, templatePath, logoPath, ccPath, hodPath, opertype):
        print(f"in {certificateChoice}")
        date= dt.date.today()

        # Add page with landscape orientation
        self.add_page(orientation="L")
        
        w = self.w
        h = self.h

        from redesignTemplate import templatedesign2
        
        finalTemplatePath = templatedesign2(templatePath, logoPath, ccPath, hodPath)
        print(f"\t\t\t{opertype} template generated. 👌 ")

        self.image(f"{finalTemplatePath}", 0, 0, w, h)

        # Calculate margins and text width for centering (optional)
        left_margin = 20  # Adjust this value for desired left padding
        right_margin = self.w - left_margin  # Calculate right margin based on page width

        # adding fonts:

        # poppins:
        self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # montserrat:
        self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )

        
        self.ln(96)

        spacedSection4 = add_spacing(name.upper(),0)
        self.section4 = f"{spacedSection4}"
        self.set_font("Montserrat-Bold", size=30, style="B")
        # self.set_font("Poppins-Bold", size=30, style="B")
        self.set_text_color(0,0,0)
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(4)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        print(f"course in cer: {spacedSection5a}")
        self.section5 = f"{spacedSection5a}            {spacedSection5b}"
        self.set_font("Montserrat-Black", size=18, style="")
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(1)
        
        self.section6 = f"FOR  PARTICIPATING  IN"
        self.set_font("Montserrat-Regular", size=15)
        self.multi_cell(277, 12, txt=self.section6, align='C')
        self.ln(1)

        spacedSection7 = add_spacing(eventname.upper(), 1)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-ExtraBold", size=16, style="B")
        self.multi_cell(277, 7, txt=self.section7, align='C')
        self.ln(2)

        self.section8 = f"O N"
        self.set_font("Arial", size=15)
        self.multi_cell(277, 7, txt=self.section8, align='C')
        self.ln(1)

        self.section9 = f"{date}"
        self.set_font("Arial", size=16, style="B")
        self.multi_cell(277, 10, txt=self.section9, align='C')
        self.ln(16)  # Add some space after title
        
        self.section10 = f"HEAD OF DEPARTMENT"
        self.section10 = f"H. O. D."
        self.set_left_margin(60)
        self.set_font("Arial", size=14, style="B")
        self.cell(100, 10, txt=self.section10, align="C")
        
        self.section10 = f"C. C."
        self.set_left_margin(180)
        self.set_font("Arial", size=14, style="B")
        self.cell(180, 10, txt=self.section10, align="L")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def certificate3(self, name, sId, course, sem, eventname, orgname, certificateChoice, templatePath, logoPath, logo2Path, ccPath, hodPath, opertype):
        print(f"in {certificateChoice}")
        date= dt.date.today()
        
        # Add page with landscape orientation
        self.add_page(orientation="L")
        
        w = self.w
        h = self.h
        
        from redesignTemplate import templatedesign
        linepath = f"./static/Images/CertificateEssentials/line1b.png"
        finalTemplatePath = templatedesign(templatePath, logoPath, logo2Path, linepath, ccPath, hodPath)

        print(f"\t\t\t{opertype} template generated. 👌 ")
        
        self.image(f"{finalTemplatePath}", 0, 0, w, h)


        left_margin = 20  
        right_margin = self.w - left_margin  

        #adding fonts:        
        # poppins:
        self.add_font('Poppins-ExtraBold', "B", f"{FONTS['Poppins']['poppinsExtraBold']}" , uni=True)
        self.add_font('Poppins-Bold', "B", f"{FONTS['Poppins']['poppinsBold']}" , uni=True)
        self.add_font('Poppins-Medium', "", f"{FONTS['Poppins']['poppinsMedium']}" , uni=True)
        self.add_font('Poppins-Light', "", f"{FONTS['Poppins']['poppinsExtraLight']}" , uni=True)
        self.add_font('Poppins-ExtraLight', "", f"{FONTS['Poppins']['poppinsLight']}" , uni=True)
        self.add_font('Poppins-Regular', "", f"{FONTS['Poppins']['poppinsRegular']}" , uni=True)
        self.add_font('Poppins-SemiBold', "B", f"{FONTS['Poppins']['poppinsSemiBold']}" , uni=True)

        # montserrat:
        self.add_font("Montserrat-Black", "", f"{FONTS['Montserrat']['MontserratBlack']}", uni=1 )
        self.add_font("Montserrat-Bold", "B", f"{FONTS['Montserrat']['MontserratBold']}", uni=1 )
        self.add_font("Montserrat-SemiBold", "B", f"{FONTS['Montserrat']['MontserratSemiBold']}", uni=1 )
        self.add_font("Montserrat-ExtraBold", "B", f"{FONTS['Montserrat']["MontserratExtraBold"]}", uni=1 )
        self.add_font("Montserrat-Regular", "", f"{FONTS['Montserrat']["MontserratRegular"]}", uni=1 )
        self.add_font("Montserrat-Thin", "", f"{FONTS['Montserrat']["MontserratThin"]}", uni=1 )
        self.add_font("Montserrat-Medium", "", f"{FONTS['Montserrat']["MontserratMedium"]}", uni=1 )

        # Set font
        self.ln(30)
        # self.section1 = f"C E R T I F I C A T E\n"
        sec1 = f"CERTIFICATE"
        # spacedSection1 = add_spacing(sec1, 1)
        self.section1 = f"{sec1}"
        self.set_font("Montserrat-Bold", size=38, style="B")
        self.set_text_color(0)
        self.multi_cell(270, 8, txt=self.section1, align='C')
        self.ln(4)
        print(f"\n\t1st heading created...")
        
        sec2 = f"OF PARTICIPATION"
        spacedSection2 = add_spacing(sec2, 1)
        self.section2 = f"{spacedSection2}"
        self.set_font(f"Montserrat-Medium", size=28)
        
        self.multi_cell(277, 8, txt=self.section2, align='C')
        self.ln(3)
        
        sec3 = f"IS  PROUDLY  PRESENTED  TO"
        # spacedSection3 = add_spacing(sec3, 2)
        self.section3 = f"{sec3}"
        self.set_font("Montserrat-Regular", size=15)
        
        self.multi_cell(277, 20, txt=self.section3, align='C')
        self.ln(5)
        
        spacedSection4 = add_spacing(name.upper(), 1)
        self.section4 = f"{spacedSection4}"

        self.set_font("Montserrat-Bold", size=30, style="UB")
        
        self.multi_cell(277, 5, txt=self.section4, align='C')
        self.ln(6)

        spacedSection5a = add_spacing(course.upper(), 2)
        spacedSection5b = add_spacing(sem.upper(), 2)
        print(f"course in cer: {spacedSection5a}")
        self.section5 = f"{spacedSection5a}                     {spacedSection5b}"
        
        self.set_font("Montserrat-Black", size=18, style="")
        self.multi_cell(277, 10, txt=self.section5, align='C')
        self.ln(10)
        
        # self.section6 = f"F O R   P A R T I C I P A T I N G  I N"
        sec6 = f"FOR  PARTICIPATING  IN"
        # spacedSection6 = add_spacing(sec6, 2)
        self.section6 = f"{sec6}"
        
        # self.set_font("Poppins-Bold", size=16, style="B")
        self.set_font("Montserrat-Regular", size=18)
        self.multi_cell(277, 8, txt=self.section6, align='C')
        self.ln(10)

        spacedSection7 = add_spacing(eventname.upper(), 1)
        self.section7 = f"{spacedSection7}"
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        
        self.multi_cell(277, 7, txt=self.section7, align='C')
        self.ln(2)

        sec8 = f"ON"
        spacedSection8 = add_spacing(sec8, 2)
        self.section8 = f"{spacedSection8}"
        
        self.set_font("Poppins-Regular", size=13)
        self.multi_cell(277, 7, txt=self.section8, align='C')

        self.section9 = f"{date}"
        
        self.set_font("Poppins-ExtraBold", size=18, style="B")
        self.multi_cell(277, 10, txt=self.section9, align='C')
        self.ln(21)  # Add some space after title

        auth1 = f"C.C."
        auth2 = f"H.O.D."
        spacedSection10a = add_spacing(auth1.upper(), 1)
        spacedSection10b = add_spacing(auth2.upper(), 1)
        self.section10 = f"{spacedSection10a}                   {spacedSection10b}"
        self.set_font("Montserrat-SemiBold", size=18, style="B")
        self.set_left_margin(95)
        self.cell(80, 3, txt=f"{spacedSection10a}", align='L')
        self.set_left_margin(50)
        self.cell(50, 3, txt=f"{spacedSection10b}", align='L')

        print(f"Certificate generated successfully...")

# --------------------------------------------------------------------------     

        

def getData(name, sId, Duration, pulse, maxPulse, calories, course, sem, i, eventname, orgName, certificateChoice, opertype, logoPath):
    print(f"i={i}")
    
    # Create PDFFolder if it doesn't exist
    if i == 1:
        if os.path.exists("./static/PDFFolder"):
            shutil.rmtree("./static/PDFFolder")
            
        os.mkdir("./static/PDFFolder")
                
    pdf = PDF()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.set_top_margin(10)
    pdf.set_auto_page_break(auto=True, margin=15)
    
    if certificateChoice == "Choice1":
        TemplatePath = f"./static/Images/CertificateEssentials/certBg.jpg"
        ccPath = f"./static/Images/CertificateEssentials/ccWhite.png"
        hodPath = f"./static/Images/CertificateEssentials/hodWhite.png"
        logo2Path = f"./static/Images/CertificateEssentials/TechGeeksLogo.png"
        pdf.certificate1(name, sId, course, sem, eventname, orgName, certificateChoice, TemplatePath, logoPath, logo2Path, ccPath, hodPath, opertype)
        print(f"course: {course}")
        
    if certificateChoice == "Choice2":
        TemplatePath = f"./static/Images/CertificateEssentials/Artboard.jpg"
        ccPath = f"./static/Images/CertificateEssentials/cc.png"
        hodPath = f"./static/Images/CertificateEssentials/hod.png"
        logoPath = f"./static/Images/CertificateEssentials/TechGeeksLogo.png"
        pdf.certificate2(name, sId, course, sem, eventname, orgName, certificateChoice, TemplatePath, logoPath, ccPath, hodPath, opertype)
    
    if certificateChoice == "Choice3":
        TemplatePath = f"./static/Images/CertificateEssentials/template5.png"
        ccPath = f"./static/Images/CertificateEssentials/cc.png"
        hodPath = f"./static/Images/CertificateEssentials/hod.png"
        logo2Path = f"./static/Images/CertificateEssentials/TechGeeksLogoColor.png"
        pdf.certificate3(name, sId, course, sem, eventname, orgName, certificateChoice, TemplatePath, logoPath, logo2Path, ccPath, hodPath, opertype)
        print(f"success")

    pdf.output(f"./static/PDFFolder/{opertype}Certificate{i}.pdf")
    


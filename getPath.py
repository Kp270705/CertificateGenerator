CertificateEssestials = f"./static/Images/CertificateEssentials"
certificate_choice = {
    "Choice1":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme1.jpg",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogo.png",

    "auth1Path" : f"{CertificateEssestials}/auth1White.png",
    "auth2Path" : f"{CertificateEssestials}/auth2White.png",
    "linepath" : f"{CertificateEssestials}/line1.png",
    },

    "Choice2":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme2.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogoColor.png",
    "auth1Path" : f"{CertificateEssestials}/auth1.png",
    "auth2Path" : f"{CertificateEssestials}/auth2.png",
    "linepath" : f"{CertificateEssestials}/line1b.png",
    },
    "Choice3":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme3.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogoColor.png",
    "auth1Path" : f"{CertificateEssestials}/auth1.png",
    "auth2Path" : f"{CertificateEssestials}/auth2.png",
    "linepath" : f"{CertificateEssestials}/line1b.png",
    },

    "Choice4":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme4.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogo.png",
    "auth1Path" : f"{CertificateEssestials}/auth1.png",
    "auth2Path" : f"{CertificateEssestials}/auth2.png",
    "linepath" : f"{CertificateEssestials}/line1g.png",
    },

    "Choice5":{
    "TemplatePath" :f"{CertificateEssestials}/cert_theme5.png",
    "logo2Path ": f"{CertificateEssestials}/TechGeeksLogoColor.png",
    "auth1Path" : f"{CertificateEssestials}/auth1.png",
    "auth2Path" : f"{CertificateEssestials}/auth2.png",
    "linepath" : f"{CertificateEssestials}/line1g.png",
    },

}

def get_Choice_data(choice):
    return certificate_choice[choice]

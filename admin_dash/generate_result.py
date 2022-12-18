from reportlab.pdfgen import canvas
from reportlab.lib.units import cm 
from reportlab.lib.colors import HexColor

def design(pdf,date):
  pdf.setTitle("Exam Report Dated: "+date)

  pdf.setFont("Courier-Bold",25)
  pdf.setFillColor(HexColor(	'#FF0000'))
  pdf.drawString(3.3*cm,28.5*cm,"Exam Report Dated: "+date)
  
  pdf.setFont("Courier-Bold",15)
  pdf.setFillColor(HexColor('#FF007F'))
  pdf.drawString(1*cm,0*cm,"-- Online Examination System Developed By Varsha B.")

  pdf.setFont("Courier-Bold",12)
  pdf.setFillColor(HexColor('#F68B2D'))
  pdf.drawString(14.5*cm,27.8*cm,"(Marks Out Of 30)")
  
  pdf.line(1*cm,28.2*cm,20*cm,28.2*cm)
  pdf.line(1*cm,28.2*cm,1*cm,1*cm)
  pdf.line(20*cm,28.2*cm,20*cm,1*cm)
  pdf.line(1*cm,1*cm,20*cm,1*cm)
  pdf.line(1*cm,27.2*cm,20*cm,27.2*cm)
  
  pdf.setFont("Courier-Bold",11)
  pdf.setFillColor(HexColor('#0066CC'))
  pdf.line(3.5*cm,28.2*cm,3.5*cm,1*cm)
  pdf.drawString(1.5*cm,27.4*cm,"REGD_ID")
  pdf.line(9.5*cm,28.2*cm,9.5*cm,1*cm)
  pdf.drawString(5*cm,27.4*cm,"STUDENT NAME")
  pdf.line(14*cm,28.2*cm,14*cm,1*cm)
  pdf.drawString(10.8*cm,27.4*cm,"COURSE")
  pdf.setFont("Courier-Bold",10)
  pdf.line(16*cm,27.8*cm,16*cm,1*cm)
  pdf.drawString(14.2*cm,27.4*cm,"PAPER-I")
  pdf.line(18*cm,27.8*cm,18*cm,1*cm)
  pdf.drawString(16.2*cm,27.4*cm,"PAPER-II")
  pdf.line(20*cm,28.2*cm,20*cm,1*cm)
  pdf.drawString(18*cm,27.4*cm,"PAPER-III")
def results(pdf,data):
  pdf.setFont("Times-Roman",9)
  pdf.setFillColor(HexColor('#000000'))
  txt=26.8
  for d in data:
    pdf.drawString(1.1*cm,txt*cm,str(d['student'].regd_id))
    pdf.drawString(3.6*cm,txt*cm,str(d['student'].name))
    pdf.drawString(9.6*cm,txt*cm,str(d['student'].course))
    pdf.drawString(14.9*cm,txt*cm,str(d['paper'][0]))
    pdf.drawString(17*cm,txt*cm,str(d['paper'][1]))
    pdf.drawString(18.9*cm,txt*cm,str(d['paper'][2]))
    
   
    pdf.line(1*cm,(txt+(-0.5))*cm,20*cm,(txt+(-0.5))*cm)
    txt=txt-0.9
    if txt<2:
      pdf.showPage()
      txt=26.9 
      design(pdf,"") 
    

  
  